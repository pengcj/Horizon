#!/usr/bin/env python3
"""
Horizon Daily Pipeline
======================
Runs Horizon, generates Chinese podcast script, and creates TTS audio.

Usage:
    python scripts/daily_pipeline.py [--hours 24] [--voice 冰糖]

Requires:
    - .env with OPENAI_API_KEY (MiMo TokenPlan key)
    - data/config.json configured
"""

import os
import sys
import json
import glob
import subprocess
import base64
import argparse
from datetime import datetime, date
from pathlib import Path

import requests

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
CONFIG_FILE = PROJECT_ROOT / "data" / "config.json"
SUMMARIES_DIR = PROJECT_ROOT / "data" / "summaries"


def load_env():
    """Load .env file into os.environ."""
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())


def get_mimo_config():
    """Get MiMo API config from environment."""
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in .env")
    # Token Plan uses a different base URL
    base_url = "https://token-plan-cn.xiaomimimo.com/v1"
    return api_key, base_url


def run_horizon(hours=24):
    """Run Horizon and return the path to the latest summary."""
    print(f"🚀 Running Horizon (last {hours} hours)...")
    env = os.environ.copy()
    # Add uv to PATH
    local_bin = str(Path.home() / ".local" / "bin")
    env["PATH"] = f"{local_bin}:{env.get('PATH', '')}"

    result = subprocess.run(
        ["uv", "run", "horizon", "--hours", str(hours)],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        env=env,
        timeout=600,  # 10 min timeout
    )

    print(result.stdout)
    if result.returncode != 0:
        print(f"⚠️ Horizon exited with code {result.returncode}")
        print(result.stderr)
        return None

    # Find the latest Chinese summary
    today = date.today().isoformat()
    zh_file = SUMMARIES_DIR / f"horizon-{today}-zh.md"
    en_file = SUMMARIES_DIR / f"horizon-{today}-en.md"

    if zh_file.exists():
        return zh_file
    elif en_file.exists():
        return en_file
    else:
        # Find most recent
        files = sorted(glob.glob(str(SUMMARIES_DIR / "horizon-*.md")))
        return Path(files[-1]) if files else None


def read_summary(summary_path):
    """Read the summary file."""
    if summary_path and summary_path.exists():
        return summary_path.read_text(encoding="utf-8")
    return ""


