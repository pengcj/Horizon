---
layout: default
title: "Horizon Summary: 2026-06-20 (EN)"
date: 2026-06-20
lang: en
---

> From 64 items, 23 important content pieces were selected

---

1. [Project Valhalla delivers key Java performance features in JDK 28 after a decade of work.](#item-1) ⭐️ 8.0/10
2. [Researchers Link 'Popa' Android Botnet to Publicly-Traded Israeli Firm](#item-2) ⭐️ 8.0/10
3. [Malware Embeds Forbidden Text to Hinder AI Security Analysis](#item-3) ⭐️ 8.0/10
4. [Stem cell therapy banishes severe autoimmune disease for 15 years.](#item-4) ⭐️ 8.0/10
5. [Genome's physical complexity challenges AI modeling in biology.](#item-5) ⭐️ 8.0/10
6. [ATProto Clarifies It Has No 'Instances' Like Mastodon](#item-6) ⭐️ 7.0/10
7. [Norway Bans AI Tools for Elementary School Students](#item-7) ⭐️ 7.0/10
8. [Hyundai Acquires Full Ownership of Boston Dynamics from SoftBank](#item-8) ⭐️ 7.0/10
9. [Proposal to Enforce Real ID for All Internet Traffic Raises Privacy and Control Concerns](#item-9) ⭐️ 7.0/10
10. [Datasette Apps: New Plugin Hosts Custom HTML Apps in Sandboxed Iframes](#item-10) ⭐️ 7.0/10
11. [Systemd v261 Released with Cloud, Security, and Kernel Update Features](#item-11) ⭐️ 7.0/10
12. [BPF programs could support coroutines for suspension and resumption](#item-12) ⭐️ 7.0/10
13. [Arch Linux AUR suffers sustained supply-chain attack via orphaned packages](#item-13) ⭐️ 7.0/10
14. [Linux Kernel 7.2 Merge Window Passes Halfway Mark with Over 7,000 Changesets](#item-14) ⭐️ 7.0/10
15. [Proposed RDMA-based modules for efficient cloud block replication](#item-15) ⭐️ 7.0/10
16. [US Government Classifies Anthropic's Fable AI as Dangerous Munition](#item-16) ⭐️ 7.0/10
17. [Kent Beck argues companies hire junior engineers to develop judgment, not just complete tasks](#item-17) ⭐️ 6.0/10
18. [MCP's Core Value Seen as Authentication Gateway for AI Agents](#item-18) ⭐️ 6.0/10
19. [Midjourney Expands into Medical Imaging with Sensor-Embedded Bathtub Scanner](#item-19) ⭐️ 6.0/10
20. [SFC releases LLM-backed generative AI recommendations for FOSS contributions.](#item-20) ⭐️ 6.0/10
21. [Mastodon 4.6 Introduces Curated Collections and New User Tools](#item-21) ⭐️ 6.0/10
22. [Historic Computers Benchmarked by Counting to a Million](#item-22) ⭐️ 6.0/10
23. [Preliminary data links obesity drugs to potential male fertility benefits.](#item-23) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Project Valhalla delivers key Java performance features in JDK 28 after a decade of work.](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 8.0/10

Project Valhalla, a long-running initiative to optimize Java's performance and memory layout, is set to deliver its core features, such as value types, in the upcoming JDK 28 release. This is significant because it directly addresses Java's historical performance gaps in memory efficiency and data-oriented programming, potentially making Java more competitive for performance-critical applications and modern workloads. A key technical feature is the introduction of 'value types' (inline classes), which allow objects to be stored without object headers and be flattened in arrays, drastically reducing memory overhead and improving CPU cache utilization.

hackernews · philonoist · Jun 19, 06:35 · [Discussion](https://news.ycombinator.com/item?id=48595511)

**Background**: Project Valhalla is an experimental OpenJDK project announced in 2014 to overhaul Java's data model by bridging the performance gap between Java's object-oriented abstractions and the efficient, flat memory layouts used by languages like C. It aims to introduce value types—immutable, identity-free objects that can be operated on directly like primitives—to reduce garbage collection pressure and improve memory locality.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language) - Wikipedia</a></li>
<li><a href="https://openjdk.org/jeps/401">JEP 401 : Value Classes and Objects (Preview)</a></li>
<li><a href="https://dev.to/adaumircosta/understanding-value-types-project-valhalla-faf">Understanding Value Types ( Project Valhalla ) - DEV Community</a></li>

</ul>
</details>

**Discussion**: The community discussion shows strong developer interest but also contains technical debates and critiques. Some commenters argue against the notion that null-safety is mentally taxing, while others question the technical accuracy of specific memory layout examples. A common sentiment acknowledges Java's significant modernization and continued evolution, with some viewing the long development time as a necessary catch-up from periods of neglect.

**Tags**: `#java`, `#jvm`, `#performance`, `#programming-languages`, `#software-engineering`

---

<a id="item-2"></a>
## [Researchers Link 'Popa' Android Botnet to Publicly-Traded Israeli Firm](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/) ⭐️ 8.0/10

Security researchers have concluded that the long-running Popa Android botnet, which has forced millions of consumer devices to relay malicious traffic, is linked to the residential proxy service NetNut, operated by publicly-traded Israeli firm Alarum Technologies. This discovery exposes a direct link between a major cybersecurity threat and a legitimate, publicly-traded technology company, raising serious questions about corporate accountability and the oversight of the residential proxy industry. The Popa botnet has been active for at least four years, utilizing compromised Android TV boxes to facilitate advertising fraud, account takeovers, and mass data scraping. NetNut, the implicated proxy service, claims to offer access to a large pool of over 10 million residential IP addresses worldwide.

rss · Krebs on Security · Jun 18, 17:37

**Background**: A botnet is a network of internet-connected devices infected with malware and controlled remotely by attackers without the owners' knowledge. Residential proxy services operate by routing a user's internet traffic through IP addresses assigned by Internet Service Providers to real households, making the traffic appear more legitimate and harder to block than traffic from data centers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.malwarebytes.com/blog/news/2025/03/android-botnet-badbox-largely-disrupted">Android botnet BadBox largely disrupted | Malwarebytes</a></li>
<li><a href="https://www.rescana.com/post/kimwolf-botnet-massive-android-tv-box-and-iot-malware-threat-exploiting-global-networks">Kimwolf Botnet: Massive Android TV Box and IoT Malware Threat Exploiting Global Networks – Rescana</a></li>
<li><a href="https://github.com/NetNut-Proxy-Network/NetNut">NetNut-Proxy-Network/NetNut: Premium Static & Rotating IPs | HTTP(s) Residential Proxy Network | Information & Code samples. · GitHub</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#botnet`, `#fraud`, `#corporate-accountability`, `#privacy`

---

<a id="item-3"></a>
## [Malware Embeds Forbidden Text to Hinder AI Security Analysis](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html) ⭐️ 8.0/10

A malware developer is embedding text about nuclear and biological weapons within spyware code comments to trigger refusal behaviors in AI-powered security analysis tools, effectively evading automated scanning. The real malicious payload, which uses ROT-style substitution obfuscation, is placed after this misleading header. This tactic represents a novel adversarial technique in the cybersecurity arms race, exploiting safety filters and content policies of AI analysis models to create blind spots for malware detection. It highlights how AI security tools themselves can become attack vectors if their decision logic is manipulated by carefully crafted inputs. The forbidden text is inserted inside a JavaScript block comment, so it does not affect code execution but is designed to derail AI scanners that analyze file headers, potentially causing context pollution, premature classification, or refusal to analyze further. The actual malware is obfuscated using a ROT-style substitution cipher, a common technique for hiding payloads.

rss · Schneier on Security · Jun 18, 11:04

**Background**: Adversarial machine learning involves crafting inputs to manipulate AI models, with evasion attacks being a common method to bypass detection systems like spam filters or malware scanners. ROT substitution ciphers, such as ROT13, are simple letter-shifting techniques frequently used by malware authors to obfuscate malicious code and evade signature-based detection. AI-powered security scanners analyze code or files to identify threats, but their effectiveness can be compromised if the input data is intentionally crafted to exploit their safety mechanisms or analysis pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Adversarial_machine_learning">Adversarial machine learning - Wikipedia</a></li>
<li><a href="https://www.infosecinstitute.com/resources/malware-analysis/simple-malware-obfuscation-techniques/">Simple malware obfuscation techniques | Infosec</a></li>
<li><a href="https://dev.to/manja316/i-found-a-way-to-bypass-ai-model-security-scanners-here-is-what-i-learned-44nb">I Found a Way to Bypass AI Model Security Scanners — Here is What I Learned - DEV Community</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#adversarial-ai`, `#malware`, `#ai-safety`, `#information-warfare`

---

<a id="item-4"></a>
## [Stem cell therapy banishes severe autoimmune disease for 15 years.](https://www.nature.com/articles/d41586-026-01925-7) ⭐️ 8.0/10

The first two patients treated with an autologous hematopoietic stem cell transplantation (AHSCT) for neuromyelitis optica spectrum disorder (NMOSD) have remained disease-free for 15 years, demonstrating unprecedented long-term efficacy. This long-term success suggests AHSCT could be a curative therapy for severe, relapsing autoimmune conditions, potentially sparing patients from lifelong immunosuppression and offering a profound quality-of-life improvement. The therapy, AHSCT, involves harvesting a patient's own stem cells, using chemotherapy to reboot the immune system, and then reinfusing the stem cells; NMOSD is a rare, debilitating autoimmune disease that attacks the optic nerves and spinal cord.

rss · Nature · Jun 19, 00:00

**Background**: Neuromyelitis optica spectrum disorder (NMOSD) is a severe autoimmune condition causing inflammatory attacks on the central nervous system, leading to vision loss and paralysis. Autologous hematopoietic stem cell transplantation (AHSCT) is an established procedure used primarily for blood cancers, which has been increasingly explored as a treatment for severe, refractory autoimmune diseases by aiming to reset the patient's faulty immune system.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Autologous_hematopoietic_stem_cell_transplantation">Autologous hematopoietic stem cell transplantation</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7091487/">Autologous hematopoietic stem cell transplantation in autoimmune ...</a></li>
<li><a href="https://starmedicstemcell.com/nmosd-neuromyelitis-optica/">NMOSD ( Neuromyelitis optica ) disease - symptoms, causes...</a></li>

</ul>
</details>

**Tags**: `#stem cells`, `#autoimmune disease`, `#medical breakthrough`, `#long-term treatment`, `#biotech`

---

<a id="item-5"></a>
## [Genome's physical complexity challenges AI modeling in biology.](https://www.quantamagazine.org/why-the-human-genomes-tangled-physicality-may-confound-ai-20260618/) ⭐️ 8.0/10

A new article argues that the human genome's tangled physical interactions and 3D structure make it fundamentally resistant to being modeled as a simple blueprint or algorithm by artificial intelligence, challenging common metaphors used in computational biology. This perspective is significant because it highlights a major gap between computational models and the physical reality of biology, suggesting that current AI approaches may be insufficient for truly understanding complex biological systems like gene regulation. The article emphasizes that the genome's non-linear interactions, such as those revealed by chromatin conformation capture techniques like Hi-C, create a dynamic and context-dependent physical landscape that algorithms struggle to capture, moving beyond a static 'book of life' analogy.

rss · Quanta Magazine · Jun 18, 14:12

**Background**: The human genome is often described using metaphors like a 'blueprint' or 'code,' but this oversimplifies its reality. Its function is deeply tied to its 3D spatial organization within the cell nucleus, which involves complex folding and interactions between distant DNA segments. Technologies like Hi-C map these chromatin conformations, revealing how physical proximity affects gene expression. Epigenetic regulation, such as chemical modifications to DNA and histones, further adds layers of complexity by altering gene activity without changing the underlying DNA sequence.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41576-018-0060-8">Organizational principles of 3D genome architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hi-C_(genomic_analysis_technique)">Hi-C (genomic analysis technique) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Epigenetic_regulation">Epigenetic regulation</a></li>

</ul>
</details>

**Tags**: `#AI limitations`, `#genomics`, `#computational biology`, `#systems biology`, `#science communication`

---

<a id="item-6"></a>
## [ATProto Clarifies It Has No 'Instances' Like Mastodon](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 7.0/10

An article explains that Bluesky's AT Protocol does not use 'instances' in the Mastodon/ActivityPub sense, clarifying that its architecture consists of separate Relays, App Views, and Personal Data Servers (PDS). This clarification addresses a widespread misconception in the decentralized social networking community and helps developers and users better understand the fundamental architectural differences between ATProto and ActivityPub-based systems. In ATProto, Personal Data Servers (PDS) host user data, Relays aggregate data from many PDSes into a 'firehose,' and App Views consume that firehose to provide application-specific features, each scaling independently.

hackernews · danabramov · Jun 19, 15:10 · [Discussion](https://news.ycombinator.com/item?id=48599515)

**Background**: The AT Protocol (ATProto) is the underlying protocol for the social network Bluesky, developed as a decentralized alternative to platforms like Twitter. ActivityPub is the protocol powering Mastodon and the 'Fediverse,' which is based on interconnected, independently operated servers often called 'instances'.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.com/guides/overview">Protocol Overview - AT Protocol</a></li>
<li><a href="https://atproto.wiki/wiki/Relay">Relay - ATProto Wiki</a></li>

</ul>
</details>

**Discussion**: The community discussion features debate over the article's analogies; some commenters argue the comparison to RSS is flawed because App Views depend heavily on Relays, while others praise the architectural separation as a beautiful system design solution. A key critique is that the article dismisses defederation without explaining how ATProto solves the moderation and community-finding problems that instances address.

**Tags**: `#ATProto`, `#decentralized-protocols`, `#Bluesky`, `#ActivityPub`, `#distributed-systems`

---

<a id="item-7"></a>
## [Norway Bans AI Tools for Elementary School Students](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/) ⭐️ 7.0/10

The Norwegian government has implemented a near-ban on the use of AI tools for elementary school students aged 6 to 13, while allowing cautious adoption for lower secondary students aged 14 to 16 under teacher supervision. This policy decision is significant as it addresses the growing debate on the appropriate age for integrating AI in education, setting a precedent for child development and technology ethics by prioritizing foundational literacy skills for younger children. The ban applies broadly to generative AI tools, aiming to prevent children from skipping essential learning processes like reading and writing, though enforcement may pose challenges for educators, as indicated by concerns about increased workload.

hackernews · ilreb · Jun 19, 16:03 · [Discussion](https://news.ycombinator.com/item?id=48600093)

**Background**: Generative AI, such as large language models, can produce human-like text and images, raising concerns in education that students might rely on it to bypass critical thinking and foundational skill development. Norway's decision reflects broader global discussions on AI regulation in schools, similar to historical debates over calculator use in mathematics education.

**Discussion**: Community comments largely support the ban, with users comparing it to not giving calculators before children understand arithmetic and noting that generative AI is sneakier because it produces finished-looking work that can mask learning gaps. However, some express confusion about implementation and raise concerns that AI has created an 'echo chamber' in education, with teachers and students both using AI, which could undermine learning outcomes.

**Tags**: `#AI regulation`, `#education policy`, `#child development`, `#technology ethics`, `#Hacker News`

---

<a id="item-8"></a>
## [Hyundai Acquires Full Ownership of Boston Dynamics from SoftBank](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/) ⭐️ 7.0/10

Hyundai Motor Group has purchased SoftBank's remaining 9% stake in Boston Dynamics for $325 million, completing its acquisition of the robotics company at a total valuation of $1.1 billion. This acquisition gives Hyundai full control of a world-leading robotics firm, potentially accelerating its automation and mobility strategies to address labor challenges and future product development. The deal stems from a put option exercised by SoftBank, following Hyundai's initial purchase of an 80% controlling stake in December 2020 for $880 million.

hackernews · ck2 · Jun 19, 16:28 · [Discussion](https://news.ycombinator.com/item?id=48600312)

**Background**: Boston Dynamics is a pioneering company known for developing highly mobile and dynamic robots like Spot and Atlas, with expertise in advanced locomotion and manipulation. SoftBank Group originally acquired Boston Dynamics from Alphabet in 2017 and has since made various investments in robotics and AI, including a recent agreement to acquire ABB's robotics business.

<details><summary>References</summary>
<ul>
<li><a href="https://bostondynamics.com/">The World’s Leading Robotics Company | Boston Dynamics</a></li>
<li><a href="https://en.wikipedia.org/wiki/SoftBank_Group">SoftBank Group - Wikipedia</a></li>
<li><a href="https://fortune.com/2026/02/12/softbank-earnings-profits-ai-boom-nvidia-openai/">'Our investments are beginning to pay off': AI boom brings SoftBank back into the black | Fortune</a></li>

</ul>
</details>

**Discussion**: The discussion expresses curiosity about Hyundai's strategy, with some questioning the commercial viability of humanoid robots for manufacturing and suggesting the acquisition might be driven by South Korea's demographic decline rather than just automotive automation. Others noted the deal was a logical completion of the initial purchase.

**Tags**: `#robotics`, `#acquisitions`, `#manufacturing automation`, `#industry news`

---

<a id="item-9"></a>
## [Proposal to Enforce Real ID for All Internet Traffic Raises Privacy and Control Concerns](https://nochan.net/b/Internet-Crap/20230829-Think-Of-The-Children/) ⭐️ 7.0/10

An article explores the proposal and implications of enforcing real identity (Real ID) requirements on all internet traffic, drawing parallels to historical digital control mechanisms and sparking significant community discussion. This topic is significant because mandatory real ID verification on the internet could fundamentally reshape online privacy, free speech, and the architecture of the web, potentially leading to pervasive surveillance and self-censorship. The discussion includes speculative defensive measures like building underground radio relay networks to circumvent controls, and draws comparisons to existing regulatory practices like KYC/AML (Know Your Customer/Anti-Money Laundering) that cause risk-averse self-censorship in platforms.

hackernews · Bender · Jun 19, 20:19 · [Discussion](https://news.ycombinator.com/item?id=48602817)

**Background**: The concept of 'Real ID' originally refers to a U.S. federal standard for driver's licenses and identification cards to enhance security. Applying this principle to internet traffic would mean linking all online activity to a verified, government-issued identity. Proposals for such digital identity systems often cite protecting children or national security as justifications, but critics warn they can enable mass surveillance and undermine online anonymity, which is seen as crucial for free expression and privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_identity">Digital identity - Wikipedia</a></li>
<li><a href="https://resources.fenergo.com/blogs/digital-identity-verification">Digital Identity Verification for KYC & AML Compliance</a></li>
<li><a href="https://www.federalregister.gov/documents/2025/01/14/2025-00484/minimum-standards-for-drivers-licenses-and-identification-cards-acceptable-by-federal-agencies-for">Minimum Standards for Driver's Licenses and Identification Cards Acceptable by Federal Agencies for Official Purposes; Phased Approach for Card-Based Enforcement</a></li>

</ul>
</details>

**Discussion**: Community comments express strong skepticism and resistance to such controls, with some proposing the creation of decentralized, underground communication networks (e.g., radio networks) as a 'final defense.' Other comments highlight how existing regulations like KYC/AML and content moderation practices already cause pervasive self-censorship and risk-averse behavior online, shifting accountability away from regulators.

**Tags**: `#internet freedom`, `#privacy`, `#digital regulation`, `#identity verification`, `#online censorship`

---

<a id="item-10"></a>
## [Datasette Apps: New Plugin Hosts Custom HTML Apps in Sandboxed Iframes](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 7.0/10

The datasette-apps plugin was launched, allowing users to host self-contained HTML and JavaScript applications within a tightly constrained iframe sandbox inside a Datasette instance, enabling interactive data exploration via read-only or configurable write SQL queries. This extends Datasette's ecosystem with a powerful extensibility mechanism, enabling developers to build custom, interactive data-driven tools and UIs that run securely alongside the core platform, potentially transforming how data is explored and manipulated. The applications run in an iframe sandboxed with attributes that prevent access to cookies or localStorage, and an injected Content Security Policy header blocks external HTTP requests, mitigating the risk of data exfiltration from malicious or buggy apps.

rss · Simon Willison · Jun 18, 23:58

**Background**: Datasette is an open-source tool for exploring and publishing data, built on SQLite, with a flexible JSON API that has long enabled custom frontend development. Iframe sandboxing is a web security feature that restricts embedded content's capabilities to prevent it from interfering with the host page or accessing sensitive resources.

<details><summary>References</summary>
<ul>
<li><a href="https://datasette.io/plugins">Datasette Plugins</a></li>
<li><a href="https://www.mbloging.com/course/html/iframe-sandboxing-html">Iframe Sandboxing in HTML for Safer Embedded Content</a></li>
<li><a href="https://javascript.plainenglish.io/demystifying-sql-query-execution-what-happens-behind-the-scenes-18111558227a">Understanding How SQL Queries Execute in a Database | JavaScript ...</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#data-tools`, `#plugin`, `#data-exploration`, `#javascript`

---

<a id="item-11"></a>
## [Systemd v261 Released with Cloud, Security, and Kernel Update Features](https://lwn.net/Articles/1078708/) ⭐️ 7.0/10

Systemd v261 has been released, introducing a new cloud Instance Metadata Service (IMDS) subsystem, 'boot secret' functionality for systems without a physical TPM, and support for the kernel's Live Update Orchestration (LUO) / Kexec Handover (KHO) systems. These features significantly enhance systemd's capabilities for cloud infrastructure, security on a wider range of hardware, and enabling more seamless, minimal-downtime kernel updates, impacting system administrators and cloud engineers. The IMDS subsystem (systemd-imdsd) provides a standardized interface for cloud instances to access metadata, the boot secret offers a software-based alternative to TPM for boot-time secrets, and the LUO/KHO support facilitates live kernel updates using a kexec-based reboot framework.

rss · LWN.net · Jun 19, 18:56

**Background**: Systemd is the init system and service manager used by most major Linux distributions, handling core system initialization and services. The Instance Metadata Service (IMDS) is a common cloud feature allowing instances to retrieve configuration and identity data from the cloud platform. TPM (Trusted Platform Module) is a hardware chip for securely storing cryptographic keys and measurements, while boot secrets are sensitive data needed early in the boot process.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/systemd-261-rc1">systemd 261-rc1 Released With OS Installer, IMDS Subsystem & New storagectl - Phoronix</a></li>
<li><a href="https://docs.kernel.org/next/core-api/liveupdate.html">Live Update Orchestrator — The Linux Kernel documentation</a></li>
<li><a href="https://lwn.net/Articles/1033364/">Kexec handover and the live update orchestrator [LWN.net]</a></li>

</ul>
</details>

**Tags**: `#systemd`, `#linux`, `#system-administration`, `#cloud-infrastructure`, `#kernel`

---

<a id="item-12"></a>
## [BPF programs could support coroutines for suspension and resumption](https://lwn.net/Articles/1076210/) ⭐️ 7.0/10

Developer Kumar Kartikeya Dwivedi is working on allowing BPF programs to be expressed as coroutines, enabling them to suspend and resume execution, which was presented at the 2026 Linux Storage, Filesystem, Memory-Management and BPF Summit. This change could significantly simplify the writing of long-running BPF tasks within the Linux kernel by removing the current requirement that programs must run to completion without blocking in their original execution context. The work is still experimental and not yet finalized, but it represents a fundamental shift from the current BPF execution model, which requires programs to always run to completion on the same CPU where they started.

rss · LWN.net · Jun 19, 15:55

**Background**: BPF (Berkeley Packet Filter) is a technology in the Linux kernel that allows users to run sandboxed programs in kernel space without changing kernel source code or loading kernel modules. Current BPF programs are validated to ensure they always run to completion and cannot block or loop indefinitely, which restricts their use for tasks that might need to wait for resources or events. Coroutines are a programming concept where execution can be suspended and later resumed, allowing a function to yield control temporarily while maintaining its state.

<details><summary>References</summary>
<ul>
<li><a href="https://noise.getoto.net/2026/06/19/suspending-and-resuming-bpf-programs/">[$] Suspending and resuming BPF programs | Noise</a></li>
<li><a href="https://ebpf.io/what-is-ebpf/">What is eBPF? An Introduction and Deep Dive into the eBPF Technology</a></li>
<li><a href="https://lwn.net/Articles/812503/">bpf: Make BPF and PREEMPT_RT co-exist - LWN.net</a></li>

</ul>
</details>

**Tags**: `#BPF`, `#Linux kernel`, `#coroutines`, `#systems programming`, `#kernel development`

---

<a id="item-13"></a>
## [Arch Linux AUR suffers sustained supply-chain attack via orphaned packages](https://lwn.net/Articles/1077619/) ⭐️ 7.0/10

The Arch User Repository (AUR) was attacked by malicious actors who created new accounts to adopt orphaned packages and push malware-laden updates, forcing maintainers into a prolonged response effort and leading to a temporary shutdown of new user registration. This incident highlights the inherent security risks in community-driven, open repositories that rely on volunteer maintainers, as it demonstrates how attackers can exploit trust and process gaps to distribute malware at scale, potentially affecting many users of a major Linux distribution. The attack was sustained, with maintainers playing 'Whac-A-Mole' for several days to respond to each newly compromised package, and it remains unclear how many users were affected or what the long-term security response will be for the AUR's collaboration model.

rss · LWN.net · Jun 19, 14:40

**Background**: The Arch User Repository (AUR) is a community-driven repository for Arch Linux that contains package build descriptions (PKGBUILDs), allowing users to compile and install software not in the official repositories. Orphaned packages are those without an active maintainer, which can be taken over by others, a process that was exploited in this attack. Supply-chain attacks target the software development and distribution process, and open-source repositories are increasingly targeted due to their open nature.

<details><summary>References</summary>
<ul>
<li><a href="https://wiki.archlinux.org/title/Arch_User_Repository">Arch User Repository - ArchWiki</a></li>
<li><a href="https://linuxbash.sh/post/handling-orphaned-packages-across-distros">Handling Orphaned Packages Across Distros - Linux Bash</a></li>
<li><a href="https://theaivibe.org/blog/supply-chain-attacks-open-source-threat">Supply Chain Attacks in Open Source : The Growing... | The AI Vibe</a></li>

</ul>
</details>

**Tags**: `#supply-chain-security`, `#linux`, `#open-source`, `#security-attack`, `#package-management`

---

<a id="item-14"></a>
## [Linux Kernel 7.2 Merge Window Passes Halfway Mark with Over 7,000 Changesets](https://lwn.net/Articles/1078068/) ⭐️ 7.0/10

The merge window for Linux kernel version 7.2, which began following the release of kernel 7.1 on June 14, has now integrated just over 7,000 non-merge changesets into the mainline codebase. This progress indicates that most major subsystem changes for the upcoming 7.2 release have been submitted, providing the community with a clearer picture of the new features and improvements to expect. The update notes that while many core subsystems have been pulled, the merge window is only halfway through, meaning additional significant changesets are still expected before it closes.

rss · LWN.net · Jun 18, 13:47

**Background**: The Linux kernel merge window is a period, typically lasting two weeks, following a major kernel release during which Linus Torvalds accepts new features and changes from subsystem maintainers. A changeset is a fundamental unit of change in version control, representing a single, logical modification to the codebase. The kernel development cycle alternates between merge windows for new features and stabilization periods for bug fixes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Changeset">Changeset - Wikipedia</a></li>
<li><a href="https://lwn.net/Articles/811086/">The 5.6 merge window opens [LWN.net]</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#operating-systems`, `#software-development`, `#open-source`

---

<a id="item-15"></a>
## [Proposed RDMA-based modules for efficient cloud block replication](https://lwn.net/Articles/1074291/) ⭐️ 7.0/10

Two new Linux kernel modules, Reliable Multicast over RTRS (RMR) and Block device over RMR (BRMR), have been proposed to provide efficient, low-overhead durable block device replication for cloud environments. The authors are seeking community feedback before upstream submission. This approach could significantly reduce the overhead for cloud providers to offer highly available and durable virtual block storage, which is critical for modern cloud infrastructure. It represents a novel kernel-level integration of RDMA for block device replication. The modules are built on top of the existing RDMA Transport Resilient Server (RTRS) kernel library and aim to achieve single-hop, active-active replication. The proposal is currently in an early stage, and the authors have presented it at the Linux Storage, Filesystem, Memory Management and BPF Summit (LSFMMBPF) to gather input.

rss · LWN.net · Jun 18, 13:25

**Background**: Remote Direct Memory Access (RDMA) allows servers to access each other's memory directly over the network with minimal CPU involvement, enabling high-performance, low-latency communication. RTRS (RDMA Transport Resilient Server) is a Linux kernel module that provides reliable messaging transport over RDMA. Cloud providers require durable virtual block devices to offer persistent storage services to their customers.

<details><summary>References</summary>
<ul>
<li><a href="https://lkml.iu.edu/2605.0/04603.html">[PATCH 01/13] RDMA/rmr: add public and ... - Linux-Kernel Archive</a></li>
<li><a href="https://www.reddit.com/r/linux/comments/1szzkfx/a_new_indevelopment_blocklevel_activeactive/">A new (in-development) block-level active-active replication solution for Linux kernel : r/linux</a></li>
<li><a href="https://lkml.iu.edu/2605.0/04605.html">[PATCH 03/13] RDMA/rmr: client: main ... - Linux-Kernel Archive</a></li>

</ul>
</details>

**Discussion**: Based on the available web search results, a Reddit thread indicates community interest in the project as a new block-level active-active replication solution for the Linux kernel. However, detailed technical discussion or criticism is not yet prominent in the provided snippets.

**Tags**: `#cloud infrastructure`, `#storage systems`, `#RDMA`, `#Linux kernel`, `#block devices`

---

<a id="item-16"></a>
## [US Government Classifies Anthropic's Fable AI as Dangerous Munition](https://www.schneier.com/blog/archives/2026/06/anthropics-fable-and-the-state-of-ai.html) ⭐️ 7.0/10

The US government classified Anthropic's new Fable generative AI model as a dangerous munition on June 12, 2026, invoking export-control authority to ban foreign nationals from accessing it, which led Anthropic to shut down the model's access for all users. This event highlights the growing tension between rapid AI capability advancement and governmental attempts at restrictive control, raising fundamental questions about the efficacy of banning specific models versus addressing the broader, unstoppable trend of AI progress. The Fable model is Anthropic's constrained version of its more powerful Mythos model, designed for complex reasoning and high-autonomy tasks. Security expert Bruce Schneier argues that targeting individual models like Fable is futile, as the real challenge lies in managing the general trend of increasing AI capabilities, which requires collective international action that is currently unattainable.

rss · Schneier on Security · Jun 19, 11:03

**Background**: Export controls are a legal tool governments use to restrict the transfer of specific technologies, like munitions or advanced chips, to foreign entities for national security reasons. Classifying advanced AI models as munitions places them in the same regulatory category as weapons, a significant escalation in the policy treatment of software. The US has previously used similar controls on AI chips to limit China's access to high-performance computing hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/06/anthropics-fable-and-the-state-of-ai.html">Anthropic's Fable and the State of AI - Schneier on Security -</a></li>
<li><a href="https://www.thewirechina.com/2025/02/05/deepseeks-lesson-america-needs-smarter-export-controls/">DeepSeek's Lesson: America Needs Smarter Export Controls</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#export controls`, `#regulation`, `#Anthropic`, `#national security`

---

<a id="item-17"></a>
## [Kent Beck argues companies hire junior engineers to develop judgment, not just complete tasks](https://newsletter.kentbeck.com/p/hey-n00b-we-didnt-hire-you-to-complete) ⭐️ 6.0/10

A newsletter article by Kent Beck posits that the primary purpose of hiring junior engineers is to cultivate their long-term engineering judgment and decision-making skills, rather than expecting them to immediately complete complex tasks. This perspective challenges the common industry view that junior developers are primarily a source of cheap labor for executing simple tasks, potentially reshaping how mentorship, hiring, and career development are structured in tech companies. The article introduces a framework categorizing junior engineers into types A, B, and C based on their learning impact, with 'B' level engineers being those who learn without causing unreasonable work for others, a standard some community members find overly simplistic or harsh.

hackernews · rrvsh · Jun 20, 00:11 · [Discussion](https://news.ycombinator.com/item?id=48604851)

**Background**: Kent Beck is a prominent software engineer known for pioneering Extreme Programming and Test-Driven Development. The debate around junior developers' roles is ongoing in the software industry, touching on issues of mentorship investment, career growth, and the economic rationale for hiring less experienced staff.

**Discussion**: The community reaction is mixed, with some agreeing that fostering judgment is a valid long-term investment, while many disagree, arguing companies hire juniors primarily to complete specific, lower-level tasks due to cost constraints. Critics also note the article's tone can come across as superior and that its classification system is overly simplistic for real-world dynamics.

**Tags**: `#software engineering`, `#career development`, `#mentorship`, `#junior developers`, `#opinion`

---

<a id="item-18"></a>
## [MCP's Core Value Seen as Authentication Gateway for AI Agents](https://simonwillison.net/2026/Jun/19/sean-lynch/#atom-everything) ⭐️ 6.0/10

A Hacker News comment by Sean Lynch argues that the primary advantage of the Model Context Protocol (MCP) is its ability to isolate authentication flows from the AI agent's context window, potentially positioning MCP as a specialized authentication gateway for APIs. This perspective highlights a critical security design benefit: by separating sensitive authentication data from the agent's operational context, MCP could significantly reduce the risk of credential leakage and misuse, which is a major concern for enterprise deployments of AI agents. The argument specifically contrasts MCP with other integration methods like 'skills' or CLI, suggesting that MCP's structured approach offers a more secure boundary for handling authentication tokens and credentials.

rss · Simon Willison · Jun 19, 22:45

**Background**: The Model Context Protocol (MCP) is an open, JSON-RPC-based standard designed to standardize how AI applications, like large language models (LLMs), access external tools, data, and resources. A key challenge in integrating AI agents with external APIs is securely managing authentication and authorization without exposing sensitive tokens within the agent's conversational context, which is often logged or processed in ways that could lead to leaks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/specification/2025-11-25">Specification - Model Context Protocol</a></li>
<li><a href="https://www.skyflow.com/post/understanding-llm-agents">Understanding AI & LLM Agents: Architecture, Security, & Deployment - Skyflow</a></li>

</ul>
</details>

**Tags**: `#model-context-protocol`, `#LLMs`, `#AI`, `#authentication`, `#API-design`

---

<a id="item-19"></a>
## [Midjourney Expands into Medical Imaging with Sensor-Embedded Bathtub Scanner](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247898354&idx=2&sn=f842f4fd953b066992ed4f5808c6c8d0) ⭐️ 6.0/10

AI image generation company Midjourney has announced a cross-industry expansion into medical health, launching a full-body scanner based on ultrasound technology that uses approximately 500,000 sensors to generate a 3D body map in 60 seconds. This move represents a significant pivot for a leading AI company from creative tools into practical health technology, potentially making advanced body composition analysis more accessible and routine for everyday use in settings like spas or homes. The scanner is described as having no radiation and no magnetic risk, utilizing ultrasound echolocation with sensors sending sound waves through the body from every angle, and it requires over two petaflops of processing power to analyze the data.

rss · 量子位 · Jun 18, 11:20

**Background**: Midjourney is widely known as an AI platform that generates images from text prompts. Traditional 3D body scanning technology often uses methods like infrared depth sensing or structured light and is employed in fitness, wellness, and healthcare for body composition analysis. The integration of such scanning into a consumer-friendly bathtub format represents a novel approach to health monitoring.

<details><summary>References</summary>
<ul>
<li><a href="https://news.aibase.com/news/29010">From Generated Images to Medical Imaging: Midjourney Launches...</a></li>
<li><a href="https://www.businesstoday.in/technology/artificial-intelligence/story/step-into-a-spa-walk-out-with-a-1-min-body-scan-midjourney-thinks-its-possible-but-will-regulators-agree-537975-2026-06-19">Step into a spa, walk out with a 1 min body scan? Midjourney thinks...</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/952011/midjourney-medical-ai-ultrasound-scan">Midjourney Medical goes from AI image generation to... | The Verge</a></li>

</ul>
</details>

**Tags**: `#AI`, `#3D_scanning`, `#health_tech`, `#Midjourney`, `#sensor_technology`

---

<a id="item-20"></a>
## [SFC releases LLM-backed generative AI recommendations for FOSS contributions.](https://lwn.net/Articles/1078521/) ⭐️ 6.0/10

The Software Freedom Conservancy (SFC), along with community volunteers, has released a set of community-developed best-practice recommendations for using LLM-backed generative AI systems when contributing to free and open-source software (FOSS). These recommendations address the growing tension between the use of proprietary AI tools and the principles of free software, aiming to help developers navigate the ethical and practical challenges to minimize potential harm to the FOSS ecosystem. The recommendations are presented as voluntary best practices rather than formal requirements, and they are intended to provide practical guidance for contributors who may use LLMs either voluntarily or due to employer mandates.

rss · LWN.net · Jun 18, 16:00

**Background**: The Software Freedom Conservancy is a US-based nonprofit that provides infrastructure and legal support to FOSS projects and advocates for users' rights to repair, improve, and reinstall software. The emergence of large language models (LLMs) capable of generating code has created new dilemmas for open-source communities, as contributions made using these systems can raise questions about licensing, code quality, and the erosion of community-driven development.

<details><summary>References</summary>
<ul>
<li><a href="https://sfconservancy.org/llm-gen-ai/llm-backed-generative-ai-recommendations.html">LLM -gen- AI - Software Freedom Conservancy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Software_Freedom_Conservancy">Software Freedom Conservancy - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#open source`, `#LLM`, `#software development`, `#policy`

---

<a id="item-21"></a>
## [Mastodon 4.6 Introduces Curated Collections and New User Tools](https://lwn.net/Articles/1078466/) ⭐️ 6.0/10

Mastodon 4.6 introduces 'Collections,' a feature for creating and sharing curated bundles of profiles to help new users discover accounts, alongside new features like email post subscriptions and a 'year in review' generator. This update enhances user onboarding and content discovery within the decentralized Fediverse ecosystem, addressing a key challenge for platforms without centralized recommendation algorithms. The Collections feature was designed with a focus on trust and safety, requiring users to agree before being added to a list to prevent abuse, and the collections are federated across compatible platforms.

rss · LWN.net · Jun 18, 13:28

**Background**: Mastodon is a leading open-source, decentralized social media platform that is part of the Fediverse, a network of interconnected servers using common protocols like ActivityPub. Profile discovery has been a long-standing challenge in the Fediverse due to its distributed nature, making features like curated lists valuable for helping users find others with similar interests. This feature is conceptually similar to 'Starter Packs' on the competing Bluesky platform.

<details><summary>References</summary>
<ul>
<li><a href="https://www.neowin.net/news/mastodon-is-getting-its-own-version-of-blueskys-starter-packs-called-collections/">Mastodon is getting its own version of Bluesky's Starter... - Neowin</a></li>
<li><a href="https://docs.joinmastodon.org/client/collections/">Implementing Collections - Mastodon documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fediverse">Fediverse - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#fediverse`, `#social-media`, `#open-source`, `#release-notes`, `#privacy`

---

<a id="item-22"></a>
## [Historic Computers Benchmarked by Counting to a Million](https://hackaday.com/2026/06/19/making-old-computers-count-to-a-million/) ⭐️ 6.0/10

The National Museum of Computing benchmarked classic computers like the WWII-era Colossus and the 1980s BBC Micro to measure how quickly they could count to one million. This experiment provides a tangible and engaging way to compare the raw processing capabilities of historically significant but vastly different machines, highlighting the evolution of computing from specialized codebreaking hardware to general-purpose personal computers. The Colossus, built in 1943-44, was not a stored-program computer but a specialized machine for codebreaking, while the BBC Micro, introduced in 1981, was a general-purpose microcomputer based on the 6502 processor that later spawned the influential ARM architecture.

rss · Hackaday · Jun 20, 05:00

**Background**: The Colossus computer was a series of machines developed by British codebreakers during WWII to help decipher encrypted German High Command messages, representing one of the first electronic digital computers. The BBC Micro was a popular home and educational computer in the UK during the 1980s, famous for its use in schools and for its modular 'Tube' interface that allowed for processor upgrades.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_computer">Colossus computer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/BBC_Micro">BBC Micro - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#retrocomputing`, `#benchmarking`, `#computing-history`, `#hardware`

---

<a id="item-23"></a>
## [Preliminary data links obesity drugs to potential male fertility benefits.](https://www.nature.com/articles/d41586-026-01963-1) ⭐️ 6.0/10

A Nature news briefing discusses preliminary research indicating that GLP-1 receptor agonist drugs, commonly used for obesity and diabetes, might boost testosterone levels and sperm parameters in men. This finding is significant because it suggests a potential repurposing of widely prescribed drugs to address male infertility, a common condition often linked to obesity, potentially offering a new therapeutic avenue. The data is described as preliminary, and the briefing also mentions a separate, two-year clinical trial of a brain–computer interface (BCI), highlighting the breadth of current biomedical research.

rss · Nature · Jun 19, 00:00

**Background**: GLP-1 receptor agonists are a class of medications that mimic the action of the natural hormone GLP-1; they work primarily by stimulating insulin production, suppressing glucagon release, and promoting a feeling of fullness, which leads to reduced food intake and weight loss. Male infertility is often associated with obesity and metabolic syndrome, so drugs that effectively treat obesity could have downstream effects on reproductive health.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLP-1_receptor_agonist">GLP-1 receptor agonist - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Brain–computer_interface">Brain–computer interface - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#biotechnology`, `#medical_research`, `#obesity_drugs`, `#brain_computer_interface`, `#fertility`

---