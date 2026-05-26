---
layout: default
title: "Horizon Summary: 2026-05-26 (ZH)"
date: 2026-05-26
lang: zh
---

> From 48 items, 21 important content pieces were selected

---

1. [AI（Claude）发现关键 macOS 内核漏洞 CVE-2026-28952。](#item-1) ⭐️ 8.0/10
2. [2026 年 Linux 峰会讨论使用大语言模型审查内核补丁](#item-2) ⭐️ 8.0/10
3. [软件自由保护协会因 Bambu Lab 违反 AGPLv3 协议，启动逆向工程项目作为回应](#item-3) ⭐️ 8.0/10
4. [z386：基于原始微码的开源 FPGA 版 80386 处理器](#item-4) ⭐️ 8.0/10
5. [神经科学家认为脑理论必须超越计算机隐喻](#item-5) ⭐️ 8.0/10
6. [Mullvad VPN 正式推出针对出口 IP 指纹追踪的修复方案。](#item-6) ⭐️ 7.0/10
7. [加利福尼亚州提议豁免 Linux 系统适用其即将出台的年龄验证法](#item-7) ⭐️ 7.0/10
8. [梵蒂冈发布新通谕探讨人工智能伦理，呼应历史语境](#item-8) ⭐️ 7.0/10
9. [针对 DeepSeek V4 的新工具缓存命中率达 99.82%，可将 AI 推理成本降低 80%](#item-9) ⭐️ 7.0/10
10. [提案改进 Linux 内存控制器以支持分层内存系统](#item-10) ⭐️ 7.0/10
11. [使用唯一名称标识符扩展视图过渡](#item-11) ⭐️ 7.0/10
12. [玻璃通孔：玻璃基板应用于 PCB 道路上的关键挑战](#item-12) ⭐️ 7.0/10
13. [倡导以更慢速、更注重质量的迭代方式使用 AI 编程](#item-13) ⭐️ 6.0/10
14. [理解沙米尔秘密共享技术](#item-14) ⭐️ 6.0/10
15. [挪威国家图书馆部署 2PB 华为存储用于主权 LLM](#item-15) ⭐️ 6.0/10
16. [编程书籍销量下降，学习方式随之演变](#item-16) ⭐️ 6.0/10
17. [林纳斯·托瓦兹发布 Linux 7.1-rc5 预发布版，并警告不必要的修复](#item-17) ⭐️ 6.0/10
18. [荷兰逮捕两人并查封 800 台服务器，打击重大网络犯罪](#item-18) ⭐️ 6.0/10
19. [遗失的 Amiga Unix 版本重现，为复古计算史补遗](#item-19) ⭐️ 6.0/10
20. [创客 3D 打印经典 Windows 弹球游戏的真实世界版本](#item-20) ⭐️ 6.0/10
21. [解析英特尔失败的 iAPX432 架构](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [AI（Claude）发现关键 macOS 内核漏洞 CVE-2026-28952。](https://support.apple.com/en-us/127115) ⭐️ 8.0/10

Anthropic 的 Claude AI 模型与 Calif.io 合作，在 Apple macOS 中发现了一个关键的内核漏洞（CVE-2026-28952），该漏洞是一个导致拒绝服务问题的整数溢出。 此事件凸显了 AI 模型在自动化安全研究中新兴且重要的角色，可能加速漏洞发现，同时也引发了关于苹果公司内部是否像谷歌等竞争对手那样广泛使用此类工具的疑问。 该漏洞影响了多个 macOS 版本，包括 Sequoia 15.7.7 和 Sonoma 14.8.7，而不仅仅是最新的 macOS Tahoe 26.5，修复方法是改进输入验证。

hackernews · dragonsenseiguy · May 25, 23:40 · [社区讨论](https://news.ycombinator.com/item?id=48273169)

**背景**: macOS 内核（XNU）是苹果操作系统的核心。AI 驱动的漏洞发现使用像 Claude 这样的大型语言模型来自动寻找软件代码中的安全缺陷，这是 Anthropic 一直在开发的能力。谷歌等公司已公开展示了大量内部发现的漏洞，为主动安全树立了基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.apple.com/en-us/127116">About the security content of macOS Sequoia 15.7.7 - Apple Support</a></li>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://www.anthropic.com/product/security">Anthropic's agentic solution for vulnerability detection | Claude ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示该漏洞是由 Calif.io 与 Anthropic 的 Claude 合作发现的，Calif.io 的一位研究员澄清这与他们独立的 MIE 攻击研究无关。其他用户则讨论了苹果的更新做法，一些人批评了过大的更新文件，并指出该漏洞也影响旧版 macOS。

**标签**: `#cybersecurity`, `#AI-research`, `#macOS`, `#vulnerability`, `#kernel`

---

<a id="item-2"></a>
## [2026 年 Linux 峰会讨论使用大语言模型审查内核补丁](https://lwn.net/Articles/1073583/) ⭐️ 8.0/10

在 2026 年 Linux 存储、文件系统、内存管理和 BPF 峰会的一场专题全体会议上，探讨了使用大语言模型审查 Linux 内核补丁的方法，这一议题在社区内引发了广泛关注。 此次讨论凸显了将人工智能融入关键且耗时的内核开发流程的重大尝试，有望提升整个开源生态系统的补丁审查效率和质量。 会议由 Roman Gushchin、Chris Mason、Josef Bacik 和 Sasha Levin 等知名内核开发者主持，讨论非常热烈，以至于当天晚些时候在文件系统专题轨道上又安排了一场后续会议。

rss · LWN.net · May 25, 21:27

**背景**: Linux 内核是 Linux 操作系统的核心组件，其开发依赖于对数千名贡献者提交的代码更改（补丁）进行严格审查的流程。大语言模型（LLM）是基于海量文本数据集训练的先进人工智能系统，能够理解和生成类人文本，目前正被探索用于自动化或辅助代码审查任务。

**标签**: `#LLMs`, `#Linux Kernel`, `#Code Review`, `#Open Source`, `#Software Development`

---

<a id="item-3"></a>
## [软件自由保护协会因 Bambu Lab 违反 AGPLv3 协议，启动逆向工程项目作为回应](https://lwn.net/Articles/1074286/) ⭐️ 8.0/10

软件自由保护协会（SFC）发起了“baltobu”逆向工程项目，旨在重新实现 Bambu Lab 的专有代码，并开始托管 Orca Slicer 软件的一个分支版本，以应对其法律威胁。 这是对 AGPLv3 许可证的一次重大执法行动，直接挑战了公司在 3D 打印生态系统中的不合规及潜在的反竞争行为，可能为维护软件自由和维修权树立先例。 此次回应的导火索是 Bambu Lab 未能为其基于 AGPLv3 许可的切片软件修改提供源代码，并对旨在实现与 Bambu 打印机互操作性的 Orca Slicer 分支作者 Paweł Jarczak 发出威胁。

rss · LWN.net · May 25, 16:48

**背景**: GNU Affero 通用公共许可证（AGPLv3）是一种强互惠性许可证，它将 GPL 的要求扩展到通过网络使用的软件，强制要求向用户提供完整的对应源代码。为实现软件互操作性而进行的逆向工程通常受欧盟《软件指令》等法律框架的保护。Orca Slicer 是一款流行的开源 3D 打印切片软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License">GNU Affero General Public License - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reverse_engineering">Reverse engineering - Wikipedia</a></li>
<li><a href="https://github.com/OrcaSlicer/OrcaSlicer">GitHub - OrcaSlicer/OrcaSlicer: G-code generator for 3 D printers ...</a></li>

</ul>
</details>

**标签**: `#open-source-licensing`, `#AGPL`, `#software-freedom`, `#3D-printing`, `#legal-enforcement`

---

<a id="item-4"></a>
## [z386：基于原始微码的开源 FPGA 版 80386 处理器](https://hackaday.com/2026/05/25/z386-an-open-source-80386-built-around-original-microcode/) ⭐️ 8.0/10

开发者[nand2mario]发布了 z386，这是一个用 SystemVerilog 编写的、为 FPGA 设计的开源 80386 兼容 CPU 内核，其独特之处在于它构建在原始的 Intel 386 微码之上。 该项目为复古计算和处理器架构教育提供了一种新颖且具有历史价值的方法，使爱好者能够研究一个经典的 x86 CPU 实现，并与原始固件逻辑直接关联。 该实现是一个面向 FPGA 的紧凑型 CPU 内核，已在 GitHub 上开源。其对原始微码的使用，为深入理解处理器控制单元如何执行复杂的 x86 指令提供了独特视角。

rss · Hackaday · May 25, 23:00

**背景**: Intel 80386 于 1985 年推出，是一款具有里程碑意义的 32 位 x86 处理器。微码是 CPU 内部的一个低级指令层，它将高级机器指令（如 x86 指令）转换为处理器内部的、硬件级的操作。在 FPGA（现场可编程门阵列）上实现 CPU，涉及配置数字逻辑芯片以模仿处理器架构，而使用原始微码来完成此举在技术上是一种新颖的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nand2mario/z386">GitHub - nand2mario/z386: Compact 80386 CPU in SystemVerilog</a></li>
<li><a href="https://nand2mario.github.io/posts/2026/z386/">z386: An Open-Source 80386 Built Around Original Microcode - Small...</a></li>

</ul>
</details>

**标签**: `#fpga`, `#retrocomputing`, `#cpu-design`, `#open-source-hardware`, `#x86`

---

<a id="item-5"></a>
## [神经科学家认为脑理论必须超越计算机隐喻](https://www.nature.com/articles/d41586-026-01619-0) ⭐️ 8.0/10

在 2026 年发表于《自然》杂志的一篇文章中，一位神经科学家提出，神经科学领域需要进行根本性的范式转移，不再将大脑视为计算机。 这一观点挑战了神经科学中一个长期存在的核心隐喻，并表明理解意识和认知的进展需要全新的理论框架，这可能重新引导未来的研究方向。 这一批评直指计算隐喻的局限性，认为尽管大脑处理信息，但将其比作被动的、顺序处理信息的处理器的类比，可能不足以对高级认知形成有意义的理解。

rss · Nature · May 25, 00:00

**背景**: “大脑如计算机”的隐喻在神经科学和认知科学领域占据主导地位数十年，将心智框定为信息处理、算法和表征。批评者认为，这种方法虽然强大，但可能过度简化了大脑的具身性、动态性以及可能的非计算本质。生物自然主义和整合信息理论等替代理论为意识提出了不同的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2022.810358/full">Frontiers | The Brain-Computer Metaphor Debate Is Useless: A Matter of Semantics</a></li>
<li><a href="https://www.theguardian.com/science/2020/feb/27/why-your-brain-is-not-a-computer-neuroscience-neural-networks-consciousness">Why your brain is not a computer | Neuroscience | The Guardian</a></li>
<li><a href="https://oecs.mit.edu/pub/zf1nbs6d/release/1">Consciousness and AI · Open Encyclopedia of Cognitive Science</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#brain theory`, `#computational metaphor`, `#consciousness`, `#paradigm shift`

---

<a id="item-6"></a>
## [Mullvad VPN 正式推出针对出口 IP 指纹追踪的修复方案。](https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout) ⭐️ 7.0/10

Mullvad VPN 正在为其服务器部署一种分配出口 IP 地址的新方法，该方法将防止用户活动在不同的 VPN 服务器之间或与同一服务器上的其他用户被关联起来。 此修复方案解决了一个重大的隐私漏洞，该漏洞可能导致用户在不同的 VPN 会话中被追踪，直接影响了 VPN 服务的核心隐私承诺，并展示了 Mullvad 对安全问题的积极响应态度。 该修复正在其服务器网络中逐步推出，建议切换服务器的用户立即登出并重新登录以重新生成其 WireGuard 密钥。新方法确保使用一个出口 IP 地址不会泄露在另一台服务器上或由其他用户使用的是哪个出口地址的信息。

hackernews · Cider9986 · May 25, 17:45 · [社区讨论](https://news.ycombinator.com/item?id=48269580)

**背景**: 出口 IP 指纹追踪是一种技术，指 VPN 服务器分配给用户的特定 IP 地址可用于在不同服务器或会话之间追踪其活动，即使他们使用的是同一个 VPN 账户。这之所以可能，是因为传统的分配方法可能会使用可预测的内部 IP 地址，从而创建出可链接的模式。VPN 提供商的目标是让所有用户流量看起来都来自一个共享的匿名 IP 地址池。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mullvad.net/en/blog/exit-ip-fingerprinting-between-vpn-servers">Exit IP fingerprinting between VPN servers | Mullvad VPN</a></li>
<li><a href="https://www.techradar.com/vpn/vpn-services/mullvad-to-patch-vpn-fingerprinting-issue-to-stop-your-activity-from-being-tracked-across-servers">Mullvad to patch VPN fingerprinting issue to stop your activity from being tracked across servers | TechRadar</a></li>
<li><a href="https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout">Exit IP VPN servers mitigation rollout</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，用户对 Mullvad 迅速回应此问题表示惊讶和赞赏。讨论中也涉及其他隐私解决方案，例如使用带有随机模式的 Mullvad 浏览器，或者浏览器需要伪造一致的设备指纹以对抗追踪的需求。

**标签**: `#VPN`, `#privacy`, `#security`, `#fingerprinting`, `#online-tracking`

---

<a id="item-7"></a>
## [加利福尼亚州提议豁免 Linux 系统适用其即将出台的年龄验证法](https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law) ⭐️ 7.0/10

加利福尼亚州一名议员提出修正案，提议将 Linux 操作系统从该州即将出台的年龄验证法中豁免，该法律原计划要求操作系统收集用户年龄信息。 此举意义重大，因为它直接回应了社区的强烈反对，并保护了开源的 Linux 生态系统免受潜在繁重且侵犯隐私的合规负担。 该豁免修正案由起草原始法律的同一议员提出，这表明立法者直接回应了批评，即认为将此类强制要求应用于操作系统不切实际且范围过广。

hackernews · rbanffy · May 25, 18:19 · [社区讨论](https://news.ycombinator.com/item?id=48269961)

**背景**: 这项法律是加利福尼亚州一项旨在为互联网用户实施年龄验证以保护未成年人的法案。最初提案的措辞宽泛，可能被解释为包括操作系统，这引发了 Linux 和开源社区的强烈反对，他们认为这在技术上不可行，并对隐私和用户自由构成威胁。

**社区讨论**: 在线讨论显示出对法律起草过程的普遍质疑，评论询问究竟是谁起草了这项立法，并指出由于监管机构未能有效监管大公司，法律转而加重了消费者的负担。一些用户甚至尖刻地猜测，提出豁免是为了防止 Linux 开发者基于宪法第一修正案提出法律挑战。

**标签**: `#linux`, `#policy`, `#internet-regulation`, `#privacy`, `#open-source`

---

<a id="item-8"></a>
## [梵蒂冈发布新通谕探讨人工智能伦理，呼应历史语境](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything) ⭐️ 7.0/10

教皇利奥十四世颁布了名为《伟大的人类》的通谕，提出了梵蒂冈在人工智能时代维护人类尊严的伦理框架。 这是来自一个重要的非技术性全球道德权威的重大干预，提供了一个结构化的伦理视角，可能影响围绕人工智能发展和融入社会的更广泛辩论及政策考量。 这份通谕的文笔因其异常清晰且易于理解（即使对非天主教徒而言）而受到赞扬，它直接与教皇利奥十三世 1891 年关于第一次工业革命社会动荡的通谕《新事》建立了历史联系。

rss · Simon Willison · May 25, 23:58

**背景**: 教皇通谕是教皇写给主教和更广泛教会团体的正式信函，概述教会对特定议题的教导和指引。教皇利奥十四世选择此名以纪念利奥十三世，后者于 1891 年颁布的里程碑式通谕《新事》处理了工业革命期间资本与劳动的权利和义务问题，奠定了现代天主教社会训导的基础。新通谕明确将当前的人工智能时代定性为需要类似道德回应的另一场‘工业革命’。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Catholic_social_teaching">Catholic social teaching - Wikipedia</a></li>
<li><a href="https://www.vatican.va/content/leo-xiii/en/encyclicals/documents/hf_l-xiii_enc_15051891_rerum-novarum.html">Encyclical Rerum Novarum of Leo XIII , 15 May 1891</a></li>
<li><a href="https://en.wikipedia.org/wiki/Encyclical">Encyclical - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#societal impact`, `#Vatican`, `#enclicical`, `#policy`

---

<a id="item-9"></a>
## [针对 DeepSeek V4 的新工具缓存命中率达 99.82%，可将 AI 推理成本降低 80%](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247892730&idx=1&sn=3da5702f8033c5ed6690bd71d90a581d) ⭐️ 7.0/10

一款专门针对 DeepSeek V4 优化的新工具已发布，其在推理任务中实现了高达 99.82%的缓存命中率，这相当于最高可带来 80%的成本节约。 这一在缓存优化上的突破，显著提升了运行 DeepSeek V4 等大语言模型的成本效益，对于大规模部署 AI 以管理计算开支的开发者和企业至关重要。 该工具被描述为一个专为 DeepSeek 打造的“终端编程 Harness”，报告的 99.82%命中率表明其前缀缓存或类似策略的实现非常高效，但提供的内容中并未详细说明具体的技术方法。

rss · 量子位 · May 25, 04:27

**背景**: DeepSeek 是一个大语言模型系列，其中 V4 是最新版本，以其庞大的规模（例如高达 1 万亿参数）而闻名。推理缓存是一种优化技术，它存储并重用之前的计算结果（如键值缓存），以避免冗余处理，从而大幅降低延迟和成本。“编程 Harness”是模型周围的一个操作系统层，负责管理上下文、工具和控制循环，以优化其在编程等特定任务中的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem">Serving DeepSeek - V 4 : why million-token context is an inference...</a></li>
<li><a href="https://inferencesystemsauthority.com/inference-caching-strategies">Inference Caching Strategies for Speed... | Inference Systems Authority</a></li>
<li><a href="https://pinggy.io/blog/best_ai_harnesses_to_supercharge_llm_models/">AI Harness Engineering: The Layer That Makes Your LLM Applications...</a></li>

</ul>
</details>

**社区讨论**: 提供的内容中不包含社区评论，因此无法总结讨论内容。

**标签**: `#AI`, `#inference optimization`, `#caching`, `#DeepSeek`, `#cost efficiency`

---

<a id="item-10"></a>
## [提案改进 Linux 内存控制器以支持分层内存系统](https://lwn.net/Articles/1073400/) ⭐️ 7.0/10

Linux 内核开发者 Joshua Hahn 在 2026 年 Linux 存储、文件系统、内存管理和 BPF 峰会上提出一项改进提案，旨在让控制组内存控制器更好地支持分层内存系统，因为该控制器最初并非为此设计。 这一改进意义重大，因为现代硬件越来越多地采用分层内存架构，而一个正常工作的内存控制器对于此类系统中的资源分配和隔离至关重要，可以防止任务间的干扰。 控制组的内存控制器负责资源分配、记账和防止干扰，但它目前缺乏在不同内存层级间有效管理内存的特定逻辑。

rss · LWN.net · May 25, 15:03

**背景**: 控制组（cgroups）是 Linux 内核的一个功能，用于限制、记账和隔离一组进程的资源使用（如 CPU、内存和 I/O）。分层内存系统使用具有不同速度和容量（如快速的 DRAM 和较慢的持久内存）的内存技术层次结构，以优化性能和成本。Linux 峰会的内存管理分论坛是讨论此类内核改进的关键场所。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cgroups">cgroups - Wikipedia</a></li>
<li><a href="https://www.kernel.org/doc/html/v4.18/admin-guide/cgroup-v2.html">Control Group v2 — The Linux Kernel documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_hierarchy">Memory hierarchy - Wikipedia</a></li>

</ul>
</details>

**标签**: `#linux-kernel`, `#memory-management`, `#cgroups`, `#tiered-memory`, `#systems-programming`

---

<a id="item-11"></a>
## [使用唯一名称标识符扩展视图过渡](https://css-tricks.com/cross-document-view-transitions-part-2/) ⭐️ 7.0/10

文章提出了一种在多个元素之间管理 CSS `view-transition-name` 属性的实用解决方案，以防止在扩展过程中产生难以管理的伪元素选择器爆炸问题。 这对于使用视图过渡 API 实现复杂动画的开发者来说很重要，因为它解决了一个常见的扩展瓶颈，该瓶颈会使代码库变得难以驾驭和维护，从而确保为富交互式 Web 应用程序提供更顺畅的开发体验。 核心问题是页面上的每个 `view-transition-name` 都必须是唯一的，并且每个名称都需要在 CSS 中有对应的伪元素选择器，这会导致选择器膨胀。来自 CSS-Tricks 的这篇文章重点介绍了在大规模情况下高效管理这些唯一标识符的策略。

rss · CSS-Tricks · May 25, 13:46

**背景**: 视图过渡 API 是一个 Web 平台功能，它简化了在网站的不同状态或视图之间创建动画过渡的过程，由 CSS 动画驱动。其一个关键机制是为元素分配一个 `view-transition-name` CSS 属性，以便对其过渡快照和动画进行精细控制。尽管功能强大，但在实际应用中，为大量元素管理唯一名称会带来显著的扩展挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API">View Transition API - Web APIs | MDN</a></li>
<li><a href="https://www.patterns.dev/vanilla/view-transitions/">Animating View Transitions</a></li>

</ul>
</details>

**标签**: `#CSS`, `#Web Development`, `#Animation`, `#View Transitions API`, `#Frontend`

---

<a id="item-12"></a>
## [玻璃通孔：玻璃基板应用于 PCB 道路上的关键挑战](https://hackaday.com/2026/05/25/through-glass-vias-and-the-long-road-to-glass-substrates/) ⭐️ 7.0/10

本文探讨了制造可靠玻璃通孔（TGVs）的具体工程难题，这仍然是阻碍玻璃基板在先进电路板和半导体封装中广泛应用的主要瓶颈。 克服 TGV 挑战至关重要，因为玻璃基板具有更优的材料特性，如更好的热稳定性和更低的电气损耗，有望推动下一代高性能电子封装的发展。 TGV 技术通过结合激光和蚀刻工艺在玻璃上制造微小的垂直电气连接，康宁等公司正在研究该技术用于半导体封装，因为玻璃具有更低的信号损耗。

rss · Hackaday · May 26, 02:00

**背景**: 玻璃基板正逐渐成为 PCB 和芯片封装中传统有机基板（如环氧树脂层压板）的潜在替代品，其优势包括更高的耐温性、更好的光刻平整度以及更佳的尺寸稳定性。玻璃通孔（TGVs）是一个基本构件，类似于 3D 芯片堆叠中的硅通孔（TSVs），为基于玻璃的中介层或基板中的层间提供必要的电气路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Via_(electronics)">Via (electronics) - Wikipedia</a></li>
<li><a href="https://www.pcbaaa.com/through-glass-viatgv-a-critical-technology-for-advanced-packaging/">Through - glass Via( TGV ) - A Critical Technology For Advanced...</a></li>
<li><a href="https://avecas.in/glass-substrates-vs-organic-ai-interconnects/">Glass Substrates vs . Organic : Why the Industry is Shifting... - Avecas</a></li>

</ul>
</details>

**标签**: `#semiconductor_packaging`, `#materials_science`, `#electronics`, `#glass_substrate`, `#PCB`

---

<a id="item-13"></a>
## [倡导以更慢速、更注重质量的迭代方式使用 AI 编程](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/) ⭐️ 6.0/10

一篇文章主张使用 AI 编程助手应采用更慢速、迭代的过程，专注于生产更高质量的代码，而不是追求速度最大化。 这一观点挑战了 AI 工具主要加速开发的主流叙事，强调其价值也可以通过仔细、迭代的改进来提升代码质量。 该方法包括多轮审查和改进，例如使用一个 AI 模型进行设计，另一个模型进行代码审查以发现边界情况，一些实践者发现这增加了总体开发时间但改善了最终产出。

hackernews · signa11 · May 25, 23:16 · [社区讨论](https://news.ycombinator.com/item?id=48272984)

**背景**: AI 编程助手由大型语言模型（LLMs）驱动，被广泛用于自动化代码生成和加速软件开发。普遍预期是这些工具将使编程更快、更高效。

**社区讨论**: 讨论中的实践者分享了迭代 AI 工作流的经验，一些人同意他们在审查循环中花费的时间比手动编码多，但认为提高了代码质量的价值。另一些人反驳了速度是唯一目标的观点，指出 AI 工具可以产生不同水平的代码质量，其使用是细致入微的。

**标签**: `#AI-assisted programming`, `#software development workflow`, `#code quality`, `#LLM applications`

---

<a id="item-14"></a>
## [理解沙米尔秘密共享技术](https://ente.com/blog/how-shamirs-secret-sharing-works/) ⭐️ 6.0/10

这是一篇教育性博文，以通俗易懂的方式解释了沙米尔秘密共享（SSS）这一基础密码学技术，而非报道一项新进展。 理解 SSS 很重要，因为它是阈值密码学的核心基础，能够将私钥等秘密安全地分发给多个参与方，从而增强加密货币钱包和密钥恢复等系统的安全性。 该技术依赖于多项式插值，特别是拉格朗日插值，将秘密分成多个份额，需要预设的阈值数量份额才能重建。它常与里德-所罗门码和多签名方案等其他方法进行比较，涉及信息论安全性和实现复杂性之间的权衡。

hackernews · subract · May 25, 22:37 · [社区讨论](https://news.ycombinator.com/item?id=48272715)

**背景**: 沙米尔秘密共享是由阿迪·沙米尔于 1979 年发明的一种密码学算法，它将一个秘密分成多个称为“份额”的部分。其关键特性是，达到阈值数量的任意份额子集可以重建原始秘密，而少于该阈值的份额则不泄露任何信息。这构成了阈值密码系统的基础，在这种系统中，密码操作可以集体执行，而无需在单个位置重建秘密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lagrange_polynomial">Lagrange polynomial - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Threshold_cryptosystem">Threshold cryptosystem - Wikipedia</a></li>
<li><a href="https://crypto.stackexchange.com/questions/95943/different-secret-sharing-schemes-instead-of-shamirs">Different secret sharing schemes instead of Shamir ' s ?</a></li>

</ul>
</details>

**社区讨论**: 社区成员讨论了该技术的教育价值，有人指出它可以在中学教授。关于其用于保护根 DNS 密钥的实际问题，人们将其复杂性与保险箱等物理安全措施进行了比较。此外，技术层面的讨论还将它与里德-所罗门码和全有或全无转换（AONT）进行了对比，强调了信息论安全性和有效载荷处理方面的差异。

**标签**: `#cryptography`, `#secret-sharing`, `#information-security`, `#educational`

---

<a id="item-15"></a>
## [挪威国家图书馆部署 2PB 华为存储用于主权 LLM](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910) ⭐️ 6.0/10

挪威国家图书馆（Nasjonalbiblioteket）正在使用一套 2PB 的华为闪存存储系统，以支持训练一个主权挪威语大语言模型（LLM）。该倡议由图书馆的 IT 平台主管在华为 2026 年 ID 论坛上介绍。 该项目体现了主权 AI 倡议日益增长的全球趋势，即各国寻求发展自身的 AI 能力，以保存大型、以英语为中心的模型可能无法充分捕捉的语言和文化细微差别。它凸显了即使拥有先进数字基础设施的国家也在投资国家 AI 主权。 其存储基础设施为华为闪存系统，训练依赖于一套相对适中的 HPE Cray 超级计算机，拥有 448 个 GPU 和超过 64,000 个 CPU 核心。一些社区成员质疑，与微调开源模型相比，该硬件规模是否足以支持完整的 LLM 训练。

hackernews · rbanffy · May 25, 19:37 · [社区讨论](https://news.ycombinator.com/item?id=48270770)

**背景**: 主权 AI 是指一个国家出于对数据主权、文化保护以及减少对外国技术供应商依赖的考量，而建设和控制自身 AI 模型及基础设施的战略努力。大语言模型（LLM）是基于海量文本数据训练的 AI 系统，用于生成和理解人类语言；当主要基于英语数据训练时，它们往往在其他语言和文化方面表现不佳或缺乏语境。通用闪存存储（UFS）是用于现代电子设备的高性能闪存规范，但此处很可能指的是华为的企业级闪存阵列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://e.huawei.com/en/products/storage/hybrid-flash-storage">OceanStor Hybrid Flash Storage | Huawei Enterprise</a></li>
<li><a href="https://byteswall.com/news/sovereign-ai-initiatives-propel-strategic-autonomy-and-national-resilience/">Sovereign AI Initiatives Propel Strategic Autonomy and... | BytesWall</a></li>

</ul>
</details>

**社区讨论**: 社区讨论观点不一；部分人认同主权 AI 对于文化和语言代表性的必要性，而另一些人则持怀疑态度，指出主要的 LLM 提供商可能已经在多语言数据上训练，且所描述的硬件可能不足以从头训练一个完整模型。一位挪威用户赞扬了国家图书馆出色的搜索界面，另一位用户则将此项目置于更广泛的、常被炒作的高管层“主权 AI”趋势背景下。

**标签**: `#sovereign AI`, `#LLM training`, `#national language models`, `#data storage`

---

<a id="item-16"></a>
## [编程书籍销量下降，学习方式随之演变](https://unix.foo/posts/nobody-cracks-open-a-programming-book/) ⭐️ 6.0/10

O'Reilly《Learning Go》的作者分享了销售数据，显示过去 13 个月里纸质书的销量总体呈下降趋势，月销量在 124 到 484 册之间波动。 这一趋势反映了开发者学习编程方式的广泛转变，从传统书籍转向在线资源，这对作者、出版商以及编程语言的复杂性都产生了影响，因为语言不再需要完全能被书籍消化。 作者指出，尽管销量下降，但历史上一直有波动，自 2021 年第一版以来总销量约为 2 万册，这表明市场并未消亡，而是在发生变化。

hackernews · zdw · May 25, 23:21 · [社区讨论](https://news.ycombinator.com/item?id=48273030)

**背景**: 传统上，编程书籍是学习一门语言的综合指南，以结构化的形式涵盖语法、惯用法和最佳实践。像谷歌这样的搜索引擎和像 Stack Overflow 这样的社区问答网站的兴起，提供了更快、更易获取的替代方案，让开发者能够按需学习特定任务。这种转变也使得编程语言能够变得更复杂，因为详细的文档可以在线维护，而不受印刷卷册的限制。

**社区讨论**: 社区提供了多样化的观点：一位评论者分享了具体的销售数据，显示销量有波动但长期下降；另一位则认为，书籍销量的下降解除了对语言复杂性的限制，导致像 C++这样的语言变得过于复杂，连专家都难以跟上。还有人反驳说，对于像 Rust 这样复杂的语言，通过书籍深入阅读对于掌握惯用法和细微之处仍然很有价值，这凸显了快速在线查询与专注、彻底学习之间的分歧。

**标签**: `#programming education`, `#book publishing`, `#software learning`, `#language complexity`, `#developer trends`

---

<a id="item-17"></a>
## [林纳斯·托瓦兹发布 Linux 7.1-rc5 预发布版，并警告不必要的修复](https://lwn.net/Articles/1074172/) ⭐️ 6.0/10

林纳斯·托瓦兹发布了 Linux 7.1-rc5 内核预发布版供测试，同时他对在发布周期后期提交如此多的琐碎驱动程序修复表示不满。 这标志着内核发布管理纪律可能发生转变，因为托瓦兹警告说他将在候选发布阶段拒绝非关键性修复，这可能影响未来内核开发人员提交补丁的方式。 托瓦兹明确指出，许多修复是由 AI 代码审查触发的，对于 rc5 阶段来说过于琐碎，他强调在发布周期的这个后期阶段只有回归修复才是适当的。

rss · LWN.net · May 24, 22:59

**背景**: Linux 内核采用基于时间的发布模型，在合并窗口期接受新功能，随后是几个用于错误修复的候选发布版（rc）。linux-next 树是一个暂存区，补丁在合并窗口期合并前会在此进行测试。预发布版或 rc 内核是面向开发人员和爱好者的测试用预发布版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kernel.org/releases.html">Active kernel releases</a></li>
<li><a href="https://www.kernel.org/doc/man-pages/linux-next.html">Working with linux - next</a></li>

</ul>
</details>

**标签**: `#linux-kernel`, `#open-source`, `#software-development`, `#release-management`

---

<a id="item-18"></a>
## [荷兰逮捕两人并查封 800 台服务器，打击重大网络犯罪](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/) ⭐️ 6.0/10

荷兰当局逮捕了两家互联网托管公司的共同所有者，并查封了 800 台服务器，原因是他们运营的基础设施被俄罗斯情报机构用于在欧盟内部进行网络攻击和虚假信息宣传活动。 此次行动是对关键网络犯罪基础设施的一次重大执法打击，破坏了与俄罗斯情报机构相关团体的行动能力，并发出了对协助国家资助的网络行动追究责任的强烈信号。 调查重点是接管了 Stark Industries Solutions 基础设施的运营商，该互联网服务提供商此前曾因协助俄罗斯情报机构的网络破坏活动而受到欧盟制裁。

rss · Krebs on Security · May 25, 13:21

**背景**: Stark Industries Solutions 是一家在英国注册的网络托管公司，成立于俄罗斯入侵乌克兰前不久。该公司被多次认定为网络攻击和虚假信息的跳板，并因此受到欧盟制裁。“防弹托管”的概念指的是那些明知故犯、无视或协助客户进行非法活动的互联网服务提供商，这些托管商往往成为网络犯罪和国家资助行动的基石。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2024/05/stark-industries-solutions-an-iron-hammer-in-the-cloud/">Stark Industries Solutions : An Iron Hammer in the Cloud – Krebs on...</a></li>
<li><a href="https://securityaffairs.com/192602/intelligence/dutch-authorities-dismantle-hosting-network-allegedly-used-for-cyberattacks-and-disinformation.html">Dutch authorities dismantle hosting network allegedly used for...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#law enforcement`, `#cybercrime`, `#Russia`, `#infrastructure`

---

<a id="item-19"></a>
## [遗失的 Amiga Unix 版本重现，为复古计算史补遗](https://hackaday.com/2026/05/25/lost-version-of-amiga-unix-suddenly-reappears/) ⭐️ 6.0/10

一个此前遗失的 Amiga Unix 操作系统（也称为 AMIX）版本已被重新发现。这一发现有助于补全这款为 Commodore Amiga 平台打造的小众操作系统版本的历史记录。 这一发现对复古计算领域的保存和历史记录具有重要意义，因为它填补了 Amiga Unix 已知版本谱系中的空白。它直接惠及了对 Amiga 平台和早期 Unix 实现感兴趣的爱好者、收藏家和历史研究者。 重新发现的版本补充了已有的、涵盖从 1.0 版起大多数版本的历史记录。该系统是一个设计运行在 Commodore Amiga 系列个人计算机上的 UNIX 版本。

rss · Hackaday · May 25, 20:00

**背景**: Amiga Unix（AMIX）是 AT&T 公司开发的 UNIX System V 操作系统向 Commodore Amiga 个人计算机的完整移植版本。Amiga 是 1980 年代末至 1990 年代初以先进多媒体功能闻名的热门家用电脑。Amiga 平台拥有一个专注的社区，积极保存其软件和历史。发现像这样的遗失软件版本是数字考古和保存计算遗产的关键环节。

**标签**: `#retro computing`, `#operating systems`, `#Unix`, `#historical recovery`

---

<a id="item-20"></a>
## [创客 3D 打印经典 Windows 弹球游戏的真实世界版本](https://hackaday.com/2026/05/25/3d-printing-space-cadet-pinball-into-the-real-world/) ⭐️ 6.0/10

一个创客项目成功地将经典 Windows 游戏《太空军校生弹球》重新创造为一个实体的、可玩的 3D 打印模型。 这个项目将怀旧的数字娱乐与有形的创客文化连接起来，展示了 3D 打印等现代工具如何能将复古软件概念带入物理世界进行实体互动。 这个制作基于最初的 Windows 游戏，该游戏是 Cinematronics 公司 1995 年弹球游戏《Full Tilt! Pinball》的一个版本，并且可能涉及对游戏资产或设计进行逆向工程以创建物理组件。

rss · Hackaday · May 25, 17:00

**背景**: 《太空军校生弹球》是一款捆绑在多个微软 Windows 版本（最著名的是 Windows XP）中的游戏，曾广泛成为办公室职员和家庭用户的消遣。该游戏是《Full Tilt! Pinball》的简化版，并已成为粉丝怀旧和逆向工程项目以使其在现代系统上运行的主题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Full_Tilt!_Pinball">Full Tilt! Pinball - Wikipedia</a></li>
<li><a href="https://github.com/k4zmu2a/SpaceCadetPinball">GitHub - k4zmu2a/SpaceCadetPinball: Decompilation of 3D Pinball for...</a></li>

</ul>
</details>

**标签**: `#3D printing`, `#DIY`, `#retro computing`, `#hardware project`, `#maker`

---

<a id="item-21"></a>
## [解析英特尔失败的 iAPX432 架构](https://hackaday.com/2026/05/25/just-how-bad-was-the-intel-iapx432/) ⭐️ 6.0/10

一篇近期发表在 Hackaday 的文章详细分析了英特尔 iAPX432 处理器，这款 20 世纪 80 年代初的复杂指令集计算机（CISC）架构如今被视为设计史上的一次重大失败。 研究 iAPX432 具有重要意义，因为它作为一个处理器设计的历史案例，揭示了过度复杂架构的陷阱，并印证了业界最终向更简单、高效的 RISC 理念转变的趋势。 iAPX432 是一个雄心勃勃的项目，采用了面向对象架构和基于能力的安全性等先进特性，但其极端复杂性导致了性能低下、成本高昂和商业失败，成为了计算机工程领域的一个警示故事。

rss · Hackaday · May 25, 11:00

**背景**: 在处理器设计的早期，复杂指令集计算（CISC）与精简指令集计算（RISC）之间存在重大争论。CISC 旨在通过强大、高级的指令来缩小“语义差距”，而 RISC 则专注于可以极快执行的简单指令。英特尔 iAPX432 代表了 CISC 理念的一个极端案例，其设计雄心勃勃但最终不切实际。

**标签**: `#computer-architecture`, `#processor-design`, `#history`, `#Intel`, `#RISC`

---