---
layout: default
title: "Horizon Summary: 2026-06-19 (EN)"
date: 2026-06-19
lang: en
---

> From 67 items, 25 important content pieces were selected

---

1. [Researchers discover 10,000 GitHub repos spreading Trojan malware](#item-1) ⭐️ 9.0/10
2. [Chinese lab Z.ai releases GLM-5.2, a 753B-parameter open-weights LLM under MIT license.](#item-2) ⭐️ 9.0/10
3. [Zero-Touch OAuth Proposed for Model Context Protocol Authentication](#item-3) ⭐️ 8.0/10
4. [Norwegian retailer Elkjop fined €1.8M for unlawful forced consent under GDPR.](#item-4) ⭐️ 8.0/10
5. [Datasette Apps Plugin Enables Secure Custom HTML Apps Within Datasette](#item-5) ⭐️ 8.0/10
6. [Researchers Link Massive 'Popa' Botnet to Israeli Publicly-Traded Firm](#item-6) ⭐️ 8.0/10
7. [US Government Reveals Rapid Expansion of 3,611 AI Use Cases](#item-7) ⭐️ 8.0/10
8. [Stem cell therapy achieves 15-year remission for severe autoimmune disease](#item-8) ⭐️ 8.0/10
9. [Embryonic organizer cells direct body plans across animal phyla](#item-9) ⭐️ 8.0/10
10. [Ubiquiti Launches Enterprise NAS Appliance Built on ZFS](#item-10) ⭐️ 7.0/10
11. [Cornell's Advanced Compilers Course Available as Free Self-Guided Online Resource](#item-11) ⭐️ 7.0/10
12. [Hospitals and universities repurpose drugs to slash costs by up to 90%.](#item-12) ⭐️ 7.0/10
13. [Charity Majors: AI Has Inverted Code Economics](#item-13) ⭐️ 7.0/10
14. [Software Freedom Conservancy Releases LLM-Backed Generative AI Usage Guidelines for FOSS](#item-14) ⭐️ 7.0/10
15. [Linux 7.2 merge window halfway mark shows 7,000+ changesets merged](#item-15) ⭐️ 7.0/10
16. [RMR and BRMR propose efficient Linux block replication via RDMA](#item-16) ⭐️ 7.0/10
17. [Malware Embeds Forbidden Text to Trick AI Security Scanners](#item-17) ⭐️ 7.0/10
18. [Depolymerizable Resin Enables Easy Reuse of 3D Printing Photopolymers](#item-18) ⭐️ 7.0/10
19. [AI tool use found to degrade professional skills in key sectors.](#item-19) ⭐️ 7.0/10
20. [Human Genome's 3D Structure Challenges AI Modeling](#item-20) ⭐️ 7.0/10
21. [Show HN: Are You in the Weights?](#item-21) ⭐️ 6.0/10
22. [WAI-ARIA 1.3 Introduces ariaNotify() for Programmatic Screen Reader Announcements](#item-22) ⭐️ 6.0/10
23. [Windows NT Successfully Ported to Run on Nintendo GameCube Hardware](#item-23) ⭐️ 6.0/10
24. [Brexit tore apart European science — now the research rifts are healing](#item-24) ⭐️ 6.0/10
25. [New Proof Shows How Many Sloppy Shuffles Randomize a Deck of Cards](#item-25) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Researchers discover 10,000 GitHub repos spreading Trojan malware](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

A coordinated campaign has been discovered using over 10,000 GitHub repositories to distribute Trojan malware by exploiting software agents and supply chain trust. This reveals a massive, sophisticated supply chain attack that specifically targets automated software agents, potentially compromising developer tools and build pipelines at scale during a critical election year. The attackers primarily clone new repositories rather than popular ones and frequently delete and re-push commits to appear in 'Last Updated' search results, a tactic designed to deceive automated dependency management agents rather than human developers.

hackernews · theorchid · Jun 18, 11:45 · [Discussion](https://news.ycombinator.com/item?id=48583928)

**Background**: Software supply chain attacks involve compromising the integrity of software development and distribution, often by poisoning code repositories or package managers that developers implicitly trust. A software agent, in this context, refers to automated tools or bots that assist developers by managing dependencies, searching for code, or handling other tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/orchidfiles/i-discovered-a-large-scale-malware-distribution-campaign-on-github-4m6o">I discovered a large-scale malware distribution campaign on GitHub</a></li>
<li><a href="https://www.darktrace.com/blog/when-trust-becomes-the-attack-surface-supply-chain-attacks-in-an-era-of-automation-and-implicit-trust">Supply-Chain Attacks in an Era of Automation and Implicit Trust</a></li>
<li><a href="https://www.terrabytegroup.com/the-hidden-danger-of-impersonation-and-trust-exploitation-in-supply-chain-attacks/">The Hidden Danger of Impersonation and Trust Exploitation in Supply ...</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights that the campaign's focus on frequently updating new, lesser-known repos is a deliberate strategy to target automated software agents that search for dependencies. Some commenters note personal experiences of their legitimate projects being cloned or impersonated, and there is speculation linking the timing of the campaign to major upcoming elections, suggesting a potentially broader, coordinated effort.

**Tags**: `#supply-chain-security`, `#malware`, `#github`, `#cybersecurity`, `#software-agents`

---

<a id="item-2"></a>
## [Chinese lab Z.ai releases GLM-5.2, a 753B-parameter open-weights LLM under MIT license.](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

Chinese AI lab Z.ai released GLM-5.2, a 753-billion parameter text-only open-weights LLM with a 1-million-token context window under an MIT license. Early benchmarks suggest it is now the most powerful open-weights model available. This release represents a significant advancement in open-source AI, offering a highly capable model with a permissive license that encourages commercial use and research. It intensifies competition among leading open-weights models, potentially accelerating innovation and accessibility in the AI ecosystem. Despite its massive 753B total parameters, GLM-5.2 uses a Mixture of Experts (MoE) architecture with only 40 active parameters per token, and benchmarks note it is more token-hungry than previous models. It is also ranked highly for web development tasks on the Code Arena leaderboard, a surprising result for a text-only model.

rss · Simon Willison · Jun 17, 23:58

**Background**: Open-weights LLMs release their trained model parameters (weights) for public use, often under licenses like MIT that allow broad commercial application, unlike true open-source models which also require releasing training data and code. The Mixture of Experts (MoE) architecture is a technique that increases a model's capacity by having a large total parameter count but only activating a small, dynamic subset for each input, improving computational efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@divagr1925/breaking-the-scaling-wall-an-introduction-to-mixture-of-experts-in-llm-f8447a337a05">Breaking the Scaling Wall: An Introduction to Mixture of Experts in...</a></li>
<li><a href="https://letsdatascience.com/blog/open-source-vs-closed-llms-choosing-the-right-model-in-2026">Open Source vs Closed LLMs: The 2026 Decision Framework | Let's Data Science</a></li>
<li><a href="https://artificialanalysis.ai/methodology">Language Model Benchmarking Methodology | Artificial Analysis</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open-source`, `#AI-models`, `#China`, `#benchmarks`

---

<a id="item-3"></a>
## [Zero-Touch OAuth Proposed for Model Context Protocol Authentication](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) ⭐️ 8.0/10

A new proposal for "Zero-Touch OAuth" aims to simplify and secure authentication for AI agents by integrating with enterprise identity providers, enabling automatic server connections for users upon their first login. This approach addresses critical security and user experience challenges in enterprise AI adoption by isolating authentication flows from the agent's context, which is a key advantage of the Model Context Protocol (MCP). The proposal is powered by a new token format called ID-JAG, an IETF draft standard, which enables secure data sharing across applications using the same SSO provider and is not specific to MCP.

hackernews · niyikiza · Jun 18, 21:54 · [Discussion](https://news.ycombinator.com/item?id=48592163)

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic to standardize how AI systems like large language models integrate with external tools and data sources. OAuth is a standard protocol for authorization that allows third-party services to access a user's account without exposing their credentials.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/">Enterprise-Managed Authorization: Zero - touch OAuth for MCP</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>

</ul>
</details>

**Discussion**: Community discussion highlights the technical value of MCP in isolating auth flows for security and improved user experience, while also noting that the underlying ID-JAG token format has broader applications beyond MCP. Some concerns are raised about the transparency of delegated access managed by identity providers.

**Tags**: `#OAuth`, `#AI-agents`, `#MCP`, `#authentication`, `#enterprise-security`

---

<a id="item-4"></a>
## [Norwegian retailer Elkjop fined €1.8M for unlawful forced consent under GDPR.](https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/) ⭐️ 8.0/10

Norway's data protection authority fined electronics retailer Elkjop €1.8 million for making marketing consent a mandatory condition of customer club membership, a practice a privacy advocate had reported five years earlier. The case serves as a major enforcement example of GDPR's core principle that consent must be freely given and cannot be bundled with other services, directly penalizing a large retailer for violating consumers' data rights. The violation stemmed from a single sentence in Elkjop's policy stating that receiving marketing was a condition of being a customer club member, which the authority determined was a textbook example of non-freely given consent under GDPR Articles 4(11) and 7.

hackernews · speckx · Jun 18, 18:31 · [Discussion](https://news.ycombinator.com/item?id=48589501)

**Background**: The General Data Protection Regulation (GDPR) is the EU's comprehensive data privacy law. A fundamental requirement is that consent for data processing must be specific, informed, and freely given, meaning it cannot be made a precondition for accessing a service or product unless consent is genuinely necessary for that specific service.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/">I told them forced consent was unlawful. Five years later it cost Elkjop €1.8 million — That Privacy Guy!</a></li>
<li><a href="https://gdpr-info.eu/issues/consent/">Consent - General Data Protection Regulation (GDPR ...</a></li>

</ul>
</details>

**Discussion**: The community discussion highlighted the real-world difficulty of exercising data rights, with one commenter noting that pushing back against terms and services often puts individuals at a significant disadvantage compared to those who simply agree. Another user provided links to the official Norwegian and English decision documents, adding credibility to the case details.

**Tags**: `#GDPR`, `#privacy`, `#law_enforcement`, `#data_rights`, `#consent`

---

<a id="item-5"></a>
## [Datasette Apps Plugin Enables Secure Custom HTML Apps Within Datasette](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 8.0/10

The Datasette team launched a new plugin called 'datasette-apps' that allows self-contained HTML and JavaScript applications to run in a sandboxed iframe within Datasette, enabling secure read-only SQL queries and interaction with the underlying data. This plugin significantly expands Datasette's utility by allowing users to build and host custom, interactive data exploration tools and applications directly within the platform, transforming it from a data exploration tool into a more versatile application host. The apps run in a tightly constrained iframe sandbox with Content Security Policy headers to prevent access to cookies, localStorage, and external HTTP requests, ensuring security against data exfiltration. Write queries are possible but must be explicitly configured through stored queries, adding an extra layer of safety.

rss · Simon Willison · Jun 18, 23:58

**Background**: Datasette is an open-source tool for exploring and publishing data, primarily by turning SQLite databases into interactive websites with a JSON API. Sandboxed iframes are a web security technique that isolates embedded content from the main page to prevent malicious behavior. The concept of stored queries refers to pre-defined SQL statements saved in the database, which can be used to safely control write operations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/datasette">GitHub - simonw/ datasette : An open source multi-tool for exploring and...</a></li>
<li><a href="https://www.htmlgoodies.com/news/html-iframe-sandbox/">HTML iFrame Sandbox | Securing Your Web Site | HTML Goodies</a></li>
<li><a href="https://datasette.io/">Datasette : An open source multi-tool for exploring and publishing data</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, so there is no discussion to summarize.

**Tags**: `#datasette`, `#data-tools`, `#javascript`, `#plugins`, `#web-development`

---

<a id="item-6"></a>
## [Researchers Link Massive 'Popa' Botnet to Israeli Publicly-Traded Firm](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/) ⭐️ 8.0/10

Multiple security research firms have concluded that the Popa Android botnet, which has operated for four years forcing millions of consumer TV boxes into a proxy network, is linked to the residential proxy provider NetNut, operated by the publicly-traded Israeli firm Alarum Technologies Ltd (NASDAQ: ALAR). This finding establishes a direct link between a major, large-scale cybercrime operation and a publicly-traded corporation, raising serious questions about corporate governance, accountability, and the ethical boundaries of the proxy/VPN industry. The Popa botnet hijacked Android-based consumer TV boxes to relay internet traffic for advertising fraud, account takeovers, and mass data scraping, leveraging the devices as part of a residential proxy network.

rss · Krebs on Security · Jun 18, 17:37

**Background**: A botnet is a network of internet-connected devices that have been infected with malware and are controlled by an attacker, often without the owner's knowledge. Residential proxy providers like NetNut offer IP addresses from real consumer devices, making internet traffic appear to originate from regular households, which is valued for tasks like web scraping and ad verification but can also be abused. Alarum Technologies is a publicly-traded company on the NASDAQ that operates in the internet access and data collection solutions sector.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NetNut-Proxy-Network/NetNut">GitHub - NetNut-Proxy-Network/NetNut: Premium Static & Rotating IPs | HTTP(s) Residential Proxy Network | Information & Code samples. · GitHub</a></li>
<li><a href="https://finance.yahoo.com/quote/ALAR/">Alarum Technologies Ltd . (ALAR) Stock Price... - Yahoo Finance</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#botnet`, `#corporate-governance`, `#cybercrime`, `#proxy-networks`

---

<a id="item-7"></a>
## [US Government Reveals Rapid Expansion of 3,611 AI Use Cases](https://www.schneier.com/blog/archives/2026/06/ai-use-by-the-us-government.html) ⭐️ 8.0/10

The Trump administration's Office of Management and Budget disclosed 3,611 active or planned AI use cases across the US federal government, a 70% increase from the Biden administration's final year inventory. This massive scale of AI adoption for government functions, including high-stakes areas like nuclear safety and individual freedoms, raises profound ethical and safety concerns about automated decision-making without adequate oversight. The list of use cases was disclosed by the Office of Management and Budget on April 14 and was published on GitHub, covering sensitive functions that transfer decision processes from humans to machines.

rss · Schneier on Security · Jun 17, 11:04

**Background**: An AI use case inventory is a public catalog required by executive order that lists how a government agency plans to use artificial intelligence. The rapid 70% growth indicates accelerating adoption across federal operations. Bruce Schneier is a well-known security technologist and commentator who frequently analyzes technology policy and risks.

**Tags**: `#AI governance`, `#government technology`, `#policy`, `#automation ethics`, `#Bruce Schneier`

---

<a id="item-8"></a>
## [Stem cell therapy achieves 15-year remission for severe autoimmune disease](https://www.nature.com/articles/d41586-026-01925-7) ⭐️ 8.0/10

A pioneering autologous hematopoietic stem cell transplantation (AHSCT) therapy has achieved long-term remission for 15 years in two patients with neuromyelitis optica spectrum disorder (NMOSD), a severe autoimmune condition that damages the spinal cord and optic nerve. This long-term success demonstrates the potential of stem cell therapy to provide a durable, possibly curative treatment for severe, treatment-refractory autoimmune diseases, shifting the paradigm from lifelong management to sustained remission. The therapy used autologous hematopoietic stem cell transplantation, where the patient's own stem cells are used, and the results were published in the high-impact journal Nature, underscoring the scientific significance of this long-term outcome.

rss · Nature · Jun 19, 00:00

**Background**: Neuromyelitis optica spectrum disorder (NMOSD) is a rare but severe autoimmune disease of the central nervous system that primarily attacks the optic nerves and spinal cord, often leading to blindness and paralysis. Autologous hematopoietic stem cell transplantation (AHSCT) is an intensive procedure where the patient's immune system is suppressed and then rebuilt using their own harvested stem cells, which has been explored for autoimmune diseases refractory to conventional treatments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41582-024-01050-x">Autologous haematopoietic stem cell transplantation for treatment of multiple sclerosis and neuromyelitis optica spectrum disorder — recommendations from ECTRIMS and the EBMT | Nature Reviews Neurology</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autologous_hematopoietic_stem_cell_transplantation">Autologous hematopoietic stem cell transplantation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neuromyelitis_optica_spectrum_disorder">Neuromyelitis optica spectrum disorder - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#stem_cells`, `#autoimmune_disease`, `#regenerative_medicine`, `#clinical_trial`, `#neurology`

---

<a id="item-9"></a>
## [Embryonic organizer cells direct body plans across animal phyla](https://www.nature.com/articles/d41586-026-01910-0) ⭐️ 8.0/10

Research demonstrates that embryonic 'organizer cells' can instruct embryos from diverse animal phyla on what kind of body to build, suggesting a conserved mechanism for body plan formation. This finding sheds light on the evolution of animal body structures by showing that a fundamental patterning signal may be shared across a vast evolutionary distance, potentially unifying our understanding of developmental biology. The ability of these organizer cells to function across different phyla indicates that the core signaling pathways for axis formation and tissue specification are highly conserved, though the specific downstream responses may vary.

rss · Nature · Jun 18, 00:00

**Background**: The concept of an 'organizer' in embryonic development dates back to the 1924 discovery of the Spemann-Mangold organizer in amphibians, which showed that a specific group of cells could induce the formation of a secondary body axis. These organizer cells are crucial for directing the development of the central nervous system and other structures in vertebrates. Understanding how this organizing principle evolved is key to understanding the diversity of animal body plans.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Spemann-Mangold_organizer">Spemann-Mangold organizer</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8628936/">The Organizer and Its Signaling in Embryonic Development - PMC</a></li>
<li><a href="https://www.science.org/content/article/elusive-master-organizer-human-embryo-growth-seen-first-time">Elusive master organizer of human embryo growth seen for the first time | Science | AAAS</a></li>

</ul>
</details>

**Tags**: `#developmental biology`, `#evolution`, `#embryology`, `#cell biology`, `#comparative biology`

---

<a id="item-10"></a>
## [Ubiquiti Launches Enterprise NAS Appliance Built on ZFS](https://blog.ui.com/article/introducing-enterprise-nas) ⭐️ 7.0/10

Ubiquiti has introduced a new enterprise-grade Network Attached Storage appliance built on the ZFS file system, featuring dual 25GbE SFP28 ports and redundant power supplies. This move is significant as Ubiquiti, known for disrupting networking with cost-effective hardware, enters the enterprise storage market with a model emphasizing no recurring subscription fees, potentially challenging established players. The appliance is priced at $3999 and includes high-performance networking interfaces, but community members have questioned whether the underlying HDD-based storage can fully saturate the 25GbE links.

hackernews · ksec · Jun 18, 14:24 · [Discussion](https://news.ycombinator.com/item?id=48585866)

**Background**: ZFS is an advanced, enterprise-grade file system and logical volume manager that provides features like data integrity verification, snapshots, and copy-on-write clones. 25GbE is a high-speed Ethernet standard offering 2.5 times the bandwidth of 10GbE, commonly used in data centers and enterprise environments. Enterprise NAS appliances are dedicated storage devices designed for reliability, performance, and scalability in business settings.

<details><summary>References</summary>
<ul>
<li><a href="https://pve.proxmox.com/wiki/ZFS_on_Linux">ZFS on Linux - Proxmox VE</a></li>
<li><a href="https://en.wikipedia.org/wiki/25_Gigabit_Ethernet">25 Gigabit Ethernet - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchstorage/feature/Enterprise-NAS-Vital-features-and-purchase-considerations">9 enterprise NAS features and purchase considerations | TechTarget</a></li>

</ul>
</details>

**Discussion**: Community discussion is active and mixed: supporters praise the use of superior ZFS technology and Ubiquiti's no-subscription model, while critics raise concerns about Ubiquiti's past software security incidents and question whether the hardware can deliver on the promised network performance.

**Tags**: `#ZFS`, `#NAS`, `#Ubiquiti`, `#enterprise-storage`, `#networking-hardware`

---

<a id="item-11"></a>
## [Cornell's Advanced Compilers Course Available as Free Self-Guided Online Resource](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 7.0/10

Cornell University has made its CS 6120 Advanced Compilers course available as a free, self-guided online resource, covering topics such as Static Single Assignment (SSA) form, compiler optimizations, and Just-In-Time (JIT) compilation. This provides global learners with free access to advanced, university-level compiler education, potentially impacting the broader computer science education ecosystem and lowering barriers to entry for specialized knowledge. The course materials are hosted on the official Cornell CS 6120 course page and have been featured repeatedly in technical communities, sparking discussion about its content and scope, particularly regarding the 'advanced' label.

hackernews · ibobev · Jun 18, 11:04 · [Discussion](https://news.ycombinator.com/item?id=48583606)

**Background**: CS 6120 is a graduate-level course at Cornell focusing on advanced compiler techniques. SSA (Static Single Assignment) form is a key intermediate representation in modern compilers that simplifies optimization by ensuring each variable is assigned only once. JIT (Just-In-Time) compilation is a technique that compiles code during program execution to improve performance, often used in virtual machines.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Static_single-assignment_form">Static single-assignment form - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Just-in-time_compilation">Just -in- time compilation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community discussion highlights a divide in perspective: one view questions what makes the course 'advanced,' arguing that many core topics like dead code elimination and SSA are introductory. Another point critiques the course's focus on trace compilation as an obsolete technique, suggesting more relevant concepts like type feedback and deoptimization. Comparisons to other resources, such as Nora Sandler's compiler book, also appear.

**Tags**: `#compilers`, `#education`, `#open-source`, `#computer-science`, `#optimization`

---

<a id="item-12"></a>
## [Hospitals and universities repurpose drugs to slash costs by up to 90%.](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 7.0/10

Hospitals and universities are systematically repurposing existing, approved drugs for new conditions, such as using the cancer drug Avastin to treat macular degeneration at a fraction of the cost of the purpose-built Lucentis. This practice directly challenges high pharmaceutical pricing models by providing effective, low-cost alternatives for conditions with expensive dedicated treatments, potentially improving global public health access and forcing a re-evaluation of drug development economics. A key example is Avastin (bevacizumab) and Lucentis (ranibizumab), which are molecularly similar but differ in packaging and price by approximately 30-fold ($50 vs $1500 per dose); however, such repurposing often relies on off-label use and faces regulatory and manufacturing hurdles for broader adoption.

hackernews · giuliomagnifico · Jun 18, 10:33 · [Discussion](https://news.ycombinator.com/item?id=48583386)

**Background**: Drug repurposing involves investigating existing, approved medications for new therapeutic uses, which is significantly faster and cheaper than developing new drugs from scratch. Off-label use, where physicians prescribe a drug for an unapproved indication based on medical literature, is a common pathway for repurposing, but it operates in a complex regulatory landscape without formal FDA approval for the new use.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nih.gov/news-events/nih-research-matters/repurposing-drugs-treat-age-related-macular-degeneration">Repurposing drugs to treat age-related macular degeneration | National Institutes of Health (NIH)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Off-label_use">Off-label use - Wikipedia</a></li>
<li><a href="https://www.fda.gov/patients/learn-about-expanded-access-and-other-treatment-options/understanding-unapproved-use-approved-drugs-label">Understanding Unapproved Use of Approved Drugs "Off Label" | FDA</a></li>

</ul>
</details>

**Discussion**: The community discussion validates the Avastin/Lucentis case as emblematic, with commenters sharing personal experiences with repurposed drugs (e.g., Spravato vs. ketamine) and citing nonprofits like Cures Within Reach that fund such research for rare diseases; a major concern raised is the lack of a clear regulatory pathway for extending drug uses without manufacturer consent, which limits formal adoption despite proven efficacy.

**Tags**: `#healthcare`, `#drug_repurposing`, `#healthcare_economics`, `#pharmaceutical_industry`, `#public_health`

---

<a id="item-13"></a>
## [Charity Majors: AI Has Inverted Code Economics](https://simonwillison.net/2026/Jun/17/charity-majors/#atom-everything) ⭐️ 7.0/10

Industry expert Charity Majors argues that in 2025, AI fundamentally inverted the economics of code production, making lines of code disposable and effectively free to generate. This shift implies that the value and focus in software engineering must move from code creation to higher-level concerns like system design, observability, and rigorous engineering discipline. The core argument is that while code became cheap and disposable, the need for engineering discipline to manage complex, AI-generated systems actually increased, not decreased.

rss · Simon Willison · Jun 17, 17:12

**Background**: Traditionally, writing code was a time-intensive and costly process, making each line valuable. The advent of powerful generative AI models for coding has drastically reduced this cost, prompting a reevaluation of software engineering practices and the role of the developer.

**Tags**: `#ai-assisted-programming`, `#software-engineering`, `#economics`, `#generative-ai`, `#commentary`

---

<a id="item-14"></a>
## [Software Freedom Conservancy Releases LLM-Backed Generative AI Usage Guidelines for FOSS](https://lwn.net/Articles/1078521/) ⭐️ 7.0/10

The Software Freedom Conservancy (SFC) has released community-developed recommendations for responsibly using large language model (LLM)-backed generative AI systems in free and open-source software (FOSS) contributions. The guidelines were created by the SFC and community volunteers to address the ethical and practical dilemmas these tools pose. These guidelines provide practical best practices for FOSS contributors navigating the complex integration of proprietary AI tools with free software principles, potentially influencing future contribution workflows and licensing norms in the open-source ecosystem. They help minimize the damage from using proprietary AI systems, whether contributors choose to use them or not. The recommendations are presented as best practices, not strict requirements or legal definitions, and SFC plans to refine them continuously while providing supporting materials like tutorials and podcasts. They acknowledge the variety of perspectives FOSS developers have towards LLMs, including voluntary use and employer-mandated use.

rss · LWN.net · Jun 18, 16:00

**Background**: The Software Freedom Conservancy is a non-profit organization dedicated to promoting, developing, and defending free, libre, and open-source software projects by providing them with organizational and legal support. Large language models (LLMs) and generative AI tools, like those powering code assistants, are trained on vast datasets that often include open-source code, raising significant questions about licensing compliance, code originality, and the ethical boundaries of using proprietary systems within the FOSS ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/open-source-llms">What are Open Source Large Language Models? | IBM</a></li>
<li><a href="https://www.techtarget.com/searchenterpriseai/tip/Examining-the-future-of-AI-and-open-source-software">Does AI-generated code violate open source licenses? | TechTarget</a></li>

</ul>
</details>

**Tags**: `#FOSS`, `#AI ethics`, `#LLM`, `#software licensing`, `#open source`

---

<a id="item-15"></a>
## [Linux 7.2 merge window halfway mark shows 7,000+ changesets merged](https://lwn.net/Articles/1078068/) ⭐️ 7.0/10

The first half of the Linux 7.2 merge window, which began after the 7.1 kernel release on June 14, has seen over 7,000 non-merge changesets pulled into the mainline kernel. This summary gives kernel developers and systems programmers a clear overview of the substantial changes being integrated for the next major release, helping them track upstream development and prepare for compatibility testing. The merge window is ongoing, with most core subsystem changes already merged, meaning the scope of the final 7.2 release is becoming clear. The count refers specifically to non-merge changesets, which represent direct code contributions rather than merge commits that integrate existing work.

rss · LWN.net · Jun 18, 13:47

**Background**: In Linux kernel development, a merge window is a two-week period after a stable release (like 7.1) during which new features and changes from subsystem maintainers are merged into Linus Torvalds' mainline repository. A changeset is a unit of change in the version control system; a non-merge changeset is a primary code change, distinct from a merge commit that combines other work.

<details><summary>References</summary>
<ul>
<li><a href="https://lwn.net/Articles/625735/">Kernel development [LWN.net]</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linux_kernel">Linux kernel - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#linux kernel`, `#systems programming`, `#open source`, `#kernel development`

---

<a id="item-16"></a>
## [RMR and BRMR propose efficient Linux block replication via RDMA](https://lwn.net/Articles/1074291/) ⭐️ 7.0/10

Two new Linux kernel modules, RMR (Reliable Multicast over RTRS) and BRMR (Block device over RMR), were presented at the 2026 Linux Storage, Filesystem, Memory Management and BPF Summit. They build on the existing RTRS RDMA transport library to enable single-hop, active-active block replication for durable virtual block devices. This approach could provide cloud infrastructure providers with a highly efficient and low-overhead method to create durable, fault-tolerant virtual block devices. It addresses a core infrastructure challenge by leveraging RDMA's high-throughput, low-latency capabilities directly at the block storage layer. The modules are in a development stage, and the developers are actively seeking feedback and discussion from the Linux kernel community before submitting them for upstream inclusion. RMR provides active-active block-level replication over RDMA, while BRMR exposes it as a standard Linux block device like /dev/brmrX.

rss · LWN.net · Jun 18, 13:25

**Background**: Remote Direct Memory Access (RDMA) is a technology that allows one computer to directly access the memory of another without involving the operating system, enabling very high-speed data transfers with low latency. The kernel's RDMA Transport Library (RTRS) already provides a messaging layer built on top of RDMA. Cloud providers need durable virtual block devices, which must reliably store data and survive hardware failures, often using replication across multiple nodes.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ionos-cloud/RMR">GitHub - ionos-cloud/ RMR : Reliable multicast over RTRS ( RMR ) and...</a></li>
<li><a href="https://noise.getoto.net/2026/06/18/single-hop-block-replication-with-rmr-and-brmr/">[$] Single-hop block replication with RMR and BRMR | Noise</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#storage`, `#rdma`, `#cloud-infrastructure`, `#distributed-systems`

---

<a id="item-17"></a>
## [Malware Embeds Forbidden Text to Trick AI Security Scanners](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html) ⭐️ 7.0/10

A spyware developer has been embedding text related to nuclear and biological weapons inside JavaScript code comments, which is specifically designed to trigger safety filters in AI analysis tools and disrupt automated malware detection. This technique represents a novel adversarial tactic that weaponizes the safety guardrails of AI models against security analysis, potentially creating a new cat-and-mouse game that forces security firms to develop more robust and context-aware AI scanners. The forbidden text is placed inside a large JavaScript block comment that does not affect code execution, meaning the malware remains fully functional while the comment attempts to derail AI scanners by causing refusal, confusion, or premature classification before the actual malicious payload is analyzed.

rss · Schneier on Security · Jun 18, 11:04

**Background**: Automated malware analysis often uses AI models to scan suspicious code for malicious patterns. Adversarial attacks involve crafting inputs specifically designed to fool or confuse these AI systems. ROT-style ciphers are simple substitution encryption methods where letters are shifted a fixed number of positions in the alphabet.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ROT13">ROT13 - Wikipedia</a></li>
<li><a href="https://www.aitoolgo.com/learning/detail/bypassing-content-moderation-filters-techniques">Bypassing AI Content Moderation: Techniques and Challenges | AIToolGo</a></li>
<li><a href="https://mr7.ai/blog/machine-learning-for-malware-detection-techniques-tools-mmooyc0t">Machine Learning for Malware Detection: Techniques... | mr7.ai Blog</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#adversarial-ai`, `#malware`, `#ai-analysis`

---

<a id="item-18"></a>
## [Depolymerizable Resin Enables Easy Reuse of 3D Printing Photopolymers](https://hackaday.com/2026/06/18/easily-reuse-3d-printing-photopolymers-with-depolymerizable-resin/) ⭐️ 7.0/10

A new depolymerizable resin for 3D printing has been developed, allowing the typically irreversible photopolymerization process to be reversed, enabling the reuse of cured materials. Companies like 3Dresyn are already selling additives and resins that make this possible. This innovation addresses the significant environmental waste and material cost problems in resin-based 3D printing by creating a circular material lifecycle. It could drastically reduce the environmental footprint of the additive manufacturing industry and lower operational costs for users. The key mechanism involves designing the resin's chemistry to be depolymerizable, meaning the polymer network can be broken down back into its starting monomers under specific conditions, unlike traditional thermoset resins. This approach is related to research on reversible photopolymerization and vitrimers, which are a class of materials with dynamic bonds that allow for reprocessing.

rss · Hackaday · Jun 19, 02:00

**Background**: Standard photopolymer resins used in SLA and DLP 3D printers cure (harden) irreversibly when exposed to ultraviolet light, forming a rigid, cross-linked thermoset polymer. This process is one-way, meaning cured resin cannot be melted and reshaped like thermoplastics, leading to waste. The development of depolymerizable resins and materials like vitrimers, which feature dynamic chemical bonds, represents a new frontier in creating reprocessable and sustainable thermosets.

<details><summary>References</summary>
<ul>
<li><a href="https://hackaday.com/2026/06/18/easily-reuse-3d-printing-photopolymers-with-depolymerizable-resin/">Easily Reuse 3D Printing Photopolymers With Depolymerizable Resin</a></li>
<li><a href="https://pubs.rsc.org/en/content/articlehtml/2024/gc/d3gc04215d">Design of depolymerizable polymers toward a circular economy...</a></li>
<li><a href="https://pubs.acs.org/doi/10.1021/acs.iecr.4c03705">Vitrimers for 3D Printing Technology: Current Status and Future Perspectives | Industrial & Engineering Chemistry Research</a></li>

</ul>
</details>

**Tags**: `#3D Printing`, `#Materials Science`, `#Sustainability`, `#Photopolymers`, `#Recycling`

---

<a id="item-19"></a>
## [AI tool use found to degrade professional skills in key sectors.](https://www.nature.com/articles/d41586-026-01947-1) ⭐️ 7.0/10

New studies published in Nature show that reliance on AI tools leads to a degradation of core professional abilities in physicians and software engineers. This finding is significant because it presents early empirical evidence of a potential downside to AI integration, challenging the assumption that these tools only enhance productivity without cost, and it has broad implications for workforce training and the future of work. The studies specifically measured skill degradation in two high-stakes professional domains: medicine and software engineering, which are fields where precise judgment and fundamental expertise are critical.

rss · Nature · Jun 18, 00:00

**Background**: The rapid integration of AI assistants into professional workflows has been widely promoted as a way to increase efficiency and reduce errors. However, concerns have grown that over-reliance on such tools might lead to 'de-skilling,' where professionals gradually lose the ability to perform core tasks independently. This concept is analogous to how heavy reliance on GPS navigation can impair a person's innate sense of direction.

**Tags**: `#AI ethics`, `#skill degradation`, `#workforce impact`, `#software engineering`, `#medical AI`

---

<a id="item-20"></a>
## [Human Genome's 3D Structure Challenges AI Modeling](https://www.quantamagazine.org/why-the-human-genomes-tangled-physicality-may-confound-ai-20260618/) ⭐️ 7.0/10

A new article argues that the complex, tangled physical structure of the human genome presents fundamental obstacles for artificial intelligence systems attempting to model and predict genomic behavior. This highlights a critical gap in applying AI to genomics and biology, suggesting that current models may be insufficient for capturing the genome's full complexity, which could affect the development of precision medicine and our fundamental understanding of biology. The genome's 3D organization, including structures like topologically associating domains (TADs) and chromatin loops, dynamically regulates critical processes such as gene expression, but this physical architecture is highly variable and context-dependent, making it difficult for AI to learn universal rules.

rss · Quanta Magazine · Jun 18, 14:12

**Background**: The human genome is not a simple linear code but is organized into a complex 3D structure within the cell nucleus. This architecture is studied using techniques like Hi-C, a form of chromatin conformation capture, which maps interactions between different genomic regions. A key organizational unit is the Topologically Associating Domain (TAD), a self-interacting region where DNA sequences interact frequently with each other, bounded by proteins like CTCF and cohesin, and crucial for proper gene regulation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41580-021-00362-w">Understanding 3D genome organization by multidisciplinary methods | Nature Reviews Molecular Cell Biology</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6312108/">Organizational Principles of 3D Genome Architecture - PMC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Topologically_associating_domain">Topologically associating domain</a></li>

</ul>
</details>

**Tags**: `#genomics`, `#AI`, `#computational-biology`, `#systems-biology`, `#complexity`

---

<a id="item-21"></a>
## [Show HN: Are You in the Weights?](https://www.intheweights.com/) ⭐️ 6.0/10

A website that tests how well various LLMs recognize personal names by querying them in parallel and clustering responses.

hackernews · turtlesoup · Jun 18, 20:49 · [Discussion](https://news.ycombinator.com/item?id=48591348)

**Tags**: `#LLM`, `#privacy`, `#web-tools`, `#AI-experimentation`, `#Hacker-News`

---

<a id="item-22"></a>
## [WAI-ARIA 1.3 Introduces ariaNotify() for Programmatic Screen Reader Announcements](https://css-tricks.com/the-siren-song-of-arianotify/) ⭐️ 6.0/10

The WAI-ARIA 1.3 specification defines a new `ariaNotify()` method on DOM elements that allows developers to programmatically queue a text string for announcement by a screen reader. This provides a focused, imperative API for web developers to directly trigger assistive technology narration, offering a more reliable and intentional tool for enhancing web accessibility beyond declarative ARIA attributes. The `ariaNotify()` method is designed as a write-only API intentionally, meaning developers cannot determine from a return value if the notification was delivered, a design choice to prevent potential fingerprinting abuse.

rss · CSS-Tricks · Jun 17, 15:32

**Background**: WAI-ARIA (Web Accessibility Initiative – Accessible Rich Internet Applications) is a technical specification that defines ways to make web content and web applications more accessible to people with disabilities. It works by providing semantic roles, states, and properties that assistive technologies, like screen readers, can use to interpret and interact with user interface elements. A screen reader is a form of assistive technology that converts text and elements on a screen into speech or braille output for users with visual impairments.

<details><summary>References</summary>
<ul>
<li><a href="https://w3c.github.io/aria/">Accessible Rich Internet Applications (WAI-ARIA) 1.3</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaNotify">Element: ariaNotify () method - Web APIs | MDN</a></li>
<li><a href="https://azukiazusa.dev/en/blog/aria-notify-method/">Imperatively Notify Assistive Technologies with the ` ariaNotify ...</a></li>

</ul>
</details>

**Tags**: `#accessibility`, `#ARIA`, `#web-development`, `#front-end`

---

<a id="item-23"></a>
## [Windows NT Successfully Ported to Run on Nintendo GameCube Hardware](https://hackaday.com/2026/06/18/running-windows-nt-on-the-nintendo-gamecube/) ⭐️ 6.0/10

A hobbyist project has achieved the port of Windows NT, a 1990s-era workstation operating system, to run on the Nintendo GameCube console, a gaming device not designed for general-purpose computing. This project is a notable technical feat of retro computing and hardware hacking, demonstrating the flexibility of Windows NT's Hardware Abstraction Layer (HAL) and the versatility of the GameCube's PowerPC-based hardware for tasks far beyond its original intent. The success hinges on creating a custom HAL for the GameCube's unique 'Broadway' processor (a derivative of IBM's PowerPC 750) and its specific memory and I/O architecture, which differs significantly from the standard PCs Windows NT was built for.

rss · Hackaday · Jun 19, 05:00

**Background**: Windows NT is a family of operating systems from Microsoft first released in 1993, known for its portability across different CPU architectures via its Hardware Abstraction Layer (HAL). The Nintendo GameCube, released in 2001, uses a custom IBM 'Gekko' (later 'Broadway' in the Wii) PowerPC-based CPU. Porting an OS requires writing low-level drivers to make the OS communicate with the console's specific hardware, a complex reverse-engineering task.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HAL_(software)">HAL (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Broadway_(processor)">Broadway (processor) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gekko_(processor)">Gekko (processor) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#retro computing`, `#OS porting`, `#hardware hacking`, `#Nintendo`, `#Windows NT`

---

<a id="item-24"></a>
## [Brexit tore apart European science — now the research rifts are healing](https://www.nature.com/articles/d41586-026-01841-w) ⭐️ 6.0/10

UK research funding from the EU is increasing after Brexit, but the scientific networks that were disrupted are still difficult to restore.

rss · Nature · Jun 18, 00:00

**Tags**: `#research policy`, `#international collaboration`, `#science funding`, `#Brexit impact`

---

<a id="item-25"></a>
## [New Proof Shows How Many Sloppy Shuffles Randomize a Deck of Cards](https://www.quantamagazine.org/seven-perfect-shuffles-randomize-a-deck-of-cards-but-how-many-sloppy-ones-20260617/) ⭐️ 6.0/10

A new mathematical proof extends a decades-old result by showing how many imperfect (sloppy) riffle shuffles are needed to fully randomize a standard 52-card deck, removing the previous requirement for a precise, perfect cut. This proof provides a more realistic model for card shuffling in practical settings, bridging the gap between theoretical mathematics and real-world card games or casino procedures, and it advances our understanding of randomization processes. The proof builds on the known result that seven perfect riffle shuffles are sufficient for randomization, but now accounts for the natural imprecision in human shuffling by using a metric called total variation distance to measure how close the deck is to being truly random.

rss · Quanta Magazine · Jun 17, 14:35

**Background**: The Gilbert-Shannon-Reeds model describes a perfect riffle shuffle, where the deck is split exactly in half and interleaved perfectly, and a 1992 proof by Persi Diaconis and others showed that seven such shuffles are enough to randomize a 52-card deck. Total variation distance is a mathematical measure used to compare how different two probability distributions are, with a value of zero indicating they are identical and one indicating they are completely different.

<details><summary>References</summary>
<ul>
<li><a href="https://www.quantamagazine.org/seven-perfect-shuffles-randomize-a-deck-of-cards-but-how-many-sloppy-ones-20260617/">Seven Perfect Shuffles Randomize a Deck of Cards. But How Many Sloppy Ones? | Quanta Magazine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gilbert–Shannon–Reeds_model">Gilbert–Shannon–Reeds model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shuffling">Shuffling - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#probability`, `#combinatorics`, `#research`

---