---
layout: default
title: "Horizon Summary: 2026-05-24 (EN)"
date: 2026-05-24
lang: en
---

> From 49 items, 11 important content pieces were selected

---

1. [Microsoft open-sources earliest known DOS source code from paper archives](#item-1) ⭐️ 9.0/10
2. [CISA contractor leaks highly privileged AWS GovCloud keys on public GitHub](#item-2) ⭐️ 9.0/10
3. [Using BPF for Custom Linux Page Cache Eviction Policies](#item-3) ⭐️ 8.0/10
4. [A 16-Byte Demo Combining Graphics and Sound Achieves Record-Breaking Optimization](#item-4) ⭐️ 7.0/10
5. [C# introduces union types in .NET 11 preview](#item-5) ⭐️ 7.0/10
6. [AI Data Centers' Demand for HBM Memory to Increase Consumer Electronics Prices](#item-6) ⭐️ 7.0/10
7. [Linux Summit Tackles Page Fault Lock Contention](#item-7) ⭐️ 7.0/10
8. [Reverse Engineering of Unitree Go2's GO-M8018-6 Motor Controller](#item-8) ⭐️ 7.0/10
9. [Debating the HTML Definition List Element's Value and Limitations](#item-9) ⭐️ 6.0/10
10. [Linux stable kernels released with Fragnesia vulnerability fix](#item-10) ⭐️ 6.0/10
11. [Touchable Mid-Air POV Display Developed by University Team](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Microsoft open-sources earliest known DOS source code from paper archives](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 9.0/10

Microsoft has released the source listings for the earliest known 86-DOS 1.00 kernel and early PC-DOS utilities, which were transcribed from paper printouts to commemorate the 45th anniversary of 86-DOS. This release preserves a foundational piece of personal computing history, showing the very origins of the operating system that powered IBM PCs and launched Microsoft's dominance, and it demonstrates a significant effort in digital archaeology. The source code was not originally stored digitally; a team of historians painstakingly scanned and transcribed it from decades-old paper printouts provided by original developer Tim Paterson, a process made difficult by the poor quality of the documents.

hackernews · DamnInteresting · May 24, 01:21 · [Discussion](https://news.ycombinator.com/item?id=48253386)

**Background**: 86-DOS, originally called QDOS (Quick and Dirty Operating System), was created by Seattle Computer Products for Intel 8086-based computers. Microsoft purchased the rights to it in 1981, renamed it MS-DOS, and licensed it to IBM, which became the foundational operating system for the IBM PC and its clones, defining the early PC era.

<details><summary>References</summary>
<ul>
<li><a href="https://redmondmag.com/articles/2026/04/29/microsoft-open-sources-earliest-dos-code-on-anniversary.aspx">Microsoft Open Sources Earliest DOS Code on Anniversary -- Redmondmag.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/86-DOS">86-DOS - Wikipedia</a></li>
<li><a href="https://historyofinformation.com/detail.php?id=99">History of Information</a></li>

</ul>
</details>

**Discussion**: Community sentiment is overwhelmingly positive, with users expressing rare thanks to Microsoft for this preservation effort. Discussions highlight the historical significance of the code, the difficulty of the OCR process, and speculation about whether source code for early Windows versions might also be released in the future.

**Tags**: `#computing-history`, `#open-source`, `#microsoft`, `#DOS`, `#preservation`

---

<a id="item-2"></a>
## [CISA contractor leaks highly privileged AWS GovCloud keys on public GitHub](https://www.schneier.com/blog/archives/2026/05/cisa-security-leak.html) ⭐️ 9.0/10

A contractor for the U.S. Cybersecurity and Infrastructure Security Agency (CISA) left a public GitHub repository containing credentials for several highly privileged AWS GovCloud accounts and details of internal CISA systems exposed for an unknown period. This is considered one of the most egregious government data leaks in recent history, as it exposed the keys to a secure cloud environment used for sensitive government work, potentially allowing attackers to compromise critical infrastructure and agency operations. The public archive included files detailing how CISA internally builds, tests, and deploys software, and while there's no confirmed breach yet, the exposed credentials represent a severe vulnerability that officials are struggling to contain and invalidate.

rss · Schneier on Security · May 22, 13:58

**Background**: AWS GovCloud is an isolated Amazon Web Services region designed to host sensitive government workloads and data, requiring separate credentials from the standard AWS cloud. A GitHub repository is a version-controlled project folder that can be set as public (visible to anyone) or private (restricted access), and accidentally exposing secrets in public repos is a common security mistake.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techrepublic.com/article/news-cisa-contractor-github-credential-leak/">CISA Contractor Exposed Sensitive Credentials in Public GitHub Repository</a></li>
<li><a href="https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/signing-into-govcloud.md">docs. aws . amazon .com/ govcloud -us/latest/UserGuide/signing-into...</a></li>
<li><a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories">About repositories - GitHub Docs</a></li>

</ul>
</details>

**Discussion**: The incident has prompted immediate demands for answers from lawmakers in both houses of Congress, and security experts are describing it as an inexcusable failure in basic security hygiene for the nation's top cybersecurity agency.

**Tags**: `#cybersecurity`, `#government-security`, `#data-leak`, `#AWS`, `#critical-infrastructure`

---

<a id="item-3"></a>
## [Using BPF for Custom Linux Page Cache Eviction Policies](https://lwn.net/Articles/1073103/) ⭐️ 8.0/10

A proposal to enable customizable page-cache eviction policies for specific workloads using BPF was presented by Tal Zussman at the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit. This approach could significantly improve system performance by allowing the kernel's page-cache eviction to be optimized for specific application workloads, moving beyond the current one-size-fits-all policy. The proposal leverages the cache_ext framework, which uses eBPF struct_ops to allow BPF programs to hook into kernel page-cache operations and can attach policies to specific cgroups for targeted workload management.

rss · LWN.net · May 22, 14:37

**Background**: The Linux kernel's page cache stores recently accessed file data in memory (managed as folios) to reduce slow disk I/O. Its default eviction policy decides which data to remove when memory is needed. BPF (extended Berkeley Packet Filter) is a technology that allows safe, efficient programs to run in the kernel without modifying kernel source code, making the kernel dynamically programmable.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cache-ext/cache_ext">GitHub - cache-ext/cache_ext: cache_ext is a framework to ...</a></li>
<li><a href="https://deepwiki.com/cache-ext/cache_ext/3.2-ebpf-policy-system">eBPF Policy System | cache-ext/cache_ext | DeepWiki</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3731569.3764820">cache_ext: Customizing the Page Cache with eBPF</a></li>

</ul>
</details>

**Tags**: `#Linux kernel`, `#BPF`, `#memory management`, `#page cache`, `#systems performance`

---

<a id="item-4"></a>
## [A 16-Byte Demo Combining Graphics and Sound Achieves Record-Breaking Optimization](https://hellmood.111mb.de/wake_up_16b_writeup.html) ⭐️ 7.0/10

A detailed write-up has been published explaining the creation of a 16-byte demoscene demo that successfully generates both visual graphics and audio sound within an extraordinarily tiny binary size. This project represents a significant leap in size-coding artistry, pushing the boundaries of what is technically possible with extreme code compression and inspiring admiration across the creative programming community. The demo is a masterpiece that integrates both visual output and sound synthesis, which is exceptionally challenging within a 16-byte constraint, far surpassing previous 32-byte demos that often lacked audio.

hackernews · MaximilianEmel · May 24, 00:30 · [Discussion](https://news.ycombinator.com/item?id=48253060)

**Background**: The demoscene is a computer art subculture where programmers create audiovisual presentations called 'demos', often under strict size limitations. Size-coding, or creating programs with the smallest possible binary size, is a specialized discipline within this scene that demands profound knowledge of computer architecture, instruction sets, and creative exploitation of system behaviors.

<details><summary>References</summary>
<ul>
<li><a href="http://www.sizecoding.org/wiki/Main_Page">SizeCoding.org</a></li>
<li><a href="http://www.sizecoding.org/wiki/Design_Tips_and_Demoscene_effects_with_pseudo_code">Design Tips and Demoscene effects with pseudo code - SizeCoding</a></li>

</ul>
</details>

**Discussion**: The community reaction on Hacker News was overwhelmingly positive, with users expressing deep admiration for the technical artistry, calling it a 'masterpiece' and a testament to why they love programming. Some expressed a sense of awe that such creative coding is often undervalued in the modern software industry dominated by AI and large-scale applications.

**Tags**: `#demoscene`, `#size-coding`, `#low-level-programming`, `#creative-coding`

---

<a id="item-5"></a>
## [C# introduces union types in .NET 11 preview](https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/) ⭐️ 7.0/10

The C# programming language is adding union types, a feature now available in the .NET 11 preview, allowing developers to define a value that can be exactly one of a fixed set of types with compiler-enforced exhaustive pattern matching. This is a significant enhancement to C#'s type system that improves type safety and code expressiveness, aligning the language with a long-standing feature from modern functional languages like F# and responding to years of community requests. The new `union` keyword declares that a value is exactly one of a fixed set of types, and the implementation supports exhaustive pattern matching, meaning the compiler will ensure all possible cases are handled.

hackernews · ingve · May 22, 12:28 · [Discussion](https://news.ycombinator.com/item?id=48234954)

**Background**: Union types, also known as discriminated unions or tagged unions, are a fundamental data structure in functional programming that allow a value to be one of several distinct, predefined types. Languages like F#, OCaml, and Haskell have long featured them, enabling more precise modeling of data and robust error handling. In the context of C# and .NET, this feature has been a top user request for over a decade.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union">Union types - C# reference | Microsoft Learn</a></li>
<li><a href="https://devblogs.microsoft.com/dotnet/csharp-15-union-types/">Explore union types in C# 15 - .NET Blog</a></li>

</ul>
</details>

**Discussion**: The community response is largely positive and reflects long-awaited anticipation, with users appreciating the effort of the C# team. Several comments draw direct comparisons to F#, noting that C# has historically adopted successful features from its functional sibling, with one user humorously quipping that 'C# is basically just slowly becoming F# with a C-style syntax.'

**Tags**: `#C#`, `#.NET`, `#programming-languages`, `#type-system`, `#language-features`

---

<a id="item-6"></a>
## [AI Data Centers' Demand for HBM Memory to Increase Consumer Electronics Prices](https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything) ⭐️ 7.0/10

AI data centers' rapidly growing demand for High Bandwidth Memory (HBM) is projected to consume 20% of global memory wafer capacity by the end of 2026, up from just 2% previously. This significant reallocation is expected to reduce the supply of consumer-grade memory like DDR and LPDDR, leading to higher prices for devices such as smartphones. This supply chain shift threatens to make budget consumer electronics, particularly sub-$100 smartphones crucial for markets in Africa and South Asia, significantly more expensive. It demonstrates how the booming AI industry's hardware demands can have direct, tangible impacts on everyday consumer products and digital inclusion. A single gigabyte of HBM consumes over three times the wafer capacity compared to a gigabyte of standard DDR or LPDDR memory due to its complex 3D-stacked architecture. Memory manufacturers, now consolidated to three major players, historically tend to under-provision production capacity, which will constrain consumer memory supply for several years.

rss · Simon Willison · May 22, 22:01

**Background**: The global memory market is dominated by three companies: Samsung, SK Hynix, and Micron. They produce different types of DRAM on a shared, fixed pool of wafer capacity. DDR is used in PCs and servers, LPDDR is optimized for mobile devices, and HBM is a high-performance, 3D-stacked variant essential for AI and high-performance computing accelerators. The allocation of wafer capacity between these product types is a critical factor in supply and pricing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://semiwiki.com/wikis/semiconductor-ip-wikis/ddr-vs-lpddr-vs-hbm-wiki/">DDR vs. LPDDR vs. HBM Wiki - SemiWiki</a></li>

</ul>
</details>

**Tags**: `#supply chain`, `#memory shortage`, `#HBM`, `#consumer electronics`, `#AI impact`

---

<a id="item-7"></a>
## [Linux Summit Tackles Page Fault Lock Contention](https://lwn.net/Articles/1073071/) ⭐️ 7.0/10

At the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit, Barry Song led a session focused on finding an enduring solution to the lock contention problem caused by major page faults when multiple threads share an address space. This lock contention is a significant performance bottleneck for multi-threaded applications that frequently trigger major page faults, and solving it could improve system efficiency for a wide range of server and high-performance computing workloads. A major page fault occurs when data must be read from storage into RAM, a time-consuming operation that can cause threads to contend for kernel locks while waiting for I/O, degrading overall performance.

rss · LWN.net · May 22, 13:50

**Background**: A page fault is an exception that occurs when a program accesses memory not currently in physical RAM. A major fault requires slow I/O from disk or swap, unlike a minor fault that can be resolved with data already in memory. When multiple threads share the same address space, concurrent faults can create contention on kernel data structures, slowing down the entire process.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Page_fault">Page fault - Wikipedia</a></li>
<li><a href="https://bowshock.nl/stories/memory_management/">Mysterious kernel lock contention – Bow Shock Systems Consulting</a></li>

</ul>
</details>

**Tags**: `#Linux kernel`, `#memory management`, `#performance optimization`, `#lock contention`

---

<a id="item-8"></a>
## [Reverse Engineering of Unitree Go2's GO-M8018-6 Motor Controller](https://hackaday.com/2026/05/23/unitree-go-m8018-6-motor-reverse-engineering/) ⭐️ 7.0/10

A detailed reverse engineering analysis of the Unitree Go2 quadruped robot's GO-M8018-6 motor controller has been published, revealing its internal hardware and control mechanisms. This analysis provides valuable insights into the hardware design and control systems of an affordable commercial robot, which can be used by robotics enthusiasts and engineers for education, modification, or development of open-source projects. The reverse-engineered motor is a compact integrated actuator featuring a built-in reducer, magnetic encoder, 3-phase inverter, current sensing, RS485 communication, and a Cortex-M0 based CMS32M57xx motor-control MCU, making it a promising platform for open-source Field-Oriented Control firmware.

rss · Hackaday · May 23, 08:00

**Background**: The Unitree Go2 is a commercially available quadruped robot known for its relatively low price point, making advanced robotics hardware more accessible. Field-Oriented Control (FOC) is a sophisticated method for controlling brushless DC motors that provides precise torque and speed control. Reverse engineering such commercial hardware involves deducing its design through inspection, documentation, and observation to enable custom firmware development.

<details><summary>References</summary>
<ul>
<li><a href="https://hackaday.com/2026/05/23/unitree-go-m8018-6-motor-reverse-engineering/">Unitree GO-M8018-6 Motor Reverse Engineering | Hackaday</a></li>
<li><a href="https://community.simplefoc.com/t/unitree-go2-go-m8018-6-motor-as-an-open-foc-platform/8140">Unitree Go2 / GO-M8018-6 motor as an open FOC platform?</a></li>
<li><a href="https://github.com/thomasfla/go2_motor_analysis/">thomasfla/go2_motor_analysis - GitHub</a></li>

</ul>
</details>

**Discussion**: The analysis has generated interest in the robotics and open-source hardware communities, with discussions focusing on the potential to use the motor as a platform for developing custom open-source FOC firmware, as seen in the SimpleFOC community thread.

**Tags**: `#reverse-engineering`, `#robotics`, `#motor-control`, `#hardware-hacking`, `#open-source`

---

<a id="item-9"></a>
## [Debating the HTML Definition List Element's Value and Limitations](https://benmyers.dev/blog/on-the-dl/) ⭐️ 6.0/10

A blog post and subsequent Hacker News discussion highlighted the semantic confusion and practical limitations surrounding the underutilized HTML `<dl>` (definition list) element, questioning its modern relevance and proper accessibility usage. This debate touches on core challenges in semantic HTML, forcing developers to weigh the theoretical benefits of semantic markup against the practical constraints of real-world design and accessibility requirements, which impacts how we build maintainable and accessible interfaces. Community comments revealed a specific accessibility pitfall: using `aria-label` on a `<dl>` element is incorrect because it lacks a corresponding ARIA role, highlighting the gap between developer assumptions and specification conformance.

hackernews · ravenical · May 23, 13:03 · [Discussion](https://news.ycombinator.com/item?id=48247325)

**Background**: The `<dl>` element was originally intended for definition lists or glossaries but its semantic meaning was expanded in HTML5 to represent any name-value pair group, which has led to ongoing debate about its appropriate use cases. Semantic HTML elements are designed to provide meaning to both browsers and developers, improving accessibility and maintainability, but their adoption is often hindered by perceived inflexibility in complex layouts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.w3schools.com/html/html5_semantic_elements.asp">HTML Semantic Elements</a></li>
<li><a href="https://www.accessibilitychecker.org/wcag-guides/ensure-elements-are-structured-correctly/">Structuring dl Elements Correctly | WCAG Guidelines</a></li>
<li><a href="https://css-tricks.com/on-the-dl/">Blogging about HTML elements ¹? *chefs kiss* | CSS-Tricks</a></li>

</ul>
</details>

**Discussion**: The discussion revealed deep divides: one user argued that life became easier after abandoning semantic HTML due to the `<dl>` element's lack of flexibility for real-world design needs, while others pointed to its historical significance, noting its use in the world's first website and origins predating the web in 1980s IBM systems. A key technical correction was made regarding incorrect ARIA attribute usage, emphasizing the gap between intent and specification compliance.

**Tags**: `#HTML`, `#accessibility`, `#web-development`, `#semantic-web`, `#frontend`

---

<a id="item-10"></a>
## [Linux stable kernels released with Fragnesia vulnerability fix](https://lwn.net/Articles/1074117/) ⭐️ 6.0/10

A batch of seven Linux stable kernel updates (versions 7.0.10, 6.18.33, 6.12.91, 6.6.141, 6.1.174, 5.15.208, and 5.10.257) have been released, with the first four being large maintenance releases and the last three being smaller updates specifically addressing the Fragnesia vulnerability. These updates are critical for system administrators and users because they include patches for the high-severity Fragnesia local privilege escalation vulnerability (CVE-2026-46300), which could allow unprivileged users to gain root access, and they provide essential maintenance fixes across multiple long-term support kernel branches. The large updates, such as 7.0.10, contain over a thousand commits backported from the mainline, while the smaller updates for older kernels (5.10, 5.15, 6.1) are targeted security fixes; the Fragnesia exploit is notably reliable as it does not require a race condition.

rss · LWN.net · May 23, 13:55

**Background**: The Linux kernel has a tiered release system with mainline, stable, and long-term support (LTS) branches. Stable kernels receive backported bug fixes and security patches from the mainline development tree. The Fragnesia vulnerability is a significant local privilege escalation flaw in the kernel that allows any unprivileged user to gain root access without complex exploitation steps.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/fragnesia-linux-vulnerability/">Fragnesia - New Linux Kernel Vulnerability Enables Root Access</a></li>
<li><a href="https://www.kernel.org/releases.html">Active kernel releases</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linux_kernel_version_history">Linux kernel version history - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#security`, `#software-updates`, `#system-administration`

---

<a id="item-11"></a>
## [Touchable Mid-Air POV Display Developed by University Team](https://hackaday.com/2026/05/23/touchable-pov-display-blooms-in-mid-air/) ⭐️ 6.0/10

A team from the University developed a novel persistence-of-vision (POV) display that projects visuals in mid-air and allows users to physically touch and interact with the displayed images. This advancement bridges the gap between virtual visuals and physical interaction, potentially enabling new forms of touch-based interfaces for gaming, education, and public installations without requiring wearable devices. The display uses the persistence-of-vision principle, where rapidly moving LEDs create the illusion of a solid image, and the key innovation is integrating a sensing method that detects physical touch on these projected visuals in open air.

rss · Hackaday · May 23, 23:00

**Background**: Persistence-of-vision (POV) displays create images by moving light sources quickly enough that the human eye perceives a continuous pattern. Mid-air haptic systems use technologies like ultrasound arrays to create tactile sensations on bare skin without direct contact. Touchable volumetric displays are an emerging field aiming to let users directly interact with 3D projected images.

<details><summary>References</summary>
<ul>
<li><a href="https://hades.mech.northwestern.edu/index.php/Persistence-of-Vision_Display">Persistence - of - Vision Display - Northwestern Mechatronics Wiki</a></li>
<li><a href="https://hackaday.com/2025/04/14/elastic-bands-enable-touchable-volumetric-display/">Elastic Bands Enable Touchable Volumetric Display | Hackaday</a></li>
<li><a href="https://www.davide-dicenso.com/projects/midair-haptics-zcm6z">Mid-Air Haptic Feedback SYSTEM - Davide Di Censo</a></li>

</ul>
</details>

**Tags**: `#display-technology`, `#human-computer-interaction`, `#POV`, `#haptics`

---