---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 49 items, 11 important content pieces were selected

---

1. [微软开源已发现最早的 DOS 源代码，该代码源自纸质存档](#item-1) ⭐️ 9.0/10
2. [CISA 承包商在公共 GitHub 上泄露高权限 AWS GovCloud 密钥](#item-2) ⭐️ 9.0/10
3. [利用 BPF 实现 Linux 页面缓存自定义驱逐策略](#item-3) ⭐️ 8.0/10
4. [一个结合图形与声音的 16 字节演示程序，实现了破纪录的代码优化](#item-4) ⭐️ 7.0/10
5. [C#在.NET 11 预览版中引入联合类型](#item-5) ⭐️ 7.0/10
6. [AI 数据中心对 HBM 内存的需求将导致消费电子产品涨价](#item-6) ⭐️ 7.0/10
7. [Linux 峰会探讨页错误锁争用问题](#item-7) ⭐️ 7.0/10
8. [对宇树 Go2 四足机器人 GO-M8018-6 电机控制器的逆向工程分析](#item-8) ⭐️ 7.0/10
9. [关于 HTML 定义列表元素的价值与局限性的讨论](#item-9) ⭐️ 6.0/10
10. [Linux 稳定内核更新，修复 Fragnesia 漏洞](#item-10) ⭐️ 6.0/10
11. [研究团队开发可触摸的空中视觉暂留显示器](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [微软开源已发现最早的 DOS 源代码，该代码源自纸质存档](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 9.0/10

微软已发布已知最早的 86-DOS 1.00 内核源代码列表及早期 PC-DOS 实用程序的源代码，这些代码是从纸质打印件转录而来，以纪念 86-DOS 发布 45 周年。 此次发布保存了个人计算史上一个基础性的篇章，展示了驱动 IBM PC 并奠定微软霸主地位的操作系统的起源，同时也体现了数字考古领域的重大努力。 这些源代码最初并非以数字形式存储；一支由历史学家组成的团队从原始开发者蒂姆·帕特森提供的、有数十年历史的纸质打印件中精心扫描并转录了代码，由于文件质量较差，这一过程颇具难度。

hackernews · DamnInteresting · May 24, 01:21 · [社区讨论](https://news.ycombinator.com/item?id=48253386)

**背景**: 86-DOS，最初名为 QDOS（快速且粗糙的操作系统），由西雅图计算机产品公司为英特尔 8086 架构的计算机开发。微软于 1981 年购买了其版权，将其更名为 MS-DOS，并授权给 IBM 使用，这成为了 IBM PC 及其兼容机的基础操作系统，定义了早期的 PC 时代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://redmondmag.com/articles/2026/04/29/microsoft-open-sources-earliest-dos-code-on-anniversary.aspx">Microsoft Open Sources Earliest DOS Code on Anniversary -- Redmondmag.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/86-DOS">86-DOS - Wikipedia</a></li>
<li><a href="https://historyofinformation.com/detail.php?id=99">History of Information</a></li>

</ul>
</details>

**社区讨论**: 社区反响极为正面，用户对微软的这一保护工作表达了罕见的感谢。讨论重点强调了该代码的历史意义、OCR 转录过程的艰难，以及对未来是否会发布早期 Windows 版本源代码的猜测。

**标签**: `#computing-history`, `#open-source`, `#microsoft`, `#DOS`, `#preservation`

---

<a id="item-2"></a>
## [CISA 承包商在公共 GitHub 上泄露高权限 AWS GovCloud 密钥](https://www.schneier.com/blog/archives/2026/05/cisa-security-leak.html) ⭐️ 9.0/10

美国网络安全和基础设施安全局（CISA）的一名承包商将一个包含多个高权限 AWS GovCloud 账户凭证和 CISA 内部系统详细信息的 GitHub 仓库公开暴露，持续时间未知。 这被认为是近年来最严重的政府数据泄露事件之一，因为它暴露了用于敏感政府工作的安全云环境的密钥，攻击者可能借此破坏关键基础设施和机构运作。 公开的存档中包含了详细描述 CISA 内部如何构建、测试和部署软件的文件，尽管目前尚未确认发生实际入侵，但暴露的凭证构成严重漏洞，官方正在努力控制和撤销这些凭证。

rss · Schneier on Security · May 22, 13:58

**背景**: AWS GovCloud 是亚马逊云服务中一个隔离的区域，专为托管敏感的政府工作负载和数据而设计，其凭证与标准 AWS 云完全独立。GitHub 仓库是一个版本控制的项目文件夹，可以设置为公开（所有人可见）或私有（访问受限），在公共仓库中意外暴露密钥是一个常见的安全失误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techrepublic.com/article/news-cisa-contractor-github-credential-leak/">CISA Contractor Exposed Sensitive Credentials in Public GitHub Repository</a></li>
<li><a href="https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/signing-into-govcloud.md">docs. aws . amazon .com/ govcloud -us/latest/UserGuide/signing-into...</a></li>
<li><a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories">About repositories - GitHub Docs</a></li>

</ul>
</details>

**社区讨论**: 该事件已导致国会两院议员立即要求作出解释，安全专家则将其描述为国家最高网络安全机构在基本安全规范方面不可原谅的失败。

**标签**: `#cybersecurity`, `#government-security`, `#data-leak`, `#AWS`, `#critical-infrastructure`

---

<a id="item-3"></a>
## [利用 BPF 实现 Linux 页面缓存自定义驱逐策略](https://lwn.net/Articles/1073103/) ⭐️ 8.0/10

在 2026 年 Linux 存储、文件系统、内存管理和 BPF 峰会上，Tal Zussman 提出了一项利用 BPF 为特定工作负载启用可定制页面缓存驱逐策略的提案。 这种方法可以通过允许针对特定应用程序工作负载优化内核的页面缓存驱逐，从而显著提升系统性能，超越当前的通用策略。 该提案利用了 cache_ext 框架，该框架使用 eBPF 的 struct_ops 机制允许 BPF 程序挂钩到内核页面缓存操作，并可以将策略附加到特定的 cgroup 以进行目标工作负载管理。

rss · LWN.net · May 22, 14:37

**背景**: Linux 内核的页面缓存将最近访问的文件数据存储在内存中（以 folio 为单位管理），以减少缓慢的磁盘 I/O。其默认驱逐策略决定了在需要内存时移除哪些数据。BPF（扩展伯克利包过滤器）是一种允许安全、高效的程序在内核中运行而无需修改内核源代码的技术，使内核可动态编程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cache-ext/cache_ext">GitHub - cache-ext/cache_ext: cache_ext is a framework to ...</a></li>
<li><a href="https://deepwiki.com/cache-ext/cache_ext/3.2-ebpf-policy-system">eBPF Policy System | cache-ext/cache_ext | DeepWiki</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3731569.3764820">cache_ext: Customizing the Page Cache with eBPF</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#BPF`, `#memory management`, `#page cache`, `#systems performance`

---

<a id="item-4"></a>
## [一个结合图形与声音的 16 字节演示程序，实现了破纪录的代码优化](https://hellmood.111mb.de/wake_up_16b_writeup.html) ⭐️ 7.0/10

一篇详尽的解析文章已经发布，解释了如何在一个极小的 16 字节二进制文件中，成功地同时生成图形和声音的演示程序。 该项目代表了代码体积优化艺术的一次重大飞跃，将极端代码压缩的技术可能性推向了新的边界，并赢得了创意编程社区的广泛赞誉。 该演示是一个集成了视觉输出和声音合成的杰作，在 16 字节的严苛限制下实现这一点极具挑战性，远远超越了此前通常没有音频的 32 字节演示。

hackernews · MaximilianEmel · May 24, 00:30 · [社区讨论](https://news.ycombinator.com/item?id=48253060)

**背景**: Demoscene（演示场景）是一种计算机艺术亚文化，程序员在此创作被称为'演示'的视听作品，通常受到严格的字节大小限制。代码体积优化（size-coding），即以尽可能小的二进制文件创建程序，是这一场景中的专门领域，要求对计算机架构、指令集以及创造性地利用系统行为有深刻的理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.sizecoding.org/wiki/Main_Page">SizeCoding.org</a></li>
<li><a href="http://www.sizecoding.org/wiki/Design_Tips_and_Demoscene_effects_with_pseudo_code">Design Tips and Demoscene effects with pseudo code - SizeCoding</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的社区反应极为正面，用户对这种技术艺术性表达了深深的钦佩，称其为'杰作'，并感叹这正是他们热爱编程的原因。一些人感到惋惜，认为这种富有创造性的编程在由人工智能和大型应用程序主导的现代软件行业中常常被低估。

**标签**: `#demoscene`, `#size-coding`, `#low-level-programming`, `#creative-coding`

---

<a id="item-5"></a>
## [C#在.NET 11 预览版中引入联合类型](https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/) ⭐️ 7.0/10

C#编程语言正在添加联合类型，此功能现已在.NET 11 预览版中可用，允许开发者定义一个值，该值必须是固定类型集中的一个，编译器会强制执行穷举模式匹配。 这是对 C#类型系统的重大增强，提高了类型安全性和代码表达能力，使该语言与 F#等现代函数式语言的长期特性保持一致，并回应了社区多年的请求。 新的`union`关键字声明一个值必须是固定类型集中的一个，并且该实现支持穷举模式匹配，这意味着编译器将确保所有可能的情况都已处理。

hackernews · ingve · May 22, 12:28 · [社区讨论](https://news.ycombinator.com/item?id=48234954)

**背景**: 联合类型（也称为可区分联合或标记联合）是函数式编程中的一种基本数据结构，它允许一个值是几个不同预定义类型中的一个。F#、OCaml 和 Haskell 等语言早已具备此功能，能够更精确地建模数据并实现健壮的错误处理。在 C#和.NET 的背景下，此功能是用户超过十年的首要请求之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union">Union types - C# reference | Microsoft Learn</a></li>
<li><a href="https://devblogs.microsoft.com/dotnet/csharp-15-union-types/">Explore union types in C# 15 - .NET Blog</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，反映了长期的期待，用户们赞赏 C#团队的努力。一些评论直接与 F#进行了比较，指出 C#历史上从其函数式兄弟语言中采纳了许多成功特性，一位用户甚至幽默地评论道：“C#基本上只是在慢慢变成一个带 C 风格语法的 F#。”

**标签**: `#C#`, `#.NET`, `#programming-languages`, `#type-system`, `#language-features`

---

<a id="item-6"></a>
## [AI 数据中心对 HBM 内存的需求将导致消费电子产品涨价](https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything) ⭐️ 7.0/10

AI 数据中心对高带宽内存（HBM）的快速增长需求预计到 2026 年底将占据全球内存晶圆产能的 20%，此前仅为 2%。这一重大的产能重新分配预计将减少 DDR 和 LPDDR 等消费级内存的供应，从而导致智能手机等设备价格上涨。 这种供应链的转变可能导致平价消费电子产品——特别是对非洲和南亚市场至关重要的百美元以下智能手机——价格大幅上涨。这表明了蓬勃发展的 AI 产业硬件需求如何能对日常消费品及数字普惠产生直接而切实的影响。 由于其复杂的 3D 堆叠架构，1GB 的 HBM 所消耗的晶圆产能是 1GB 标准 DDR 或 LPDDR 内存的三倍以上。目前仅存的三大内存制造商历来倾向于保守配置产能，这将限制消费级内存供应长达数年。

rss · Simon Willison · May 22, 22:01

**背景**: 全球内存市场由三星、SK 海力士和美光三家公司主导。它们在共享、固定的晶圆产能池上生产不同类型的 DRAM。DDR 用于个人电脑和服务器，LPDDR 针对移动设备优化，而 HBM 是 AI 和高性能计算加速器不可或缺的高性能 3D 堆叠变体。在这些产品类型之间分配晶圆产能是影响供应和定价的关键因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://semiwiki.com/wikis/semiconductor-ip-wikis/ddr-vs-lpddr-vs-hbm-wiki/">DDR vs. LPDDR vs. HBM Wiki - SemiWiki</a></li>

</ul>
</details>

**标签**: `#supply chain`, `#memory shortage`, `#HBM`, `#consumer electronics`, `#AI impact`

---

<a id="item-7"></a>
## [Linux 峰会探讨页错误锁争用问题](https://lwn.net/Articles/1073071/) ⭐️ 7.0/10

在 2026 年 Linux 存储、文件系统、内存管理与 BPF 峰会上，Barry Song 主持了一场会议，旨在为多个线程共享地址空间时，由主缺页中断（major page fault）引起的锁争用问题寻找一个持久的解决方案。 这种锁争用是频繁触发主缺页中断的多线程应用程序的一个重要性能瓶颈，解决此问题可以提升各类服务器和高性能计算工作负载的系统效率。 主缺页中断发生时，数据必须从存储设备读入 RAM，这是一个耗时的操作，可能导致线程在等待 I/O 完成时争用内核锁，从而降低整体性能。

rss · LWN.net · May 22, 13:50

**背景**: 页错误是当程序访问当前不在物理内存中的内存时发生的异常。与只需内存中已有数据即可解决的轻微错误不同，主错误需要从磁盘或交换区进行缓慢的 I/O 操作。当多个线程共享同一地址空间时，并发的错误会导致对内核数据结构的争用，从而减慢整个进程的速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Page_fault">Page fault - Wikipedia</a></li>
<li><a href="https://bowshock.nl/stories/memory_management/">Mysterious kernel lock contention – Bow Shock Systems Consulting</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#memory management`, `#performance optimization`, `#lock contention`

---

<a id="item-8"></a>
## [对宇树 Go2 四足机器人 GO-M8018-6 电机控制器的逆向工程分析](https://hackaday.com/2026/05/23/unitree-go-m8018-6-motor-reverse-engineering/) ⭐️ 7.0/10

一份对宇树 Go2 四足机器人 GO-M8018-6 电机控制器的详细逆向工程分析已经发布，揭示了其内部硬件和控制机制。 该分析为机器人爱好者和工程师提供了对一款平价商用机器人硬件设计和控制系统的宝贵见解，可用于教育、改装或开发开源项目。 被逆向工程的电机是一款紧凑型集成执行器，内置减速器、磁编码器、三相逆变器、电流感应、RS485 通信以及基于 Cortex-M0 的 CMS32M57xx 电机控制 MCU，使其成为开发开源磁场定向控制固件的理想平台。

rss · Hackaday · May 23, 08:00

**背景**: 宇树 Go2 是一款商用四足机器人，以其相对低廉的价格而闻名，使先进的机器人硬件更加普及。磁场定向控制（FOC）是一种用于控制无刷直流电机的先进方法，可提供精确的扭矩和速度控制。对此类商业硬件进行逆向工程，需要通过检查、文档分析和观察来推断其设计，以实现自定义固件的开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hackaday.com/2026/05/23/unitree-go-m8018-6-motor-reverse-engineering/">Unitree GO-M8018-6 Motor Reverse Engineering | Hackaday</a></li>
<li><a href="https://community.simplefoc.com/t/unitree-go2-go-m8018-6-motor-as-an-open-foc-platform/8140">Unitree Go2 / GO-M8018-6 motor as an open FOC platform?</a></li>
<li><a href="https://github.com/thomasfla/go2_motor_analysis/">thomasfla/go2_motor_analysis - GitHub</a></li>

</ul>
</details>

**社区讨论**: 该分析引起了机器人和开源硬件社区的兴趣，讨论集中在利用该电机作为开发自定义开源 FOC 固件平台的潜力上，这在 SimpleFOC 社区的帖子中可见一斑。

**标签**: `#reverse-engineering`, `#robotics`, `#motor-control`, `#hardware-hacking`, `#open-source`

---

<a id="item-9"></a>
## [关于 HTML 定义列表元素的价值与局限性的讨论](https://benmyers.dev/blog/on-the-dl/) ⭐️ 6.0/10

一篇博文及随后的 Hacker News 讨论聚焦于未被充分利用的 HTML `<dl>`（定义列表）元素所带来的语义困惑和实际局限性，质疑其在现代开发中的相关性及正确的无障碍用法。 这场辩论触及了语义化 HTML 的核心挑战，迫使开发者在理论上的语义标记优势与现实设计和无障碍需求的实际限制之间做出权衡，这影响着我们构建可维护和无障碍界面的方式。 社区评论揭示了一个具体的无障碍陷阱：在`<dl>`元素上使用`aria-label`是错误的，因为它缺乏对应的 ARIA 角色，这凸显了开发者假设与规范符合性之间的差距。

hackernews · ravenical · May 23, 13:03 · [社区讨论](https://news.ycombinator.com/item?id=48247325)

**背景**: `<dl>`元素最初用于定义列表或词汇表，但其语义含义在 HTML5 中被扩展，用于表示任何名称-值对的分组，这导致了关于其适用场景的持续争论。语义化 HTML 元素旨在为浏览器和开发者提供含义，以改善无障碍性和可维护性，但其采用常常受到复杂布局中灵活性不足的看法阻碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.w3schools.com/html/html5_semantic_elements.asp">HTML Semantic Elements</a></li>
<li><a href="https://www.accessibilitychecker.org/wcag-guides/ensure-elements-are-structured-correctly/">Structuring dl Elements Correctly | WCAG Guidelines</a></li>
<li><a href="https://css-tricks.com/on-the-dl/">Blogging about HTML elements ¹? *chefs kiss* | CSS-Tricks</a></li>

</ul>
</details>

**社区讨论**: 讨论揭示了深刻分歧：一位用户认为，由于`<dl>`元素缺乏灵活性以满足实际设计需求，放弃语义化 HTML 后生活变得更轻松，而其他人则指出了其历史意义，注意到它在世界首个网站中的使用及其起源于 1980 年代 IBM 系统甚至早于网络。一个关键的错误用法被技术性地纠正，强调了意图与规范符合性之间的差距。

**标签**: `#HTML`, `#accessibility`, `#web-development`, `#semantic-web`, `#frontend`

---

<a id="item-10"></a>
## [Linux 稳定内核更新，修复 Fragnesia 漏洞](https://lwn.net/Articles/1074117/) ⭐️ 6.0/10

一批共七个 Linux 稳定内核更新版本（7.0.10、6.18.33、6.12.91、6.6.141、6.1.174、5.15.208 和 5.10.257）已发布，其中前四个为大型维护版本，后三个为专门修复 Fragnesia 漏洞的小型更新。 这些更新对系统管理员和用户至关重要，因为它们包含了针对高严重性 Fragnesia 本地权限提升漏洞（CVE-2026-46300）的补丁，该漏洞可能允许非特权用户获得 root 权限，并且它们为多个长期支持内核分支提供了重要的维护修复。 大型更新（如 7.0.10）包含超过一千个从主线反向移植的提交，而针对较旧内核（5.10、5.15、6.1）的较小更新则是有针对性的安全修复；Fragnesia 漏洞利用特别可靠，因为它不需要竞争条件。

rss · LWN.net · May 23, 13:55

**背景**: Linux 内核采用分层发布系统，包括主线、稳定和长期支持（LTS）分支。稳定内核接收从主线开发树反向移植的错误修复和安全补丁。Fragnesia 漏洞是内核中一个重大的本地权限提升缺陷，它允许任何非特权用户无需复杂的利用步骤即可获得 root 访问权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/fragnesia-linux-vulnerability/">Fragnesia - New Linux Kernel Vulnerability Enables Root Access</a></li>
<li><a href="https://www.kernel.org/releases.html">Active kernel releases</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linux_kernel_version_history">Linux kernel version history - Wikipedia</a></li>

</ul>
</details>

**标签**: `#linux-kernel`, `#security`, `#software-updates`, `#system-administration`

---

<a id="item-11"></a>
## [研究团队开发可触摸的空中视觉暂留显示器](https://hackaday.com/2026/05/23/touchable-pov-display-blooms-in-mid-air/) ⭐️ 6.0/10

一个研究团队开发了一种新颖的视觉暂留显示器，该显示器能在空中投射影像，并允许用户物理触摸和交互所显示的图像。 这一进步弥合了虚拟视觉与物理交互之间的鸿沟，可能为游戏、教育和公共设施带来无需穿戴设备的、基于触摸的新界面形式。 该显示器利用视觉暂留原理，通过快速移动的 LED 灯形成稳固图像的错觉，其关键创新在于集成了能探测用户对这些空中投影影像进行物理触摸的传感方法。

rss · Hackaday · May 23, 23:00

**背景**: 视觉暂留显示器通过快速移动光源来产生图像，速度快到人眼能感知到连续的图案。空中触觉反馈系统使用超声波阵列等技术，在不直接接触皮肤的情况下产生触觉感受。可触摸的体积显示是一个新兴领域，旨在让用户直接与投影的三维图像进行交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hades.mech.northwestern.edu/index.php/Persistence-of-Vision_Display">Persistence - of - Vision Display - Northwestern Mechatronics Wiki</a></li>
<li><a href="https://hackaday.com/2025/04/14/elastic-bands-enable-touchable-volumetric-display/">Elastic Bands Enable Touchable Volumetric Display | Hackaday</a></li>
<li><a href="https://www.davide-dicenso.com/projects/midair-haptics-zcm6z">Mid-Air Haptic Feedback SYSTEM - Davide Di Censo</a></li>

</ul>
</details>

**标签**: `#display-technology`, `#human-computer-interaction`, `#POV`, `#haptics`

---