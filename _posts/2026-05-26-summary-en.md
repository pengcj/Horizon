---
layout: default
title: "Horizon Summary: 2026-05-26 (EN)"
date: 2026-05-26
lang: en
---

> From 48 items, 21 important content pieces were selected

---

1. [AI (Claude) discovers critical macOS kernel vulnerability CVE-2026-28952.](#item-1) ⭐️ 8.0/10
2. [Linux Summit 2026 discusses using LLMs for kernel patch review](#item-2) ⭐️ 8.0/10
3. [SFC Responds to Bambu Lab AGPLv3 Violations with Reverse-Engineering Project](#item-3) ⭐️ 8.0/10
4. [z386: Open-Source FPGA Implementation of 80386 Using Original Microcode](#item-4) ⭐️ 8.0/10
5. [Neuroscientist argues brain theory must move beyond computer metaphor](#item-5) ⭐️ 8.0/10
6. [Mullvad VPN rolls out mitigation for exit IP fingerprinting issue.](#item-6) ⭐️ 7.0/10
7. [California proposes exempting Linux from its upcoming age-verification law](#item-7) ⭐️ 7.0/10
8. [Vatican's New Encyclical Addresses AI Ethics, Echoing Historical Context](#item-8) ⭐️ 7.0/10
9. [New tool for DeepSeek V4 achieves 99.82% cache hit rate, cutting AI inference costs by 80%](#item-9) ⭐️ 7.0/10
10. [Proposal to Make Linux Memory Controller Support Tiered-Memory Systems](#item-10) ⭐️ 7.0/10
11. [Scaling View Transitions with Unique Name Identifiers](#item-11) ⭐️ 7.0/10
12. [Through-Glass Vias: A Key Challenge on the Path to Glass Substrates for PCBs](#item-12) ⭐️ 7.0/10
13. [Advocating for AI Coding in a Slower, Quality-Focused Iterative Process](#item-13) ⭐️ 6.0/10
14. [Understanding Shamir's Secret Sharing Technique](#item-14) ⭐️ 6.0/10
15. [Norway's National Library Deploys 2PB Huawei Storage for Sovereign LLM](#item-15) ⭐️ 6.0/10
16. [Programming book sales decline as learning methods evolve](#item-16) ⭐️ 6.0/10
17. [Linus Torvalds Releases Linux 7.1-rc5, Warns of Unnecessary Fixes](#item-17) ⭐️ 6.0/10
18. [Netherlands Arrests Two, Seizes 800 Servers in Major Cybercrime Raid](#item-18) ⭐️ 6.0/10
19. [Lost Version of Amiga Unix Rediscovered for Retro Computing History](#item-19) ⭐️ 6.0/10
20. [Maker 3D-Prints a Real-World Version of Classic Windows Pinball Game](#item-20) ⭐️ 6.0/10
21. [Analysis of Intel's Failed iAPX432 Architecture](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [AI (Claude) discovers critical macOS kernel vulnerability CVE-2026-28952.](https://support.apple.com/en-us/127115) ⭐️ 8.0/10

Anthropic's Claude AI model, in collaboration with Calif.io, discovered a critical kernel vulnerability (CVE-2026-28952) in Apple macOS, which was an integer overflow leading to a denial-of-service issue. This event highlights the emerging and significant role of AI models in automated security research, potentially accelerating vulnerability discovery, while also raising questions about Apple's internal use of such tools compared to competitors like Google. The vulnerability affected multiple macOS versions, including Sequoia 15.7.7 and Sonoma 14.8.7, not just the latest macOS Tahoe 26.5, and the fix involved improved input validation.

hackernews · dragonsenseiguy · May 25, 23:40 · [Discussion](https://news.ycombinator.com/item?id=48273169)

**Background**: The macOS kernel (XNU) is the core of Apple's operating systems. AI-driven vulnerability discovery uses large language models like Claude to automatically find security flaws in software code, a capability Anthropic has been developing. Companies like Google have publicly shown high volumes of internally-discovered vulnerabilities, setting a benchmark for proactive security.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/en-us/127116">About the security content of macOS Sequoia 15.7.7 - Apple Support</a></li>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://www.anthropic.com/product/security">Anthropic's agentic solution for vulnerability detection | Claude ...</a></li>

</ul>
</details>

**Discussion**: Community comments revealed that the vulnerability was found by Calif.io in collaboration with Anthropic's Claude, and a researcher from Calif.io clarified it was unrelated to their separate MIE attack research. Other users debated Apple's update practices, with some criticizing large update sizes, and noted the vulnerability impacted older macOS versions too.

**Tags**: `#cybersecurity`, `#AI-research`, `#macOS`, `#vulnerability`, `#kernel`

---

<a id="item-2"></a>
## [Linux Summit 2026 discusses using LLMs for kernel patch review](https://lwn.net/Articles/1073583/) ⭐️ 8.0/10

A dedicated plenary session at the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit explored the use of large language models for reviewing Linux kernel patches, a topic generating significant community interest. This discussion highlights a major effort to integrate AI into the critical, labor-intensive process of kernel development, which could improve patch review efficiency and quality across the open-source ecosystem. The session was led by prominent kernel developers including Roman Gushchin, Chris Mason, Josef Bacik, and Sasha Levin, and the discussion was so extensive that it required a follow-up session in the filesystem track later that day.

rss · LWN.net · May 25, 21:27

**Background**: The Linux kernel is the core component of the Linux operating system, and its development relies on a rigorous process of submitting and reviewing code changes (patches) from thousands of contributors. Large language models (LLMs) are advanced AI systems trained on vast text datasets, capable of understanding and generating human-like text, which is now being explored for automated or assisted code review tasks.

**Tags**: `#LLMs`, `#Linux Kernel`, `#Code Review`, `#Open Source`, `#Software Development`

---

<a id="item-3"></a>
## [SFC Responds to Bambu Lab AGPLv3 Violations with Reverse-Engineering Project](https://lwn.net/Articles/1074286/) ⭐️ 8.0/10

The Software Freedom Conservancy launched the 'baltobu' reverse-engineering project to re-implement Bambu Lab's proprietary code and began hosting a fork of the Orca Slicer software to defend it from legal threats. This is a significant enforcement action for the AGPLv3 license, directly challenging a company's non-compliance and potential anti-competitive behavior in the 3D printing ecosystem, which could set a precedent for upholding software freedom and the right to repair. The response was triggered by Bambu Lab's failure to provide source code for its AGPLv3-licensed slicer modifications and its threats against Paweł Jarczak, the creator of an Orca Slicer fork designed for interoperability with Bambu printers.

rss · LWN.net · May 25, 16:48

**Background**: The GNU Affero General Public License (AGPLv3) is a strong copyleft license that extends the requirements of the GPL to software used over a network, mandating that the complete corresponding source code be made available to users. Reverse engineering for the purpose of achieving software interoperability is generally protected under legal frameworks like the EU's Software Directive. Orca Slicer is a popular open-source 3D printing slicer application.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License">GNU Affero General Public License - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reverse_engineering">Reverse engineering - Wikipedia</a></li>
<li><a href="https://github.com/OrcaSlicer/OrcaSlicer">GitHub - OrcaSlicer/OrcaSlicer: G-code generator for 3 D printers ...</a></li>

</ul>
</details>

**Tags**: `#open-source-licensing`, `#AGPL`, `#software-freedom`, `#3D-printing`, `#legal-enforcement`

---

<a id="item-4"></a>
## [z386: Open-Source FPGA Implementation of 80386 Using Original Microcode](https://hackaday.com/2026/05/25/z386-an-open-source-80386-built-around-original-microcode/) ⭐️ 8.0/10

A developer known as [nand2mario] released z386, an open-source 80386-compatible CPU core written in SystemVerilog for FPGAs, which is uniquely built around the original Intel 386 microcode. This project provides a novel and historically valuable approach to retrocomputing and processor architecture education, allowing enthusiasts to study a classic x86 CPU implementation with a direct link to its original firmware logic. The implementation is a compact CPU core targeting FPGAs and is available on GitHub. Its use of original microcode offers deep insight into how the processor's control unit executed complex x86 instructions.

rss · Hackaday · May 25, 23:00

**Background**: The Intel 80386, introduced in 1985, was a landmark 32-bit x86 processor. Microcode is a layer of low-level instructions inside a CPU that translates higher-level machine instructions (like x86 instructions) into the processor's internal, hardware-level operations. Implementing a CPU on an FPGA (Field-Programmable Gate Array) involves configuring the digital logic chips to mimic the processor's architecture, and using the original microcode for this is a technically novel method.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/nand2mario/z386">GitHub - nand2mario/z386: Compact 80386 CPU in SystemVerilog</a></li>
<li><a href="https://nand2mario.github.io/posts/2026/z386/">z386: An Open-Source 80386 Built Around Original Microcode - Small...</a></li>

</ul>
</details>

**Tags**: `#fpga`, `#retrocomputing`, `#cpu-design`, `#open-source-hardware`, `#x86`

---

<a id="item-5"></a>
## [Neuroscientist argues brain theory must move beyond computer metaphor](https://www.nature.com/articles/d41586-026-01619-0) ⭐️ 8.0/10

In a 2026 article published in Nature, a neuroscientist argues that the field of neuroscience needs to fundamentally shift its paradigm by moving beyond treating the brain as if it were a computer. This argument challenges a core, long-standing metaphor in neuroscience and suggests that progress in understanding consciousness and cognition requires fundamentally new theoretical frameworks, which could redirect future research priorities. The critique targets the computational metaphor's limitations, suggesting that while brains process information, the analogy of them as passive, sequential processors may be insufficient for a meaningful understanding of higher cognition.

rss · Nature · May 25, 00:00

**Background**: The 'brain as a computer' metaphor has been dominant in neuroscience and cognitive science for decades, framing the mind in terms of information processing, algorithms, and representations. Critics argue this approach, while powerful, can oversimplify the brain's embodied, dynamic, and possibly non-computational nature. Alternative theories, such as biological naturalism and integrated information theory, propose different foundations for consciousness.

<details><summary>References</summary>
<ul>
<li><a href="https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2022.810358/full">Frontiers | The Brain-Computer Metaphor Debate Is Useless: A Matter of Semantics</a></li>
<li><a href="https://www.theguardian.com/science/2020/feb/27/why-your-brain-is-not-a-computer-neuroscience-neural-networks-consciousness">Why your brain is not a computer | Neuroscience | The Guardian</a></li>
<li><a href="https://oecs.mit.edu/pub/zf1nbs6d/release/1">Consciousness and AI · Open Encyclopedia of Cognitive Science</a></li>

</ul>
</details>

**Tags**: `#neuroscience`, `#brain theory`, `#computational metaphor`, `#consciousness`, `#paradigm shift`

---

<a id="item-6"></a>
## [Mullvad VPN rolls out mitigation for exit IP fingerprinting issue.](https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout) ⭐️ 7.0/10

Mullvad VPN is deploying a new method for assigning exit IP addresses to its servers, which will prevent user activity from being linked across different VPN servers or to other users on the same server. This mitigation addresses a significant privacy vulnerability where users could be tracked across different VPN sessions, directly impacting the core privacy promises of a VPN service and demonstrating Mullvad's responsive approach to security. The fix is being rolled out incrementally across their server network, and users switching servers are advised to log out and back in to regenerate their WireGuard key as an immediate step. The new method ensures that using one exit IP address provides no information about which exit address is used on another server or by another user.

hackernews · Cider9986 · May 25, 17:45 · [Discussion](https://news.ycombinator.com/item?id=48269580)

**Background**: Exit IP fingerprinting is a technique where the specific IP address assigned to a user by a VPN server can be used to track their activity across different servers or sessions, even when they are using the same VPN account. This is possible because traditional assignment methods might use predictable internal IP addresses that create a linkable pattern. VPN providers aim to make all user traffic appear to come from a pool of shared, anonymous IP addresses.

<details><summary>References</summary>
<ul>
<li><a href="https://mullvad.net/en/blog/exit-ip-fingerprinting-between-vpn-servers">Exit IP fingerprinting between VPN servers | Mullvad VPN</a></li>
<li><a href="https://www.techradar.com/vpn/vpn-services/mullvad-to-patch-vpn-fingerprinting-issue-to-stop-your-activity-from-being-tracked-across-servers">Mullvad to patch VPN fingerprinting issue to stop your activity from being tracked across servers | TechRadar</a></li>
<li><a href="https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout">Exit IP VPN servers mitigation rollout</a></li>

</ul>
</details>

**Discussion**: The community reaction is largely positive, with users expressing surprise and appreciation for Mullvad's prompt response to the issue. There is also discussion about alternative privacy solutions, such as using the Mullvad Browser with its Random mode, or the need for browsers to spoof consistent device fingerprints to combat tracking.

**Tags**: `#VPN`, `#privacy`, `#security`, `#fingerprinting`, `#online-tracking`

---

<a id="item-7"></a>
## [California proposes exempting Linux from its upcoming age-verification law](https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law) ⭐️ 7.0/10

A California lawmaker has proposed an amendment to exempt the Linux operating system from the state's upcoming age-verification law, which would have originally required operating systems to collect users' ages. This exemption is significant as it directly addresses community backlash and protects the open-source Linux ecosystem from a potentially onerous and privacy-invasive compliance burden. The exemption amendment was proposed by the same lawmaker who wrote the original law, indicating a direct response to the criticism that applying such mandates to operating systems is impractical and overly broad.

hackernews · rbanffy · May 25, 18:19 · [Discussion](https://news.ycombinator.com/item?id=48269961)

**Background**: The law in question is a California bill aimed at implementing age verification for internet users to protect minors. The initial proposal's broad language, which could be interpreted to include operating systems, sparked a significant backlash from the Linux and open-source communities, who argued it was technically infeasible and a threat to privacy and user freedom.

**Discussion**: The online discussion shows widespread skepticism about the law's drafting process, with comments questioning who actually wrote the legislation and suggesting it burdens consumers because regulators failed to control large companies. Some users also cynically speculate the exemption was offered to prevent Linux developers from mounting a constitutional challenge.

**Tags**: `#linux`, `#policy`, `#internet-regulation`, `#privacy`, `#open-source`

---

<a id="item-8"></a>
## [Vatican's New Encyclical Addresses AI Ethics, Echoing Historical Context](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything) ⭐️ 7.0/10

Pope Leo XIV issued the encyclical 'Magnifica Humanitas,' which presents the Vatican's ethical framework for safeguarding human dignity in the age of artificial intelligence. This is a significant intervention from a major non-technical, global moral authority, providing a structured ethical perspective that could influence broader societal debates and policy considerations surrounding AI development and integration. The encyclical's writing is praised for being exceptionally clear and approachable even for non-Catholics, and it draws a direct historical parallel to Pope Leo XIII's 1891 encyclical 'Rerum Novarum,' which addressed the social upheaval of the first Industrial Revolution.

rss · Simon Willison · May 25, 23:58

**Background**: A papal encyclical is a formal letter from the Pope to bishops and the broader Church, outlining the Church's teaching and guidance on a specific issue. Pope Leo XIV chose his name to honor Leo XIII, whose landmark 1891 encyclical 'Rerum Novarum' addressed the rights and duties of capital and labor during the Industrial Revolution, establishing foundations for modern Catholic social teaching. The new encyclical explicitly frames the current AI era as another 'industrial revolution' requiring a similar moral response.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Catholic_social_teaching">Catholic social teaching - Wikipedia</a></li>
<li><a href="https://www.vatican.va/content/leo-xiii/en/encyclicals/documents/hf_l-xiii_enc_15051891_rerum-novarum.html">Encyclical Rerum Novarum of Leo XIII , 15 May 1891</a></li>
<li><a href="https://en.wikipedia.org/wiki/Encyclical">Encyclical - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#societal impact`, `#Vatican`, `#enclicical`, `#policy`

---

<a id="item-9"></a>
## [New tool for DeepSeek V4 achieves 99.82% cache hit rate, cutting AI inference costs by 80%](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247892730&idx=1&sn=3da5702f8033c5ed6690bd71d90a581d) ⭐️ 7.0/10

A new tool specifically optimized for DeepSeek V4 has been released, achieving an exceptionally high cache hit rate of 99.82% for inference tasks, which translates to potential cost savings of up to 80%. This breakthrough in cache optimization significantly enhances the cost-efficiency of running large language models like DeepSeek V4, which is crucial for developers and businesses deploying AI at scale to manage computational expenses. The tool is described as a 'terminal coding harness' built specifically for DeepSeek, and the reported 99.82% hit rate suggests a highly effective implementation of prefix caching or a similar strategy, though the specific technical methodology is not detailed in the provided content.

rss · 量子位 · May 25, 04:27

**Background**: DeepSeek is a series of large language models, with V4 being a recent version noted for its massive scale (e.g., up to 1T parameters). Inference caching is an optimization technique that stores and reuses previous computation results (like key-value caches) to avoid redundant processing, drastically reducing latency and cost. A 'coding harness' is an operating layer around a model that manages context, tools, and control loops to optimize its performance for specific tasks like coding.

<details><summary>References</summary>
<ul>
<li><a href="https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem">Serving DeepSeek - V 4 : why million-token context is an inference...</a></li>
<li><a href="https://inferencesystemsauthority.com/inference-caching-strategies">Inference Caching Strategies for Speed... | Inference Systems Authority</a></li>
<li><a href="https://pinggy.io/blog/best_ai_harnesses_to_supercharge_llm_models/">AI Harness Engineering: The Layer That Makes Your LLM Applications...</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, so there is no discussion to summarize.

**Tags**: `#AI`, `#inference optimization`, `#caching`, `#DeepSeek`, `#cost efficiency`

---

<a id="item-10"></a>
## [Proposal to Make Linux Memory Controller Support Tiered-Memory Systems](https://lwn.net/Articles/1073400/) ⭐️ 7.0/10

Linux kernel developer Joshua Hahn presented a proposal at the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit to improve the cgroup memory controller for better support of tiered-memory systems, which it was not originally designed for. This improvement is significant because modern hardware increasingly uses tiered-memory architectures, and a properly functioning memory controller is essential for resource allocation and isolation in such systems, preventing interference between tasks. The memory controller for cgroups is responsible for resource allocation, accounting, and protection from interference, but it currently lacks the specific logic to manage memory across different tiers effectively.

rss · LWN.net · May 25, 15:03

**Background**: Control groups (cgroups) are a Linux kernel feature that limits, accounts for, and isolates resource usage (like CPU, memory, and I/O) for a collection of processes. Tiered-memory systems use a hierarchy of memory technologies with different speeds and capacities (such as fast DRAM and slower persistent memory) to optimize performance and cost. The memory-management track at the Linux summit is a key venue for discussing such kernel improvements.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cgroups">cgroups - Wikipedia</a></li>
<li><a href="https://www.kernel.org/doc/html/v4.18/admin-guide/cgroup-v2.html">Control Group v2 — The Linux Kernel documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_hierarchy">Memory hierarchy - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#memory-management`, `#cgroups`, `#tiered-memory`, `#systems-programming`

---

<a id="item-11"></a>
## [Scaling View Transitions with Unique Name Identifiers](https://css-tricks.com/cross-document-view-transitions-part-2/) ⭐️ 7.0/10

The article presents a practical solution for managing the CSS `view-transition-name` property across many elements, preventing the explosion of unmanageable pseudo-element selectors that can occur during scaling. This is significant for developers implementing complex animations with the View Transitions API, as it addresses a common scaling bottleneck that can make codebases unwieldy and difficult to maintain, ensuring smoother development for rich, interactive web applications. The core problem is that every `view-transition-name` on a page must be unique, and each name requires a corresponding pseudo-element selector in CSS, leading to selector bloat. The article from CSS-Tricks focuses on strategies to manage these unique identifiers efficiently at scale.

rss · CSS-Tricks · May 25, 13:46

**Background**: The View Transitions API is a web platform feature that simplifies the creation of animated transitions between different states or views of a website, powered by CSS Animations. A key mechanism involves assigning a `view-transition-name` CSS property to elements to enable granular control over their transition snapshots and animations. While powerful, managing unique names for a large number of elements presents a significant scaling challenge in real-world applications.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API">View Transition API - Web APIs | MDN</a></li>
<li><a href="https://www.patterns.dev/vanilla/view-transitions/">Animating View Transitions</a></li>

</ul>
</details>

**Tags**: `#CSS`, `#Web Development`, `#Animation`, `#View Transitions API`, `#Frontend`

---

<a id="item-12"></a>
## [Through-Glass Vias: A Key Challenge on the Path to Glass Substrates for PCBs](https://hackaday.com/2026/05/25/through-glass-vias-and-the-long-road-to-glass-substrates/) ⭐️ 7.0/10

The article examines the specific engineering hurdle of creating reliable through-glass vias (TGVs), which remains a significant bottleneck preventing the widespread adoption of glass substrates in advanced circuit board and semiconductor packaging. Overcoming the TGV challenge is crucial because glass substrates offer superior material properties like better thermal stability and lower electrical loss, potentially enabling next-generation, high-performance electronics packaging. TGV technology involves creating tiny vertical electrical connections through glass using combined laser and etching processes, a technique studied by companies like Corning for semiconductor packaging due to glass's reduced signal loss.

rss · Hackaday · May 26, 02:00

**Background**: Glass substrates are emerging as a potential replacement for traditional organic substrates (like epoxy-based laminates) used in PCBs and chip packaging, offering advantages such as higher temperature tolerance, better flatness for lithography, and improved dimensional stability. Through-glass vias (TGVs) are a fundamental building block analogous to through-silicon vias (TSVs) in 3D chip stacking, providing the necessary electrical pathways between layers in a glass-based interposer or substrate.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Via_(electronics)">Via (electronics) - Wikipedia</a></li>
<li><a href="https://www.pcbaaa.com/through-glass-viatgv-a-critical-technology-for-advanced-packaging/">Through - glass Via( TGV ) - A Critical Technology For Advanced...</a></li>
<li><a href="https://avecas.in/glass-substrates-vs-organic-ai-interconnects/">Glass Substrates vs . Organic : Why the Industry is Shifting... - Avecas</a></li>

</ul>
</details>

**Tags**: `#semiconductor_packaging`, `#materials_science`, `#electronics`, `#glass_substrate`, `#PCB`

---

<a id="item-13"></a>
## [Advocating for AI Coding in a Slower, Quality-Focused Iterative Process](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/) ⭐️ 6.0/10

An article argues for using AI coding assistants in a slower, iterative process focused on producing higher-quality code rather than maximizing speed. This perspective challenges the dominant narrative that AI tools primarily accelerate development, emphasizing that their value can also lie in improving code quality through careful, iterative refinement. The approach involves multiple rounds of review and refinement, such as using one AI model for design and another for code review to catch corner cases, which some practitioners find increases overall development time but improves the final output.

hackernews · signa11 · May 25, 23:16 · [Discussion](https://news.ycombinator.com/item?id=48272984)

**Background**: AI coding assistants, powered by large language models (LLMs), are widely used to automate code generation and speed up software development. The common expectation is that these tools will make programming faster and more efficient.

**Discussion**: Practitioners in the discussion shared experiences of iterative AI workflows, with some agreeing that they spend more time in review loops than manual coding but find value in the improved code quality. Others pushed back on the idea that speed is the sole goal, noting that AI tools can produce varying levels of code quality and that their use is nuanced.

**Tags**: `#AI-assisted programming`, `#software development workflow`, `#code quality`, `#LLM applications`

---

<a id="item-14"></a>
## [Understanding Shamir's Secret Sharing Technique](https://ente.com/blog/how-shamirs-secret-sharing-works/) ⭐️ 6.0/10

The news is an educational blog post that explains the fundamental cryptographic technique of Shamir's Secret Sharing (SSS) in an accessible manner, rather than reporting a new development. Understanding SSS is significant because it is a core building block in threshold cryptography, enabling secure distribution of secrets like private keys across multiple parties for enhanced security in systems like cryptocurrency wallets and key recovery. The technique relies on polynomial interpolation, specifically Lagrange interpolation, to split a secret into multiple shares where a predefined threshold number of shares is required for reconstruction. It's often compared to other methods like Reed-Solomon codes and multisignature schemes, with trade-offs involving information-theoretic security and implementation complexity.

hackernews · subract · May 25, 22:37 · [Discussion](https://news.ycombinator.com/item?id=48272715)

**Background**: Shamir's Secret Sharing, invented by Adi Shamir in 1979, is a cryptographic algorithm that divides a secret into multiple parts, called shares. The key property is that any subset of shares meeting a threshold can reconstruct the original secret, while any fewer shares reveal no information about it. This forms the basis for threshold cryptosystems, where cryptographic operations can be performed collectively without reconstructing the secret in a single location.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lagrange_polynomial">Lagrange polynomial - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Threshold_cryptosystem">Threshold cryptosystem - Wikipedia</a></li>
<li><a href="https://crypto.stackexchange.com/questions/95943/different-secret-sharing-schemes-instead-of-shamirs">Different secret sharing schemes instead of Shamir ' s ?</a></li>

</ul>
</details>

**Discussion**: Community members discussed the technique's educational value, with one noting it could be taught in secondary schools. Practical questions arose about its use for securing root DNS keys, comparing its complexity to physical security measures like safes. Additional technical comparisons were made to Reed-Solomon codes and All-or-Nothing Transforms (AONT), highlighting differences in information-theoretic security and payload handling.

**Tags**: `#cryptography`, `#secret-sharing`, `#information-security`, `#educational`

---

<a id="item-15"></a>
## [Norway's National Library Deploys 2PB Huawei Storage for Sovereign LLM](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910) ⭐️ 6.0/10

Norway's national library (Nasjonalbiblioteket) is using a 2-petabyte Huawei flash storage system to support the training of a sovereign Norwegian-language large language model (LLM). The initiative was presented by the library's Head of IT Platform at Huawei's ID Forum 2026. This project exemplifies the growing global trend of sovereign AI initiatives, where nations seek to develop their own AI capabilities to preserve linguistic and cultural nuances that large, English-centric models may not adequately capture. It highlights how even countries with advanced digital infrastructure are investing in national AI sovereignty. The storage infrastructure is a Huawei flash system, and the training relies on a relatively modest HPE Cray supercomputer with 448 GPUs and over 64,000 CPU cores, which some community members question as being sufficient for full-scale LLM training compared to fine-tuning open-source models.

hackernews · rbanffy · May 25, 19:37 · [Discussion](https://news.ycombinator.com/item?id=48270770)

**Background**: Sovereign AI refers to a nation's strategic effort to build and control its own AI models and infrastructure, driven by concerns over data sovereignty, cultural preservation, and reducing reliance on foreign tech providers. Large language models (LLMs) are AI systems trained on vast text data to generate and understand human language; when trained primarily on English data, they often perform poorly or miss context for other languages and cultures. Universal Flash Storage (UFS) is a high-performance flash storage specification used in modern electronic devices, though the term here likely refers to enterprise-grade flash arrays from Huawei.

<details><summary>References</summary>
<ul>
<li><a href="https://e.huawei.com/en/products/storage/hybrid-flash-storage">OceanStor Hybrid Flash Storage | Huawei Enterprise</a></li>
<li><a href="https://byteswall.com/news/sovereign-ai-initiatives-propel-strategic-autonomy-and-national-resilience/">Sovereign AI Initiatives Propel Strategic Autonomy and... | BytesWall</a></li>

</ul>
</details>

**Discussion**: The community discussion is mixed; some agree with the necessity of sovereign AI for cultural and linguistic representation, while others are skeptical, noting that major LLM providers likely already train on multilingual data and that the described hardware may be insufficient for training a full model from scratch. One Norwegian user praises the national library's excellent search interface, and another user contextualizes the project within the broader, often buzzword-driven 'sovereign AI' trend in executive leadership.

**Tags**: `#sovereign AI`, `#LLM training`, `#national language models`, `#data storage`

---

<a id="item-16"></a>
## [Programming book sales decline as learning methods evolve](https://unix.foo/posts/nobody-cracks-open-a-programming-book/) ⭐️ 6.0/10

An O'Reilly author of 'Learning Go' has shared sales data showing a general downward trend in paperback book sales over the past 13 months, with monthly figures ranging from 124 to 484 copies sold. This trend reflects a broader shift in how developers learn to code, moving away from traditional books towards online resources, which has implications for authors, publishers, and the complexity of programming languages that no longer need to be fully book-digestible. The author notes that while sales are down, they have fluctuated historically, with total sales of the first edition since 2021 reaching roughly 20,000 copies, indicating the market is not dead but changing.

hackernews · zdw · May 25, 23:21 · [Discussion](https://news.ycombinator.com/item?id=48273030)

**Background**: Traditionally, programming books served as comprehensive guides to learning a language, covering syntax, idioms, and best practices in a structured format. The rise of online search engines like Google and community Q&A sites like Stack Overflow provided faster, more accessible alternatives, allowing developers to learn specific tasks on demand. This shift also enabled programming languages to grow more complex, as detailed documentation could be maintained online rather than constrained by print volumes.

**Discussion**: The community offers diverse perspectives: one commenter shares concrete sales data showing fluctuations but a long-term decline, while another argues that declining book sales have removed constraints on language complexity, leading to languages like C++ becoming too intricate for experts. Others counter that for complex languages like Rust, deep reading from books is still valuable for mastering idioms and subtle points, highlighting a split between quick online lookups and committed, thorough learning.

**Tags**: `#programming education`, `#book publishing`, `#software learning`, `#language complexity`, `#developer trends`

---

<a id="item-17"></a>
## [Linus Torvalds Releases Linux 7.1-rc5, Warns of Unnecessary Fixes](https://lwn.net/Articles/1074172/) ⭐️ 6.0/10

Linus Torvalds released the Linux 7.1-rc5 kernel prepatch for testing, while expressing his unhappiness with the large amount of trivial driver fixes being submitted so late in the release cycle. This signals a potential shift in release management discipline, as Torvalds warns he will reject non-critical fixes during the release candidate phase, which could affect how kernel developers submit patches in the future. Torvalds explicitly stated that many of the fixes were triggered by AI code review and are too trivial for the rc5 stage, emphasizing that only regression fixes are appropriate this late in the release cycle.

rss · LWN.net · May 24, 22:59

**Background**: The Linux kernel uses a time-based release model with a merge window for new features followed by several release candidates (rc) for bug fixes. The linux-next tree is a staging area where patches are tested before being merged during the merge window. Prepatch or rc kernels are pre-release versions meant for testing by developers and enthusiasts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kernel.org/releases.html">Active kernel releases</a></li>
<li><a href="https://www.kernel.org/doc/man-pages/linux-next.html">Working with linux - next</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#open-source`, `#software-development`, `#release-management`

---

<a id="item-18"></a>
## [Netherlands Arrests Two, Seizes 800 Servers in Major Cybercrime Raid](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/) ⭐️ 6.0/10

Dutch authorities arrested two individuals who co-owned hosting companies and seized 800 servers for operating infrastructure used by Russian intelligence for cyberattacks and disinformation campaigns within the EU. This action represents a significant law enforcement strike against critical cybercrime infrastructure, disrupting the operational capabilities of Russian intelligence-linked groups and sending a strong signal about accountability for enabling state-sponsored cyber operations. The investigation focused on the operators who took over the infrastructure of Stark Industries Solutions, an ISP previously sanctioned by the EU for facilitating cyber mischief from Russian intelligence agencies.

rss · Krebs on Security · May 25, 13:21

**Background**: Stark Industries Solutions is a UK-incorporated web hosting firm founded shortly before Russia's invasion of Ukraine. It has been repeatedly identified as a staging ground for cyberattacks and disinformation, leading to EU sanctions. The concept of 'bulletproof hosting' refers to internet service providers that knowingly ignore or facilitate illegal activities by their clients, often becoming a cornerstone for cybercriminal and state-sponsored operations.

<details><summary>References</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2024/05/stark-industries-solutions-an-iron-hammer-in-the-cloud/">Stark Industries Solutions : An Iron Hammer in the Cloud – Krebs on...</a></li>
<li><a href="https://securityaffairs.com/192602/intelligence/dutch-authorities-dismantle-hosting-network-allegedly-used-for-cyberattacks-and-disinformation.html">Dutch authorities dismantle hosting network allegedly used for...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#law enforcement`, `#cybercrime`, `#Russia`, `#infrastructure`

---

<a id="item-19"></a>
## [Lost Version of Amiga Unix Rediscovered for Retro Computing History](https://hackaday.com/2026/05/25/lost-version-of-amiga-unix-suddenly-reappears/) ⭐️ 6.0/10

A previously lost version of the Amiga Unix operating system, also known as AMIX, has been rediscovered. This find helps complete the historical record of the versions of this niche OS for the Commodore Amiga platform. This recovery is significant for retro computing preservation and historical documentation, as it fills a gap in the known version lineage of Amiga Unix. It directly benefits enthusiasts, collectors, and historians interested in the Amiga platform and early Unix implementations. The rediscovered version adds to an existing historical record that already includes most versions from 1.0 onwards. The system was a version of UNIX designed to run on the Commodore Amiga line of personal computers.

rss · Hackaday · May 25, 20:00

**Background**: Amiga Unix (AMIX) was a full port of the UNIX System V operating system developed by AT&T for the Commodore Amiga, a popular home computer known for its advanced multimedia capabilities in the late 1980s and early 1990s. The Amiga platform has a dedicated community that actively preserves its software and history. Finding lost software versions like this is a key part of digital archaeology and preserving computing heritage.

**Tags**: `#retro computing`, `#operating systems`, `#Unix`, `#historical recovery`

---

<a id="item-20"></a>
## [Maker 3D-Prints a Real-World Version of Classic Windows Pinball Game](https://hackaday.com/2026/05/25/3d-printing-space-cadet-pinball-into-the-real-world/) ⭐️ 6.0/10

A maker project has successfully recreated the classic Windows game, Space Cadet Pinball, as a physical, playable 3D-printed model. This project bridges nostalgic digital entertainment with tangible maker culture, demonstrating how modern tools like 3D printing can bring retro software concepts into the physical world for hands-on interaction. The build is based on the original Windows game, which was a version of the 1995 pinball title 'Full Tilt! Pinball' by Cinematronics, and likely involved reverse engineering the game's assets or design to create the physical components.

rss · Hackaday · May 25, 17:00

**Background**: Space Cadet Pinball was a game bundled with several versions of Microsoft Windows, most famously Windows XP, and became a widespread distraction for office workers and home users alike. The game was a simplified version of 'Full Tilt! Pinball' and has been the subject of fan nostalgia and reverse engineering projects to run on modern systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Full_Tilt!_Pinball">Full Tilt! Pinball - Wikipedia</a></li>
<li><a href="https://github.com/k4zmu2a/SpaceCadetPinball">GitHub - k4zmu2a/SpaceCadetPinball: Decompilation of 3D Pinball for...</a></li>

</ul>
</details>

**Tags**: `#3D printing`, `#DIY`, `#retro computing`, `#hardware project`, `#maker`

---

<a id="item-21"></a>
## [Analysis of Intel's Failed iAPX432 Architecture](https://hackaday.com/2026/05/25/just-how-bad-was-the-intel-iapx432/) ⭐️ 6.0/10

A recent article on Hackaday provides a detailed examination of the Intel iAPX432 processor, a complex instruction set computer (CISC) architecture from the early 1980s that is now recognized as a significant failure in design history. Studying the iAPX432 is important as it serves as a historical case study in processor design, illustrating the pitfalls of overcomplicated architectures and reinforcing the eventual industry shift towards the simpler, more efficient RISC philosophy. The iAPX432 was an ambitious project featuring advanced features like object-oriented architecture and capability-based security, but its extreme complexity resulted in poor performance, high cost, and commercial failure, becoming a cautionary tale in computer engineering.

rss · Hackaday · May 25, 11:00

**Background**: In the early days of processor design, there was significant debate between Complex Instruction Set Computing (CISC) and Reduced Instruction Set Computing (RISC) approaches. CISC aimed to reduce the 'semantic gap' by having powerful, high-level instructions, while RISC focused on simple instructions that could be executed very quickly. The Intel iAPX432 represented an extreme case of the CISC philosophy with a highly ambitious but ultimately impractical design.

**Tags**: `#computer-architecture`, `#processor-design`, `#history`, `#Intel`, `#RISC`

---