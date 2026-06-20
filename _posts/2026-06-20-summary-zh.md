---
layout: default
title: "Horizon Summary: 2026-06-20 (ZH)"
date: 2026-06-20
lang: zh
---

> From 64 items, 23 important content pieces were selected

---

1. [历经十年开发，Valhalla 项目将在 JDK 28 中交付关键 Java 性能特性。](#item-1) ⭐️ 8.0/10
2. [研究人员将'Popa'安卓僵尸网络与一家以色列上市公司联系起来](#item-2) ⭐️ 8.0/10
3. [恶意软件嵌入违禁文本以干扰人工智能安全分析](#item-3) ⭐️ 8.0/10
4. [干细胞疗法成功根除严重自身免疫性疾病长达 15 年。](#item-4) ⭐️ 8.0/10
5. [基因组的物理复杂性挑战了 AI 在生物学中的建模能力。](#item-5) ⭐️ 8.0/10
6. [ATProto 澄清其架构中没有像 Mastodon 那样的‘实例’](#item-6) ⭐️ 7.0/10
7. [挪威禁止小学生使用 AI 工具](#item-7) ⭐️ 7.0/10
8. [现代汽车从软银手中完成对波士顿动力公司的全资收购](#item-8) ⭐️ 7.0/10
9. [对所有互联网流量实施真实身份验证的提议引发隐私与控制担忧](#item-9) ⭐️ 7.0/10
10. [Datasette Apps：新插件在沙盒化 iframe 中托管自定义 HTML 应用](#item-10) ⭐️ 7.0/10
11. [Systemd v261 发布，新增云实例元数据、启动密钥及内核热更新支持](#item-11) ⭐️ 7.0/10
12. [BPF 程序可能支持协程以实现挂起与恢复](#item-12) ⭐️ 7.0/10
13. [Arch Linux AUR 遭受持续供应链攻击，攻击者利用孤儿包投毒](#item-13) ⭐️ 7.0/10
14. [Linux 内核 7.2 合并窗口过半，已集成超过 7000 个变更集](#item-14) ⭐️ 7.0/10
15. [为高效云块设备复制提出的基于 RDMA 的新内核模块](#item-15) ⭐️ 7.0/10
16. [美国政府将 Anthropic 的 Fable AI 模型列为危险军需品](#item-16) ⭐️ 7.0/10
17. [肯特·贝克认为公司雇佣初级工程师是为了培养判断力，而非仅仅完成任务](#item-17) ⭐️ 6.0/10
18. [MCP 的核心价值被视为 AI 代理的认证网关](#item-18) ⭐️ 6.0/10
19. [Midjourney 跨界医疗影像，推出嵌入传感器的浴缸式扫描仪](#item-19) ⭐️ 6.0/10
20. [软件自由保护协会发布针对开源贡献使用大语言模型生成式 AI 的建议。](#item-20) ⭐️ 6.0/10
21. [Mastodon 4.6 推出策展集合功能及新的用户工具](#item-21) ⭐️ 6.0/10
22. [历史计算机被基准测试：看谁数到一百万最快](#item-22) ⭐️ 6.0/10
23. [初步数据显示肥胖药物可能对男性生育能力有益。](#item-23) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [历经十年开发，Valhalla 项目将在 JDK 28 中交付关键 Java 性能特性。](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 8.0/10

Valhalla 项目，一项长期旨在优化 Java 性能和内存布局的计划，将在即将到来的 JDK 28 版本中交付其核心特性，如值类型。 这非常重要，因为它直接解决了 Java 在内存效率和面向数据编程方面的历史性能差距，有望使 Java 在性能关键型应用和现代工作负载中更具竞争力。 一个关键技术特性是引入了“值类型”（内联类），它允许对象在没有对象头的情况下存储，并可以在数组中扁平化，从而大幅减少内存开销并提高 CPU 缓存利用率。

hackernews · philonoist · Jun 19, 06:35 · [社区讨论](https://news.ycombinator.com/item?id=48595511)

**背景**: Valhalla 项目是 OpenJDK 于 2014 年宣布的一个实验性项目，旨在通过弥合 Java 面向对象抽象与 C 等语言使用的高效扁平内存布局之间的性能差距，来彻底改革 Java 的数据模型。其目标是引入值类型——一种不可变、无标识的对象，可以像原始类型一样直接操作——以减少垃圾回收压力并提高内存局部性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language) - Wikipedia</a></li>
<li><a href="https://openjdk.org/jeps/401">JEP 401 : Value Classes and Objects (Preview)</a></li>
<li><a href="https://dev.to/adaumircosta/understanding-value-types-project-valhalla-faf">Understanding Value Types ( Project Valhalla ) - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出开发者强烈的兴趣，但也存在技术辩论和批评。一些评论者反对“空安全令人费解”的观点，而另一些则质疑特定内存布局示例的技术准确性。一种普遍的情绪是承认 Java 的重大现代化和持续演进，有些人认为漫长的开发时间是弥补此前疏忽的必要过程。

**标签**: `#java`, `#jvm`, `#performance`, `#programming-languages`, `#software-engineering`

---

<a id="item-2"></a>
## [研究人员将'Popa'安卓僵尸网络与一家以色列上市公司联系起来](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/) ⭐️ 8.0/10

安全研究人员得出结论，存在已久的 Popa 安卓僵尸网络与以色列上市公司 Alarum Technologies 运营的住宅代理服务 NetNut 有关。该僵尸网络曾迫使数百万台消费设备中继恶意网络流量。 这一发现揭示了一个重大网络安全威胁与一家合法的、公开上市的科技公司之间的直接联系，从而引发了对公司责任和住宅代理行业监管的严重质疑。 Popa 僵尸网络已活跃至少四年，利用被入侵的安卓电视盒子协助进行广告欺诈、账户接管和大规模数据抓取。被牵涉的代理服务 NetNut 声称可提供访问全球超过 1000 万个住宅 IP 地址的庞大网络。

rss · Krebs on Security · Jun 18, 17:37

**背景**: 僵尸网络是指一组被恶意软件感染并受攻击者远程控制的联网设备网络，设备所有者通常不知情。住宅代理服务通过互联网服务提供商分配给真实家庭的 IP 地址来路由用户的网络流量，使其流量看起来比来自数据中心的流量更合法、更难被封锁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.malwarebytes.com/blog/news/2025/03/android-botnet-badbox-largely-disrupted">Android botnet BadBox largely disrupted | Malwarebytes</a></li>
<li><a href="https://www.rescana.com/post/kimwolf-botnet-massive-android-tv-box-and-iot-malware-threat-exploiting-global-networks">Kimwolf Botnet: Massive Android TV Box and IoT Malware Threat Exploiting Global Networks – Rescana</a></li>
<li><a href="https://github.com/NetNut-Proxy-Network/NetNut">NetNut-Proxy-Network/NetNut: Premium Static & Rotating IPs | HTTP(s) Residential Proxy Network | Information & Code samples. · GitHub</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#botnet`, `#fraud`, `#corporate-accountability`, `#privacy`

---

<a id="item-3"></a>
## [恶意软件嵌入违禁文本以干扰人工智能安全分析](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html) ⭐️ 8.0/10

一名恶意软件开发者正在间谍软件的代码注释中嵌入有关核武器和生物武器的文本，以触发人工智能驱动安全分析工具的拒绝行为，从而有效规避自动扫描。真正的恶意负载采用 ROT 式替换混淆技术，放置在这个误导性头部之后。 这种策略代表了网络安全军备竞赛中一种新型的对抗技术，它利用人工智能分析模型的安全过滤器和内容策略，为恶意软件检测制造盲区。它突显了人工智能安全工具本身如何可能成为攻击向量，如果其决策逻辑被精心构造的输入所操纵。 违禁文本被插入在一个 JavaScript 块注释中，因此不会影响代码执行，但旨在干扰那些分析文件头的人工智能扫描器，可能导致上下文污染、过早分类或拒绝进一步分析。实际的恶意软件使用 ROT 式替换密码进行混淆，这是一种隐藏有效负载的常见技术。

rss · Schneier on Security · Jun 18, 11:04

**背景**: 对抗性机器学习涉及制作输入来操纵人工智能模型，其中规避攻击是一种绕过垃圾邮件过滤器或恶意软件扫描器等检测系统的常见方法。ROT 替换密码（如 ROT13）是恶意软件作者常用的简单字母移位技术，用于混淆恶意代码并规避基于签名的检测。人工智能驱动的安全扫描器分析代码或文件以识别威胁，但如果输入数据被故意制作以利用其安全机制或分析管道，其有效性可能会受到损害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Adversarial_machine_learning">Adversarial machine learning - Wikipedia</a></li>
<li><a href="https://www.infosecinstitute.com/resources/malware-analysis/simple-malware-obfuscation-techniques/">Simple malware obfuscation techniques | Infosec</a></li>
<li><a href="https://dev.to/manja316/i-found-a-way-to-bypass-ai-model-security-scanners-here-is-what-i-learned-44nb">I Found a Way to Bypass AI Model Security Scanners — Here is What I Learned - DEV Community</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#adversarial-ai`, `#malware`, `#ai-safety`, `#information-warfare`

---

<a id="item-4"></a>
## [干细胞疗法成功根除严重自身免疫性疾病长达 15 年。](https://www.nature.com/articles/d41586-026-01925-7) ⭐️ 8.0/10

首批接受自体造血干细胞移植 (AHSCT) 治疗视神经脊髓炎谱系障碍 (NMOSD) 的两名患者已保持无病状态长达 15 年，展示了前所未有的长期疗效。 这一长期成功表明，AHSCT 可能成为治疗严重、复发性自身免疫性疾病的根治性疗法，有望让患者免于终身免疫抑制治疗，并极大改善生活质量。 该疗法 AHSCT 包括采集患者自身的干细胞、使用化疗重启免疫系统，然后回输干细胞；NMOSD 是一种罕见且致残的自身免疫性疾病，会攻击视神经和脊髓。

rss · Nature · Jun 19, 00:00

**背景**: 视神经脊髓炎谱系障碍（NMOSD）是一种严重的自身免疫性疾病，会导致中枢神经系统发生炎症性攻击，引发视力丧失和瘫痪。自体造血干细胞移植（AHSCT）是一种主要用于治疗血癌的成熟疗法，近年来越来越多地被探索用于治疗严重、难治性自身免疫性疾病，其目标是重置患者失常的免疫系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Autologous_hematopoietic_stem_cell_transplantation">Autologous hematopoietic stem cell transplantation</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7091487/">Autologous hematopoietic stem cell transplantation in autoimmune ...</a></li>
<li><a href="https://starmedicstemcell.com/nmosd-neuromyelitis-optica/">NMOSD ( Neuromyelitis optica ) disease - symptoms, causes...</a></li>

</ul>
</details>

**标签**: `#stem cells`, `#autoimmune disease`, `#medical breakthrough`, `#long-term treatment`, `#biotech`

---

<a id="item-5"></a>
## [基因组的物理复杂性挑战了 AI 在生物学中的建模能力。](https://www.quantamagazine.org/why-the-human-genomes-tangled-physicality-may-confound-ai-20260618/) ⭐️ 8.0/10

一篇新文章指出，人类基因组纠缠的物理相互作用和三维结构使其从根本上无法被人工智能建模为简单的蓝图或算法，这挑战了计算生物学中常用的隐喻。 这一观点很重要，因为它突出了计算模型与生物学物理现实之间的巨大差距，表明当前的 AI 方法可能不足以真正理解像基因调控这样复杂的生物系统。 文章强调，基因组的非线性相互作用——例如通过 Hi-C 等染色体构象捕获技术所揭示的——创造了一种动态且依赖于背景的物理景观，算法难以捕捉，这超越了静态的“生命之书”类比。

rss · Quanta Magazine · Jun 18, 14:12

**背景**: 人类基因组常被描述为“蓝图”或“代码”，但这过度简化了其现实。其功能与它在细胞核内的三维空间组织密切相关，这涉及到复杂的折叠以及远距离 DNA 片段之间的相互作用。Hi-C 等技术绘制了这些染色体构象图谱，揭示了物理邻近性如何影响基因表达。表观遗传调控，如对 DNA 和组蛋白的化学修饰，通过在不改变底层 DNA 序列的情况下改变基因活性，进一步增加了复杂性的层次。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41576-018-0060-8">Organizational principles of 3D genome architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hi-C_(genomic_analysis_technique)">Hi-C (genomic analysis technique) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Epigenetic_regulation">Epigenetic regulation</a></li>

</ul>
</details>

**标签**: `#AI limitations`, `#genomics`, `#computational biology`, `#systems biology`, `#science communication`

---

<a id="item-6"></a>
## [ATProto 澄清其架构中没有像 Mastodon 那样的‘实例’](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 7.0/10

一篇文章解释，Bluesky 所使用的 AT 协议并不像 Mastodon/ActivityPub 那样使用‘实例’的概念，澄清了其架构由独立的中继器、应用视图和个人数据服务器（PDS）组成。 这一澄清解决了去中心化社交网络社区中一个普遍的误解，并帮助开发者和用户更好地理解 ATProto 与基于 ActivityPub 的系统之间的根本架构差异。 在 ATProto 中，个人数据服务器（PDS）托管用户数据，中继器将来自众多 PDS 的数据聚合到一个‘信息流’中，而应用视图则消费该信息流以提供特定应用的功能，每个组件都可以独立扩展。

hackernews · danabramov · Jun 19, 15:10 · [社区讨论](https://news.ycombinator.com/item?id=48599515)

**背景**: AT 协议（ATProto）是社交网络 Bluesky 的底层协议，被开发为一个去中心化的替代方案。ActivityPub 是支持 Mastodon 和‘Fediverse’（联邦宇宙）的协议，它基于相互连接的、通常被称为‘实例’的独立运营服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.com/guides/overview">Protocol Overview - AT Protocol</a></li>
<li><a href="https://atproto.wiki/wiki/Relay">Relay - ATProto Wiki</a></li>

</ul>
</details>

**社区讨论**: 社区讨论围绕文章的类比展开争论；一些评论者认为与 RSS 的比较存在缺陷，因为应用视图严重依赖中继器，而另一些人则称赞这种架构分离是一个优美的系统设计解决方案。一个关键的批评是，文章在驳斥‘隔离联合’概念时，并未解释 ATProto 如何解决实例所能解决的审核和社区发现问题。

**标签**: `#ATProto`, `#decentralized-protocols`, `#Bluesky`, `#ActivityPub`, `#distributed-systems`

---

<a id="item-7"></a>
## [挪威禁止小学生使用 AI 工具](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/) ⭐️ 7.0/10

挪威政府实施了一项近乎全面的禁令，禁止 6 至 13 岁的小学生使用人工智能工具，同时允许 14 至 16 岁的初中生在教师监督下谨慎使用。 这一政策决定意义重大，因为它回应了关于在教育中引入人工智能的合适年龄的日益增长的争论，为儿童发展和技术伦理树立了先例，优先保障年幼儿童的基础读写能力。 该禁令广泛适用于生成式 AI 工具，旨在防止儿童跳过阅读和写作等基本学习过程，尽管如评论指出，这可能给教育工作者带来执行挑战，例如增加工作负担。

hackernews · ilreb · Jun 19, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48600093)

**背景**: 生成式 AI（如大型语言模型）能够生成类人文本和图像，在教育领域引发了担忧，即学生可能依赖它来规避批判性思维和基础技能的培养。挪威的决定反映了全球范围内关于学校 AI 监管的更广泛讨论，类似于历史上关于数学教育中计算器使用的争论。

**社区讨论**: 社区评论大多支持该禁令，用户将其比作在孩子掌握算术之前不给他们计算器，并指出生成式 AI 更隐蔽，因为它能生成看似完整的作品，从而掩盖学习差距。然而，一些人对实施方式表示困惑，并担忧 AI 已在教育中制造了一个“回音室”，教师和学生都在使用 AI，这可能会削弱学习成果。

**标签**: `#AI regulation`, `#education policy`, `#child development`, `#technology ethics`, `#Hacker News`

---

<a id="item-8"></a>
## [现代汽车从软银手中完成对波士顿动力公司的全资收购](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/) ⭐️ 7.0/10

现代汽车集团以 3.25 亿美元收购了软银集团持有的波士顿动力公司剩余 9%的股份，以总计 11 亿美元的估值完成了对该机器人公司的收购。 此次收购使现代汽车完全控制了一家世界领先的机器人公司，可能加速其自动化和移动出行战略，以应对劳动力挑战和未来产品开发。 这笔交易源于软银行使其持有的看跌期权，此前现代汽车已于 2020 年 12 月以 8.8 亿美元收购了该公司 80%的控股权。

hackernews · ck2 · Jun 19, 16:28 · [社区讨论](https://news.ycombinator.com/item?id=48600312)

**背景**: 波士顿动力是一家开创性公司，以开发高度移动和动态的机器人而闻名，如 Spot 和 Atlas，在先进的运动和操作技术方面拥有专业知识。软银集团于 2017 年从 Alphabet 手中收购了波士顿动力，此后在机器人和人工智能领域进行了多项投资，包括最近达成的收购 ABB 机器人业务的协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bostondynamics.com/">The World’s Leading Robotics Company | Boston Dynamics</a></li>
<li><a href="https://en.wikipedia.org/wiki/SoftBank_Group">SoftBank Group - Wikipedia</a></li>
<li><a href="https://fortune.com/2026/02/12/softbank-earnings-profits-ai-boom-nvidia-openai/">'Our investments are beginning to pay off': AI boom brings SoftBank back into the black | Fortune</a></li>

</ul>
</details>

**社区讨论**: 讨论表达了对现代汽车战略的好奇，一些人质疑人形机器人在制造业中的商业可行性，并认为此次收购可能更多是受到韩国人口结构变化（而非单纯的汽车自动化）的驱动。其他人则指出，该交易是完成初始收购的合乎逻辑的步骤。

**标签**: `#robotics`, `#acquisitions`, `#manufacturing automation`, `#industry news`

---

<a id="item-9"></a>
## [对所有互联网流量实施真实身份验证的提议引发隐私与控制担忧](https://nochan.net/b/Internet-Crap/20230829-Think-Of-The-Children/) ⭐️ 7.0/10

一篇文章探讨了对所有互联网流量实施真实身份（Real ID）要求的提议及其影响，并将其与历史上的数字控制机制相提并论，引发了社区内的广泛讨论。 这一议题至关重要，因为强制性的互联网真实身份验证可能从根本上重塑网络隐私、言论自由和互联网架构，可能导致普遍的监控和自我审查。 讨论中包含了推测性的防御措施，例如建立地下无线电中继网络来规避控制，并将提议与现有的监管实践（如 KYC/AML）进行了比较，后者已导致平台采取规避风险的自我审查行为。

hackernews · Bender · Jun 19, 20:19 · [社区讨论](https://news.ycombinator.com/item?id=48602817)

**背景**: “Real ID”概念最初是指美国联邦为增强安全性而制定的驾驶执照和身份证明卡标准。将这一原则应用于互联网流量意味着将所有在线活动与经核实的政府颁发身份相关联。此类数字身份系统的提议通常以保护儿童或国家安全为理由，但批评者警告说，它们可能促成大规模监控，并破坏在线匿名性——这被视为言论自由和隐私的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_identity">Digital identity - Wikipedia</a></li>
<li><a href="https://resources.fenergo.com/blogs/digital-identity-verification">Digital Identity Verification for KYC & AML Compliance</a></li>
<li><a href="https://www.federalregister.gov/documents/2025/01/14/2025-00484/minimum-standards-for-drivers-licenses-and-identification-cards-acceptable-by-federal-agencies-for">Minimum Standards for Driver's Licenses and Identification Cards Acceptable by Federal Agencies for Official Purposes; Phased Approach for Card-Based Enforcement</a></li>

</ul>
</details>

**社区讨论**: 社区评论对这种控制表达了强烈的怀疑和抵制，有人提出建立去中心化的地下通信网络（如无线电网络）作为“最后的防御”。其他评论指出，现有的 KYC/AML 等监管和内容审核实践已经导致网络上普遍的自我审查和规避风险的行为，将责任从监管机构转移。

**标签**: `#internet freedom`, `#privacy`, `#digital regulation`, `#identity verification`, `#online censorship`

---

<a id="item-10"></a>
## [Datasette Apps：新插件在沙盒化 iframe 中托管自定义 HTML 应用](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 7.0/10

datasette-apps 插件正式发布，允许用户在 Datasette 实例内部一个严格受限的 iframe 沙盒中托管自包含的 HTML 和 JavaScript 应用，从而通过只读或可配置的写 SQL 查询实现交互式数据探索。 这为 Datasette 生态系统增添了一个强大的可扩展性机制，使开发者能够构建安全运行在核心平台旁边的自定义交互式数据驱动工具和用户界面，可能改变数据探索和操作的方式。 这些应用运行在设置了特定属性的 iframe 沙盒中，无法访问 cookies 或 localStorage，并且注入的 Content Security Policy 头阻止了外部 HTTP 请求，从而降低了恶意或错误应用泄露数据的风险。

rss · Simon Willison · Jun 18, 23:58

**背景**: Datasette 是一个基于 SQLite 构建的、用于探索和发布数据的开源工具，其灵活的 JSON API 长期以来支持自定义前端开发。Iframe 沙盒化是一种网页安全功能，它限制嵌入内容的能力，以防止其干扰宿主页面或访问敏感资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/plugins">Datasette Plugins</a></li>
<li><a href="https://www.mbloging.com/course/html/iframe-sandboxing-html">Iframe Sandboxing in HTML for Safer Embedded Content</a></li>
<li><a href="https://javascript.plainenglish.io/demystifying-sql-query-execution-what-happens-behind-the-scenes-18111558227a">Understanding How SQL Queries Execute in a Database | JavaScript ...</a></li>

</ul>
</details>

**标签**: `#datasette`, `#data-tools`, `#plugin`, `#data-exploration`, `#javascript`

---

<a id="item-11"></a>
## [Systemd v261 发布，新增云实例元数据、启动密钥及内核热更新支持](https://lwn.net/Articles/1078708/) ⭐️ 7.0/10

Systemd v261 版本发布，主要新特性包括：新增了云实例元数据服务（IMDS）子系统；为缺乏物理 TPM 的系统引入了“启动密钥”功能；并支持内核的实时更新编排（LUO）/ Kexec 移交（KHO）系统。 这些特性极大地增强了 systemd 在云基础设施、更广泛硬件上的安全性以及支持更无缝、低停机时间的内核更新方面的能力，对系统管理员和云工程师影响深远。 IMDS 子系统（systemd-imdsd）为云实例访问元数据提供了标准化接口；启动密钥为引导时密钥提供了基于软件的 TPM 替代方案；而 LUO/KHO 支持则利用基于 kexec 的重启框架来实现内核的实时更新。

rss · LWN.net · Jun 19, 18:56

**背景**: Systemd 是大多数主流 Linux 发行版使用的初始化系统和服务管理器，负责核心系统初始化和服务。实例元数据服务（IMDS）是一项常见的云功能，允许实例从云平台检索配置和身份数据。TPM（可信平台模块）是用于安全存储加密密钥和测量值的硬件芯片，而启动密钥是在引导过程早期所需的敏感数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/systemd-261-rc1">systemd 261-rc1 Released With OS Installer, IMDS Subsystem & New storagectl - Phoronix</a></li>
<li><a href="https://docs.kernel.org/next/core-api/liveupdate.html">Live Update Orchestrator — The Linux Kernel documentation</a></li>
<li><a href="https://lwn.net/Articles/1033364/">Kexec handover and the live update orchestrator [LWN.net]</a></li>

</ul>
</details>

**标签**: `#systemd`, `#linux`, `#system-administration`, `#cloud-infrastructure`, `#kernel`

---

<a id="item-12"></a>
## [BPF 程序可能支持协程以实现挂起与恢复](https://lwn.net/Articles/1076210/) ⭐️ 7.0/10

开发者 Kumar Kartikeya Dwivedi 正在研究允许 BPF 程序以协程形式表达，使其能够挂起和恢复执行，这项工作已在 2026 年 Linux 存储、文件系统、内存管理与 BPF 峰会上进行了展示。 这一变化可能通过消除当前要求程序必须在原始执行上下文中连续完成而不能阻塞的限制，极大地简化在 Linux 内核中编写长时间运行的 BPF 任务。 该工作仍处于实验阶段，尚未最终确定，但它代表了当前 BPF 执行模型的根本性转变，当前模型要求程序必须在启动的同一 CPU 上连续运行完成。

rss · LWN.net · Jun 19, 15:55

**背景**: BPF（伯克利数据包过滤器）是 Linux 内核中的一种技术，允许用户在内核空间运行沙盒程序，而无需更改内核源代码或加载内核模块。当前的 BPF 程序经过验证，确保其始终连续完成运行，不能阻塞或无限循环，这限制了它们用于可能需要等待资源或事件的任务。协程是一种编程概念，其中执行可以被挂起并稍后恢复，允许函数在保持其状态的同时暂时让出控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://noise.getoto.net/2026/06/19/suspending-and-resuming-bpf-programs/">[$] Suspending and resuming BPF programs | Noise</a></li>
<li><a href="https://ebpf.io/what-is-ebpf/">What is eBPF? An Introduction and Deep Dive into the eBPF Technology</a></li>
<li><a href="https://lwn.net/Articles/812503/">bpf: Make BPF and PREEMPT_RT co-exist - LWN.net</a></li>

</ul>
</details>

**标签**: `#BPF`, `#Linux kernel`, `#coroutines`, `#systems programming`, `#kernel development`

---

<a id="item-13"></a>
## [Arch Linux AUR 遭受持续供应链攻击，攻击者利用孤儿包投毒](https://lwn.net/Articles/1077619/) ⭐️ 7.0/10

Arch 用户软件包仓库(AUR)遭到恶意行为者攻击，他们创建新账户来接管被遗弃的软件包并推送包含恶意软件的更新，迫使维护者进行长时间的应对工作，并导致新用户注册功能被暂时关闭。 此事件凸显了依赖志愿者维护者的社区驱动型开放代码库所固有的安全风险，它表明攻击者可以利用信任和流程漏洞大规模分发恶意软件，可能影响一个主要 Linux 发行版的众多用户。 攻击持续了数天，维护者就像玩'打地鼠'游戏一样应对每个新发现的恶意包，目前尚不清楚有多少用户受到影响，以及 AUR 的合作模式在长期内会采取何种安全响应措施。

rss · LWN.net · Jun 19, 14:40

**背景**: Arch 用户软件包仓库(AUR)是 Arch Linux 的社区驱动仓库，包含软件包构建描述文件(PKGBUILDs)，允许用户编译和安装不在官方仓库中的软件。孤儿包是指没有活跃维护者的软件包，可以被其他人接管，这一过程在此次攻击中被利用。供应链攻击针对软件开发和分发流程，而开源仓库因其开放性正日益成为攻击目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki.archlinux.org/title/Arch_User_Repository">Arch User Repository - ArchWiki</a></li>
<li><a href="https://linuxbash.sh/post/handling-orphaned-packages-across-distros">Handling Orphaned Packages Across Distros - Linux Bash</a></li>
<li><a href="https://theaivibe.org/blog/supply-chain-attacks-open-source-threat">Supply Chain Attacks in Open Source : The Growing... | The AI Vibe</a></li>

</ul>
</details>

**标签**: `#supply-chain-security`, `#linux`, `#open-source`, `#security-attack`, `#package-management`

---

<a id="item-14"></a>
## [Linux 内核 7.2 合并窗口过半，已集成超过 7000 个变更集](https://lwn.net/Articles/1078068/) ⭐️ 7.0/10

Linux 内核 7.2 的合并窗口自 6 月 14 日内核 7.1 发布后启动，目前已有超过 7000 个非合并变更集被集成到主线代码库中。 这一进展表明，即将发布的 7.2 版本的大多数主要子系统变更已经提交，这为社区提供了一个更清晰的预期，了解将有哪些新功能和改进。 该更新指出，尽管许多核心子系统已被合并，但合并窗口仅过去一半，这意味着在窗口关闭前预计还会有更多重要的变更集。

rss · LWN.net · Jun 18, 13:47

**背景**: Linux 内核的合并窗口是主要内核发布后的一个时期，通常持续两周，期间 Linus Torvalds 会接受来自子系统维护者的新功能和更改。变更集是版本控制中的一个基本变更单位，代表对代码库的一次逻辑性修改。内核开发周期在用于新功能的合并窗口和用于修复错误的稳定期之间交替进行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Changeset">Changeset - Wikipedia</a></li>
<li><a href="https://lwn.net/Articles/811086/">The 5.6 merge window opens [LWN.net]</a></li>

</ul>
</details>

**标签**: `#linux-kernel`, `#operating-systems`, `#software-development`, `#open-source`

---

<a id="item-15"></a>
## [为高效云块设备复制提出的基于 RDMA 的新内核模块](https://lwn.net/Articles/1074291/) ⭐️ 7.0/10

提出了两个新的 Linux 内核模块——可靠多播 RTRS（RMR）和块设备 RMR（BRMR），旨在为云环境提供高效、低开销的持久性块设备复制。开发者正在提交上游前寻求社区反馈。 该方案能显著降低云提供商提供高可用和持久虚拟块存储的开销，这对现代云基础设施至关重要。它代表了将 RDMA 用于块设备复制的一种新颖的内核级集成方式。 这些模块建立在现有的 RDMA 传输弹性服务器（RTRS）内核库之上，旨在实现单跳、主动-主动复制。该提案目前处于早期阶段，作者已在 Linux 存储、文件系统、内存管理和 BPF 峰会（LSFMMBPF）上进行了介绍，以收集意见。

rss · LWN.net · Jun 18, 13:25

**背景**: 远程直接内存访问（RDMA）允许服务器通过网络直接访问彼此的内存，CPU 参与度极低，从而实现高性能、低延迟的通信。RTRS（RDMA 传输弹性服务器）是一个 Linux 内核模块，用于在 RDMA 上提供可靠的消息传输。云提供商需要持久的虚拟块设备来为其客户提供持久存储服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lkml.iu.edu/2605.0/04603.html">[PATCH 01/13] RDMA/rmr: add public and ... - Linux-Kernel Archive</a></li>
<li><a href="https://www.reddit.com/r/linux/comments/1szzkfx/a_new_indevelopment_blocklevel_activeactive/">A new (in-development) block-level active-active replication solution for Linux kernel : r/linux</a></li>
<li><a href="https://lkml.iu.edu/2605.0/04605.html">[PATCH 03/13] RDMA/rmr: client: main ... - Linux-Kernel Archive</a></li>

</ul>
</details>

**社区讨论**: 根据现有的网络搜索结果，Reddit 上的一个讨论帖表明社区对该项目感兴趣，将其视为 Linux 内核的一个新的块级主动-主动复制解决方案。然而，在提供的片段中，详细的技术讨论或批评尚不突出。

**标签**: `#cloud infrastructure`, `#storage systems`, `#RDMA`, `#Linux kernel`, `#block devices`

---

<a id="item-16"></a>
## [美国政府将 Anthropic 的 Fable AI 模型列为危险军需品](https://www.schneier.com/blog/archives/2026/06/anthropics-fable-and-the-state-of-ai.html) ⭐️ 7.0/10

2026 年 6 月 12 日，美国政府将 Anthropic 新发布的 Fable 生成式 AI 模型列为危险军需品，并援引出口管制权力禁止外国公民访问，这导致 Anthropic 关闭了所有用户对该模型的访问权限。 这一事件凸显了 AI 能力快速进步与政府限制性管控之间日益加剧的紧张关系，并引发了一个根本性问题：是禁止特定模型，还是应对 AI 进步这一更广泛且不可阻挡的趋势，哪个才是更有效的策略？ Fable 模型是 Anthropic 更强大的 Mythos 模型的约束版本，专为复杂推理和高自主性任务设计。安全专家 Bruce Schneier 认为，针对 Fable 等单个模型的行动是徒劳的，因为真正的挑战在于管理 AI 能力不断增强的总体趋势，而这需要当前难以实现的国际集体行动。

rss · Schneier on Security · Jun 19, 11:03

**背景**: 出口管制是政府用于限制特定技术（如军需品或先进芯片）向外国实体转让的法律工具，其目的是维护国家安全。将先进的 AI 模型归类为军需品，意味着将其与武器置于同一监管类别，这是对软件政策处理方式的重大升级。此前，美国已对 AI 芯片实施过类似管制，以限制中国获取高性能计算硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/06/anthropics-fable-and-the-state-of-ai.html">Anthropic's Fable and the State of AI - Schneier on Security -</a></li>
<li><a href="https://www.thewirechina.com/2025/02/05/deepseeks-lesson-america-needs-smarter-export-controls/">DeepSeek's Lesson: America Needs Smarter Export Controls</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#export controls`, `#regulation`, `#Anthropic`, `#national security`

---

<a id="item-17"></a>
## [肯特·贝克认为公司雇佣初级工程师是为了培养判断力，而非仅仅完成任务](https://newsletter.kentbeck.com/p/hey-n00b-we-didnt-hire-you-to-complete) ⭐️ 6.0/10

肯特·贝克的一篇通讯文章提出，雇佣初级工程师的主要目的是培养其长期的工程判断力和决策能力，而非期望他们立即完成复杂任务。 这一观点挑战了行业普遍看法，即初级开发者主要是执行简单任务的廉价劳动力，可能重塑科技公司在指导、招聘和职业发展方面的结构。 文章引入了一个框架，根据初级工程师的学习影响将其分为 A、B、C 三类，其中‘B’级工程师是那些学习时不给他人造成不合理工作量的人，一些社区成员认为这一标准过于简单化或严苛。

hackernews · rrvsh · Jun 20, 00:11 · [社区讨论](https://news.ycombinator.com/item?id=48604851)

**背景**: 肯特·贝克是一位著名的软件工程师，以开创极限编程和测试驱动开发而闻名。围绕初级开发者角色的争论在软件行业中持续存在，涉及指导投入、职业发展以及雇佣经验较少员工的经济理由等问题。

**社区讨论**: 社区反应不一，一些人同意培养判断力是一项有效的长期投资，但许多人不同意，认为公司雇佣初级员工主要是出于成本限制来完成特定的低级别任务。批评者还指出，文章的语气可能显得居高临下，且其分类系统对现实世界动态来说过于简单。

**标签**: `#software engineering`, `#career development`, `#mentorship`, `#junior developers`, `#opinion`

---

<a id="item-18"></a>
## [MCP 的核心价值被视为 AI 代理的认证网关](https://simonwillison.net/2026/Jun/19/sean-lynch/#atom-everything) ⭐️ 6.0/10

Hacker News 用户 Sean Lynch 的一条评论指出，模型上下文协议 (MCP) 的主要优势在于能够将认证流程与 AI 代理的上下文窗口隔离开来，这可能使 MCP 成为 API 的专用认证网关。 这一观点强调了一个关键的安全设计优势：通过将敏感的认证数据与代理的操作上下文分离，MCP 可以显著降低凭证泄露和滥用的风险，这是企业部署 AI 代理时的主要担忧。 该论点特别将 MCP 与“技能”或命令行接口等其他集成方法进行对比，暗示 MCP 的结构化方法为处理认证令牌和凭证提供了更安全的边界。

rss · Simon Willison · Jun 19, 22:45

**背景**: 模型上下文协议 (MCP) 是一个开放的、基于 JSON-RPC 的标准，旨在规范化 AI 应用程序（如大型语言模型）访问外部工具、数据和资源的方式。将 AI 代理与外部 API 集成时的一个关键挑战是安全地管理认证和授权，避免敏感令牌暴露在代理的对话上下文中，因为该上下文可能被记录或以可能导致泄露的方式处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/specification/2025-11-25">Specification - Model Context Protocol</a></li>
<li><a href="https://www.skyflow.com/post/understanding-llm-agents">Understanding AI & LLM Agents: Architecture, Security, & Deployment - Skyflow</a></li>

</ul>
</details>

**标签**: `#model-context-protocol`, `#LLMs`, `#AI`, `#authentication`, `#API-design`

---

<a id="item-19"></a>
## [Midjourney 跨界医疗影像，推出嵌入传感器的浴缸式扫描仪](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247898354&idx=2&sn=f842f4fd953b066992ed4f5808c6c8d0) ⭐️ 6.0/10

AI 图像生成公司 Midjourney 宣布跨界进入医疗健康领域，推出了一款基于超声波技术的全身扫描仪，该设备使用约 50 万个传感器，可在 60 秒内生成 3D 人体地图。 此举标志着一家领先的 AI 公司从创意工具向实用健康技术的重大转型，有望让先进的体成分分析在水疗中心或家庭等日常场景中变得更普及和常规化。 该扫描仪被描述为无辐射、无磁性风险，利用超声波回声定位技术，传感器从各个角度向身体发送声波，并且需要超过两千万亿次浮点运算的处理能力来分析数据。

rss · 量子位 · Jun 18, 11:20

**背景**: Midjourney 广为人知的是一个根据文本提示生成图像的 AI 平台。传统的 3D 身体扫描技术通常使用红外深度感知或结构光等方法，应用于健身、健康和医疗保健领域进行体成分分析。将此类扫描技术整合到消费友好的浴缸形态中，代表了一种健康监测的新颖方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/news/29010">From Generated Images to Medical Imaging: Midjourney Launches...</a></li>
<li><a href="https://www.businesstoday.in/technology/artificial-intelligence/story/step-into-a-spa-walk-out-with-a-1-min-body-scan-midjourney-thinks-its-possible-but-will-regulators-agree-537975-2026-06-19">Step into a spa, walk out with a 1 min body scan? Midjourney thinks...</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/952011/midjourney-medical-ai-ultrasound-scan">Midjourney Medical goes from AI image generation to... | The Verge</a></li>

</ul>
</details>

**标签**: `#AI`, `#3D_scanning`, `#health_tech`, `#Midjourney`, `#sensor_technology`

---

<a id="item-20"></a>
## [软件自由保护协会发布针对开源贡献使用大语言模型生成式 AI 的建议。](https://lwn.net/Articles/1078521/) ⭐️ 6.0/10

软件自由保护协会（SFC）与社区志愿者合作，发布了一套社区制定的最佳实践建议，用于在向自由和开源软件（FOSS）贡献时使用基于大语言模型的生成式 AI 系统。 这些建议解决了使用专有 AI 工具与自由软件原则之间日益加剧的紧张关系，旨在帮助开发者应对伦理和实践挑战，以最小化对自由开源软件生态系统的潜在损害。 这些建议被作为自愿性的最佳实践而非正式要求提出，旨在为那些可能自愿或因雇主强制要求而使用大语言模型的贡献者提供实用指导。

rss · LWN.net · Jun 18, 16:00

**背景**: 软件自由保护协会（SFC）是一家美国非营利组织，为自由开源软件项目提供基础设施和法律支持，并倡导用户维修、改进和重新安装软件的权利。能够生成代码的大语言模型（LLM）的出现给开源社区带来了新的困境，因为使用这些系统进行的贡献可能引发关于许可、代码质量以及社区驱动开发被侵蚀的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sfconservancy.org/llm-gen-ai/llm-backed-generative-ai-recommendations.html">LLM -gen- AI - Software Freedom Conservancy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Software_Freedom_Conservancy">Software Freedom Conservancy - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#open source`, `#LLM`, `#software development`, `#policy`

---

<a id="item-21"></a>
## [Mastodon 4.6 推出策展集合功能及新的用户工具](https://lwn.net/Articles/1078466/) ⭐️ 6.0/10

Mastodon 4.6 推出了「Collections」功能，允许用户创建和分享策划好的账户列表，以帮助新用户发现值得关注的账户，同时还增加了帖子邮件订阅和「年度回顾」生成器等新功能。 此次更新增强了去中心化联邦宇宙生态系统中的用户引导和内容发现能力，解决了这类平台在没有集中式推荐算法时面临的关键挑战。 Collections 功能的设计重点在于信任与安全，用户必须同意才能被添加到列表中，以防止滥用，并且这些集合会在兼容的平台之间进行联邦同步。

rss · LWN.net · Jun 18, 13:28

**背景**: Mastodon 是一个领先的开源、去中心化社交媒体平台，属于联邦宇宙的一部分。联邦宇宙是一个使用如 ActivityPub 等通用协议互联的服务器网络。由于其分布式特性，档案发现一直是联邦宇宙中的一项长期挑战，因此策划列表这类功能对于帮助用户找到志同道合者非常有价值。这个功能在概念上类似于竞争对手 Bluesky 平台的「Starter Packs」。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.neowin.net/news/mastodon-is-getting-its-own-version-of-blueskys-starter-packs-called-collections/">Mastodon is getting its own version of Bluesky's Starter... - Neowin</a></li>
<li><a href="https://docs.joinmastodon.org/client/collections/">Implementing Collections - Mastodon documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fediverse">Fediverse - Wikipedia</a></li>

</ul>
</details>

**标签**: `#fediverse`, `#social-media`, `#open-source`, `#release-notes`, `#privacy`

---

<a id="item-22"></a>
## [历史计算机被基准测试：看谁数到一百万最快](https://hackaday.com/2026/06/19/making-old-computers-count-to-a-million/) ⭐️ 6.0/10

英国国家计算博物馆对经典计算机进行了基准测试，包括二战时期的“巨人”计算机和 1980 年代的 BBC Micro，以测量它们数到一百万的速度。 这个实验提供了一种具体而有趣的方式，来比较具有历史意义但截然不同的机器的原始处理能力，凸显了计算从专用密码破译硬件到通用个人计算机的演变。 “巨人”计算机建于 1943-1944 年，并非存储程序计算机，而是一台用于密码破译的专用机器；而 BBC Micro 于 1981 年推出，是基于 6502 处理器的通用微型计算机，其后续型号催生了影响深远的 ARM 架构。

rss · Hackaday · Jun 20, 05:00

**背景**: “巨人”计算机是二战期间英国密码破译人员开发的一系列机器，用于帮助破译德国最高指挥部的加密信息，是最早的电子数字计算机之一。BBC Micro 是 1980 年代英国流行的家庭和教育用计算机，因其在学校的广泛使用和允许处理器升级的模块化“Tube”接口而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_computer">Colossus computer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/BBC_Micro">BBC Micro - Wikipedia</a></li>

</ul>
</details>

**标签**: `#retrocomputing`, `#benchmarking`, `#computing-history`, `#hardware`

---

<a id="item-23"></a>
## [初步数据显示肥胖药物可能对男性生育能力有益。](https://www.nature.com/articles/d41586-026-01963-1) ⭐️ 6.0/10

《自然》新闻简报讨论了一项初步研究，表明常用于治疗肥胖和糖尿病的 GLP-1 受体激动剂药物可能会提高男性的睾酮水平并改善精子参数。 这一发现很重要，因为它暗示了广泛处方的药物可能被重新用于治疗男性不育症——这种常见疾病常与肥胖相关，从而可能提供一条新的治疗途径。 该数据被描述为初步结果，该简报还提到了一项为期两年的脑机接口（BCI）临床试验，突显了当前生物医学研究的广度。

rss · Nature · Jun 19, 00:00

**背景**: GLP-1 受体激动剂是一类模拟天然激素 GLP-1 作用的药物；它们主要通过刺激胰岛素生成、抑制胰高血糖素释放和增强饱腹感来发挥作用，从而减少食物摄入并导致体重减轻。男性不育症常与肥胖和代谢综合征相关，因此有效治疗肥胖的药物可能对生殖健康产生下游影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLP-1_receptor_agonist">GLP-1 receptor agonist - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Brain–computer_interface">Brain–computer interface - Wikipedia</a></li>

</ul>
</details>

**标签**: `#biotechnology`, `#medical_research`, `#obesity_drugs`, `#brain_computer_interface`, `#fertility`

---