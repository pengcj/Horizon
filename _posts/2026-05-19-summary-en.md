---
layout: default
title: "Horizon Summary: 2026-05-19 (EN)"
date: 2026-05-19
lang: en
---

> From 58 items, 20 important content pieces were selected

---

1. [Pioneering computer scientist and RISKS Digest editor Peter G. Neumann has died.](#item-1) ⭐️ 9.0/10
2. [CISA Contractor Accidentally Leaks AWS GovCloud Keys on GitHub](#item-2) ⭐️ 9.0/10
3. [YellowKey zero-day exploit bypasses Windows 11 BitLocker encryption with physical access.](#item-3) ⭐️ 9.0/10
4. [China Accelerates AI Brain Implants Toward Real-World Medical Use](#item-4) ⭐️ 8.0/10
5. [Simon Willison summarizes six months of LLM progress in a 5-minute talk.](#item-5) ⭐️ 7.0/10
6. [Anthropic Acquires Developer Tools Startup Stainless in Talent-Focused Deal](#item-6) ⭐️ 7.0/10
7. [Using Git's --author Flag to Block AI Spam Pull Requests](#item-7) ⭐️ 7.0/10
8. [UK Government Digital Service criticizes NHS's retreat from open source](#item-8) ⭐️ 7.0/10
9. [Linux Summit Explores Major Swap Subsystem Performance and SSD-Friendly Improvements](#item-9) ⭐️ 7.0/10
10. [Ebola Bundibugyo drug trials set to launch amid Congo-Uganda outbreak](#item-10) ⭐️ 7.0/10
11. [Files.md launched as open-source, self-hosted note-taking alternative to Obsidian](#item-11) ⭐️ 6.0/10
12. [Andon Labs lets four AI agents run their own live radio stations.](#item-12) ⭐️ 6.0/10
13. [Jury Rules Elon Musk Filed OpenAI Lawsuit Too Late](#item-13) ⭐️ 6.0/10
14. [Multiple Linux distributions issue security updates for various software](#item-14) ⭐️ 6.0/10
15. [Cross-Document View Transitions: Practical Pitfalls Revealed](#item-15) ⭐️ 6.0/10
16. [DIY Long-Range Night Vision Using a 3D-Printed Telescope and IR Laser](#item-16) ⭐️ 6.0/10
17. [Creating Breathable Porous Steel via 3D Printing and Foaming Agents](#item-17) ⭐️ 6.0/10
18. [DIY Enthusiast Upgrades Small Engine with Teensy-Based EFI System](#item-18) ⭐️ 6.0/10
19. [The Enhanced Games miss the point: science can clean up sport](#item-19) ⭐️ 6.0/10
20. [Quanta Magazine Explores the Meaning of Gödel's Incompleteness Theorems](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Pioneering computer scientist and RISKS Digest editor Peter G. Neumann has died.](https://lwn.net/Articles/1073186/) ⭐️ 9.0/10

Peter G. Neumann, a foundational figure in system security and the longtime editor of the RISKS Digest forum, has passed away. The news was announced by LWN.net, which also linked to a New York Times obituary. His passing marks the loss of a seminal voice who for decades shaped professional discourse on computer risks and security, influencing generations of researchers and practitioners in cybersecurity and systems engineering. The primary announcement was made via LWN.net, citing an email received, and the New York Times subsequently published a formal obituary. Neumann's career spanned decades at SRI International, where he conducted critical research in reliable and secure computing.

rss · LWN.net · May 17, 19:36

**Background**: Peter G. Neumann was a principal scientist at SRI International's Computer Science Laboratory and a leading authority on computer system security and reliability. He was the longtime moderator of the RISKS Digest, an online forum established in 1985 by the ACM Committee on Computers and Public Policy that has served as a critical public archive of discussions about the risks of computer technology to society.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISKS_Digest">RISKS Digest - Wikipedia</a></li>
<li><a href="https://catless.ncl.ac.uk/Risks/">RISKS-LIST: RISKS-FORUM Digest - catless.ncl.ac.uk</a></li>
<li><a href="https://everything.explained.today/comp.risks/">RISKS Digest explained</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#computer-science`, `#obituary`, `#risks-digest`, `#system-security`

---

<a id="item-2"></a>
## [CISA Contractor Accidentally Leaks AWS GovCloud Keys on GitHub](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) ⭐️ 9.0/10

A contractor for the U.S. Cybersecurity & Infrastructure Security Agency (CISA) inadvertently exposed highly privileged AWS GovCloud account credentials and extensive internal system details in a public GitHub repository until the past weekend. This incident represents a severe security breach for a premier U.S. government cybersecurity agency, potentially compromising critical government systems and highlighting catastrophic failures in credential management practices within organizations entrusted with national security. The exposed archive included files detailing CISA's internal software build, test, and deployment processes, and security experts have described it as one of the most egregious government data leaks in recent history.

rss · Krebs on Security · May 18, 20:48

**Background**: AWS GovCloud (US) is a specialized Amazon Web Services cloud region designed to host sensitive government workloads and meet strict U.S. compliance requirements like FedRAMP. CISA is the operational lead for federal cybersecurity, responsible for protecting the nation's critical infrastructure, making such a leak of its own privileged credentials particularly alarming.

<details><summary>References</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/">CISA Admin Leaked AWS GovCloud Keys on Github</a></li>
<li><a href="https://aws.amazon.com/govcloud-us/">AWS GovCloud (US) - Amazon Web Services</a></li>
<li><a href="https://gizmodo.com/the-worst-leak-that-ive-witnessed-u-s-cybersecurity-agency-leaves-its-digital-keys-out-in-public-on-github-2000760330">‘The Worst Leak That I’ve Witnessed’: U.S. Cybersecurity ...</a></li>

</ul>
</details>

**Discussion**: No specific community comments were provided in the search results, but based on the source (Krebs on Security) and the incident's severity, expert discussion would likely focus on the profound irony and operational security failure, the need for automated secret scanning in government pipelines, and accountability for the contractor and agency.

**Tags**: `#security`, `#AWS`, `#credential-leak`, `#government`, `#CISA`

---

<a id="item-3"></a>
## [YellowKey zero-day exploit bypasses Windows 11 BitLocker encryption with physical access.](https://www.schneier.com/blog/archives/2026/05/zero-day-exploit-against-windows-bitlocker.html) ⭐️ 9.0/10

A zero-day exploit named YellowKey, published by researcher Nightmare-Eclipse, can reliably bypass default Windows 11 BitLocker full-volume encryption protections by booting into the Windows Recovery Environment. This is significant because BitLocker is a mandatory security feature for many organizations, including government contractors, and this exploit undermines its core promise of protecting data on lost or stolen devices. The exploit requires physical access and involves placing a specially crafted 'FsTx' folder on a USB drive or EFI partition to trigger vulnerable recovery behavior and gain an unrestricted shell to the encrypted volume.

rss · Schneier on Security · May 18, 11:08

**Background**: BitLocker is Microsoft's full-volume encryption feature designed to protect data by encrypting entire disk volumes, commonly using a Trusted Platform Module (TPM) chip to securely store the encryption key. The Windows Recovery Environment (WinRE) is a separate, minimal operating system environment used for troubleshooting and repairing Windows installations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BitLocker">BitLocker - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Trusted_Platform_Module">Trusted Platform Module - Wikipedia</a></li>
<li><a href="https://www.threatlocker.com/blog/what-yellowkey-and-greenplasma-zero-day-exploits-reveal-about-trusting-native-windows-security">What YellowKey and GreenPlasma zero-day exploits reveal about trusting native Windows security | ThreatLocker Blog</a></li>

</ul>
</details>

**Discussion**: Security researcher Will Dormann independently confirmed the exploit's behavior, and cybersecurity leaders are being advised to implement immediate mitigation measures for laptops and tablets.

**Tags**: `#cybersecurity`, `#encryption`, `#vulnerability`, `#Windows`, `#BitLocker`

---

<a id="item-4"></a>
## [China Accelerates AI Brain Implants Toward Real-World Medical Use](https://www.nature.com/articles/d41586-026-01468-x) ⭐️ 8.0/10

Chinese start-up firms are intensifying efforts to develop algorithms for brain-computer interfaces that restore motor and speech functions, moving the technology from clinical trials toward practical applications. This transition marks a significant step forward in brain-computer interface technology, potentially offering transformative medical solutions for patients with neurological disorders such as paralysis or stroke. The focus is on AI-powered neural implants that interpret brain signals to control external devices or restore communication, though challenges like long-term stability and scalability in real-world settings remain.

rss · Nature · May 19, 00:00

**Background**: Brain-computer interfaces (BCIs) are systems that establish a direct communication pathway between the brain and external devices, often using electrodes to record neural activity. AI algorithms are crucial for decoding complex brain signals into actionable commands, such as movement or speech, a field that has seen rapid advancements from lab-based trials to early human applications.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12721853/">Brain Implants in the Age of Artificial Intelligence - PMC - NIH</a></li>
<li><a href="https://www.mdpi.com/2306-5354/12/8/820">Brain-Computer Interfaces for Stroke Motor Rehabilitation</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2666634024000862">Rehabilitation with brain-computer interface and upper limb motor function in ischemic stroke: A randomized controlled trial - ScienceDirect</a></li>

</ul>
</details>

**Tags**: `#brain-computer-interfaces`, `#AI-healthcare`, `#neuroscience`, `#medical-technology`

---

<a id="item-5"></a>
## [Simon Willison summarizes six months of LLM progress in a 5-minute talk.](https://simonwillison.net/2026/May/19/5-minute-llms/#atom-everything) ⭐️ 7.0/10

Simon Willison presented a lightning talk at PyCon US 2026 summarizing LLM developments from late 2025 to mid-2026, highlighting a competitive period where the 'best' model changed hands five times between Anthropic, OpenAI, and Google. This summary provides a valuable high-level overview of rapid industry shifts and intense competition among leading AI labs, helping developers and observers gauge the pace of progress and model capabilities over a short period. Willison uses his recurring 'pelican riding a bicycle' SVG generation test to illustrate qualitative differences between models, and he pinpoints November 2025 as a critical inflection point, especially for coding capabilities.

rss · Simon Willison · May 19, 01:09 · [Discussion](https://news.ycombinator.com/item?id=48188183)

**Background**: A large language model (LLM) is an AI model trained on vast amounts of text data to generate human-like responses. Companies like Anthropic, OpenAI, and Google (DeepMind) develop competing LLMs (e.g., Claude, GPT, Gemini), and their performance on benchmarks and real-world tasks is a major focus in the tech industry. PyCon US is the largest annual conference for the Python programming community, where such technical summaries are common.

**Discussion**: The community discussion is mixed, with some users like [tptacek] agreeing on a significant inflection point, particularly for security research, while others like [Insanity] question whether the perceived progress is real or just marketing, noting that models still struggle with complex 'vibe coding' tasks. A user named [throwaway2027] shares a personal timeline of model experiences from December 2025 to May 2026.

**Tags**: `#LLM`, `#PyCon`, `#AI trends`, `#industry summary`, `#annotated presentation`

---

<a id="item-6"></a>
## [Anthropic Acquires Developer Tools Startup Stainless in Talent-Focused Deal](https://www.anthropic.com/news/anthropic-acquires-stainless) ⭐️ 7.0/10

AI lab Anthropic has acquired the developer tools company Stainless, primarily as an acqui-hire to bolster its Claude Platform's API and SDK capabilities, while announcing the wind-down of all Stainless hosted products. This move signals Anthropic's strategic investment in improving the developer experience for its AI platform, which is critical for adoption and competition in the fast-evolving AI industry. Stainless was responsible for generating all official Anthropic SDKs, and its technology is used by hundreds of companies, but its standalone hosted services, including the SDK generator, will be discontinued as part of the acquisition.

hackernews · tomeraberbach · May 18, 17:01 · [Discussion](https://news.ycombinator.com/item?id=48182281)

**Background**: Stainless is a startup founded in 2022 that automates the creation and maintenance of software development kits (SDKs), which are tools that allow developers to interact with an API. An acqui-hire is a common business strategy where a company acquires another primarily to recruit its talented employees, often resulting in the acquired company's products being discontinued.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/anthropic-acquires-stainless">Anthropic acquires Stainless \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/">Anthropic has acquired the dev tools startup used by OpenAI ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Acqui-hiring">Acqui-hiring - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights a mix of sentiments, including congratulations for the Stainless team but significant concern and frustration from developers who relied on its tools about their abrupt discontinuation, viewing it as a negative precedent for developer tooling reliability. Other comments debate the strategic rationale of acqui-hires and Anthropic's broader business positioning.

**Tags**: `#AI`, `#acquisition`, `#developer-tools`, `#API`, `#business-strategy`

---

<a id="item-7"></a>
## [Using Git's --author Flag to Block AI Spam Pull Requests](https://archestra.ai/blog/only-responsible-ai) ⭐️ 7.0/10

A technical blog post describes a method using Git's `--author` flag to automatically reject AI-generated spam pull requests in GitHub repositories, providing a specific workaround for maintainers. This technique addresses the growing problem of low-quality, AI-generated code submissions that overwhelm open-source maintainers, while also exposing tensions between repository activity metrics and project health. The method leverages Git's ability to filter commits by author, but community comments highlight that it may have security implications because contributors with merged commits can bypass certain approval requirements. GitHub itself is also exploring platform-level controls and AI filters to manage the deluge of spam PRs.

hackernews · ildari · May 18, 15:24 · [Discussion](https://news.ycombinator.com/item?id=48181125)

**Background**: Open-source repositories, especially popular ones, are increasingly receiving automated pull requests generated by AI tools that often contain low-quality or irrelevant code. GitHub activity metrics, such as the number of PRs and issues, are sometimes used by investors or stakeholders to gauge project health, which can create perverse incentives. Maintainers have been seeking better tools to filter spam while keeping genuine contributions open.

<details><summary>References</summary>
<ul>
<li><a href="https://labex.io/tutorials/git-how-to-use-git-author-flag-correctly-419252">How to use Git author flag correctly | LabEx</a></li>
<li><a href="https://pupuweb.com/how-can-open-source-maintainers-stop-ai-generated-pull-request-spam-on-github-without-shutting-down-contributions/">How can open source maintainers stop AI-generated pull request spam on GitHub without shutting down contributions? - PUPUWEB</a></li>
<li><a href="https://www.infoworld.com/article/4127156/github-eyes-restrictions-on-pull-requests-to-rein-in-ai-based-code-deluge-on-maintainers.html">GitHub eyes restrictions on pull requests to rein in AI-based code deluge on maintainers | InfoWorld</a></li>

</ul>
</details>

**Discussion**: The community discussion is highly critical of the situation, with many commenters blaming both GitHub for inadequate platform controls and the broader hype around AI code generation. Key concerns include the security risks of merged contributors gaining higher privileges and the absurdity of venture capital metrics pressuring open-source projects to accept spam. Some suggest GitHub should implement basic requirements for opening PRs or temporarily block accounts with high rejection rates.

**Tags**: `#open-source`, `#AI spam`, `#GitHub`, `#software engineering`, `#security`

---

<a id="item-8"></a>
## [UK Government Digital Service criticizes NHS's retreat from open source](https://simonwillison.net/2026/May/17/gds-weighs-in/#atom-everything) ⭐️ 7.0/10

The UK's Government Digital Service (GDS) has published official guidance titled 'AI, open code and vulnerability risk in the public sector,' which publicly advocates for an 'open by default' principle in response to the NHS's decision to make its open source repositories private. This marks a rare public policy disagreement between two major UK government bodies, highlighting a fundamental tension between security-by-obscurity and transparency as a security virtue in public sector software development. The GDS guidance states that making code private 'adds additional delivery and policy costs, and can reduce reuse and scrutiny,' recommending that closure be used 'sparingly and deliberately.' The NHS's decision was triggered by vulnerability reports from Project Glasswing, an initiative using Anthropic's powerful AI model to proactively find flaws in critical open source software.

rss · Simon Willison · May 17, 15:59

**Background**: Project Glasswing is an initiative that provides maintainers of critical open source codebases access to advanced AI models to proactively identify and fix security vulnerabilities at scale. The 'open by default' principle, widely adopted in open government and data initiatives, posits that government data and code should be publicly accessible unless there is a compelling reason not to disclose it. The NHS had hundreds of open source projects on GitHub covering various tools and applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_by_default">Open by default - Wikipedia</a></li>
<li><a href="https://cipherssecurity.com/nhs-github-repositories-private-ai-security-anthropic-mythos/">NHS England Orders GitHub Repos Private Over AI Vulnerability ...</a></li>

</ul>
</details>

**Discussion**: The article interprets the GDS's public statement as a major escalation in civil service discourse, comparing it to an internal meeting 'without biscuits'—a signal of a frosty, significant disagreement. The commentary suggests this public intervention is unusually confrontational for the typically polite and consensus-driven UK civil service culture.

**Tags**: `#open-source`, `#public-sector`, `#healthcare-IT`, `#policy`, `#security`

---

<a id="item-9"></a>
## [Linux Summit Explores Major Swap Subsystem Performance and SSD-Friendly Improvements](https://lwn.net/Articles/1072657/) ⭐️ 7.0/10

At the 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit, three dedicated sessions focused on revamping the Linux kernel's swap subsystem for better performance, maintainability, and friendliness to solid-state drives. These improvements are significant because the swap subsystem is critical for memory management under pressure, and optimizing it for modern SSDs can substantially reduce wear and improve overall system responsiveness and longevity. The discussions specifically targeted the long-unloved swap code, addressing two main tracks: one on performance and maintainability, and another shared with storage on SSD-friendly swapping techniques.

rss · LWN.net · May 18, 13:16

**Background**: The Linux swap subsystem manages anonymous pages, which are memory pages not backed by a file (like program stacks and heaps), by moving them to secondary storage when physical memory is scarce. Historically, this subsystem has been optimized for traditional hard drives, but the widespread adoption of solid-state drives (SSDs) with different performance characteristics, such as wear from write amplification, creates a need for new approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://lwn.net/Articles/1016136/">Three ways to rework the swap subsystem [LWN.net]</a></li>
<li><a href="https://docs.kernel.org/admin-guide/mm/concepts.html">Concepts overview — The Linux Kernel documentation</a></li>

</ul>
</details>

**Discussion**: The article does not include direct community comments, but the topic's prominence at a major summit indicates significant developer interest in addressing long-standing swap subsystem limitations.

**Tags**: `#linux-kernel`, `#memory-management`, `#performance-optimization`, `#storage-systems`

---

<a id="item-10"></a>
## [Ebola Bundibugyo drug trials set to launch amid Congo-Uganda outbreak](https://www.nature.com/articles/d41586-026-01607-4) ⭐️ 7.0/10

Clinical trials for treatments against the rare Ebola Bundibugyo virus are poised to launch quickly in the Democratic Republic of the Congo and Uganda, where an ongoing outbreak is only the third known to be caused by this specific strain. This rapid response is critical because there are currently no approved vaccines or therapeutics for the Bundibugyo virus, and launching trials during an outbreak is essential for developing effective countermeasures and saving lives in affected regions. The Bundibugyo virus is genetically distinct from the more common Ebola virus (Zaire ebolavirus), sharing less than 30% of its genomic sequence, which necessitates separate therapeutic development.

rss · Nature · May 18, 00:00

**Background**: The Ebola Bundibugyo virus is one of several species within the Orthoebolavirus genus that causes Ebola disease, a severe and often fatal illness in humans. The ongoing outbreak in the Democratic Republic of the Congo and Uganda represents only the third recorded outbreak of Bundibugyo virus disease, highlighting its rarity and the urgent need for specific medical countermeasures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cdc.gov/ebola/about/index.html">Ebola Disease Basics | Ebola | CDC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bundibugyo_ebolavirus">Bundibugyo ebolavirus - Wikipedia</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pfNHZhU0VSRjJGQ1EzaXZkYmZTZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en">Google News - Ebola outbreak in Congo and Uganda declared...</a></li>

</ul>
</details>

**Tags**: `#public-health`, `#clinical-trials`, `#epidemic-response`, `#infectious-disease`

---

<a id="item-11"></a>
## [Files.md launched as open-source, self-hosted note-taking alternative to Obsidian](https://github.com/zakirullin/files.md) ⭐️ 6.0/10

A new open-source, Go-based note-taking application called Files.md has been released on GitHub, offering a web-based interface that users can host on their own hardware as an alternative to Obsidian. This project addresses the growing demand for fully open-source, self-hostable productivity tools that give users complete control over their data, especially in the context of recurring debates about the licensing and openness of popular applications like Obsidian. The application is built with Go and presents a web interface, distinguishing it from native clients; however, the community notes that its feature set and workflow philosophy may differ significantly from Obsidian, so it's not a direct clone or drop-in replacement.

hackernews · zakirullin · May 18, 13:33 · [Discussion](https://news.ycombinator.com/item?id=48179677)

**Background**: Obsidian is a popular, powerful note-taking and knowledge management application that uses local Markdown files. While its core plugins and many community plugins are open-source, the main application itself is proprietary and closed-source, which has led to community interest in fully open alternatives. Tools like Joplin, also open-source, have existed for years, but developers continue to create new solutions to explore different designs and philosophies.

**Discussion**: The discussion highlights several key points: many users were surprised to realize Obsidian itself is not fully open-source, and interest is shown in various open alternatives like Files.md and others building native clients. Some commenters argue that Files.md should not be presented as a direct Obsidian alternative, as it may offer a distinct user experience and workflow rather than feature parity.

**Tags**: `#note-taking`, `#open-source`, `#Go`, `#markdown`, `#developer-tools`

---

<a id="item-12"></a>
## [Andon Labs lets four AI agents run their own live radio stations.](https://andonlabs.com/blog/andon-fm) ⭐️ 6.0/10

Andon Labs launched an experiment giving four distinct AI agents full autonomy to run a 24/7 radio broadcast, including music selection, content creation, and attempting to manage the business side like securing sponsorships. This experiment showcases the current capabilities and humorous failures of AI agents in a complex, creative, and real-time media operation, providing a public benchmark for how autonomous systems handle unpredictable tasks. The agents (using models like Claude Opus 4.7, GPT-5.5, Gemini 3.1 Pro, and Grok 4.3) were given minimal initial resources ($20 for songs) and a goal to generate profit, but early results show poor revenue and content that ranges from hilarious to glitchy and repetitive.

hackernews · lukaspetersson · May 18, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48183301)

**Background**: Autonomous AI agents are systems that can make decisions and take actions to achieve goals with minimal human oversight. Experiments like this build on previous work by Andon Labs, which has tested AI agents in managing retail businesses like vending machines and cafes to explore real-world applications and failure modes.

<details><summary>References</summary>
<ul>
<li><a href="https://andonlabs.com/blog/andon-fm">We let four AIs run radio stations. Here's what happened. | Andon Labs</a></li>
<li><a href="https://gizmodo.com/an-experiment-put-llms-in-charge-of-radio-stations-youll-never-guess-how-it-went-2000759327">An Experiment Put LLMs in Charge of Radio Stations. You'll Never Guess How It Went</a></li>
<li><a href="https://news.northeastern.edu/2026/03/09/autonomous-ai-agents-of-chaos/">These Autonomous AI Agents Quickly Became Agents of Chaos</a></li>

</ul>
</details>

**Discussion**: The community reaction on Hacker News is highly engaged and humorous, with listeners sharing amusing glitches like an AI DJ getting stuck in a loop and another discussing historical tragedies with ironic song pairings. Some commenters emphasize it's a thought-provoking experiment rather than a replacement for human stations, while others express concern about the future implications of AI in creative industries.

**Tags**: `#AI agents`, `#experiment`, `#media`, `#autonomous systems`, `#Hacker News`

---

<a id="item-13"></a>
## [Jury Rules Elon Musk Filed OpenAI Lawsuit Too Late](https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/) ⭐️ 6.0/10

A jury found that Elon Musk's lawsuit against OpenAI and Sam Altman was filed too late, resulting in a loss for Musk. The verdict was based on the timeliness of the claims rather than their merits. This outcome sets a precedent that significant business disputes in the fast-moving AI industry may become inactionable if not challenged in a timely manner. It highlights the importance of timely legal action when alleging breaches of fiduciary duty or foundational agreements. The jury's decision likely hinged on the fact that the 2019 and 2021 Microsoft deals were substantially similar to the 2023 deal Musk centered his lawsuit on, meaning he could have sued years earlier. The verdict was delivered through yes/no questions, leaving the jury's precise reasoning undisclosed.

hackernews · nycdatasci · May 18, 17:38 · [Discussion](https://news.ycombinator.com/item?id=48182754)

**Background**: Elon Musk was a co-founder of OpenAI and alleges the company, under Sam Altman's leadership, violated its founding agreement as a non-profit to benefit Microsoft. OpenAI transitioned to a 'capped-profit' model, which Musk argued betrayed its original mission. The lawsuit centered on alleged breaches of fiduciary duty and contractual obligations.

**Discussion**: Community discussion focused on the legal strategy and implications. One user noted Musk likely lost due to the statute of limitations, as similar deals occurred years prior. Others speculated the lawsuit was a strategic move to damage OpenAI's reputation and IPO prospects rather than to win, or raised concerns about the precedent of non-profits converting to for-profit entities.

**Tags**: `#OpenAI`, `#Elon Musk`, `#lawsuit`, `#AI industry`, `#legal`

---

<a id="item-14"></a>
## [Multiple Linux distributions issue security updates for various software](https://lwn.net/Articles/1073356/) ⭐️ 6.0/10

AlmaLinux, Debian, Fedora, Mageia, Slackware, and SUSE have simultaneously released security patches for a wide range of software packages including kernels, web servers like Nginx, and applications such as Firefox and Chromium. These routine updates are critical for system administrators to maintain the security and stability of servers and desktops by patching known vulnerabilities across the Linux ecosystem. The updates cover a diverse array of components, including specific Nginx modules like `nginx-mod-brotli` for compression, container runtimes like Apptainer, and in-memory data stores like Valkey, indicating the broad scope of the security maintenance.

rss · LWN.net · May 18, 12:59

**Background**: Linux distributions regularly bundle security fixes from upstream software projects into updates that users can easily install. Tools like Nginx often use optional modules (e.g., ngx_brotli for Brotli compression) to extend functionality. Container runtimes such as Apptainer manage the execution environment for containerized applications, while in-memory data stores like Valkey provide high-performance caching and database services.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google/ngx_brotli">GitHub - google/ngx_brotli: NGINX module for Brotli compression</a></li>
<li><a href="https://apptainer.org/docs/user/main/environment_and_metadata.html">Environment and Metadata — Apptainer User Guide main...</a></li>
<li><a href="https://valkey.io/">Valkey</a></li>

</ul>
</details>

**Tags**: `#security`, `#linux`, `#updates`, `#sysadmin`, `#vulnerabilities`

---

<a id="item-15"></a>
## [Cross-Document View Transitions: Practical Pitfalls Revealed](https://css-tricks.com/cross-document-view-transitions-part-1/) ⭐️ 6.0/10

The article highlights specific practical issues developers encounter when implementing cross-document view transitions, including the need to stop using a deprecated opt-in method and the existence of a little-known 4-second timeout that can break transitions. This guidance is crucial for front-end developers building multi-page applications (MPAs) to avoid common implementation bugs and ensure smooth, reliable user navigation experiences using the modern View Transition API. Key pitfalls include the deprecated use of a specific meta tag for opting into transitions and an inbound transition timeout that, if exceeded before the new page's 'pagereveal' event, causes the transition to be skipped.

rss · CSS-Tricks · May 18, 13:47

**Background**: The View Transition API allows developers to create smooth animated transitions between different views, either within a single-page application (SPA) or across different documents in a multi-page application (MPA). Cross-document view transitions, which are for MPAs, are triggered automatically during same-origin navigation if both the old and new pages opt in. This API is relatively new, with cross-document support becoming available in browsers like Chrome starting from version 126.

<details><summary>References</summary>
<ul>
<li><a href="https://css-tricks.com/cross-document-view-transitions-part-1/">Cross-Document View Transitions: The Gotchas Nobody Mentions</a></li>
<li><a href="https://developer.chrome.com/docs/web-platform/view-transitions/cross-document">Cross-document view transitions for multi-page applications</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API">View Transition API - Web APIs | MDN</a></li>

</ul>
</details>

**Tags**: `#web development`, `#CSS`, `#front-end`, `#view transitions`, `#developer tips`

---

<a id="item-16"></a>
## [DIY Long-Range Night Vision Using a 3D-Printed Telescope and IR Laser](https://hackaday.com/2026/05/18/long-range-night-vision-with-an-infrared-laser/) ⭐️ 6.0/10

A maker project has successfully combined a 3D-printed telescope with an infrared laser to create a long-range night vision device that outperforms standard consumer-grade gear. This project demonstrates an accessible and incremental innovation for the maker and optics communities, offering a practical method to enhance night vision capabilities without relying on expensive commercial systems. The approach uses near-infrared (NIR) light, which is invisible to the naked eye but detectable by modified cameras, paired with a laser for focused, long-range illumination.

rss · Hackaday · May 18, 18:30

**Background**: Consumer-grade night vision devices typically work by using a camera with its infrared-blocking filter removed, combined with an active near-infrared (NIR) illuminator to light up the scene in a spectrum invisible to the human eye. Infrared lasers offer a more focused beam compared to broad LED illuminators, which can be advantageous for long-range targeting or viewing. 3D printing has become a key enabler for such custom optics and electronics projects, allowing makers to fabricate precise housings and mounts.

<details><summary>References</summary>
<ul>
<li><a href="https://hackaday.com/2026/05/18/long-range-night-vision-with-an-infrared-laser/">Long-Range Night Vision With An Infrared Laser - Hackaday</a></li>
<li><a href="https://scienceinsights.org/what-is-night-vision-ir-light-and-how-does-it-work/">What Is Night Vision IR Light and How Does It Work?</a></li>

</ul>
</details>

**Tags**: `#night-vision`, `#infrared-laser`, `#3d-printing`, `#diy-electronics`, `#optics`

---

<a id="item-17"></a>
## [Creating Breathable Porous Steel via 3D Printing and Foaming Agents](https://hackaday.com/2026/05/18/how-to-make-steel-that-breathes/) ⭐️ 6.0/10

A novel approach combining Selective Laser Melting (SLM) additive manufacturing with a foaming agent has been demonstrated to successfully fabricate 'breathable' steel (specifically AISI 420) containing interconnected, micrometer-sized pores. This development enables the production of steel components with controlled gas permeability, which is particularly valuable for specialized applications like injection molding, where gas venting is critical for part quality and production efficiency. The breathability is achieved by creatively introducing a foaming agent during the SLM process, resulting in a structure with excellent gas permeability while maintaining the good mechanical properties of the advanced mould steel.

rss · Hackaday · May 18, 17:00

**Background**: Porous metals are materials containing voids or pores, fabricated through various techniques to achieve specific properties like controlled permeability or reduced weight. Selective Laser Melting (SLM) is a form of 3D printing that uses a laser to fuse powdered metal layer by layer, enabling complex geometries. 'Breathable' steel specifically refers to metal with a network of fine, interconnected pores that allow gases to pass through.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0264127519301303">3D printed breathable mould steel: Small micrometer-sized ...</a></li>
<li><a href="https://hackaday.com/2026/05/18/how-to-make-steel-that-breathes/">How To Make Steel That Breathes | Hackaday</a></li>

</ul>
</details>

**Tags**: `#materials-science`, `#manufacturing`, `#engineering`, `#porous-materials`, `#steel`

---

<a id="item-18"></a>
## [DIY Enthusiast Upgrades Small Engine with Teensy-Based EFI System](https://hackaday.com/2026/05/18/small-engine-gets-diy-efi-upgrade/) ⭐️ 6.0/10

A hobbyist named Carlos Takeshita successfully replaced a small engine's carburetor with a custom-built electronic fuel injection system controlled by a Teensy 4.0 microcontroller. This project demonstrates how powerful, accessible microcontrollers like the Teensy can be used to modernize legacy mechanical systems, potentially improving fuel efficiency and performance for small engines used in various applications. The Teensy 4.0 microcontroller, featuring a 600 MHz ARM Cortex-M7 processor, provides the computational power needed for real-time fuel and air mixture control. The project is a niche DIY effort, and improper installation of such custom EFI systems can cause an engine to run poorly or not at all.

rss · Hackaday · May 18, 15:30

**Background**: Small engines, such as those in lawnmowers or generators, traditionally use carburetors—a simple mechanical device that mixes air and fuel. Electronic Fuel Injection (EFI) is a more advanced system used in most modern vehicles, which uses sensors, a computer (ECU), and fuel injectors to precisely control the fuel delivery, often leading to better efficiency and lower emissions. Converting small engines to EFI is a known enthusiast pursuit, with both commercial kits and DIY solutions existing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sparkfun.com/teensy-4-0.html">Teensy 4.0 for Sale - SparkFun Electronics</a></li>
<li><a href="https://itstillruns.com/diy-fuel-injection-ecu-controller-2277150.html">How to build a simple DIY fuel injection ECU controller</a></li>
<li><a href="https://ecotrons.com/small_engine_fuel_injection_kit/">Small Engine Fuel Injection Kit - Small Engine EFI conversion kit</a></li>

</ul>
</details>

**Tags**: `#DIY Electronics`, `#Embedded Systems`, `#Automotive`, `#Microcontrollers`

---

<a id="item-19"></a>
## [The Enhanced Games miss the point: science can clean up sport](https://www.nature.com/articles/d41586-026-01574-w) ⭐️ 6.0/10

An opinion piece arguing that the Enhanced Games, which permit performance-enhancing substances, endanger athlete health and integrity, and that anti-doping science must evolve to address such challenges.

rss · Nature · May 18, 00:00

**Tags**: `#sports science`, `#ethics`, `#anti-doping`, `#public health`

---

<a id="item-20"></a>
## [Quanta Magazine Explores the Meaning of Gödel's Incompleteness Theorems](https://www.quantamagazine.org/what-do-godels-incompleteness-theorems-truly-mean-20260518/) ⭐️ 6.0/10

Quanta Magazine published a new explanatory article by columnist Natalie Wolchover that revisits Gödel's Incompleteness Theorems and their profound implications for the possibility of a complete mathematical 'theory of everything.' This high-quality popular science article helps a broader audience understand a foundational result in mathematical logic that limits formal systems and has deep implications for computer science, artificial intelligence, and the philosophy of mathematics. The article is a popular science explainer rather than a report on new technical developments, making it a valuable resource for non-experts but not novel for specialists in mathematical logic.

rss · Quanta Magazine · May 18, 15:14

**Background**: Kurt Gödel published his incompleteness theorems in 1931, which are two fundamental results in mathematical logic. The first theorem states that in any consistent formal system powerful enough to express basic arithmetic, there are true statements that cannot be proven within the system. The second theorem states that such a system cannot prove its own consistency. These theorems demonstrate inherent limitations in formal axiomatic systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems">Gödel ' s incompleteness theorems - Wikipedia</a></li>
<li><a href="https://plato.stanford.edu/entries/goedel-incompleteness/">Gödel ’ s Incompleteness Theorems (Stanford Encyclopedia of...)</a></li>

</ul>
</details>

**Tags**: `#mathematical logic`, `#foundations of mathematics`, `#philosophy of mathematics`, `#theoretical computer science`, `#Gödel`

---