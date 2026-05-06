---
layout: default
title: "Horizon Summary: 2026-05-06 (EN)"
date: 2026-05-06
lang: en
---

> From 31 items, 14 important content pieces were selected

---

1. [.de TLD Outage Caused by DNSSEC Validation Failure](#item-1) ⭐️ 8.0/10
2. [Google Releases Multi-Token Prediction Drafters to Accelerate Gemma 4 Inference](#item-2) ⭐️ 8.0/10
3. [Google Chrome silently installs a 4 GB Gemini Nano AI model on devices.](#item-3) ⭐️ 8.0/10
4. [Interactive Playground for Redis's New Array Data Type](#item-4) ⭐️ 8.0/10
5. [uv 0.11.9 Released with Python 3.14.5 Garbage Collection Fix](#item-5) ⭐️ 7.0/10
6. [Cloudflare and Stripe Enable AI Agents to Autonomously Deploy Projects](#item-6) ⭐️ 7.0/10
7. [Computer Use by AI Agents Costs 45x More Than Structured APIs](#item-7) ⭐️ 7.0/10
8. [Proposal of Three Inverse Laws for Human-AI Interaction](#item-8) ⭐️ 7.0/10
9. [Airbyte Launches Unified Data Layer for AI Agents](#item-9) ⭐️ 7.0/10
10. [Telus Uses AI to Alter Call-Agent Accents for Customer Clarity](#item-10) ⭐️ 6.0/10
11. [Coinbase announces 14% workforce reduction and management restructuring.](#item-11) ⭐️ 6.0/10
12. [AI Agent Mona Manages Stockholm Cafe, Reveals Real-World Operational Flaws](#item-12) ⭐️ 6.0/10
13. [Simon Willison tests 21 quantized Granite 4.1 3B models on SVG pelican generation.](#item-13) ⭐️ 6.0/10
14. [TRE Python binding demo shows robustness against ReDoS attacks.](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [.de TLD Outage Caused by DNSSEC Validation Failure](https://dnssec-analyzer.verisignlabs.com/nic.de) ⭐️ 8.0/10

The .de country-code top-level domain experienced a widespread outage because DENIC, the registry operator, published a malformed RRSIG signature for an NSEC3 record, causing DNSSEC-validating resolvers worldwide to return SERVFAIL errors for all .de domains. This incident is significant because it demonstrates how a single cryptographic misconfiguration at a major registry can instantly disrupt internet access for an entire country's domain space, highlighting the fragility of the DNSSEC chain of trust and its critical role in modern internet infrastructure. The failure was specifically a malformed RRSIG signature over an NSEC3 record that did not validate against the Zone Signing Key (ZSK) with keytag 33834, and the intermittent nature of the outage was due to anycast routing differences among the .de nameservers.

hackernews · warpspin · May 5, 20:16 · [Discussion](https://news.ycombinator.com/item?id=48027897)

**Background**: DNSSEC (Domain Name System Security Extensions) adds cryptographic signatures to DNS records to prevent spoofing and cache poisoning. An RRSIG (Resource Record Signature) is a DNSSEC record that contains the digital signature for a set of DNS records, and validation resolvers must check this signature against the corresponding public key (ZSK or KSK) to ensure the data is authentic and untampered. DENIC eG is the non-profit cooperative responsible for managing and operating the .de top-level domain, which is one of the largest country-code TLDs in the world.

<details><summary>References</summary>
<ul>
<li><a href="https://www.akamai.com/blog/trends/dnssec-how-it-works-key-considerations">What Is DNSSEC, and How Does It Work? - Akamai</a></li>
<li><a href="https://en.wikipedia.org/wiki/DENIC">DENIC - Wikipedia</a></li>
<li><a href="https://developers.cloudflare.com/dns/dnssec/troubleshooting/">Troubleshooting DNSSEC · Cloudflare DNS docs</a></li>

</ul>
</details>

**Discussion**: The community discussion quickly identified the root cause as a DNSSEC validation failure rather than a nameserver outage, with technical users providing detailed analysis using tools like dig and DNSViz. Some comments expressed frustration or humor about the incident's timing, while others noted that major public resolvers like Cloudflare's 1.1.1.1 temporarily disabled DNSSEC validation to restore service.

**Tags**: `#dnssec`, `#dns`, `#infrastructure`, `#outage`, `#germany`

---

<a id="item-2"></a>
## [Google Releases Multi-Token Prediction Drafters to Accelerate Gemma 4 Inference](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) ⭐️ 8.0/10

Google has released Multi-Token Prediction (MTP) drafters for the Gemma 4 model family, enabling up to a 3x speedup in tokens-per-second inference speed through speculative decoding. This advancement significantly reduces latency for large language model inference, making high-performance models like Gemma 4 more practical for real-time applications and resource-constrained environments. The technique uses a smaller draft model to predict multiple tokens autoregressively, which are then verified in parallel by the larger target model, preserving output quality while cutting latency by roughly two to three times.

hackernews · amrrs · May 5, 16:14 · [Discussion](https://news.ycombinator.com/item?id=48024540)

**Background**: Speculative decoding is an inference-time optimization for autoregressive large language models where a smaller draft model proposes candidate tokens and a larger target model verifies them in a single forward pass. This approach is analogous to speculative execution in CPU design and can significantly reduce latency without degrading the quality of the main model's output.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://ai.google.dev/gemma/docs/mtp/mtp">Gemma 4 Multi-Token Prediction (MTP) using Hugging Face Transformers | Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights speculative decoding as a clever invention that achieves faster inference with zero quality degradation, with users noting Gemma models' token efficiency compared to others like Qwen. Comments also mention ongoing integration of MTP support into tools like llama.cpp and express excitement about performance improvements for local models, though some note hardware constraints like fitting models into 24GB VRAM.

**Tags**: `#LLM inference`, `#speculative decoding`, `#model optimization`, `#Gemma`, `#open source AI`

---

<a id="item-3"></a>
## [Google Chrome silently installs a 4 GB Gemini Nano AI model on devices.](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/) ⭐️ 8.0/10

Google Chrome is automatically downloading a large on-device AI model, Gemini Nano, which can be up to 4 GB in size, without explicit user consent. This download is triggered by specific browser flags and the new Prompt API for web developers. This practice raises significant concerns about user consent, software update transparency, and the control users have over their own devices and bandwidth. It also highlights the growing trend of integrating large AI models directly into browsers, which impacts privacy, system resources, and enterprise IT management. The model download is initiated when Chrome's `#optimization-guide-on-device-model` and `#prompt-api-for-gemini-nano` flags are enabled, allowing web pages to use the `LanguageModel.create()` API. The model size is approximately 2.7 GiB for CPU or 4.0 GiB for GPU, and it is a one-time download per device.

hackernews · john-doe · May 5, 07:34 · [Discussion](https://news.ycombinator.com/item?id=48019219)

**Background**: On-device AI inference refers to running machine learning models directly on a user's device (like a laptop or smartphone) rather than on a remote server, which can improve privacy and reduce latency. Gemini Nano is a smaller, efficient version of Google's Gemini AI models designed for on-device use. Browser vendors are increasingly embedding such capabilities to enable new web features, but this often involves large downloads and background processes that users may not be aware of.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.googleblog.com/en/on-device-genai-in-chrome-chromebook-plus-and-pixel-watch-with-litert-lm/">On-device GenAI in Chrome, Chromebook Plus, and Pixel Watch ...</a></li>
<li><a href="https://www.reddit.com/r/tutanota/comments/1t4a5s5/google_chrome_silently_installs_a_4_gb_gemini/">Google Chrome silently installs a 4 GB Gemini Nano AI model on your device. - Reddit</a></li>

</ul>
</details>

**Discussion**: The community is divided: some argue that downloading the model is a normal part of software updates and auto-update consent, comparing it to a spellcheck dictionary. However, many users and system administrators express strong concerns about the lack of explicit consent, the significant disk space (4 GB) and bandwidth usage, and the operational headaches it causes in managed environments like schools and labs.

**Tags**: `#privacy`, `#browser`, `#AI-model`, `#software-consent`, `#Google-Chrome`

---

<a id="item-4"></a>
## [Interactive Playground for Redis's New Array Data Type](https://simonwillison.net/2026/May/4/redis-array/#atom-everything) ⭐️ 8.0/10

Salvatore Sanfilippo submitted a pull request to add a new array data type to Redis, introducing 18 new commands like ARSET and ARGREP. Simon Willison then created an interactive browser-based playground using a WebAssembly-compiled Redis subset to test these commands. This introduces a significant new data structure to Redis, expanding its capabilities beyond traditional key-value storage, and the interactive playground allows developers to experiment with it immediately without setting up a server. The most interesting new command is ARGREP, which performs server-side grep on array values using the TRE regex library. The implementation is currently in a branch and not yet merged into the main Redis codebase.

rss · Simon Willison · May 4, 15:53

**Background**: Redis is an open-source, in-memory data structure store commonly used as a database, cache, and message broker. It traditionally supports data types like strings, lists, sets, and hashes. WebAssembly (WASM) is a binary instruction format that allows code to run in web browsers at near-native speed, enabling complex applications like Redis to operate client-side.

<details><summary>References</summary>
<ul>
<li><a href="https://redis.io/docs/latest/develop/data-types/">Redis data types | Docs</a></li>
<li><a href="https://medium.com/fluence-network/porting-redis-to-webassembly-with-clang-wasi-af99b264ca8">Porting Redis to WebAssembly with Clang/WASI | by Mikhail Voronov | Fluence Labs | Medium</a></li>
<li><a href="https://github.com/simonw/tools/pull/277">Add redis-array.html: in-browser playground for Redis Array (PR #15162) by simonw · Pull Request #277 · simonw/tools</a></li>

</ul>
</details>

**Tags**: `#Redis`, `#data structures`, `#developer tools`, `#WASM`, `#interactive playground`

---

<a id="item-5"></a>
## [uv 0.11.9 Released with Python 3.14.5 Garbage Collection Fix](https://github.com/astral-sh/uv/releases/tag/0.11.9) ⭐️ 7.0/10

The uv 0.11.9 release includes a special Python 3.14.5 release candidate (3.14.5rc1) that reverts a problematic incremental garbage collection implementation to reduce memory pressure in production environments. This is significant because the new garbage collection in Python 3.14 caused unexpected memory pressure in production, and this release allows developers to test the fix early, impacting the stability of Python applications across the ecosystem. The release was partially published manually due to a timeout when publishing to crates.io, meaning GitHub attestations are unavailable and the crate will not be fully published to crates.io. It also includes other updates like upgrading PyPy to v7.3.22 and various bug fixes for platforms like Android and Wine.

github · zanieb · May 5, 06:56

**Background**: uv is a modern, high-performance Python package manager and installer written in Rust, designed as a fast replacement for tools like pip. Python 3.14 introduced a new incremental garbage collection implementation aimed at reducing pause times, but it unexpectedly increased memory usage in production systems, leading to a decision to revert the change in versions 3.14.5 and 3.15.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.python.org/3/library/gc.html">gc — Garbage Collector interface</a></li>
<li><a href="https://doc.rust-lang.org/cargo/reference/publishing.html">Publishing on crates.io - The Cargo Book - Learn Rust</a></li>
<li><a href="https://www.datacamp.com/tutorial/python-uv">Python UV: The Ultimate Guide to the Fastest Python Package Manager - DataCamp</a></li>

</ul>
</details>

**Tags**: `#python`, `#garbage-collection`, `#release-candidate`, `#performance`, `#dependency-management`

---

<a id="item-6"></a>
## [Cloudflare and Stripe Enable AI Agents to Autonomously Deploy Projects](https://blog.cloudflare.com/agents-stripe-projects/) ⭐️ 7.0/10

Cloudflare and Stripe have integrated their services to allow AI agents to autonomously create accounts, purchase domains, and deploy projects using their respective APIs and toolkits. This integration represents a significant step in enabling fully autonomous AI agents to manage critical web infrastructure and financial transactions, potentially accelerating automated development and deployment workflows. The capability is built on Cloudflare's Agents SDK for stateful AI agents and Stripe's Agent Toolkit, which supports popular frameworks like OpenAI's Agents SDK and LangChain, though specific practical use cases remain unclear.

hackernews · rolph · May 6, 03:10 · [Discussion](https://news.ycombinator.com/item?id=48031684)

**Background**: AI agents are semi- or fully autonomous systems that can perceive, reason, and act on their own, representing the next evolution of generative AI. Cloudflare provides cloud infrastructure services including domain registration and web deployment, while Stripe is a major payment processing platform. The integration allows these agents to directly interact with and manage these services programmatically.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/agents/">Agents - Cloudflare Docs</a></li>
<li><a href="https://docs.stripe.com/agents">Add Stripe to your agentic workflows</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>

</ul>
</details>

**Discussion**: The community discussion shows significant skepticism about the practical utility of this feature, with users questioning who would need to automate domain purchasing and deployment. Several comments express serious security and fraud concerns, imagining scenarios where malicious agents could rapidly create phishing sites or commit financial fraud at scale.

**Tags**: `#AI agents`, `#cloud infrastructure`, `#automation`, `#security`, `#developer tools`

---

<a id="item-7"></a>
## [Computer Use by AI Agents Costs 45x More Than Structured APIs](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/) ⭐️ 7.0/10

A benchmark analysis revealed that AI agents using computer use to interact with a UI required 53 steps and 551k tokens, while using auto-generated structured API endpoints for the same task required only 8 calls and 12k tokens, making computer use 45 times more expensive. This cost disparity highlights a major economic inefficiency in current AI agent design, pushing developers to prioritize structured APIs over raw computer vision for automation to achieve scalability and cost-effectiveness. The benchmark compared the two approaches on the same admin panel, with computer use consuming vastly more computational resources and tokens, which directly translates to higher operational costs and slower execution.

hackernews · palashawas · May 5, 16:34 · [Discussion](https://news.ycombinator.com/item?id=48024859)

**Background**: Computer use for AI agents refers to models that can visually perceive and interact with graphical user interfaces (GUIs) like a human, often using vision models. Structured APIs, in contrast, are programmatic interfaces that allow agents to perform actions through direct, predefined function calls, which are typically more efficient and reliable.

<details><summary>References</summary>
<ul>
<li><a href="https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/">Computer use is 45x More Expensive Than Structured APIs</a></li>
<li><a href="https://github.com/trycua/acu">trycua/acu: A curated list of resources about AI agents for Computer Use, including research papers, projects, frameworks, and tools. - GitHub</a></li>
<li><a href="https://openai.com/index/computer-using-agent/">Computer-Using Agent - OpenAI</a></li>

</ul>
</details>

**Discussion**: The community discussion largely agrees that computer use should be a last resort, with commenters sharing alternative technical approaches like building CLI tools (e.g., desktopctl) or leveraging accessibility APIs to create more efficient, token-saving workflows. Some also humorously noted that common corporate SaaS apps already employ UI patterns that would make computer use even more expensive for agents.

**Tags**: `#AI agents`, `#API design`, `#cost optimization`, `#automation`, `#human-computer interaction`

---

<a id="item-8"></a>
## [Proposal of Three Inverse Laws for Human-AI Interaction](https://susam.net/inverse-laws-of-robotics.html) ⭐️ 7.0/10

An article proposes three inverse laws for AI interaction, arguing that humans should not anthropomorphize AI, blindly trust its outputs, or defer responsibility to machines. This framework is significant because it directly addresses core ethical and safety challenges in human-AI interaction, such as misplaced trust and accountability, which are critical as AI systems become more integrated into daily life. The laws are framed as prohibitions: do not anthropomorphize AI, do not blindly trust its outputs, and do not defer responsibility to it, aiming to establish clear human-centric boundaries for interaction.

hackernews · blenderob · May 5, 15:27 · [Discussion](https://news.ycombinator.com/item?id=48023861)

**Background**: The concept is a deliberate inversion of Isaac Asimov's famous 'Three Laws of Robotics' from science fiction, which were rules programmed into robots to govern their behavior. The proposed inverse laws shift the focus from constraining the AI to guiding human behavior and mindset when interacting with AI systems.

**Discussion**: The community discussion is highly engaged and critical, with many commenters arguing that the first law against anthropomorphism is fundamentally impractical because humans are inherently prone to attributing human traits to non-human entities. Others debate the feasibility of the other laws, questioning whether humans can realistically avoid blind trust or responsibility deferral given current AI design and human psychology.

**Tags**: `#AI ethics`, `#human-AI interaction`, `#philosophy of technology`, `#AI safety`

---

<a id="item-9"></a>
## [Airbyte Launches Unified Data Layer for AI Agents](https://news.ycombinator.com/item?id=48023496) ⭐️ 7.0/10

Airbyte has launched Airbyte Agents, a unified data layer that enables AI agents to discover information and take actions across multiple operational systems like Slack, Salesforce, and Linear. This product addresses a critical bottleneck for AI agents in real-world workflows by providing a structured context layer, potentially reducing the complexity and token consumption of multi-system agent tasks. The core is a 'Context Store' optimized for agentic search, populated by Airbyte's existing data connectors, and the company claims benchmarks show up to 90% fewer tokens used compared to direct vendor MCPs.

hackernews · mtricot · May 5, 15:03

**Background**: AI agents often struggle with complex, multi-step tasks across different software systems because they must handle intricate API plumbing, authentication, and data discovery. The Model Context Protocol (MCP) is an emerging open standard for connecting AI to external systems, but current implementations are often thin API wrappers. Airbyte is a well-established data integration company that has built numerous data connectors over the past six years.

<details><summary>References</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://airbyte.com/data-engineering-resources/data-connectors">What are Data Connectors? | Airbyte</a></li>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2026/01/05/avoiding-the-ai-failure-zone-why-context-and-a-unified-data-layer-matter/">The AI Failure Zone: Why Context And A Unified Data Layer Matter</a></li>

</ul>
</details>

**Discussion**: The discussion includes positive feedback from a former employee and technical observations, such as the potential for Airbyte Agents to act as an MCP gateway. Some users raised practical questions about SQL access and concerns about SaaS platforms creating new tollgates for agent API calls, which could impact data replication.

**Tags**: `#AI agents`, `#data integration`, `#API`, `#enterprise software`, `#developer tools`

---

<a id="item-10"></a>
## [Telus Uses AI to Alter Call-Agent Accents for Customer Clarity](https://letsdatascience.com/news/telus-uses-ai-to-alter-call-agent-accents-a3868f63) ⭐️ 6.0/10

Canadian telecommunications company Telus is deploying AI technology to modify the accents of its call-center agents in real-time, aiming to improve customer comprehension during interactions. This application highlights a growing trend of using AI for real-time voice processing in customer service, potentially improving communication efficiency but also raising significant ethical questions about cultural identity and authenticity. The technology likely involves real-time speech-to-speech conversion or accent neutralization AI, which can soften accents bidirectionally while preserving the speaker's original tone and emotion.

hackernews · debo_ · May 6, 01:38 · [Discussion](https://news.ycombinator.com/item?id=48031109)

**Background**: Accent neutralization or conversion technology uses AI algorithms to modify speech patterns in real-time, often employed in call centers to reduce miscommunication caused by strong regional accents. This technology is part of a broader field of speech synthesis and voice cloning, which itself raises ethical concerns regarding deepfakes, identity, and potential misuse.

<details><summary>References</summary>
<ul>
<li><a href="https://www.omind.ai/blog/accent-harmonizer/the-guide-to-accent-neutralization-software/">The Ultimate Guide to Accent Neutralization Software: Technology, Trends & Impact - Omind</a></li>
<li><a href="https://krisp.ai/contact-center/accent-conversion/">AI Accent Conversion for Call Centers - Krisp</a></li>
<li><a href="https://www.respeecher.com/blog/ethical-dilemma-voice-synthesis-vishing-and-its-consequences">New Ethical Dilemma in Voice Synthesis: Vishing and Its ... Not My Voice! A Taxonomy of Ethical and Safety Harms of ... The Ethics of Synthetic Voices: Opportunities and Challenges Voice Synthesis: Evolution, Ethics, and Law Speech Synthesis Ethics → Area → Sustainability The Ethics of Artificial Voices: Examining the Implications ...</a></li>

</ul>
</details>

**Discussion**: The community discussion is mixed; some users support the idea for improving call clarity, while others criticize it as a superficial fix or question the quality of the source article. A key counterargument is that such AI alteration could be seen as a form of 'whitening' accents, raising ethical concerns about cultural erasure.

**Tags**: `#AI applications`, `#customer service`, `#speech processing`, `#ethics`

---

<a id="item-11"></a>
## [Coinbase announces 14% workforce reduction and management restructuring.](https://twitter.com/brian_armstrong/status/2051616759145185723) ⭐️ 6.0/10

Coinbase CEO Brian Armstrong announced the company will reduce its workforce by approximately 14%, citing financial reasons and a strategic shift toward AI enablement. The restructuring includes a new management model where leaders will have up to 15+ direct reports and must act as 'player-coaches' who are also strong individual contributors. This layoff is significant as it reflects a broader trend in the tech industry where companies are restructuring workforces to prioritize AI capabilities and improve operational efficiency. The management changes signal a move toward flatter, more hands-on leadership structures, which could impact company culture and employee workloads. The new 'player-coach' model requires managers to handle a high number of direct reports while also performing significant individual contributor work, which raises concerns about potential burnout and effectiveness. The company is also focusing on hiring 'AI-native talent,' a term that has sparked discussion about potential age discrimination.

hackernews · adrianmsmith · May 5, 12:10 · [Discussion](https://news.ycombinator.com/item?id=48021368)

**Background**: The player-coach management model, inspired by sports, involves leaders who both manage teams and actively contribute to the work, a structure often used in startups for agility. AI enablement refers to the strategic integration of artificial intelligence to automate processes and drive business restructuring, a trend accelerating across the tech sector as companies invest heavily in AI infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/markmurphy/2018/01/14/the-leadership-model-used-by-steve-jobs-henry-ford-and-thomas-edison/">The Leadership Model Used By Steve Jobs, Henry Ford And ...</a></li>
<li><a href="https://www.innovativehumancapital.com/article/the-great-ai-pivot-how-tech-giants-are-restructuring-workforces-to-fund-automation-infrastructure">The Great AI Pivot: How Tech Giants Are Restructuring ...</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about the new management model, with concerns that having 15+ direct reports while also being an individual contributor could lead to managerial overload and poor outcomes. Some users compared the announcement to satirical corporate layoffs from the TV show 'Silicon Valley,' while others defended the communication as clear, though they questioned the strategic choices.

**Tags**: `#layoffs`, `#cryptocurrency`, `#management`, `#tech-industry`, `#AI-enablement`

---

<a id="item-12"></a>
## [AI Agent Mona Manages Stockholm Cafe, Reveals Real-World Operational Flaws](https://simonwillison.net/2026/May/5/our-ai-started-a-cafe-in-stockholm/#atom-everything) ⭐️ 6.0/10

Andon Labs has launched an experiment in Stockholm where an AI agent named Mona is fully managing a cafe, handling everything from ordering and hiring to finances, following a similar AI-run retail store experiment in San Francisco. This experiment provides a tangible, real-world test of autonomous AI agents in complex service operations, highlighting both their potential and significant practical limitations, which is crucial for understanding the future integration of AI in business. Mona made several amusing but costly operational errors, such as ordering 120 eggs without a stove and 22.5 kg of canned tomatoes for fresh sandwiches, and also wasted external parties' time by submitting flawed permit applications and sending multiple 'EMERGENCY' emails to suppliers to correct its own mistakes.

rss · Simon Willison · May 5, 22:14

**Background**: Andon Labs is a Y Combinator-backed startup that previously ran an AI agent named Luna to manage a retail store in San Francisco. The current Stockholm cafe experiment uses an AI agent powered by models like Google's Gemini and Anthropic's Claude to manage all aspects of the business, representing a step towards more autonomous AI in real-world commercial settings.

<details><summary>References</summary>
<ul>
<li><a href="https://andonlabs.com/blog/andon-market-launch">We gave an AI a 3 year retail lease in SF and asked it to ...</a></li>
<li><a href="https://www.businesstoday.in/technology/story/meet-mona-the-ai-running-a-real-cafe-in-stockholm-527972-2026-04-29">No human here, AI is the boss! Inside Stockholm’s unusual cafe</a></li>
<li><a href="https://timesofindia.indiatimes.com/technology/tech-news/worlds-first-ai-run-cafe-inside-stockholms-andon-cafe-operated-by-claude-and-gemini/articleshow/130478537.cms">World’s first AI-run cafe: Inside Stockholm’s Andon Cafe ...</a></li>

</ul>
</details>

**Discussion**: The original author, Simon Willison, criticized the experiment as unethical because it wastes the time of real-world people (like suppliers and police) who did not consent to participate, drawing a parallel to a previous AI experiment that sent unsolicited emails. He argues that such experiments must keep human operators in the loop for outbound actions affecting others.

**Tags**: `#AI applications`, `#real-world experiments`, `#autonomous systems`, `#AI failures`

---

<a id="item-13"></a>
## [Simon Willison tests 21 quantized Granite 4.1 3B models on SVG pelican generation.](https://simonwillison.net/2026/May/4/granite-41-3b-svg-pelican-gallery/#atom-everything) ⭐️ 6.0/10

Simon Willison prompted 21 different GGUF quantized variants of IBM's Granite 4.1 3B model to generate an SVG image of a pelican riding a bicycle, inspired by the large total download size of the model collection. This experiment provides a practical, hands-on exploration of how different quantization levels of a small language model affect a creative, non-text generation task, offering insights into the real-world performance trade-offs of model compression. The 21 GGUF model files from Unsloth range in size from 1.2GB to 6.34GB, totaling 51.3GB, but the results showed no clear pattern linking model size to output quality, with all variants producing poor pelican images.

rss · Simon Willison · May 4, 23:49

**Background**: IBM recently released the Granite 4.1 family of open-source large language models under the Apache 2.0 license, available in 3B, 8B, and 30B parameter sizes. GGUF is a file format for quantized models, created for the llama.cpp inference engine, which allows large language models to run efficiently on consumer hardware by reducing their memory footprint and computational requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://willitrunai.com/blog/quantization-guide-gguf-explained">Q4_K_M vs Q5_K_M vs Q8 — Which GGUF Quantization Should You ...</a></li>
<li><a href="https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs">Unsloth Dynamic 2.0 GGUFs</a></li>
<li><a href="https://arxiv.org/html/2412.11102v1">Empowering LLMs to Understand and Generate Complex Vector ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#quantization`, `#model-experimentation`, `#IBM-Granite`, `#SVG`

---

<a id="item-14"></a>
## [TRE Python binding demo shows robustness against ReDoS attacks.](https://simonwillison.net/2026/May/4/tre-python-binding/#atom-everything) ⭐️ 6.0/10

Simon Willison created an experimental Python binding for the TRE regular expression engine using ctypes and demonstrated that it handles malicious regex patterns much better than Python's standard library, primarily due to its lack of backtracking support. This exploration highlights a practical security improvement for Python applications vulnerable to ReDoS attacks, offering a more robust alternative to the standard regex engine for handling untrusted input. The TRE library uses a matching algorithm with linear worst-case time complexity for text length, which prevents the exponential backtracking that causes ReDoS vulnerabilities in many regex engines.

rss · Simon Willison · May 4, 17:52

**Background**: ReDoS (Regular Expression Denial of Service) is an attack that exploits poorly written regular expressions, causing them to take extremely long to process malicious input and potentially crash a service. The TRE library is a POSIX-compliant regex engine known for its approximate matching and predictable performance, developed by Ville Laurikari. Python's standard `re` module uses a backtracking algorithm that can be vulnerable to such attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TRE_(computing)">TRE (computing) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ReDoS">ReDoS - Wikipedia</a></li>
<li><a href="https://docs.python.org/3/library/ctypes.html">ctypes — A foreign function library for Python</a></li>

</ul>
</details>

**Tags**: `#security`, `#python`, `#regular-expressions`, `#performance`, `#tools`

---