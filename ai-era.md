---
layout: default
title: "Research in the AI Era"
permalink: /ai-era/
---

<!-- # Research in the AI Era 

Research is shifting toward a world where every lab has access to powerful, fallible, semi-autonomous research co-pilots. The challenge is to shape research culture, training, and norms so we exploit AI where it amplifies creativity, rigor, and reach—while resisting it where it erodes understanding, integrity, or equity—and keeping the human parts of research (wonder, taste, responsibility) clearly in view. In the AI era, researchers increasingly act less like “push-button scientists” and more like lab heads: designing and supervising a growing cast of non-human collaborators.-->

We are entering an era of reasoning abundance enabled by AI, much as the internet ushered in an era of information abundance, opening new opportunities and challenges for research across all areas of computer science. AI is rapidly reshaping nearly every stage of the research lifecycle, from identifying and framing research topics and conducting literature reviews to theoretical analysis, experimental design and execution, interpreting results, writing and reviewing papers, and supporting reproducibility. As these tools become more tightly integrated, sometimes augmenting and sometimes automating core tasks, our notions of contribution, rigor, and expertise are evolving.

This seminar series brings together speakers from across ALL areas of computer science, spanning theory, systems, AI, and interdisciplinary, to talk about these shifts. Each talk will offer a perspective on how AI is changing research methodologies, challenging traditional assumptions about originality and rigor, and enabling new forms of collaboration. Join us to explore what research may look like in the AI era and to discuss how we can harness these tools while preserving the core values of scientific inquiry.


## Format & timing

- **Organizer**: Mohammad Hajiesmaili
- **When:** Select Fridays during the Spring 2025, immediately after the student/faculty lunch  
- **Time:** **1:00–2:00 pm ET**
- **Where:** UMass Amherst CSL E144 
- **Audience:** Faculty, students, and visitors interested in how AI is changing research practice and norms  

## Schedule

##### [Glia: A Human-Inspired AI for Automated Systems Design and Optimization](https://arxiv.org/abs/2510.27176)