def generate_podcast_script(summary_text, api_key, base_url, model="mimo-v2.5-pro"):
    """Use MiMo to generate a Chinese podcast script from the summary."""
    print("🎙️ Generating podcast script...")

    # Truncate if too long
    if len(summary_text) > 8000:
        summary_text = summary_text[:8000] + "\n...(truncated)"

    prompt = f"""你是一位专业的科技新闻播客主持人。请根据以下 Horizon 新闻日报内容，生成一段简洁的中文播客脚本。

要求：
1. 开头用一句话欢迎听众，说明今天有几条重要资讯
2. 每条新闻用 2-3 句话概括要点，语言自然口语化
3. 新闻之间用过渡词连接
4. 结尾简短总结今天的整体趋势
5. 总长度控制在 800 字以内
6. 风格：专业但不死板，像在跟朋友聊天

今日新闻日报内容：
{summary_text}

请直接输出播客脚本，不要加标题或格式说明："""

    resp = requests.post(
        f"{base_url}/chat/completions",
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 2000,
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    script = data["choices"][0]["message"]["content"]
    print(f"✅ Podcast script generated ({len(script)} chars)")
    return script


def generate_tts_audio(text, api_key, base_url, voice="冰糖", output_path=None):
    """Call MiMo TTS API to generate audio."""
    print(f"🔊 Generating TTS audio (voice: {voice})...")

    # Add style instruction for news reading
    style = "用专业新闻播报的语调，语速适中，吐字清晰，沉稳大气"

    resp = requests.post(
        f"{base_url}/chat/completions",
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
        },
        json={
            "model": "mimo-v2.5-tts",
            "messages": [
                {"role": "user", "content": style},
                {"role": "assistant", "content": text},
            ],
            "audio": {
                "format": "wav",
                "voice": voice,
            },
        },
        timeout=300,
    )
    resp.raise_for_status()
    data = resp.json()

    # Extract audio data
    audio_data = data["choices"][0]["message"]["audio"]["data"]
    audio_bytes = base64.b64decode(audio_data)

    if output_path is None:
        today = date.today().isoformat()
        output_path = SUMMARIES_DIR / f"podcast-{today}-zh.wav"

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(audio_bytes)

    size_mb = len(audio_bytes) / (1024 * 1024)
    print(f"✅ Audio saved: {output_path} ({size_mb:.1f} MB)")

    # Auto-convert WAV to MP3 for smaller file size (better for messaging)
    mp3_path = output_path.with_suffix(".mp3")
    try:
        import shutil
        if shutil.which("ffmpeg"):
            subprocess.run(
                ["ffmpeg", "-i", str(output_path),
                 "-codec:a", "libmp3lame", "-b:a", "128k",
                 str(mp3_path), "-y"],
                capture_output=True, timeout=60,
            )
            if mp3_path.exists():
                mp3_size = mp3_path.stat().st_size / (1024 * 1024)
                print(f"✅ MP3 converted: {mp3_path} ({mp3_size:.1f} MB)")
                return mp3_path
    except Exception as e:
        print(f"⚠️ MP3 conversion failed: {e}, using WAV")

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Horizon Daily Pipeline")
    parser.add_argument("--hours", type=int, default=24, help="Hours to look back")
    parser.add_argument("--voice", default="冰糖", help="TTS voice name")
    parser.add_argument("--skip-horizon", action="store_true", help="Skip running Horizon, use existing summary")
    parser.add_argument("--summary", type=str, help="Path to summary file (with --skip-horizon)")
    args = parser.parse_args()

    load_env()
    api_key, base_url = get_mimo_config()

    today = date.today().isoformat()

    # Step 1: Run Horizon (or use existing)
    if args.skip_horizon and args.summary:
        summary_path = Path(args.summary)
    elif args.skip_horizon:
        # Find latest summary
        zh_file = SUMMARIES_DIR / f"horizon-{today}-zh.md"
        en_file = SUMMARIES_DIR / f"horizon-{today}-en.md"
        summary_path = zh_file if zh_file.exists() else en_file
    else:
        summary_path = run_horizon(hours=args.hours)

    if not summary_path or not summary_path.exists():
        print("❌ No summary found!")
        sys.exit(1)

    # Step 2: Read summary
    summary_text = read_summary(summary_path)
    if not summary_text.strip():
        print("❌ Summary is empty!")
        sys.exit(1)
    print(f"📄 Loaded summary: {summary_path} ({len(summary_text)} chars)")

    # Step 3: Check for Chinese summary
    zh_file = SUMMARIES_DIR / f"horizon-{today}-zh.md"
    if zh_file.exists() and summary_path != zh_file:
        zh_summary = read_summary(zh_file)
        if zh_summary.strip():
            summary_text = zh_summary
            print(f"📄 Using Chinese summary: {zh_file}")

    # Step 4: Generate podcast script
    podcast_script = generate_podcast_script(summary_text, api_key, base_url)

    # Save podcast script
    script_path = SUMMARIES_DIR / f"podcast-{today}-zh.txt"
    script_path.write_text(podcast_script, encoding="utf-8")
    print(f"📝 Podcast script saved: {script_path}")

    # Step 5: Generate TTS audio
    audio_path = generate_tts_audio(
        podcast_script, api_key, base_url,
        voice=args.voice,
    )

    print("\n" + "=" * 50)
    print("✅ Daily pipeline complete!")
    print(f"  📄 Summary: {summary_path}")
    print(f"  🎙️ Script:  {script_path}")
    print(f"  🔊 Audio:   {audio_path}")
    print("=" * 50)

    return {
        "summary_path": str(summary_path),
        "script_path": str(script_path),
        "audio_path": str(audio_path),
        "podcast_script": podcast_script,
    }


if __name__ == "__main__":
    main()
