---
layout: default
title: "Horizon Summary: 2026-06-19 (ZH)"
date: 2026-06-19
lang: zh
---

> From 67 items, 25 important content pieces were selected

---

1. [研究人员发现一万个 GitHub 仓库传播特洛伊木马恶意软件](#item-1) ⭐️ 9.0/10
2. [中国实验室 Z.ai 发布 7530 亿参数开源权重大模型 GLM-5.2，采用 MIT 许可证。](#item-2) ⭐️ 9.0/10
3. [为模型上下文协议认证提出零接触 OAuth 方案](#item-3) ⭐️ 8.0/10
4. [挪威零售商 Elkjop 因违反 GDPR 强制同意规定被罚 180 万欧元。](#item-4) ⭐️ 8.0/10
5. [Datasette Apps 插件支持在 Datasette 中安全托管自定义 HTML 应用](#item-5) ⭐️ 8.0/10
6. [研究人员将大规模“Popa”僵尸网络与以色列上市公司关联](#item-6) ⭐️ 8.0/10
7. [美国政府公布 3611 个人工智能用例，应用迅速扩张](#item-7) ⭐️ 8.0/10
8. [干细胞疗法使严重自身免疫病缓解长达 15 年](#item-8) ⭐️ 8.0/10
9. [胚胎“组织者”细胞可跨动物门指导身体构型形成](#item-9) ⭐️ 8.0/10
10. [Ubiquiti 推出基于 ZFS 的企业级 NAS 设备](#item-10) ⭐️ 7.0/10
11. [康奈尔大学高级编译器课程现已作为免费自学在线资源开放](#item-11) ⭐️ 7.0/10
12. [医院与大学通过药物再利用将成本削减高达 90%。](#item-12) ⭐️ 7.0/10
13. [Charity Majors：AI 颠倒了代码的经济逻辑](#item-13) ⭐️ 7.0/10
14. [软件自由保护协会发布针对自由开源软件贡献的 LLM 生成式 AI 使用指南](#item-14) ⭐️ 7.0/10
15. [Linux 7.2 合并窗口过半，已合并超过 7000 个变更集](#item-15) ⭐️ 7.0/10
16. [RMR 和 BRMR 提议通过 RDMA 实现高效的 Linux 块复制](#item-16) ⭐️ 7.0/10
17. [恶意软件嵌入违禁文本以欺骗人工智能安全扫描器](#item-17) ⭐️ 7.0/10
18. [可解聚树脂实现 3D 打印光敏聚合物的轻松重复利用](#item-18) ⭐️ 7.0/10
19. [研究发现，使用 AI 工具正在侵蚀关键行业的专业技能。](#item-19) ⭐️ 7.0/10
20. [人类基因组的三维结构对 AI 建模构成挑战](#item-20) ⭐️ 7.0/10
21. [Show HN: Are You in the Weights?](#item-21) ⭐️ 6.0/10
22. [WAI-ARIA 1.3 引入 ariaNotify() 方法以实现程序化屏幕阅读器通知](#item-22) ⭐️ 6.0/10
23. [Windows NT 成功移植到 Nintendo GameCube 硬件上运行](#item-23) ⭐️ 6.0/10
24. [Brexit tore apart European science — now the research rifts are healing](#item-24) ⭐️ 6.0/10
25. [新证明揭示需要多少次随意洗牌才能真正打乱一副牌](#item-25) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [研究人员发现一万个 GitHub 仓库传播特洛伊木马恶意软件](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

一个协调的攻击活动被发现，该活动利用超过一万个 GitHub 仓库，通过利用软件代理和供应链信任来传播特洛伊木马恶意软件。 这揭示了一场大规模、复杂的供应链攻击，专门针对自动化软件代理，可能在关键的选举年大规模破坏开发者工具和构建管道。 攻击者主要克隆新仓库而非流行仓库，并频繁删除和重新推送提交以出现在“最近更新”的搜索结果中，这种策略旨在欺骗自动化的依赖管理代理，而非人类开发者。

hackernews · theorchid · Jun 18, 11:45 · [社区讨论](https://news.ycombinator.com/item?id=48583928)

**背景**: 软件供应链攻击涉及破坏软件开发和分发的完整性，通常是通过毒害开发者隐式信任的代码仓库或包管理器来实现。在此背景下，软件代理指的是自动化工具或机器人，它们通过管理依赖项、搜索代码或处理其他任务来辅助开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/orchidfiles/i-discovered-a-large-scale-malware-distribution-campaign-on-github-4m6o">I discovered a large-scale malware distribution campaign on GitHub</a></li>
<li><a href="https://www.darktrace.com/blog/when-trust-becomes-the-attack-surface-supply-chain-attacks-in-an-era-of-automation-and-implicit-trust">Supply-Chain Attacks in an Era of Automation and Implicit Trust</a></li>
<li><a href="https://www.terrabytegroup.com/the-hidden-danger-of-impersonation-and-trust-exploitation-in-supply-chain-attacks/">The Hidden Danger of Impersonation and Trust Exploitation in Supply ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论指出，该活动专注于频繁更新新的、不太知名的仓库，是一种刻意针对搜索依赖项的自动化软件代理的策略。一些评论者提到自己的合法项目被克隆或冒充的个人经历，并且有人猜测该活动的时机与即将到来的重大选举有关，暗示可能存在更广泛的协调努力。

**标签**: `#supply-chain-security`, `#malware`, `#github`, `#cybersecurity`, `#software-agents`

---

<a id="item-2"></a>
## [中国实验室 Z.ai 发布 7530 亿参数开源权重大模型 GLM-5.2，采用 MIT 许可证。](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

中国人工智能实验室 Z.ai 发布了 GLM-5.2，这是一个拥有 7530 亿参数、仅处理文本的开源权重大语言模型，具有 100 万令牌的上下文窗口，并采用 MIT 许可证。早期基准测试表明，它可能是目前最强大的开源权重模型。 此次发布代表了开源人工智能领域的重大进步，提供了一个性能卓越且采用宽松许可证的模型，鼓励商业应用和研究。它加剧了领先开源权重模型之间的竞争，可能加速人工智能生态系统的创新和可及性。 尽管拥有 7530 亿的总参数，GLM-5.2 采用了混合专家（MoE）架构，每个令牌仅激活 40 个参数，且基准测试指出它比前代模型更消耗令牌。在 Code Arena 排行榜上，它在 Web 开发任务中也排名靠前，这对于一个纯文本模型来说是一个令人惊讶的结果。

rss · Simon Willison · Jun 17, 23:58

**背景**: 开源权重大语言模型发布其训练好的模型参数（权重）供公众使用，通常采用 MIT 等允许广泛商业应用的许可证，这与要求同时发布训练数据和代码的真正开源模型不同。混合专家（MoE）架构是一种通过拥有大量总参数但仅为每个输入激活一小部分动态子集来提高模型容量和计算效率的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@divagr1925/breaking-the-scaling-wall-an-introduction-to-mixture-of-experts-in-llm-f8447a337a05">Breaking the Scaling Wall: An Introduction to Mixture of Experts in...</a></li>
<li><a href="https://letsdatascience.com/blog/open-source-vs-closed-llms-choosing-the-right-model-in-2026">Open Source vs Closed LLMs: The 2026 Decision Framework | Let's Data Science</a></li>
<li><a href="https://artificialanalysis.ai/methodology">Language Model Benchmarking Methodology | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#AI-models`, `#China`, `#benchmarks`

---

<a id="item-3"></a>
## [为模型上下文协议认证提出零接触 OAuth 方案](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) ⭐️ 8.0/10

一项关于“零接触 OAuth”的新提案旨在通过与企业身份提供商集成，来简化并保护人工智能代理的认证，从而让用户在首次登录时即可自动连接到所需的服务器。 这种方法通过将认证流程与代理的上下文隔离开来（这正是模型上下文协议（MCP）的一个关键优势），解决了企业采用人工智能所面临的关键安全性和用户体验挑战。 该提案由一种名为 ID-JAG 的新令牌格式驱动，这是一个 IETF 草案标准，它能够在使用同一 SSO 提供商的应用程序之间实现安全的数据共享，并且并非 MCP 专属。

hackernews · niyikiza · Jun 18, 21:54 · [社区讨论](https://news.ycombinator.com/item?id=48592163)

**背景**: 模型上下文协议（MCP）是 Anthropic 推出的一项开放标准，旨在规范像大语言模型这样的人工智能系统与外部工具和数据源的集成方式。OAuth 是一个授权标准协议，它允许第三方服务在不暴露用户凭据的情况下访问用户的账户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/">Enterprise-Managed Authorization: Zero - touch OAuth for MCP</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调了 MCP 在隔离认证流程以保障安全和改善用户体验方面的技术价值，同时也指出其底层的 ID-JAG 令牌格式在 MCP 之外具有更广泛的应用。也有用户对身份提供商管理的委托访问的透明性表示了担忧。

**标签**: `#OAuth`, `#AI-agents`, `#MCP`, `#authentication`, `#enterprise-security`

---

<a id="item-4"></a>
## [挪威零售商 Elkjop 因违反 GDPR 强制同意规定被罚 180 万欧元。](https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/) ⭐️ 8.0/10

挪威数据保护机构对电子零售商 Elkjop 处以 180 万欧元罚款，原因是该公司将营销同意作为顾客俱乐部会员资格的强制性条件，而这一做法早在五年前就被一位隐私倡导者举报。 此案成为 GDPR 核心原则——同意必须是自由给出且不能与其他服务捆绑——的重大执法案例，直接处罚了一家侵犯消费者数据权利的大型零售商。 违规行为源于 Elkjop 政策中的一句话，该条款规定接收营销信息是成为顾客俱乐部会员的条件，监管机构认定这是 GDPR 第 4(11)条和第 7 条规定的非自由给予同意的典型例子。

hackernews · speckx · Jun 18, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48589501)

**背景**: 《通用数据保护条例》（GDPR）是欧盟的综合性数据隐私法律。其基本要求是，数据处理的同意必须是具体、知情且自由给予的，这意味着除非同意是特定服务所真正必需的，否则不能将其作为获取服务或产品的先决条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/">I told them forced consent was unlawful. Five years later it cost Elkjop €1.8 million — That Privacy Guy!</a></li>
<li><a href="https://gdpr-info.eu/issues/consent/">Consent - General Data Protection Regulation (GDPR ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调了行使数据权利在现实中的困难，一位评论者指出，与那些简单同意的人相比，反对条款和服务的个人往往处于显著劣势。另一位用户提供了官方挪威语和英文裁决文件的链接，增加了案例细节的可信度。

**标签**: `#GDPR`, `#privacy`, `#law_enforcement`, `#data_rights`, `#consent`

---

<a id="item-5"></a>
## [Datasette Apps 插件支持在 Datasette 中安全托管自定义 HTML 应用](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 8.0/10

Datasette 团队发布了一个名为 'datasette-apps' 的新插件，该插件允许自包含的 HTML 和 JavaScript 应用在 Datasette 内的沙盒化 iframe 中运行，从而实现对底层数据的安全只读 SQL 查询和交互。 这个插件极大地扩展了 Datasette 的用途，允许用户直接在平台内构建和托管自定义的、交互式的数据探索工具和应用，从而将其从一个数据探索工具转变为更通用的应用宿主。 这些应用运行在一个严格受限的 iframe 沙盒中，并使用内容安全策略（CSP）标头来防止访问 cookies、localStorage 以及发出外部 HTTP 请求，从而确保数据不会被窃取。写入查询是可行的，但必须通过存储查询进行显式配置，这增加了一层额外的安全性。

rss · Simon Willison · Jun 18, 23:58

**背景**: Datasette 是一个用于探索和发布数据的开源工具，主要是将 SQLite 数据库转换为带有 JSON API 的交互式网站。沙盒化 iframe 是一种网页安全技术，它将嵌入的内容与主页面隔离，以防止恶意行为。存储查询的概念是指保存在数据库中的预定义 SQL 语句，可用于安全地控制写入操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/datasette">GitHub - simonw/ datasette : An open source multi-tool for exploring and...</a></li>
<li><a href="https://www.htmlgoodies.com/news/html-iframe-sandbox/">HTML iFrame Sandbox | Securing Your Web Site | HTML Goodies</a></li>
<li><a href="https://datasette.io/">Datasette : An open source multi-tool for exploring and publishing data</a></li>

</ul>
</details>

**社区讨论**: 提供的内容中没有包含社区评论，因此没有讨论可以总结。

**标签**: `#datasette`, `#data-tools`, `#javascript`, `#plugins`, `#web-development`

---

<a id="item-6"></a>
## [研究人员将大规模“Popa”僵尸网络与以色列上市公司关联](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/) ⭐️ 8.0/10

多家安全研究公司得出结论，运营了四年、迫使数百万消费电视盒子成为代理网络一部分的 Popa 安卓僵尸网络，与由以色列上市公司 Alarum Technologies Ltd（纳斯达克代码：ALAR）运营的住宅代理服务提供商 NetNut 有关。 这一发现建立了大型、大规模网络犯罪行动与一家上市公司之间的直接联系，引发了对公司治理、问责制以及代理/VPN 行业道德界限的严重质疑。 Popa 僵尸网络劫持了基于安卓的消费电视盒子，用以中继用于广告欺诈、账户接管和大规模数据抓取的互联网流量，将这些设备作为住宅代理网络的一部分加以利用。

rss · Krebs on Security · Jun 18, 17:37

**背景**: 僵尸网络是指一组感染了恶意软件并被攻击者控制的联网设备网络，通常设备所有者并不知情。像 NetNut 这样的住宅代理提供商提供来自真实消费设备的 IP 地址，使互联网流量看起来来自普通家庭，这在网页抓取和广告验证等任务中很有价值，但也可能被滥用。Alarum Technologies 是一家在纳斯达克上市的公司，从事互联网访问和数据收集解决方案领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NetNut-Proxy-Network/NetNut">GitHub - NetNut-Proxy-Network/NetNut: Premium Static & Rotating IPs | HTTP(s) Residential Proxy Network | Information & Code samples. · GitHub</a></li>
<li><a href="https://finance.yahoo.com/quote/ALAR/">Alarum Technologies Ltd . (ALAR) Stock Price... - Yahoo Finance</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#botnet`, `#corporate-governance`, `#cybercrime`, `#proxy-networks`

---

<a id="item-7"></a>
## [美国政府公布 3611 个人工智能用例，应用迅速扩张](https://www.schneier.com/blog/archives/2026/06/ai-use-by-the-us-government.html) ⭐️ 8.0/10

特朗普政府的行政管理与预算局披露了美国联邦政府内部 3611 个活跃或计划中的人工智能用例，较拜登政府任期最后一年的清单增加了 70%。 人工智能在包括核安全和个人自由等高风险政府职能领域的大规模采用，引发了人们对缺乏充分监督的自动化决策的深刻伦理和安全担忧。 该用例清单于 4 月 14 日由行政管理与预算局披露，并发布在 GitHub 上，涵盖了将决策过程从人类转移给机器的敏感职能。

rss · Schneier on Security · Jun 17, 11:04

**背景**: 人工智能用例清单是根据行政命令要求编制的公开目录，列出了政府机构计划如何使用人工智能。70%的快速增长表明联邦各机构的采用正在加速。布鲁斯·施奈尔是一位著名的安全技术专家和评论员，经常分析技术政策和风险。

**标签**: `#AI governance`, `#government technology`, `#policy`, `#automation ethics`, `#Bruce Schneier`

---

<a id="item-8"></a>
## [干细胞疗法使严重自身免疫病缓解长达 15 年](https://www.nature.com/articles/d41586-026-01925-7) ⭐️ 8.0/10

一项开创性的自体造血干细胞移植疗法，在两名患有视神经脊髓炎谱系障碍的患者身上实现了长达 15 年的长期缓解，这是一种损害脊髓和视神经的严重自身免疫性疾病。 这一长期成功案例证明了干细胞疗法在治疗严重、难治性自身免疫疾病方面具有持久乃至治愈的潜力，可能将治疗模式从终身管理转向持续缓解。 该疗法采用了自体造血干细胞移植，即使用患者自身的干细胞，相关成果发表在高影响力期刊《自然》上，突显了这一长期疗效的科学重要性。

rss · Nature · Jun 19, 00:00

**背景**: 视神经脊髓炎谱系障碍是一种罕见但严重的中枢神经系统自身免疫性疾病，主要攻击视神经和脊髓，常导致失明和瘫痪。自体造血干细胞移植是一种强化治疗过程，通过抑制患者免疫系统并使用其自身采集的干细胞进行重建，该方法已被探索用于治疗对传统疗法无效的自身免疫疾病。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41582-024-01050-x">Autologous haematopoietic stem cell transplantation for treatment of multiple sclerosis and neuromyelitis optica spectrum disorder — recommendations from ECTRIMS and the EBMT | Nature Reviews Neurology</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autologous_hematopoietic_stem_cell_transplantation">Autologous hematopoietic stem cell transplantation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neuromyelitis_optica_spectrum_disorder">Neuromyelitis optica spectrum disorder - Wikipedia</a></li>

</ul>
</details>

**标签**: `#stem_cells`, `#autoimmune_disease`, `#regenerative_medicine`, `#clinical_trial`, `#neurology`

---

<a id="item-9"></a>
## [胚胎“组织者”细胞可跨动物门指导身体构型形成](https://www.nature.com/articles/d41586-026-01910-0) ⭐️ 8.0/10

研究表明，胚胎“组织者”细胞能够指示来自不同动物门的胚胎构建何种身体形态，这暗示了一种保守的身体构型形成机制。 这一发现通过揭示一种基本的模式化信号可能在巨大的进化距离上被共享，为动物身体结构的进化提供了线索，有望统一我们对发育生物学的理解。 这些组织者细胞跨不同门发挥功能的能力表明，用于轴形成和组织特化的核心信号通路是高度保守的，尽管具体的下游反应可能有所不同。

rss · Nature · Jun 18, 00:00

**背景**: 胚胎发育中“组织者”的概念可追溯至 1924 年施佩曼-曼戈尔德组织者在两栖动物中的发现，该发现表明一组特定的细胞可以诱导次级身体轴的形成。这些组织者细胞对指导脊椎动物中枢神经系统及其他结构的发育至关重要。理解这一组织原则如何进化，是理解动物身体构型多样性的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Spemann-Mangold_organizer">Spemann-Mangold organizer</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8628936/">The Organizer and Its Signaling in Embryonic Development - PMC</a></li>
<li><a href="https://www.science.org/content/article/elusive-master-organizer-human-embryo-growth-seen-first-time">Elusive master organizer of human embryo growth seen for the first time | Science | AAAS</a></li>

</ul>
</details>

**标签**: `#developmental biology`, `#evolution`, `#embryology`, `#cell biology`, `#comparative biology`

---

<a id="item-10"></a>
## [Ubiquiti 推出基于 ZFS 的企业级 NAS 设备](https://blog.ui.com/article/introducing-enterprise-nas) ⭐️ 7.0/10

Ubiquiti 发布了一款基于 ZFS 文件系统的企业级网络附属存储（NAS）设备，配备双 25GbE SFP28 端口和冗余电源。 此举意义重大，因为以高性价比硬件闻名的 Ubiquiti 进入了企业存储市场，其模式强调无经常性订阅费用，可能对现有厂商构成挑战。 该设备售价 3999 美元，包含高性能网络接口，但社区成员质疑其基于 HDD 的存储能否充分利用 25GbE 链路的带宽。

hackernews · ksec · Jun 18, 14:24 · [社区讨论](https://news.ycombinator.com/item?id=48585866)

**背景**: ZFS 是一种先进的企业级文件系统和逻辑卷管理器，提供数据完整性校验、快照和写时复制克隆等功能。25GbE 是一种高速以太网标准，提供比 10GbE 高 2.5 倍的带宽，常用于数据中心和企业环境。企业级 NAS 设备是专为商业环境中的可靠性、性能和可扩展性设计的专用存储设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pve.proxmox.com/wiki/ZFS_on_Linux">ZFS on Linux - Proxmox VE</a></li>
<li><a href="https://en.wikipedia.org/wiki/25_Gigabit_Ethernet">25 Gigabit Ethernet - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchstorage/feature/Enterprise-NAS-Vital-features-and-purchase-considerations">9 enterprise NAS features and purchase considerations | TechTarget</a></li>

</ul>
</details>

**社区讨论**: 社区讨论活跃且意见不一：支持者赞扬其采用的先进 ZFS 技术和 Ubiquiti 的无订阅模式，而批评者则对 Ubiquiti 过去的软件安全事件表示担忧，并质疑硬件能否实现承诺的网络性能。

**标签**: `#ZFS`, `#NAS`, `#Ubiquiti`, `#enterprise-storage`, `#networking-hardware`

---

<a id="item-11"></a>
## [康奈尔大学高级编译器课程现已作为免费自学在线资源开放](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 7.0/10

康奈尔大学已将 CS 6120 高级编译器课程作为免费的自学在线资源开放，涵盖静态单赋值(SSA)形式、编译器优化和即时(JIT)编译等主题。 这为全球学习者提供了免费获取高级大学级别编译器教育的机会，可能对更广泛的计算机科学教育生态系统产生影响，并降低获取专业知识的门槛。 课程资料托管在康奈尔大学 CS 6120 的官方课程页面上，并已在技术社区中多次出现，引发了关于其内容和范围（特别是“高级”标签）的讨论。

hackernews · ibobev · Jun 18, 11:04 · [社区讨论](https://news.ycombinator.com/item?id=48583606)

**背景**: CS 6120 是康奈尔大学一门专注于高级编译器技术的研究生课程。SSA（静态单赋值）形式是现代编译器中一种关键的中间表示，通过确保每个变量仅被赋值一次来简化优化。JIT（即时）编译是一种在程序执行期间编译代码以提高性能的技术，常用于虚拟机中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Static_single-assignment_form">Static single-assignment form - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Just-in-time_compilation">Just -in- time compilation - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论凸显了观点分歧：一种观点质疑课程的“高级”性，认为死代码消除和 SSA 等许多核心主题属于入门级内容。另一种观点批评课程对轨迹编译的关注，认为这是一种过时的技术，并建议涵盖更相关的概念，如类型反馈和反优化。讨论中还将该课程与其他资源（如诺拉·桑德勒的编译器书籍）进行了比较。

**标签**: `#compilers`, `#education`, `#open-source`, `#computer-science`, `#optimization`

---

<a id="item-12"></a>
## [医院与大学通过药物再利用将成本削减高达 90%。](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 7.0/10

医院与大学正在系统性地将现有已批准药物重新用于治疗新病症，例如使用抗癌药阿瓦斯汀（Avastin）治疗黄斑变性，其成本仅为专用药雷珠单抗（Lucentis）的一小部分。 这种做法通过为具有昂贵专用治疗方案的病症提供有效且低成本的替代品，直接挑战了高昂的药品定价模式，有望改善全球公共卫生的可及性，并迫使业界重新评估药物开发的经济学。 一个关键例子是阿瓦斯汀（贝伐珠单抗）和雷珠单抗（兰尼珠单抗），两者分子结构相似，但包装和价格相差约 30 倍（每剂 50 美元 vs 1500 美元）；然而，这种再利用通常依赖超说明书用药，并在更广泛采用时面临监管和生产上的障碍。

hackernews · giuliomagnifico · Jun 18, 10:33 · [社区讨论](https://news.ycombinator.com/item?id=48583386)

**背景**: 药物再利用是指研究现有已批准药物用于新的治疗用途，这比从头开发新药更快、成本更低。超说明书用药，即医生根据医学文献将药物用于未获批准的适应症，是再利用的常见途径，但其运作处于复杂的监管环境中，缺乏美国食品药品监督管理局（FDA）对该新用途的正式批准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nih.gov/news-events/nih-research-matters/repurposing-drugs-treat-age-related-macular-degeneration">Repurposing drugs to treat age-related macular degeneration | National Institutes of Health (NIH)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Off-label_use">Off-label use - Wikipedia</a></li>
<li><a href="https://www.fda.gov/patients/learn-about-expanded-access-and-other-treatment-options/understanding-unapproved-use-approved-drugs-label">Understanding Unapproved Use of Approved Drugs "Off Label" | FDA</a></li>

</ul>
</details>

**社区讨论**: 社区讨论证实了阿瓦斯汀/雷珠单抗案例的代表性，评论者分享了使用再利用药物（如 Spravato vs. 氯胺酮）的个人经历，并援引了 Cures Within Reach 等资助此类罕见病研究的非营利组织；讨论中提出的一个主要担忧是，在没有制造商同意的情况下扩展药物用途缺乏明确的监管途径，这限制了尽管已证实有效但无法正式采用的情况。

**标签**: `#healthcare`, `#drug_repurposing`, `#healthcare_economics`, `#pharmaceutical_industry`, `#public_health`

---

<a id="item-13"></a>
## [Charity Majors：AI 颠倒了代码的经济逻辑](https://simonwillison.net/2026/Jun/17/charity-majors/#atom-everything) ⭐️ 7.0/10

行业专家 Charity Majors 认为，2025 年，AI 从根本上颠倒了代码生产的经济逻辑，使得代码行变得可丢弃且生成成本近乎为零。 这种转变意味着，软件工程的价值和关注点必须从代码创建转向更高层次的关切，例如系统设计、可观测性以及严格的工程纪律。 其核心论点是，尽管代码变得廉价和可丢弃，但管理复杂 AI 生成系统所需的工程纪律实际上增加了，而非减少了。

rss · Simon Willison · Jun 17, 17:12

**背景**: 传统上，编写代码是一个耗时且成本高昂的过程，使得每一行代码都很宝贵。强大的生成式 AI 编程模型的出现大幅降低了这一成本，促使人们重新评估软件工程实践和开发者的角色。

**标签**: `#ai-assisted-programming`, `#software-engineering`, `#economics`, `#generative-ai`, `#commentary`

---

<a id="item-14"></a>
## [软件自由保护协会发布针对自由开源软件贡献的 LLM 生成式 AI 使用指南](https://lwn.net/Articles/1078521/) ⭐️ 7.0/10

软件自由保护协会（SFC）发布了由社区共同制定的指南，旨在指导在自由开源软件（FOSS）贡献中负责任地使用基于大语言模型（LLM）的生成式 AI 系统。这些指南由 SFC 和社区志愿者共同创建，以应对此类工具带来的伦理和实际困境。 这些指南为在将专有 AI 工具与自由软件原则进行复杂整合中摸索前行的 FOSS 贡献者提供了实用的指导方针，可能会影响未来开源生态系统中的贡献工作流程和许可规范。它们有助于减少使用专有 AI 系统所带来的损害，无论贡献者是否选择使用这些系统。 这些建议被定位为最佳实践，而非严格的要求或法律定义，并且 SFC 计划持续完善它们，同时提供教程和播客等支持材料。指南承认 FOSS 开发者对大语言模型持有多种不同观点，包括自愿使用和雇主强制使用的情况。

rss · LWN.net · Jun 18, 16:00

**背景**: 软件自由保护协会是一个非营利组织，致力于通过提供组织和法律支持来推广、开发和捍卫自由、自由及开源软件项目。大语言模型（LLM）和生成式 AI 工具（如驱动代码助手的工具）是在通常包含开源代码的庞大数据集上训练的，这引发了关于许可合规性、代码原创性以及在 FOSS 生态系统内使用专有系统的伦理边界等重要问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/open-source-llms">What are Open Source Large Language Models? | IBM</a></li>
<li><a href="https://www.techtarget.com/searchenterpriseai/tip/Examining-the-future-of-AI-and-open-source-software">Does AI-generated code violate open source licenses? | TechTarget</a></li>

</ul>
</details>

**标签**: `#FOSS`, `#AI ethics`, `#LLM`, `#software licensing`, `#open source`

---

<a id="item-15"></a>
## [Linux 7.2 合并窗口过半，已合并超过 7000 个变更集](https://lwn.net/Articles/1078068/) ⭐️ 7.0/10

Linux 7.2 合并窗口的前半程已结束，自 6 月 14 日发布 7.1 内核后启动，已有超过 7000 个非合并变更集被拉入主线内核。 这份摘要为内核开发者和系统程序员提供了清晰的概述，展示了即将集成到下一个主要版本中的大量变更，帮助他们跟踪上游开发并为兼容性测试做准备。 合并窗口仍在进行中，大多数核心子系统的变更已经合并，这意味着最终 7.2 版本的范围正在变得清晰。该数字特指非合并变更集，它们代表直接的代码贡献，而非集成现有工作的合并提交。

rss · LWN.net · Jun 18, 13:47

**背景**: 在 Linux 内核开发中，合并窗口是稳定版本（如 7.1）发布后的两周时间，在此期间，子系统维护者的新功能和更改会被合并到 Linus Torvalds 的主线仓库中。变更集是版本控制系统中的一个变更单元；非合并变更集是指一次主要的代码更改，与合并其他工作的合并提交不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/625735/">Kernel development [LWN.net]</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linux_kernel">Linux kernel - Wikipedia</a></li>

</ul>
</details>

**标签**: `#linux kernel`, `#systems programming`, `#open source`, `#kernel development`

---

<a id="item-16"></a>
## [RMR 和 BRMR 提议通过 RDMA 实现高效的 Linux 块复制](https://lwn.net/Articles/1074291/) ⭐️ 7.0/10

在 2026 年 Linux 存储、文件系统、内存管理和 BPF 峰会上，展示了两个新的 Linux 内核模块：RMR（基于 RTRS 的可靠多播）和 BRMR（基于 RMR 的块设备）。它们建立在现有的 RTRS RDMA 传输库之上，能够为持久化虚拟块设备实现单跳、双活块复制。 这种方法可以为云基础设施提供商提供一种高效、低开销的方式来创建持久、容错的虚拟块设备。它通过直接在块存储层利用 RDMA 的高吞吐、低延迟特性，解决了一个核心基础设施挑战。 这些模块处于开发阶段，开发者们正在积极寻求 Linux 内核社区的反馈和讨论，然后再提交上游合入。RMR 提供了基于 RDMA 的双活块级复制，而 BRMR 将其作为标准的 Linux 块设备（如 /dev/brmrX）暴露出来。

rss · LWN.net · Jun 18, 13:25

**背景**: 远程直接内存访问 (RDMA) 是一种技术，允许一台计算机直接访问另一台计算机的内存而无需操作系统介入，从而实现高速、低延迟的数据传输。内核的 RDMA 传输库 (RTRS) 已经提供了一个建立在 RDMA 之上的消息传递层。云提供商需要持久化的虚拟块设备，这些设备必须可靠地存储数据并在硬件故障时幸存，通常需要跨多个节点进行复制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ionos-cloud/RMR">GitHub - ionos-cloud/ RMR : Reliable multicast over RTRS ( RMR ) and...</a></li>
<li><a href="https://noise.getoto.net/2026/06/18/single-hop-block-replication-with-rmr-and-brmr/">[$] Single-hop block replication with RMR and BRMR | Noise</a></li>

</ul>
</details>

**标签**: `#linux-kernel`, `#storage`, `#rdma`, `#cloud-infrastructure`, `#distributed-systems`

---

<a id="item-17"></a>
## [恶意软件嵌入违禁文本以欺骗人工智能安全扫描器](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html) ⭐️ 7.0/10

一名间谍软件开发者开始在 JavaScript 代码注释中嵌入涉及核武器和生物武器的文本，其专门设计是为了触发人工智能分析工具的安全过滤器，并干扰自动化恶意软件检测。 这种技术代表了一种新颖的对抗策略，它将人工智能模型的安全防护栏变成了对抗安全分析的武器，可能催生新的猫鼠游戏，迫使安全公司开发更强大、更具情境感知能力的人工智能扫描器。 违禁文本被放置在一个大型的 JavaScript 块注释中，这并不影响代码执行，这意味着恶意软件仍然功能完整，而该注释则试图通过引发拒绝、混淆或提前分类来破坏人工智能扫描器，从而在实际恶意负载被分析之前就将其误导。

rss · Schneier on Security · Jun 18, 11:04

**背景**: 自动化恶意软件分析通常使用人工智能模型来扫描可疑代码中的恶意模式。对抗性攻击是指精心设计输入数据，专门用于欺骗或混淆这些人工智能系统。ROT 类密码是一种简单的替换加密方法，其字母在字母表中按固定位数进行移位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ROT13">ROT13 - Wikipedia</a></li>
<li><a href="https://www.aitoolgo.com/learning/detail/bypassing-content-moderation-filters-techniques">Bypassing AI Content Moderation: Techniques and Challenges | AIToolGo</a></li>
<li><a href="https://mr7.ai/blog/machine-learning-for-malware-detection-techniques-tools-mmooyc0t">Machine Learning for Malware Detection: Techniques... | mr7.ai Blog</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#adversarial-ai`, `#malware`, `#ai-analysis`

---

<a id="item-18"></a>
## [可解聚树脂实现 3D 打印光敏聚合物的轻松重复利用](https://hackaday.com/2026/06/18/easily-reuse-3d-printing-photopolymers-with-depolymerizable-resin/) ⭐️ 7.0/10

一种新型可解聚树脂已被开发用于 3D 打印，它使得通常不可逆的光聚合过程可以逆转，从而实现固化材料的重复利用。像 3Dresyn 这样的公司已经在销售使此成为可能的添加剂和树脂。 这项创新通过创建循环材料生命周期，解决了树脂基 3D 打印中严重的环境废弃物和材料成本问题。它可以大幅减少增材制造行业的环境足迹，并降低用户的运营成本。 其关键机制在于设计树脂的化学结构使其可解聚，这意味着聚合物网络在特定条件下可以分解回其起始单体，这与传统热固性树脂不同。这种方法与可逆光聚合和 Vitrimers（一种具有动态键、允许再加工的材料）的研究相关。

rss · Hackaday · Jun 19, 02:00

**背景**: 用于 SLA 和 DLP 3D 打印机的标准光敏聚合物树脂在暴露于紫外线时会不可逆地固化（硬化），形成刚性的交联热固性聚合物。这个过程是单向的，意味着固化后的树脂不能像热塑性塑料那样熔化重塑，从而产生废弃物。可解聚树脂和像 Vitrimers 这样具有动态化学键的材料的发展，代表了创造可再加工和可持续热固性塑料的新前沿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hackaday.com/2026/06/18/easily-reuse-3d-printing-photopolymers-with-depolymerizable-resin/">Easily Reuse 3D Printing Photopolymers With Depolymerizable Resin</a></li>
<li><a href="https://pubs.rsc.org/en/content/articlehtml/2024/gc/d3gc04215d">Design of depolymerizable polymers toward a circular economy...</a></li>
<li><a href="https://pubs.acs.org/doi/10.1021/acs.iecr.4c03705">Vitrimers for 3D Printing Technology: Current Status and Future Perspectives | Industrial & Engineering Chemistry Research</a></li>

</ul>
</details>

**标签**: `#3D Printing`, `#Materials Science`, `#Sustainability`, `#Photopolymers`, `#Recycling`

---

<a id="item-19"></a>
## [研究发现，使用 AI 工具正在侵蚀关键行业的专业技能。](https://www.nature.com/articles/d41586-026-01947-1) ⭐️ 7.0/10

发表在《自然》杂志上的新研究表明，对 AI 工具的依赖导致了医生和软件工程师核心专业能力的退化。 这一发现意义重大，因为它提供了 AI 整合可能存在负面影响的早期实证证据，挑战了认为这些工具只提升生产力而无代价的假设，并对劳动力培训和未来的工作方式有着广泛影响。 这些研究特别测量了两个高风险专业领域的技能退化：医学和软件工程，这些领域中精确的判断和基础专业知识至关重要。

rss · Nature · Jun 18, 00:00

**背景**: 将 AI 助手快速整合到专业工作流程中，被广泛宣传为提高效率和减少错误的一种方式。然而，人们日益担忧，过度依赖此类工具可能导致‘技能退化’，即专业人员逐渐失去独立执行核心任务的能力。这个概念类似于过度依赖 GPS 导航可能会损害人的天生方向感。

**标签**: `#AI ethics`, `#skill degradation`, `#workforce impact`, `#software engineering`, `#medical AI`

---

<a id="item-20"></a>
## [人类基因组的三维结构对 AI 建模构成挑战](https://www.quantamagazine.org/why-the-human-genomes-tangled-physicality-may-confound-ai-20260618/) ⭐️ 7.0/10

一篇新文章认为，人类基因组复杂缠绕的物理结构为试图建模和预测基因组行为的人工智能系统带来了根本性障碍。 这凸显了将人工智能应用于基因组学和生物学的一个关键差距，表明现有模型可能不足以捕捉基因组的全部复杂性，这可能影响精准医学的发展以及我们对生物学的基本理解。 基因组的三维组织结构，包括拓扑关联结构域（TADs）和染色质环等结构，动态调控着基因表达等关键过程，但这种物理架构具有高度的变异性和背景依赖性，使得人工智能难以学习普遍适用的规则。

rss · Quanta Magazine · Jun 18, 14:12

**背景**: 人类基因组并非简单的线性代码，而是在细胞核内被组织成复杂的三维结构。这种结构通过染色质构象捕获技术（如 Hi-C）进行研究，该技术可以绘制不同基因组区域之间的相互作用图谱。一个关键的组织单元是拓扑关联结构域（TAD），它是一个自我相互作用的区域，其中 DNA 序列彼此频繁互作，由 CTCF 和 cohesin 等蛋白界定，对正确的基因调控至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41580-021-00362-w">Understanding 3D genome organization by multidisciplinary methods | Nature Reviews Molecular Cell Biology</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6312108/">Organizational Principles of 3D Genome Architecture - PMC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Topologically_associating_domain">Topologically associating domain</a></li>

</ul>
</details>

**标签**: `#genomics`, `#AI`, `#computational-biology`, `#systems-biology`, `#complexity`

---

<a id="item-21"></a>
## [Show HN: Are You in the Weights?](https://www.intheweights.com/) ⭐️ 6.0/10

A website that tests how well various LLMs recognize personal names by querying them in parallel and clustering responses.

hackernews · turtlesoup · Jun 18, 20:49 · [社区讨论](https://news.ycombinator.com/item?id=48591348)

**标签**: `#LLM`, `#privacy`, `#web-tools`, `#AI-experimentation`, `#Hacker-News`

---

<a id="item-22"></a>
## [WAI-ARIA 1.3 引入 ariaNotify() 方法以实现程序化屏幕阅读器通知](https://css-tricks.com/the-siren-song-of-arianotify/) ⭐️ 6.0/10

WAI-ARIA 1.3 规范在 DOM 元素上定义了一个新的 `ariaNotify()` 方法，该方法允许开发者以编程方式将一段文本字符串加入队列，由屏幕阅读器进行播报。 这为网页开发者提供了一个专注的、命令式的 API，可以直接触发辅助技术的语音播报，为增强网页可访问性提供了一个比声明式 ARIA 属性更可靠和有意识的工具。 `ariaNotify()` 方法被有意设计为只写 API，这意味着开发者无法从返回值确定通知是否已被送达，这一设计选择是为了防止潜在的指纹识别滥用。

rss · CSS-Tricks · Jun 17, 15:32

**背景**: WAI-ARIA（网页可访问性倡议 - 可访问富互联网应用）是一项技术规范，它定义了如何使网页内容和网页应用程序对残障人士更具可访问性。其工作原理是提供语义化角色、状态和属性，供屏幕阅读器等辅助技术用来解释和与用户界面元素交互。屏幕阅读器是一种辅助技术，它将屏幕上的文本和元素转换为语音或盲文输出，服务于视障用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://w3c.github.io/aria/">Accessible Rich Internet Applications (WAI-ARIA) 1.3</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaNotify">Element: ariaNotify () method - Web APIs | MDN</a></li>
<li><a href="https://azukiazusa.dev/en/blog/aria-notify-method/">Imperatively Notify Assistive Technologies with the ` ariaNotify ...</a></li>

</ul>
</details>

**标签**: `#accessibility`, `#ARIA`, `#web-development`, `#front-end`

---

<a id="item-23"></a>
## [Windows NT 成功移植到 Nintendo GameCube 硬件上运行](https://hackaday.com/2026/06/18/running-windows-nt-on-the-nintendo-gamecube/) ⭐️ 6.0/10

一个爱好者项目成功地将 1990 年代的工作站操作系统 Windows NT 移植到了 Nintendo GameCube 游戏机上运行，而这款游戏机本身并非为通用计算设计。 这个项目是复古计算和硬件破解领域的一项显著技术成就，它展示了 Windows NT 硬件抽象层（HAL）的灵活性，以及 GameCube 基于 PowerPC 的硬件在完成远超其原始设计用途任务方面的多功能性。 该项目的成功关键在于为 GameCube 独特的“Broadway”处理器（IBM PowerPC 750 的衍生版本）及其特定的内存和 I/O 架构创建了一个自定义的 HAL，这套架构与 Windows NT 原本面向的标准 PC 差异巨大。

rss · Hackaday · Jun 19, 05:00

**背景**: Windows NT 是微软在 1993 年首次发布的一个操作系统系列，以其通过硬件抽象层（HAL）实现跨不同 CPU 架构的可移植性而闻名。Nintendo GameCube 于 2001 年发布，采用定制的 IBM “Gekko”（后在 Wii 中称为“Broadway”）基于 PowerPC 的 CPU。移植操作系统需要编写底层驱动程序以使操作系统与游戏机的特定硬件通信，这是一项复杂的逆向工程任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HAL_(software)">HAL (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Broadway_(processor)">Broadway (processor) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gekko_(processor)">Gekko (processor) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#retro computing`, `#OS porting`, `#hardware hacking`, `#Nintendo`, `#Windows NT`

---

<a id="item-24"></a>
## [Brexit tore apart European science — now the research rifts are healing](https://www.nature.com/articles/d41586-026-01841-w) ⭐️ 6.0/10

UK research funding from the EU is increasing after Brexit, but the scientific networks that were disrupted are still difficult to restore.

rss · Nature · Jun 18, 00:00

**标签**: `#research policy`, `#international collaboration`, `#science funding`, `#Brexit impact`

---

<a id="item-25"></a>
## [新证明揭示需要多少次随意洗牌才能真正打乱一副牌](https://www.quantamagazine.org/seven-perfect-shuffles-randomize-a-deck-of-cards-but-how-many-sloppy-ones-20260617/) ⭐️ 6.0/10

一个新的数学证明扩展了几十年来的旧结果，它展示了需要多少次不完美的（随意的）拨牌式洗牌才能完全随机化一副标准的 52 张扑克牌，从而消除了之前对精确、完美切牌的要求。 这个证明为实际场景中的洗牌提供了一个更现实的模型，弥合了理论数学与现实世界纸牌游戏或赌场程序之间的鸿沟，并推进了我们对随机化过程的理解。 该证明建立在已知结果之上，即七次完美的拨牌式洗牌足以实现随机化，但现在它通过使用一种称为总变差距离的度量来衡量牌组接近真正随机的程度，从而考虑了人类洗牌中自然的不精确性。

rss · Quanta Magazine · Jun 17, 14:35

**背景**: 吉尔伯特-香农-里兹模型描述了完美的拨牌式洗牌，即牌组被精确地分成两半并完美地交错，而 1992 年由佩尔西·戴康尼斯等人证明，七次这样的洗牌足以随机化一副 52 张的牌。总变差距离是一种数学度量，用于比较两个概率分布的差异程度，其值为零表示两者完全相同，为一则表示完全不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.quantamagazine.org/seven-perfect-shuffles-randomize-a-deck-of-cards-but-how-many-sloppy-ones-20260617/">Seven Perfect Shuffles Randomize a Deck of Cards. But How Many Sloppy Ones? | Quanta Magazine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gilbert–Shannon–Reeds_model">Gilbert–Shannon–Reeds model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shuffling">Shuffling - Wikipedia</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#probability`, `#combinatorics`, `#research`

---