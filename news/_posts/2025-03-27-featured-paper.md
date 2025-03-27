---
title: "Featured Paper: Efficiency is Not Enough: A Critical Perspective of Environmentally Sustainable AI"
shortversion: "This perspective paper discusses several reasons why it is crucial to look at the impact of machine learning (ML) using systems thinking, i.e. across the entire life cycle of models, from development to deployment."
abstract: "This perspective paper discusses several reasons why it is crucial to look at the impact of machine learning (ML) using systems thinking, i.e. across the entire life cycle of models, from development to deployment."
socialmedia: "This perspective paper discusses several reasons why it is crucial to look at the impact of machine learning (ML) using systems thinking, i.e. across the entire life cycle of models, from development to deployment."
people:
- Nico Lang
image: /images/posts/2025-03-27-featured-paper.png
imagealt: "Figure 1: The Deep Learning model life cycle. (Wright et al., 2024\)"
---

Authors: **Dustin Wright, Christian Igel, Gabrielle Samuel and Raghavendra Selvan<br />
University of Copenhagen and King’s College London**

**Paper:** [https://arxiv.org/abs/2309.02065](https://arxiv.org/abs/2309.02065), *Accepted to Communications of the ACM*

**TL;DR:** This perspective paper discusses several reasons why it is crucial to look at the impact of machine learning (ML) using *systems thinking*, i.e. across the entire life cycle of models, from development to deployment.

The machine learning (ML) community is getting aware of the environmental impacts of this technology. Today, the ML community heavily relies on measuring *efficiency* as the major metric to achieve environmentally sustainable models. Efficiency can indeed reduce carbon emissions and it is often straightforward to implement as a metric. However, are these efforts enough to actually have a positive impact in practice? What are the hidden consequences of more efficient models? Should we move beyond efficiency to develop a more nuanced view of the environmental impact of ML systems? This paper provides an in-depth discussion of the limitations of considering compute efficiency alone by summarizing three high-level discrepancies:

* *Discrepancy 1:* Compute efficiency ≠ energy efficiency ≠ carbon efficiency.
* *Discrepancy 2:* Efficiency has unexpected effects on operational emissions across the ML model life cycle.
* *Discrepancy 3:* Efficiency does not account for, and can potentially exacerbate, broader environmental impacts from hardware platforms

**Compute efficiency ≠ energy efficiency ≠ carbon efficiency**
Common metrics of compute include FLOPS, number of parameters, and runtime, which are all easy to measure. However, operational carbon emissions are a function of both energy consumption and carbon intensity, which varies heavily by location and time. For example, selecting a different region in a cloud can change the carbon intensity up to a factor 10\. A simple way to explore such regional differences yourself is by using e.g. this [ML Emissions Calculator](https://mlco2.github.io/impact/#compute). Furthermore, energy is a complex function of several factors, which is not fully captured by metrics of compute. Thus, making a model more compute efficient can only sometimes improve energy efficiency.

**Efficiency has unexpected effects across the model life cycle**
Efficiency will impact the decisions one makes throughout the model life cycle (see Figure 1), which will not always lead to reductions in carbon emissions. If we think of an emission budget as a whole for development and deployment, we need to manage the resource consumed by each phase in the model life cycle. Let us take neural architecture search as an example, which is highly compute intensive during the development of a model. If an efficient solution is found, it has the potential to reduce emissions during deployment of that model, but the gains during the deployment phase need to compensate for the increased emissions during the development phase. Another aspect highlighted is the context of the life cycle is the *rebound effect*. Increasing the efficiency of a resource can lead to increased usage of that resource. Rebounds in terms of energy consumption have been seen at multiple companies using ML.

**Hardware platforms have broader environmental impacts**
The hardware platforms that power ML systems have broad environmental impacts, coming from several aspects. Manufacturing the devices to run ML systems requires the mining of raw materials which leads to deforestation (i.e. carbon emissions) and pollution as well as hazardous products such as radioactive and toxic chemical components. Carbon emissions are also caused by the manufacturing and transportation, and the cooling of compute devices can even cause water scarcity. Finally, the lack of disposal of old hardware can lead to additional pollution and even health hazards for biodiversity and people exposed to polluted water and soil.

**Beyond efficiency: Systems thinking**
As AI tools are becoming more and more prominent in our daily lives, we need to develop ML systems that take into account environmental, economical, and social aspects of sustainability. Therefore, we need to carefully reconsider the system boundaries to provide holistic assessments that allow us to make progress towards the sustainable development goals. As a way forward, the authors propose to use *systems thinking* as conceptual framework to deal with the complexity of ML.

*"A key feature of systems thinking is the insight that complex systems are more than the sum of their parts. This is revealed through the systems lens, which looks at the behavior of the entire system as a whole, relating the components of the system to each other through causal feedback loops." (Wright et al., 2025\)*
