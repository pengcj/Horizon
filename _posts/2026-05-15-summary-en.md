---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 76 items, 29 important content pieces were selected

---

1. [First Public macOS Kernel Exploit on Apple M5 Silicon Disclosed](#item-1) ⭐️ 9.0/10
2. [arXiv to Ban Authors for One Year Over Hallucinated References](#item-2) ⭐️ 8.0/10
3. [Bun runtime merges major rewrite of core from Zig to Rust](#item-3) ⭐️ 8.0/10
4. [Fragnesia: New Linux Kernel Local Privilege Escalation Vulnerability](#item-4) ⭐️ 8.0/10
5. [Anthropic Restricts Access to Mythos AI Due to Extreme Security Vulnerability-Finding Capability](#item-5) ⭐️ 8.0/10
6. [Study finds over 140,000 fake citations in 2025 preprints, highest in social sciences.](#item-6) ⭐️ 8.0/10
7. [Mullvad VPN exit IPs are deterministic, creating a fingerprinting vector.](#item-7) ⭐️ 7.0/10
8. [Guide to removing modem and GPS from 2024 Toyota RAV4 for privacy](#item-8) ⭐️ 7.0/10
9. [Antirez Introduces DwarfStar4, a Focused LLM Inference Runtime for DeepSeek 4](#item-9) ⭐️ 7.0/10
10. [Critical Nginx Remote Code Execution Vulnerability Discovered](#item-10) ⭐️ 7.0/10
11. [OpenAI Integrates Codex Agent into ChatGPT Mobile App](#item-11) ⭐️ 7.0/10
12. [A Technical Deep-Dive into the GGUF File Format's Structure and Limitations](#item-12) ⭐️ 7.0/10
13. [AI Coding Agents Enable Safer Tech Migrations, Reducing Lock-In Fears](#item-13) ⭐️ 7.0/10
14. [Mitchell Hashimoto on modern programming languages becoming more fungible](#item-14) ⭐️ 7.0/10
15. [Proposal for Policy Groups to Enhance Linux Kernel Memory Management](#item-15) ⭐️ 7.0/10
16. [Linux Summit Debates Buffered Atomic Writes for PostgreSQL](#item-16) ⭐️ 7.0/10
17. [Linux kernel developer proposes replacing anonymous reverse mapping with COW context.](#item-17) ⭐️ 7.0/10
18. [Kernel summit explores managing memory pages outside the direct map](#item-18) ⭐️ 7.0/10
19. [Linux mshare advances shared page tables for memory optimization](#item-19) ⭐️ 7.0/10
20. [German Sovereign Tech Fund Awards Over €1 Million to KDE](#item-20) ⭐️ 7.0/10
21. [UK AI Institute Finds GPT-5.5 Matches Claude Mythos in Vulnerability Detection](#item-21) ⭐️ 7.0/10
22. [NIH Staffing Shortage Threatens to Cut New Research Grants This Year](#item-22) ⭐️ 7.0/10
23. [Old T cells impair brain function; blocking them improves memory in mice.](#item-23) ⭐️ 7.0/10
24. [RTX 5090 eGPU Successfully Used with M4 MacBook Air for Gaming and AI](#item-24) ⭐️ 6.0/10
25. [Technical Article on HDD Firmware Hacking and Community Insights](#item-25) ⭐️ 6.0/10
26. [Datasette Plugin Released for IP-Based Rate Limiting Against Crawlers](#item-26) ⭐️ 6.0/10
27. [Critique Highlights Ambiguity in 'AI Agents' Terminology](#item-27) ⭐️ 6.0/10
28. [CSP Allow-list Experiment Manages Sandbox Permissions Dynamically](#item-28) ⭐️ 6.0/10
29. [Red Hat's AI Desktop Proposal for Fedora Faces Community Opposition and Vote Reversal](#item-29) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [First Public macOS Kernel Exploit on Apple M5 Silicon Disclosed](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

The security research team Calif has publicly disclosed the first known kernel memory corruption exploit for macOS running on Apple's latest M5 silicon. The exploit was reportedly developed in just five days using Anthropic's Mythos AI, bypassing Apple's five-year security hardening efforts. This disclosure demonstrates that even Apple's latest, heavily fortified hardware and software stack contains exploitable vulnerabilities, potentially undermining confidence in the security of Apple Silicon devices. It also highlights the emerging role of AI tools like LLMs in accelerating complex vulnerability discovery and exploit development, posing new challenges for defenders. The exploit bypasses Apple's Memory Tagging Extension (MTE), a key hardware security feature designed to prevent memory corruption attacks, raising questions about the effectiveness of such mitigations. Based on Apple's bug bounty program, the exploit could be worth between $100,000 and $1.5 million depending on how it is packaged and demonstrated.

hackernews · quadrige · May 14, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48139219)

**Background**: Kernel memory corruption vulnerabilities target the core of an operating system (the kernel), potentially allowing an attacker to gain the highest level of control over a device. Apple's M-series chips integrate hardware security features like the Secure Enclave and Memory Tagging Extension (MTE) to make such attacks significantly harder. LLMs (Large Language Models) like Anthropic's Mythos are AI systems being explored for both cybersecurity defense and offense.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://9to5mac.com/2026/05/14/calif-team-details-how-anthropic-mythos-helped-build-a-working-macos-exploit-in-five-days/">Anthropic Mythos helped Calif build a macOS exploit in five days - 9to5Mac</a></li>
<li><a href="https://thecodersblog.com/beyond-the-headlines-deconstructing-the-first-public-m5-kernel-memory-corruption-exploit/">Beyond the Headlines: Deconstructing the First Public M5 Kernel Memory ...</a></li>

</ul>
</details>

**Discussion**: The community discussion expresses surprise that Apple's allegedly safe Swift language wasn't used to prevent such bugs, skepticism about the completeness of the disclosed technical details, and significant concern about the dual-use potential of LLMs in security. One comment estimates the exploit's monetary value under Apple's bug bounty program, while others question how the vulnerability survived Apple's MTE hardware mitigations.

**Tags**: `#apple-security`, `#kernel-exploitation`, `#cybersecurity`, `#vulnerability-disclosure`, `#hardware-security`

---

<a id="item-2"></a>
## [arXiv to Ban Authors for One Year Over Hallucinated References](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv has announced a new policy that will impose a one-year submission ban on authors who submit papers containing hallucinated or fabricated references, and subsequent submissions will require prior acceptance by a reputable peer-reviewed venue. This policy is a significant step to uphold academic integrity and combat the growing problem of unreliable, potentially AI-generated citations, thereby protecting the credibility of the scientific record. The penalty involves a mandatory one-year ban followed by a requirement for prior peer-reviewed acceptance for future submissions, and the policy's current implementation status on the official arXiv policies page was questioned by the community.

hackernews · gjuggler · May 14, 20:39 · [Discussion](https://news.ycombinator.com/item?id=48140922)

**Background**: arXiv is a widely used, free online repository for preprints in fields like physics, mathematics, and computer science, which allows researchers to share findings before formal peer review. The term 'hallucinated references' typically refers to citations that are fabricated or do not exist, a problem exacerbated by the use of large language models (LLMs) which can generate plausible but incorrect bibliographic entries.

**Discussion**: Community reactions are largely supportive, viewing the policy as a strong move for science, though some questioned its implementation details and visibility. Discussions also touched on the need for better citation management tools and noted opposition from 'LLM hypers' who resist constraints on AI use in research.

**Tags**: `#academic policy`, `#research integrity`, `#AI ethics`, `#citation standards`, `#arXiv`

---

<a id="item-3"></a>
## [Bun runtime merges major rewrite of core from Zig to Rust](https://github.com/oven-sh/bun/pull/30412) ⭐️ 8.0/10

The Bun JavaScript runtime has merged a significant pull request that rewrites its core components from the Zig programming language to Rust, aiming to leverage Rust's memory safety features to eliminate bugs like use-after-free. This shift represents a major commitment to memory safety for a large, popular open-source JavaScript runtime, potentially reducing a significant class of security vulnerabilities and memory bugs for its users and the broader ecosystem. The rewrite adds over 1 million lines of Rust code and involved detailed mapping of Zig idioms to Rust, with the Rust borrow checker expected to catch issues like double-free at compile time. However, some memory safety issues, such as leaks from holding references too long or cross-JS-boundary re-entry, still require manual attention.

hackernews · Chaoses · May 14, 08:15 · [Discussion](https://news.ycombinator.com/item?id=48132488)

**Background**: Bun is a fast, all-in-one JavaScript runtime and toolkit designed as a drop-in replacement for Node.js, built initially using the Zig programming language. Rust is a systems programming language that emphasizes memory safety through its ownership and borrow checker model, which prevents common bugs like use-after-free at compile time. Zig, in contrast, offers manual memory management and is designed as a safer successor to C, but it does not enforce the same compile-time safety guarantees as Rust.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://blog.logrocket.com/comparing-rust-vs-zig-performance-safety-more/">Comparing Rust vs. Zig : Performance, safety , and... - LogRocket Blog</a></li>

</ul>
</details>

**Discussion**: The community discussion is highly technical, with comments analyzing the code statistics, noting the Bun codebase was already prepared with types mapping to Rust equivalents, and sharing Rust's `unsafe` block counts from the new code. Maintainer Jarred acknowledged the safety benefits but clarified that Rust won't catch all memory bugs, and some users noted the irony given earlier doubts about the merge.

**Tags**: `#bun`, `#rust`, `#zig`, `#javascript-runtime`, `#memory-safety`

---

<a id="item-4"></a>
## [Fragnesia: New Linux Kernel Local Privilege Escalation Vulnerability](https://lwn.net/Articles/1072647/) ⭐️ 8.0/10

A new local privilege escalation vulnerability named Fragnesia (CVE-2026-46300) has been disclosed, exploiting a logic bug in the Linux kernel's XFRM ESP-in-TCP subsystem to achieve arbitrary writes into the kernel page cache. A patch is in development but has not yet been merged into the mainline or stable kernel trees. This vulnerability allows a local attacker to escalate privileges to root on affected Linux systems without requiring a race condition, posing a significant threat to system security. It is a separate bug in the same class as the recent Dirty Frag vulnerabilities, indicating ongoing challenges in securing the kernel's page cache subsystem. The exploit achieves arbitrary byte writes into the kernel page cache of read-only files, and a public proof-of-concept is available. The mitigation is the same as for the Dirty Frag vulnerability, but the Dirty Frag patches do not fix this specific bug.

rss · LWN.net · May 13, 15:26

**Background**: The Linux kernel's page cache is a memory area that stores recently accessed data from files to speed up disk operations. The XFRM subsystem in the kernel handles IPsec networking transformations, and ESP-in-TCP refers to the encapsulation of Encapsulating Security Payload (ESP) packets within TCP streams. Dirty Frag is a class of vulnerabilities that exploit flaws in the kernel's handling of page-cache writes, allowing unauthorized modifications to sensitive in-memory files.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tenable.com/blog/fragnesia-cve-2026-46300-faq-about-new-linux-kernel-xfrm-esp-in-tcp-priv-esc">CVE-2026-46300 (Fragnesia): Linux Kernel ESP-in-TCP LPE FAQ - Tenable®</a></li>
<li><a href="https://github.com/V4bel/dirtyfrag">GitHub - V4bel/dirtyfrag · GitHub</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#security`, `#vulnerability`, `#local-privilege-escalation`

---

<a id="item-5"></a>
## [Anthropic Restricts Access to Mythos AI Due to Extreme Security Vulnerability-Finding Capability](https://www.schneier.com/blog/archives/2026/05/how-dangerous-is-anthropics-mythos-ai.html) ⭐️ 8.0/10

Anthropic announced that its new AI model, Claude Mythos Preview, is so exceptionally skilled at finding software security vulnerabilities that it will not be released to the general public. Instead, access will be restricted to a select group of companies to help them scan and secure their own software. This decision highlights the growing dual-use dilemma in advanced AI, where capabilities that can be used for defensive cybersecurity also pose significant offensive threats if misused, forcing companies to implement unprecedented restrictions. It signals a potential industry shift towards gated access for the most powerful AI models to mitigate safety risks. Anthropic's Mythos model is described as a 'step change' in capability, excelling not only in finding vulnerabilities but also in reverse engineering stripped binaries. However, the UK's AI Security Institute found that OpenAI's generally available GPT-5.5 model has comparable offensive cyber capabilities, suggesting such extreme proficiency is not unique to Mythos.

rss · Schneier on Security · May 14, 11:04

**Background**: AI models are increasingly being tested and used for cybersecurity purposes, including autonomous vulnerability detection and code analysis. A 'Cyber Reasoning System' like Aisle's is designed to autonomously find and fix application flaws. The concept of 'dual-use' technology refers to tools developed for benign purposes that can be repurposed for harmful activities, a central concern in AI safety.

<details><summary>References</summary>
<ul>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>
<li><a href="https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities">Our evaluation of OpenAI's GPT - 5 . 5 cyber capabilities | AISI Work</a></li>
<li><a href="https://www.helpnetsecurity.com/2025/10/17/aisle-ai-native-cyber-reasoning-system/">AISLE emerges from stealth with AI -native cyber... - Help Net Security</a></li>

</ul>
</details>

**Discussion**: The provided content does not include explicit community comments, but the broader context shows concern from security experts and agencies; for instance, six spy agencies have warned that agentic AI poses a live security risk, and evaluations have revealed that models like GPT-5.5 can bypass safety guardrails entirely, amplifying the debate on necessary restrictions.

**Tags**: `#AI Safety`, `#Cybersecurity`, `#AI Regulation`, `#Vulnerability Disclosure`, `#Anthropic`

---

<a id="item-6"></a>
## [Study finds over 140,000 fake citations in 2025 preprints, highest in social sciences.](https://www.nature.com/articles/d41586-026-01545-1) ⭐️ 8.0/10

A large-scale analysis identified over 140,000 fabricated citations in papers and preprints published across four research repositories during 2025, with social sciences preprints showing the highest prevalence. This discovery exposes a significant and widespread threat to research integrity, undermining the reliability of scholarly literature and potentially damaging trust in academic publishing, especially in fields heavily reliant on preprints. The analysis focused on papers and preprints from 2025 across multiple repositories, quantifying the scale of citation fraud; the specific prevalence in social sciences suggests potential disciplinary differences in research practices or vulnerability to such fraud.

rss · Nature · May 14, 00:00

**Background**: Preprints are scholarly manuscripts shared publicly before formal peer review, enabling rapid dissemination but with less editorial oversight. Citations are fundamental to academic work, as they credit sources and build upon existing knowledge; fabricated citations misrepresent the scholarly record and can mislead researchers and readers.

**Tags**: `#research_integrity`, `#academic_publishing`, `#AI_ethics`, `#preprints`, `#citation_fraud`

---

<a id="item-7"></a>
## [Mullvad VPN exit IPs are deterministic, creating a fingerprinting vector.](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/) ⭐️ 7.0/10

It has been revealed that Mullvad VPN assigns exit IP addresses to users deterministically based on their WireGuard key, rather than randomly upon each connection, which creates a consistent fingerprinting vector that can link a user's activity across different sessions. This finding challenges the common assumption that using a VPN effectively anonymizes a user for each session, as the deterministic IP allocation allows entities like forum moderators or advertisers to correlate different user sessions, potentially de-anonymizing users who rely on Mullvad for privacy. The exit IP is based on the user's WireGuard key, which in the official client rotates every 1 to 30 days, but a third-party client could keep it static indefinitely, prolonging the fingerprint's lifespan. The article provides an example where IP range overlaps with a >99% probability indicate the same user.

hackernews · RGBCube · May 15, 02:35 · [Discussion](https://news.ycombinator.com/item?id=48143880)

**Background**: WireGuard is a modern VPN protocol known for its speed and simplicity. In a typical VPN setup, a user's internet traffic appears to originate from an exit IP address belonging to the VPN provider. Fingerprinting is a technique used to track users by collecting unique attributes of their device, browser, or network configuration, even without traditional cookies.

<details><summary>References</summary>
<ul>
<li><a href="https://swissvpn.pro/en/blog/browser-fingerprinting-protection">What Is Browser Fingerprinting & How to Stop It... | Swiss VPN Blog</a></li>
<li><a href="https://routeharden.com/blog/os-and-tcpip-stack-fingerprinting">OS and TCP/ IP stack fingerprinting · RouteHarden</a></li>

</ul>
</details>

**Discussion**: Some commenters argue that VPNs are not designed for full anonymity and users seeking that should use Tor, which sparked debate about VPN anonymity expectations. Others noted technical limitations, like third-party clients not rotating keys, and shared methods for blocking VPN IPs. A user likened the design to one an intelligence agency might use, highlighting privacy concerns.

**Tags**: `#privacy`, `#VPN`, `#fingerprinting`, `#cybersecurity`, `#networking`

---

<a id="item-8"></a>
## [Guide to removing modem and GPS from 2024 Toyota RAV4 for privacy](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 7.0/10

A detailed guide was published documenting the physical removal of the modem and GPS hardware from a 2024 Toyota RAV4 hybrid to prevent the vehicle from transmitting telemetry data back to the manufacturer. This guide addresses growing consumer concerns about automotive data privacy by providing a practical hardware modification to limit vehicle telemetry, highlighting the tension between modern connected car features and user privacy. The modification involves removing the DCM (Data Communication Module) and GPS unit, but community comments warn that even after removal, connecting a phone via Bluetooth may allow the car to use the phone's connection to still transmit data, whereas a wired USB connection like CarPlay does not.

hackernews · arkadiyt · May 14, 17:08 · [Discussion](https://news.ycombinator.com/item?id=48138136)

**Background**: Modern vehicles like the Toyota RAV4 contain a Telematics Control Unit (TCU) or Data Communication Module (DCM) that uses an embedded SIM (eSIM) to connect to cellular networks, enabling remote services but also transmitting vehicle location, usage, and diagnostic data to the manufacturer. This connectivity is a core part of services like remote start, navigation updates, and over-the-air software updates.

<details><summary>References</summary>
<ul>
<li><a href="https://www.toyotanation.com/threads/question-regarding-dealer-procedure-removing-dcm-module.1726677/">Question regarding dealer procedure removing DCM module | Toyota Forum</a></li>
<li><a href="https://www.rav4world.com/threads/2019-rav4-dcm-deactivate-procedure.304339/">2019 Rav4 DCM deactivate procedure | Toyota RAV4 Forums</a></li>
<li><a href="https://en.wikipedia.org/wiki/Telematic_control_unit">Telematic control unit - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community discussion reveals nuanced privacy trade-offs, with one user explaining that removing the modem doesn't fully prevent data transmission if Bluetooth is used, as the car can leverage the phone's data connection. Others share experiences with similar issues in different vehicles (like the Ford Maverick) and cite Toyota's reported practice of sharing data with insurance companies as a key concern.

**Tags**: `#privacy`, `#automotive-hacking`, `#telemetry`, `#hardware-modification`

---

<a id="item-9"></a>
## [Antirez Introduces DwarfStar4, a Focused LLM Inference Runtime for DeepSeek 4](https://antirez.com/news/165) ⭐️ 7.0/10

Antirez (Salvatore Sanfilippo), the creator of Redis, released DwarfStar4, a specialized LLM inference runtime designed to run the DeepSeek 4 model on high-memory hardware, with backends for Apple Metal, NVIDIA CUDA, and AMD ROCm. This project provides a focused, open-source tool for running a powerful new large language model locally, potentially democratizing access to advanced AI capabilities and challenging the business models of cloud-based AI services like Anthropic's Claude. The runtime currently targets Apple Silicon Macs with 96GB of unified memory as its primary platform and acknowledges its foundation on llama.cpp and GGML. The AMD ROCm backend is maintained in a separate community branch due to the developer's lack of direct hardware access.

hackernews · caust1c · May 14, 22:29 · [Discussion](https://news.ycombinator.com/item?id=48142108)

**Background**: DwarfStar4 (DS4) is an inference engine, a specialized runtime optimized to execute a machine learning model efficiently on specific hardware. DeepSeek V4 is a recent series of large language models from DeepSeek AI, featuring architectures like Mixture-of-Experts (MoE) with variants such as DeepSeek-V4-Pro (1.6T parameters) and DeepSeek-V4-Flash (284B parameters).

<details><summary>References</summary>
<ul>
<li><a href="https://pasqualepillitteri.it/en/news/2253/ds4-antirez-deepseek-v4-flash-inference-engine">DwarfStar4 (DS4) Roadmap by antirez: DeepSeek V4 Flash on Apple Silicon and CUDA</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://deepwiki.com/mlc-ai/mlc-llm">mlc-ai/mlc-llm | DeepWiki</a></li>

</ul>
</details>

**Discussion**: Community comments express excitement about the project's focused nature and its ability to run DeepSeek 4 locally, with one user noting its performance feels surprisingly close to Claude. A key discussion point is the potential disruption to Anthropic's business model if locally-run models become 'intelligent enough' for tasks like coding, and users are optimistic about future hardware efficiency improvements.

**Tags**: `#LLM`, `#inference-runtime`, `#DeepSeek`, `#performance`, `#open-source`

---

<a id="item-10"></a>
## [Critical Nginx Remote Code Execution Vulnerability Discovered](https://github.com/DepthFirstDisclosures/Nginx-Rift) ⭐️ 7.0/10

A new critical vulnerability (CVE-2026-42945) has been disclosed in the Nginx rewrite module, enabling unauthenticated denial-of-service and potentially remote code execution. The exploit requires specific configurations involving `rewrite` and `set` directives with unnamed regex captures. This vulnerability is significant because Nginx powers a substantial portion of the world's web servers, making any critical remote code execution flaw a widespread risk. It affects deployments using common rewrite directives, potentially impacting many legacy and active systems. The exploit uses a technique called 'cross-request heap feng shui' to manipulate memory, and a proof-of-concept assumes ASLR is disabled for demonstration. Mitigations include upgrading to patched Nginx versions (1.31.0, 1.30.1) or switching to named regex captures (e.g., `$user_id` instead of `$1`).

hackernews · hetsaraiya · May 14, 17:17 · [Discussion](https://news.ycombinator.com/item?id=48138268)

**Background**: The Nginx rewrite module processes directives like `rewrite`, `set`, and `if` to manipulate URLs and request data, compiling them into bytecode that executes for each request. ASLR is a standard security feature that randomizes memory addresses to make exploitation of memory corruption bugs more difficult. Memory safety vulnerabilities in web servers can allow attackers to crash the service or, in severe cases, execute arbitrary code on the server.

<details><summary>References</summary>
<ul>
<li><a href="https://orca.security/resources/blog/nginx-rewrite-module-vulnerability-cve-2026-42945/">NGINX Rewrite Module Flaw (CVE-2026-42945) | Orca Security</a></li>
<li><a href="https://devops-daily.com/posts/nginx-rift-cve-2026-42945-rewrite-rce">NGINX Rift (CVE-2026-42945): The 18-Year-Old Rewrite Bug That...</a></li>
<li><a href="https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability">NGINX Rift: Achieving NGINX Remote Code Execution via... | depthfirst</a></li>

</ul>
</details>

**Discussion**: Security professionals in the community are debating the true severity, with some emphasizing that the published proof-of-concept disables ASLR, while others warn that reliable ASLR bypass techniques likely exist. There is agreement that the vulnerability requires specific preconditions (rewrite and set directives), and discussion focuses on practical mitigations like using named captures and applying official patches.

**Tags**: `#security`, `#nginx`, `#vulnerability`, `#web-server`, `#exploit`

---

<a id="item-11"></a>
## [OpenAI Integrates Codex Agent into ChatGPT Mobile App](https://openai.com/index/work-with-codex-from-anywhere/) ⭐️ 7.0/10

OpenAI has integrated its Codex coding agent directly into the ChatGPT mobile application, allowing users to access AI-powered coding assistance remotely from their phones. This integration enables developers to manage and direct coding agents from anywhere, potentially transforming workflows by allowing tasks to continue without being tied to a desktop computer. A notable aspect is that Codex is available on OpenAI's free plan, though user interactions may contribute to model training; community feedback also highlights concerns that mobile constraints like smaller screens might lead to less precise direction and increased technical debt compared to desktop use.

hackernews · mikeevans · May 14, 20:06 · [Discussion](https://news.ycombinator.com/item?id=48140529)

**Background**: Codex is an AI coding agent developed by OpenAI that integrates with ChatGPT to assist with software development tasks such as code review, bug identification, and parallel project work in cloud environments. It functions as an autonomous agent that can execute multi-step coding assignments, making it a tool for augmenting developer productivity.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent ) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community discussion reveals mixed sentiments; some users praise the workflow flexibility and free access, noting it's a 'game changer' for remote coding, while others report practical drawbacks such as diminished effectiveness on mobile due to screen and input limitations, which may hinder detailed task direction.

**Tags**: `#OpenAI`, `#mobile-development`, `#coding-assistants`, `#developer-tools`, `#AI-agents`

---

<a id="item-12"></a>
## [A Technical Deep-Dive into the GGUF File Format's Structure and Limitations](https://nobodywho.ooo/posts/whats-in-a-gguf/) ⭐️ 7.0/10

A detailed technical analysis of the GGUF file format's internal structure was published, highlighting its single-file ethos while also identifying key missing features such as tool calling functionality. Understanding GGUF's structure and gaps is crucial for the open-source ML ecosystem, as formats like GGUF underpin widely-used projects like llama.cpp, enabling efficient local model deployment across diverse hardware. The analysis notes that a major missing feature is a standardized format for tool calling, which is essential for transitioning from standalone LLMs to AI agents. The format's design philosophy prioritizes simplicity by bundling all necessary data into a single binary file, contrasting with multi-file formats like Safetensors.

hackernews · bashbjorn · May 14, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48138332)

**Background**: GGUF is a binary file format designed by Georgi Gerganov for the ggml library, primarily used for storing large language models for inference with tools like llama.cpp. It evolved from the older GGML format to provide better metadata and extensibility. The format's key advantage is its portability and single-file nature, which simplifies distribution and execution across different platforms and hardware backends.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">llama.cpp - Wikipedia</a></li>
<li><a href="https://apxml.com/courses/practical-llm-quantization/chapter-5-quantization-formats-tooling/gguf-format">GGUF File Format Explained (llama.cpp)</a></li>
<li><a href="https://medium.com/@vimalkansal/understanding-the-gguf-format-a-comprehensive-guide-67de48848256">Understanding the GGUF Format : A Comprehensive Guide | Medium</a></li>

</ul>
</details>

**Discussion**: The community discussion, including insights from GGUF's original designer Philpax, acknowledges the format's critical importance to the open-source ML space but expresses a shared regret that projection models ended up as separate files, contrary to the single-file design ethos. Commenters also strongly agree that adding a standard tool calling format would be a significant milestone for enabling AI agents.

**Tags**: `#ML infrastructure`, `#file formats`, `#local AI`, `#GGUF`, `#open-source ML`

---

<a id="item-13"></a>
## [AI Coding Agents Enable Safer Tech Migrations, Reducing Lock-In Fears](https://simonwillison.net/2026/May/14/not-so-locked-in/#atom-everything) ⭐️ 7.0/10

A medium-sized technology company successfully used AI coding agents to rewrite its legacy native iPhone and Android applications into React Native, and they feel confident this decision is reversible. This anecdote illustrates a broader industry trend where AI tools are drastically lowering the cost and risk of technology migrations, allowing engineers to make architectural choices with less fear of permanent vendor or framework lock-in. The decision to migrate was driven by the improved capabilities of React Native over the years and the newfound confidence that AI-assisted porting could facilitate a return to native development if needed in the future.

rss · Simon Willison · May 14, 22:53

**Background**: React Native is a cross-platform mobile development framework that allows developers to build apps for iOS and Android using JavaScript and React, sharing a significant amount of code. The 'New React Native Architecture' with components like JSI and Fabric has been a major improvement. Technology lock-in refers to the high cost and difficulty of switching from one technology stack, programming language, or vendor to another, which has historically been a major risk in software architecture decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://reactnative.dev/architecture/overview">Architecture Overview · React Native</a></li>
<li><a href="https://www.linkedin.com/pulse/why-new-react-native-architecture-game-changer-francis-beasley-ter4e?tl=en">Why the New React Native Architecture is a Game-Changer for...</a></li>

</ul>
</details>

**Tags**: `#react-native`, `#coding-agents`, `#technology-migration`, `#mobile-development`, `#software-architecture`

---

<a id="item-14"></a>
## [Mitchell Hashimoto on modern programming languages becoming more fungible](https://simonwillison.net/2026/May/14/mitchell-hashimoto/#atom-everything) ⭐️ 7.0/10

Prominent developer Mitchell Hashimoto observed that modern programming languages have become increasingly fungible, using Bun's successful porting of its codebase from Zig to Rust as a key example. This observation challenges the long-held notion that choosing a programming language implies significant lock-in, suggesting that modern tooling and architecture allow for greater flexibility in technology stacks. Hashimoto specifically highlighted that Bun demonstrated the ability to rewrite its codebase in a different language within roughly one or two weeks, portraying languages like Rust as potentially 'expendable' tools rather than permanent commitments.

rss · Simon Willison · May 14, 22:31

**Background**: Bun is a modern, high-performance JavaScript runtime built for speed, while Zig is a system-level programming language aiming to be a better C. Rust is another systems language focused on safety and concurrency. The concept of 'fungibility' here refers to the interchangeability or replaceability of one programming language with another for a given project without incurring prohibitive costs or effort.

<details><summary>References</summary>
<ul>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fungibility">Fungibility - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#programming-languages`, `#rust`, `#zig`, `#software-engineering`, `#developer-tools`

---

<a id="item-15"></a>
## [Proposal for Policy Groups to Enhance Linux Kernel Memory Management](https://lwn.net/Articles/1072517/) ⭐️ 7.0/10

At the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit, developer Chris Li presented a proposed enhancement called 'policy groups' to address shortcomings in the Linux kernel's control-group subsystem for resource management. This proposal targets known limitations of the widely used control-group (cgroup) subsystem, which could lead to more flexible and powerful resource management in Linux systems if adopted. While control groups work well for resource management, they have shortcomings for other use cases that the proposed policy groups aim to fix, though consensus on the final design remains distant.

rss · LWN.net · May 14, 19:02

**Background**: The Linux kernel's control-group (cgroup) subsystem is a core feature that allows administrators to allocate and limit system resources like CPU time, memory, and network bandwidth to user-defined groups of processes. It operates hierarchically and is fundamental for containerization, cloud computing, and system resource isolation. The memory-management track at the LSFMMBPF summit is a key venue for discussing such deep kernel subsystem changes.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/resource_management_guide/ch01">Chapter 1. Introduction to Control Groups (Cgroups) | Resource Management Guide | Red Hat Enterprise Linux | 6</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kernel_(operating_system)">Kernel (operating system) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Linux kernel`, `#memory management`, `#control groups`, `#operating systems`, `#systems programming`

---

<a id="item-16"></a>
## [Linux Summit Debates Buffered Atomic Writes for PostgreSQL](https://lwn.net/Articles/1072019/) ⭐️ 7.0/10

At the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit, developers discussed the in-progress atomic-buffered-writes feature for the Linux kernel, with a focus on a PostgreSQL use case and a new writethrough-based implementation approach proposed by Ojaswin Mujoo. This feature could significantly improve the performance and data integrity of database systems like PostgreSQL on Linux by enabling more efficient, atomic writes at the filesystem level, which is a critical advancement for storage-heavy applications. The proposed writethrough approach means the kernel writes data immediately to disk rather than waiting for page cache writeback, which simplifies atomicity guarantees but requires careful developer debate on implementation trade-offs.

rss · LWN.net · May 14, 14:54

**Background**: Atomic-buffered-writes is a Linux kernel feature aimed at allowing applications to perform writes that are both buffered for performance and atomic for data integrity, meaning a write either fully completes or has no effect. PostgreSQL, a popular open-source relational database, often requires such guarantees for transaction logs and data files to prevent corruption. The writethrough approach differs from traditional writeback caching by synchronizing writes to storage immediately.

**Discussion**: The summit sessions featured substantial developer debate among filesystem and storage experts, indicating that the implementation of this feature involves complex technical trade-offs and is still under active discussion within the kernel community.

**Tags**: `#Linux Kernel`, `#Filesystems`, `#Storage`, `#Database`, `#OS Development`

---

<a id="item-17"></a>
## [Linux kernel developer proposes replacing anonymous reverse mapping with COW context.](https://lwn.net/Articles/1072378/) ⭐️ 7.0/10

Lorenzo Stoakes has proposed a new 'COW context' abstraction to replace the existing, complex anonymous reverse mapping system in the Linux kernel's memory management subsystem. The proposal was presented as a session topic for the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit. This refactoring aims to simplify a core and notoriously complex part of the kernel, which could improve both code maintainability and runtime performance for memory-intensive workloads. If adopted, it would modernize a fundamental mechanism used for managing anonymous memory pages. The proposal describes the current anonymous reverse mapping implementation as a 'very broken abstraction' due to its complexity. The new COW context is presented as a simpler replacement, though the specific technical implementation details were provided in 'raw form' at the summit.

rss · LWN.net · May 14, 13:14

**Background**: In the Linux kernel, reverse mapping is the mechanism used to find all page table entries that point to a specific physical memory page. This is crucial for operations like swapping pages out to disk. Anonymous pages, which are not backed by a file (like heap or stack memory), have historically used a more complex reverse mapping system compared to file-backed pages, leading to performance and maintenance challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linux.org/threads/lwn-net-keeping-cows-in-context-a-k-a-anonymous-reverse-mapping.66412/latest">[LWN.net] [$] Keeping COWs in context (a.k.a. anonymous reverse mapping) | Linux.org</a></li>
<li><a href="https://blogs.oracle.com/linux/anonymous-reverse-mapping">The Anonymous Reverse Mapping – An Introduction | linux - Oracle Blogs</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#memory-management`, `#systems-programming`, `#performance`

---

<a id="item-18"></a>
## [Kernel summit explores managing memory pages outside the direct map](https://lwn.net/Articles/1072367/) ⭐️ 7.0/10

At the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit, a session shifted focus from a proposed pagetable library to discussing methods for efficiently managing kernel pages not covered by the direct map. This addresses a significant subsystem challenge in Linux kernel memory management, as pages outside the direct map (often for special memory like device I/O or secret memory) require careful handling to maintain performance and correctness, impacting kernel developers and system performance. The original session idea, a 'pagetable library for the kernel', was described as having 'fizzled', leading to the pivot to the direct-map management topic, which suggests an evolving focus on practical memory management issues.

rss · LWN.net · May 13, 14:20

**Background**: The kernel's direct map is a large, contiguous virtual address mapping of all physical memory, simplifying access for the kernel. However, some pages, such as those for secret memory or certain device mappings, are intentionally excluded from this map for security or hardware reasons, requiring alternative management strategies that can be complex and performance-critical.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Page_table">Page table - Wikipedia</a></li>
<li><a href="https://github.com/misc0110/PTEditor">misc0110/PTEditor: A small library to modify all page-table levels of all processes from user space for x86_64 and ARMv8. - GitHub</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#memory-management`, `#operating-systems`, `#systems-programming`, `#performance-optimization`

---

<a id="item-19"></a>
## [Linux mshare advances shared page tables for memory optimization](https://lwn.net/Articles/1072333/) ⭐️ 7.0/10

The mshare feature, which enables shared page tables for shared memory, was discussed at the 2026 LSFMM+BPF summit, presenting ongoing development to address a known scalability issue in Linux memory management. This optimization is significant because it can drastically reduce the memory overhead of page tables in systems with many processes sharing memory regions, improving performance for high-performance computing and similar workloads. The core problem is that while Linux can share memory between processes, each process typically maintains its own page tables, causing their combined size to sometimes exceed the shared memory itself when many processes are involved.

rss · LWN.net · May 13, 13:19

**Background**: In Linux and other operating systems, page tables are data structures used by the memory management unit (MMU) to map virtual addresses to physical memory addresses. Shared memory is a mechanism that allows multiple processes to access the same region of physical memory, which is critical for inter-process communication and efficient resource use. The mshare concept aims to extend this sharing to the page tables themselves, reducing redundant data structures.

<details><summary>References</summary>
<ul>
<li><a href="https://lwn.net/Articles/895217/">Sharing page tables with mshare() - LWN.net</a></li>
<li><a href="https://blogs.oracle.com/linux/mshare">Introduction to mshare | linux - Oracle Blogs</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#memory-management`, `#systems-optimization`, `#page-tables`, `#operating-systems`

---

<a id="item-20"></a>
## [German Sovereign Tech Fund Awards Over €1 Million to KDE](https://lwn.net/Articles/1072565/) ⭐️ 7.0/10

The KDE project has been awarded over €1 million from Germany's Sovereign Tech Fund specifically to strengthen the structural reliability, security, and infrastructure of its desktop environment and frameworks. This is a significant institutional investment in a major open-source desktop environment, signaling strong support for improving the security and stability of critical digital infrastructure that underpins many systems in Europe. The investment will focus on KDE's core infrastructure, including the Plasma desktop, KDE Linux, and the frameworks that support its communication services like KDE Connect.

rss · LWN.net · May 13, 13:09

**Background**: The Sovereign Tech Fund is a German government program that strategically invests in open-source software components deemed essential for economic competitiveness and innovation. KDE is a major international free software community producing a complete desktop environment and a wide range of applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sovereign.tech/programs/fund">Strategic investments in the digital infrastructure of our economy and society - Sovereign Tech Fund</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_Tech_Agency">Sovereign Tech Agency - Wikipedia</a></li>
<li><a href="https://pulse2.com/kde-e1-million-investment-from-sovereign-tech-fund-to-strengthen-open-source-infrastructure/">KDE: €1 Million Investment From Sovereign Tech Fund To Strengthen Open Source Infrastructure - Pulse 2.0</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#KDE`, `#funding`, `#desktop environment`, `#security`

---

<a id="item-21"></a>
## [UK AI Institute Finds GPT-5.5 Matches Claude Mythos in Vulnerability Detection](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html) ⭐️ 7.0/10

The UK's AI Security Institute evaluated OpenAI's generally available GPT-5.5 model and found its cybersecurity vulnerability detection capabilities are comparable to Anthropic's Claude Mythos model. This comparison by a reputable government institute validates that high-level AI cybersecurity capabilities are becoming accessible across major providers, and suggests that smaller, cheaper models can achieve similar results with better prompting scaffolding. A key nuance highlighted is that a smaller, cheaper AI model can also perform as well as these top-tier models if provided with more sophisticated prompting scaffolding from the user.

rss · Schneier on Security · May 13, 11:03

**Background**: The UK AI Security Institute (AISI) is a government body that evaluates the safety and capabilities of advanced AI systems. Claude Mythos is Anthropic's flagship AI model, which has been highlighted for its powerful cybersecurity and vulnerability detection capabilities. In AI development, 'scaffolding' refers to the structured prompts, tools, and frameworks provided to a language model to guide it toward a specific, complex task.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model ) - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html">Anthropic Claims Its New A.I. Model , Mythos , Is a Cybersecurity...</a></li>
<li><a href="https://cs191.stanford.edu/projects/Ji,+Junyi+(Joey)_CS191W.pdf">[PDF] CTF Agents: An Analysis of Different Agent Scaffolds for Cybersecurity Tasks</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#cybersecurity`, `#vulnerability detection`, `#LLM evaluation`, `#AI capabilities`

---

<a id="item-22"></a>
## [NIH Staffing Shortage Threatens to Cut New Research Grants This Year](https://www.nature.com/articles/d41586-026-01537-1) ⭐️ 7.0/10

The US National Institutes of Health (NIH) is facing such severe staffing shortages in some of its units that they are being forced to prioritize mandated grant renewals over issuing new awards. This situation could significantly reduce funding for new scientific research projects in the US, impacting the broader research ecosystem, including communities reliant on federal grants such as those in AI, machine learning, and systems research. The understaffed units are focusing on mandated grant renewals, which are contractual obligations, as they lack the capacity to process and evaluate new applications at the normal rate.

rss · Nature · May 14, 00:00

**Background**: The National Institutes of Health (NIH) is the primary agency of the United States government responsible for biomedical and public health research, and is the largest public funder of such research in the world. Research grants are competitive awards that fund specific scientific projects, and a reduction in new grants can slow down scientific progress and affect career opportunities for researchers.

**Tags**: `#research-funding`, `#public-policy`, `#science-policy`, `#NIH`

---

<a id="item-23"></a>
## [Old T cells impair brain function; blocking them improves memory in mice.](https://www.nature.com/articles/d41586-026-01531-7) ⭐️ 7.0/10

A new study published in Nature found that aged T cells in the blood secrete an enzyme that impairs brain function in mice, and that blocking these cells can improve memory. This discovery identifies a specific immune cell mechanism driving cognitive aging, offering a potential therapeutic target for preventing or treating age-related cognitive decline in humans. The research demonstrates a direct link between the immune system and brain aging in an animal model, but it is a single mouse study, meaning the findings need to be replicated and their applicability to humans remains to be proven.

rss · Nature · May 14, 00:00

**Background**: Cognitive aging refers to the gradual decline in mental abilities such as memory, attention, and processing speed that occurs with increasing age. T cells are a type of white blood cell that plays a central role in the body's adaptive immune response, and their function is known to change with age. Understanding how immune system changes contribute to brain aging is a key area of research in neuroscience and gerontology.

**Tags**: `#neuroscience`, `#aging`, `#immunology`, `#cognitive-decline`, `#medical-research`

---

<a id="item-24"></a>
## [RTX 5090 eGPU Successfully Used with M4 MacBook Air for Gaming and AI](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 6.0/10

A user successfully connected an external NVIDIA RTX 5090 GPU to an M4 MacBook Air, achieving notable performance gains in gaming benchmarks and local large language model (LLM) inference, a setup previously considered unsupported on Apple Silicon. This setup challenges Apple's official stance that eGPUs require Intel processors and demonstrates a viable path for significantly boosting graphics and AI inference performance on modern MacBooks, which could expand their utility for gamers and developers working with local models. The article notes that while game benchmarks showed improvement, the most significant gains were in LLM inference, particularly addressing the slow prompt processing (prefill) speed inherent to Apple Silicon. The process requires specific hardware and software workarounds, and macOS's poor OpenGL support remains a barrier for many games.

hackernews · allenleee · May 14, 15:47 · [Discussion](https://news.ycombinator.com/item?id=48137145)

**Background**: Apple has officially stated that external GPU (eGPU) support requires a Mac with an Intel processor and typically supports only AMD GPUs. Apple Silicon Macs use a unified memory architecture and lack the traditional PCIe support that eGPUs rely on, making NVIDIA eGPU compatibility a major technical hurdle that the community has been working to overcome through unofficial drivers and workarounds.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reddit.com/r/mac/comments/1kj6ull/massive_news_amd_egpu_support_on_apple_silicon/">Massive news: AMD eGPU support on Apple Silicon!! : r/mac - Reddit</a></li>
<li><a href="https://techenclave.com/t/useful-info-using-nvidia-amd-egpus-on-apple-silicon-m1-m2-m3-for-ai/423407">Useful info: Using NVIDIA/AMD eGPUs on Apple Silicon (M1/M2/M3) for AI - TechEnclave</a></li>
<li><a href="https://news.ycombinator.com/item?id=47640380">Apple approves driver that lets Nvidia eGPUs work with Arm Macs | Hacker News</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights that while the technical achievement is impressive, Apple has not officially supported this functionality, with one commenter noting their long-standing requests for GPU passthrough in virtual machines were ignored. Others point out the significant practical value for local LLM inference over gaming, and that alternative, less complex solutions like adding Vulkan support for specific games might be preferable.

**Tags**: `#eGPU`, `#Apple Silicon`, `#Mac gaming`, `#LLM inference`, `#hardware hacking`

---

<a id="item-25"></a>
## [Technical Article on HDD Firmware Hacking and Community Insights](https://icode4.coffee/?p=1465) ⭐️ 6.0/10

A technical article details methods for hacking HDD firmware, while community discussion shares practical techniques for bypassing vendor obfuscation, such as exploiting Linux SSD firmware updaters to extract decrypted code. Understanding firmware hacking techniques is significant for security researchers and enthusiasts to assess hardware vulnerabilities and improve device security, potentially exposing weaknesses in vendor protections across storage devices. Key details include using seccomp to intercept system calls in vendor updaters to obtain decrypted firmware, and references to projects like the reverse-engineering of Samsung's 840 EVO SSD firmware before encryption was implemented.

hackernews · jsploit · May 14, 16:19 · [Discussion](https://news.ycombinator.com/item?id=48137553)

**Background**: Firmware is low-level software that controls hardware devices like hard disk drives (HDDs) and solid-state drives (SSDs), and vendors often obfuscate or encrypt it to prevent unauthorized modifications or reverse engineering. Hardware security involves protecting devices from attacks, and firmware hacking can reveal vulnerabilities or enable customization. Community forums and technical blogs are common venues for sharing such reverse-engineering knowledge.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nozominetworks.com/blog/reverse-engineering-obfuscated-firmware-for-vulnerability-analysis">How to Reverse Engineer Obfuscated Firmware for Vulnerability Analysis</a></li>

</ul>
</details>

**Discussion**: Community members share experiences with firmware updates for fun and optimization, highlight trivial vendor obfuscation methods that can be easily bypassed, and reference related projects like Samsung SSD firmware decompilation, indicating a practical and collaborative approach to hardware hacking.

**Tags**: `#firmware`, `#reverse-engineering`, `#hardware-security`, `#storage-devices`

---

<a id="item-26"></a>
## [Datasette Plugin Released for IP-Based Rate Limiting Against Crawlers](https://simonwillison.net/2026/May/14/datasette-ip-rate-limit/#atom-everything) ⭐️ 6.0/10

Simon Willison announced the release of datasette-ip-rate-limit 0.1a0, a new plugin designed to protect Datasette instances by rate-limiting requests from specific IP addresses. This plugin provides a practical solution for Datasette users to defend their sites from poorly-behaved web crawlers that can overwhelm server resources and disrupt services for legitimate users. The plugin is highly configurable, allowing settings such as per-IP request limits over a time window, temporary blocking durations, and exempting certain paths like static assets. The author used Codex (GPT-5.5 xhigh) to help build it and has deployed it in production on the datasette.io site.

rss · Simon Willison · May 14, 04:10

**Background**: Datasette is an open-source tool for exploring and publishing data, often used to serve databases as interactive websites or APIs. Rate limiting is a common technique used in web services to control the amount of incoming traffic from a single source, preventing abuse and ensuring service availability. Aggressive web crawlers can generate excessive load by making rapid, automated requests, which can degrade performance for all users.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/May/14/datasette-ip-rate-limit/">Release: datasette - ip - rate - limit 0.1a0 | Simon Willison’s Weblog</a></li>
<li><a href="https://pypi.org/project/datasette-ip-rate-limit/">Rate limit Datasette requests by client IP address</a></li>

</ul>
</details>

**Tags**: `#Datasette`, `#web-scraping`, `#API-security`, `#open-source`

---

<a id="item-27"></a>
## [Critique Highlights Ambiguity in 'AI Agents' Terminology](https://simonwillison.net/2026/May/13/boris-mann/#atom-everything) ⭐️ 6.0/10

Boris Mann, quoted by Simon Willison, argued that the phrase '11 AI agents' is as vague and unhelpful as saying '11 spreadsheets,' underscoring a lack of precision in how AI agents are discussed. This critique points to a broader issue in the AI industry where jargon and imprecise language can obscure the actual capabilities and functions of systems, potentially leading to confusion among developers and stakeholders. The comparison to '11 spreadsheets' or '11 browser tabs' suggests that simply counting AI agents without defining their roles, autonomy, or interaction patterns provides little meaningful information about a system's architecture or utility.

rss · Simon Willison · May 13, 16:15

**Background**: An 'AI agent' generally refers to a software system that can perceive its environment, make decisions, and take actions to achieve specific goals with some degree of autonomy. However, the term is used loosely in the industry to describe a wide range of systems, from simple scripts to complex multi-agent frameworks, leading to ambiguity.

**Tags**: `#ai-agents`, `#terminology`, `#ai-commentary`, `#industry-jargon`

---

<a id="item-28"></a>
## [CSP Allow-list Experiment Manages Sandbox Permissions Dynamically](https://simonwillison.net/2026/May/13/csp-allow/#atom-everything) ⭐️ 6.0/10

Simon Willison built a tool that demonstrates intercepting Content Security Policy (CSP) errors within a sandboxed iframe using a custom `fetch()` function, passing these errors to a parent window which then prompts the user to dynamically add blocked domains to an allow-list and refresh the page. This experiment provides a practical, interactive approach to managing CSP, which is notoriously difficult to configure correctly, by allowing users to build a policy through actual application behavior rather than guessing in advance. The tool was built using GPT-5.5 xhigh running in the Codex desktop app, and it relies on a sandboxed iframe with a strict CSP that initially blocks all external connections.

rss · Simon Willison · May 13, 04:50

**Background**: Content Security Policy (CSP) is a security standard designed to prevent attacks like cross-site scripting (XSS) by restricting the sources from which a web page can load resources. A sandboxed iframe uses the `sandbox` attribute to severely limit an embedded frame's capabilities, providing a layer of isolation. A common challenge with CSP is creating accurate allow-lists, as policies that are too permissive offer little protection, while overly strict ones break legitimate application functionality.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Content_Security_Policy">Content Security Policy - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP">Content Security Policy (CSP) - HTTP - MDN Web Docs</a></li>
<li><a href="https://simonwillison.net/2026/May/13/csp-allow/">Tool: CSP Allow-list Experiment | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Tags**: `#web-security`, `#sandboxing`, `#Content-Security-Policy`, `#javascript`, `#experimental-tool`

---

<a id="item-29"></a>
## [Red Hat's AI Desktop Proposal for Fedora Faces Community Opposition and Vote Reversal](https://lwn.net/Articles/1071949/) ⭐️ 6.0/10

A Red Hat-led proposal to create a Fedora 'AI Developer Desktop' with out-of-tree kernel driver and AI toolkit support was initially approved by the Fedora Council but was sent back for reconsideration after a council member changed their vote against it. This dispute highlights fundamental tensions within the open-source community regarding the adoption of proprietary or out-of-tree components for AI tooling, and it reveals challenges in community governance when a major corporate sponsor's initiatives conflict with long-standing community principles. The proposal faced over a month of 'sometimes heated discussion' and the initial council vote to approve it was reversed by a last-minute change of heart from council member Justin Wheeler, at least temporarily blocking the initiative.

rss · LWN.net · May 13, 16:05

**Background**: Fedora is a popular Linux distribution sponsored by Red Hat and is known for its strong commitment to free and open-source software principles. 'Out-of-tree' kernel drivers are modules not included in the official Linux kernel source tree, which is often discouraged in distributions like Fedora. The proposed 'AI Developer Desktop' likely aimed to bundle specific proprietary or non-free AI frameworks and drivers to simplify AI development, which can conflict with strict open-source policies.

**Discussion**: The content indicates the proposal generated significant community opposition from long-time Fedora members, leading to 'sometimes heated discussion', though no specific comments or detailed viewpoints are provided in the available text.

**Tags**: `#open-source`, `#Linux`, `#AI-tools`, `#governance`, `#Fedora`

---