[Hari Balakrishnan](http://nms.csail.mit.edu/~hari/) (MIT) --  *Friday, February 6 @ 1 pm*

**Category:** Systems

<details markdown="1">
<summary>Description</summary>
This talk will focus on how AI can be used to autonomously design and optimize complex systems. This directly ties into the seminar's theme by showcasing how AI is automating the core tasks of experimental design and execution, bringing an era of reasoning abundance to the systems research lifecycle.
</details>

<details markdown="1">
<summary>Abstract</summary>

Can an AI autonomously design mechanisms for computer systems on par with the creativity and reasoning of human experts? We present Glia, an AI architecture for networked systems design that uses large language models (LLMs) in a human-inspired, multi-agent workflow. Each agent specializes in reasoning, experimentation, and analysis, collaborating through an evaluation framework that grounds abstract reasoning in empirical feedback. Unlike prior ML-for-systems methods that optimize black-box policies, Glia generates interpretable designs and exposes its reasoning process. When applied to a distributed GPU cluster for LLM inference, it produces new algorithms for request routing, scheduling, and auto-scaling that perform at human-expert levels in significantly less time, while yielding novel insights into workload behavior. Our results suggest that by combining reasoning LLMs with structured experimentation, an AI can produce creative and understandable designs for complex systems problems. 

</details>

<hr>

<!-- ################################### -->

##### [Man-Made Heuristics Are Dead. Long Live Code Generators!](https://arxiv.org/abs/2510.08803)

[Aditya Akella](https://www.cs.utexas.edu/~akella/) (UT Austin) --  *Friday, February 27 @ 1 pm*

**Category:** Systems

<details markdown="1">
<summary>Description</summary>
This work suggests a focus on AI's ability to generate code and replace traditionally human-designed components (heuristics) in research. This connects to the seminar by showcasing how AI is moving beyond simple augmentation to automating core tasks within experimental design and execution, forcing researchers to redefine the role of human expertise.
</details>

<details markdown="1">
<summary>Abstract</summary>
Policy design for various systems controllers has conventionally been a manual process, with domain experts carefully tailoring heuristics for the specific instance in which the policy will be deployed. In this paper, we re-imagine policy design via a novel automated search technique fueled by recent advances in generative models, specifically Large Language Model (LLM)-driven code generation. We outline the design and implementation of PolicySmith, a framework that applies LLMs to synthesize instance-optimal heuristics. We apply PolicySmith to two long-standing systems policies - web caching and congestion control, highlighting the opportunities unraveled by this LLM-driven heuristic search. For caching, PolicySmith discovers heuristics that outperform established baselines on standard open-source traces. For congestion control, we show that PolicySmith can generate safe policies that integrate directly into the Linux kernel. 
</details>

<hr>

<!-- ################################### -->

##### [Braintrust: social knowledgebases as scientific fiduciaries]()

[Evan Coleman](https://eacoleman.github.io/) (MIT) --  *Friday, March 6  @ 1 pm*

**Category:** interdisciplinary

<details markdown="1">
<summary>Description</summary>
This talk will demonstrate how accelerated research enabled by AI can unlock tackling interdisciplinary and long-horizon problems like climate change. 
</details>

<details markdown="1">
<summary>Abstract</summary>
Climate change presents a rare existential challenge. Nearly every economic sector contributes to it, since greenhouse gases are common byproducts of thermodynamically and economically favorable processes. At the same time, it is a planetary-scale problem with a single shared benchmark: atmospheric greenhouse gas concentration (CO2e). These conditions make climate change mitigation a natural test case for how experts coordinate to scale critical technologies under a unified, decades-long objective. Addressing and adapting to a changing climate requires navigating complex technology pathways that span many domains and do not necessarily admit end-to-end automation or simulation-driven discovery. These pathways resemble a "tech tree": a structured narrative of progress that links partially developed ideas across disciplines to downstream sources of value.
In this talk, I will present Braintrust, an early-stage open-source effort using language models to build navigable tech trees for science. Our goal is to convene researchers, research administrators, and financiers around shared representations of scientific progress. Basic research struggles to support such coordination because expertise is fragmented, first-of-a-kind efforts are risky, and incentives are weakly coupled to downstream economic value. Braintrust models tech trees as interactive structures that evolve with new evidence and human input. This approach is orthogonal to using LLMs for scientific execution: we use semantics to surface cross-domain connections, situate speculative ideas relative to established work, and represent uncertainty at the frontier where coordination and investment decisions are made. I will provide real-world examples within climate technology, and conclude by framing social knowledge bases as fiduciary tools that can support the allocation of resources in high-risk, high-reward scientific programs.
</details>

<hr>


<!-- ################################### -->

##### [Scientific production in the era of large language models](https://www.science.org/doi/10.1126/science.adw3000)

[Yian Yin](https://www.yianyin.net/) (Cornell) --  *Friday, March 13  @ 1 pm*

**Category:** AI/interdisciplinary

<details markdown="1">
<summary>Description</summary>
This topic explores scientific production in the era of LLMs, examining the practical and conceptual shifts caused by powerful AI tools. This directly addresses the seminar's core question of how AI is reshaping research methodologies, forcing a re-evaluation of traditional assumptions about originality, rigor, and contribution in the face of machine-assisted work. See this [X thread](https://x.com/yian_yin/status/2003507218768101485?s=20).
</details>

<details markdown="1">
<summary>Abstract</summary>
Despite growing excitement (and concern) about the fast adoption of generative artificial intelligence (Gen AI) across all academic disciplines, empirical evidence remains fragmented, and systematic understanding of the impact of large language models (LLMs) across scientific domains is limited. We analyzed large-scale data from three major preprint repositories to show that the use of LLMs accelerates manuscript output, reduces barriers for non-native English speakers, and diversifies the discovery of prior literatures. However, traditional signals of scientific quality such as language complexity are becoming unreliable indicators of merit, just as we are experiencing an upswing in the quantity of scientific work. As AI systems advance, they will challenge our fundamental assumptions about research quality, scholarly communication, and the nature of intellectual labor. Science policy-makers must consider how to evolve our scientific institutions to accommodate the rapidly changing scientific production process.
</details>

<hr>

<!-- ################################### -->

##### [TBD]()

[Aaron Roth](https://www.cis.upenn.edu/~aaroth/) (UPenn) --  *Friday, March 27  @ 1 pm*

**Category:** Theory

<details markdown="1">
<summary>Description</summary>
As a theoretical AI researcher, Aaron Roth will likely explore the fundamental changes and challenges that AI introduces to theoretical analysis and the establishment of scientific rigor. This perspective is vital to the seminar as it examines how AI's influence is evolving our notions of contribution and expertise across all areas of computer science research. See this [X thread](https://x.com/Aaroth/status/2002816644419346517?s=20).
</details>

<details markdown="1">
<summary>Abstract</summary>
TBD
</details>

<hr>

<!-- ################################### -->

##### [On Learning-Curve Monotonicity for Maximum Likelihood Estimators](https://arxiv.org/abs/2512.10220)

[Mark Sellke](https://msellke.com/) (Harvard/OpenAI) --  *Friday, April 3  @ 1 pm*

**Category:** Theory

<details markdown="1">
<summary>Description</summary>
This talk is based on work, On Learning-Curve Monotonicity for Maximum Likelihood Estimators, where all the results were derived by AI models (variants of GPT-5.2 Pro) with humans only providing prompts and verification. This strikingly illustrates the seminar's theme by demonstrating AI's capacity to automate the demanding task of theoretical analysis and proof generation, profoundly challenging traditional views on human-driven discovery and scientific originality.
</details>

<details markdown="1">
<summary>Abstract</summary>
The property of learning-curve monotonicity, highlighted in a recent series of work by Loog, Mey and Viering, describes algorithms which only improve in average performance given more data, for any underlying data distribution within a given family. We establish the first nontrivial monotonicity guarantees for the maximum likelihood estimator in a variety of well-specified parametric settings. For sequential prediction with log loss, we show monotonicity (in fact complete monotonicity) of the forward KL divergence for Gaussian vectors with unknown covariance and either known or unknown mean, as well as for Gamma variables with unknown scale parameter. The Gaussian setting was explicitly highlighted as open in the aforementioned works, even in dimension 1. Finally we observe that for reverse KL divergence, a folklore trick yields monotonicity for very general exponential families.
All results in this paper were derived by variants of GPT-5.2 Pro. Humans did not provide any proof strategies or intermediate arguments, but only prompted the model to continue developing additional results, and verified and transcribed its proofs. 
</details>

<hr>

<!-- ################################### -->

##### [TBD]()

[Amir Yazdanbakhsh](https://www.ayazdan.com/) (Google) --  *Friday, April 10  @ 1 pm*

**Category:** Systems

<details markdown="1">
<summary>Description</summary>
TBD
</details>

<details markdown="1">
<summary>Abstract</summary>
TBD
</details>

<hr>

<!-- ################################### -->

##### [Gemini-based automated feedback for theoretical CS papers](https://research.google/blog/gemini-provides-automated-feedback-for-theoretical-computer-scientists-at-stoc-2026/)

[David Woodruff](https://www.cs.cmu.edu/~dwoodruf/) (CMU) --  *Friday, April 17  @ 1 pm*

**Category:** Theory/Automated Review

<details markdown="1">
<summary>Description</summary>
Focusing on Gemini-based automated feedback for theoretical CS papers, this session will cover the application of AI to the peer review process. This directly relates to the seminar series by showing how AI is being integrated into the later stages of the research lifecycle, specifically, augmenting and automating the critical tasks of writing and reviewing papers to support reproducibility and rigor.
</details>

<details markdown="1">
<summary>Abstract</summary>
The pursuit of truth in theoretical computer science and mathematics relies on the highest standards of proof, rigor, and clarity. While peer review is the crucial final check, the process of drafting and refining complex theoretical work often takes months, with simple errors, inconsistent variables, or subtle logical gaps frequently slowing down the entire research pipeline. But could a highly specialized AI tool act as a fast, rigorous collaborator, helping authors pre-vet their work before it ever reaches human reviewers?

To test this potential, we created an experimental program for the Annual ACM Symposium on Theory of Computing (STOC 2026) — one of the most prestigious venues in theoretical computer science. This program offered authors automated, pre-submission feedback generated by a specialized Gemini AI tool. Our objective was to provide constructive suggestions and identify potential technical issues within 24 hours of submission, helping authors polish their final drafts before the submission deadline.

The responses were very positive: the tool successfully identified a variety of issues, including calculation and logic errors. Here we report how we developed the tool and the results of its use.
</details>

<hr>

<!-- ################################### -->

<!-- ##### []()

[]() () --  *Friday, February  @ 1 pm*

**Category:** 

<details markdown="1">
<summary>Description</summary>

</details>

<details markdown="1">
<summary>Abstract</summary>

</details>

<hr> -->

<!-- ####################################################### -->

<!-- ## Initial invited speakers (initial list (dates to be confirmed))

1. **Mohammad Alizadeh (MIT)** or **Hari Balakrishnan (MIT)**  
   - Related work: *Glia: A Human-Inspired AI for Automated Systems Design and Optimization* (arXiv:2510.27176)  
   - Link: https://arxiv.org/abs/2510.27176

2. **Aaron Roth (UPenn)**  
   - Related work: *On Learning-Curve Monotonicity for Maximum Likelihood Estimators* (arXiv:2512.10220)  
   - Link: https://arxiv.org/abs/2512.10220

3. **Mark Sellke (Harvard)**  
   - Related work: *On Learning-Curve Monotonicity for Maximum Likelihood Estimators* (arXiv:2512.10220)  
   - Link: https://arxiv.org/abs/2512.10220

4. **Vincent Cohen-Addad (Google Research)**  
   - Related work: Gemini-based automated feedback for theoretical CS papers (STOC 2026 experiment)  
   - Link: https://research.google/blog/gemini-provides-automated-feedback-for-theoretical-computer-scientists-at-stoc-2026/ -->

<!-- ## Spring schedule (TBA) -->

<!-- We will meet on **selected Fridays** during the Spring semester, **right after the student/faculty lunch**.  
Specific dates and speakers will be posted here as they are confirmed. -->
