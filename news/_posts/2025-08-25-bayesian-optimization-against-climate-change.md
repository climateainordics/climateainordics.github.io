---
title: "Featured paper: Bayesian Optimisation Against Climate Change: Applications and Benchmarks"
people:
- Sigrid Passano Hellan
image: /images/posts/2025-08-28-bayesian-optimization-against-climate-change-1.png
summary: "This paper explores the potential for using neural networks to model atmospheric particle formation. The neural network-based model, tasked here to predict cluster binding energies, achieved the target chemical accuracy of less than 1 kcal/mol, although kernel ridge regression had a slightly lower error. Training was over an order of magnitude faster with the neural network compared to kernel ridge regression."
---

**

**Authors:** Sigrid Passano Hellan, Christopher G. Lucas and Nigel H. Goddard.

**Paper:** [arxiv.org/abs/2306.04343](https://arxiv.org/abs/2306.04343), (publication forthcoming in Springer Lecture Notes in Computer Science as part of the proceedings for the 19th Learning and Intelligent Optimization Conference, LION19).

A lot of work related to climate change can be phrased in terms of an optimisation problem: where would my wind turbine produce the most electricity; what solar panel material will be the most efficient? One machine learning (ML) method to solve optimisation problems is Bayesian optimisation. It has been applied to solar panel material design, wind farm planning and operation, and to environmental monitoring, among many other applications. This succinct survey discusses and groups applications from the literature, and identifies four benchmarks as starting points for ML practitioners wanting to apply Bayesian optimisation to problems related to climate change.

Bayesian optimisation is a type of probabilistic, surrogate-based optimisation. That means we use a probabilistic model of the quantity we are optimising. So if we are operating a solar panel with adjustable panel angles (see Fig 2), we use a model of the relationship between panel angles and electricity production (1) to tell us what would be promising or informative angles to try next (2). Then we collect more data (3) and update our model (back to 1) before continuing. Usually, the surrogate model we use is a Gaussian process.

![](/images/posts/2025-08-28-bayesian-optimization-against-climate-change-2.png)

Previous work was grouped into four main use cases:
* material discovery — accelerating the development of e.g. new solar panels
* wind farm layouts — choosing where to place individual turbines
* optimal renewable control — choosing operating parameters of solar panels or wind turbines
* environmental monitoring — choosing where to place sensors.

For each of the use cases a suitable starting benchmark was identified. Two of these were simulation based, the other two based on observations. In the first, the material properties of solar panels were optimised. In the second the layout of a small wind park of five turbines was planned. In the third the direction of a solar panel was optimised and in the final one the location of maximum pollution in a city was sought.

In the survey the most common use cases were highlighted, but there were many others. A few examples are scheduling smart household appliances; optimising heating and cooling systems; targeting informative training data for climate models; and parameter tuning for a land surface model.

At Climate AI Nordics there are several people interested in Bayesian optimisation (you can filter people by interest on the web page). For example: the authors of the featured paper have worked on Bayesian optimisation for air pollution monitoring, and Sanna Jarl and colleagues at Uppsala university and RISE are working on Bayesian optimisation to make solar panels from less toxic and rare materials. You can read more about the latter in:

**Jarl, S.**, Sjölund, J., Frost, R. J., Holst, A., & Scragg, J. J. (2025). Machine learning for in-situ composition mapping in a self-driving magnetron sputtering system. arXiv preprint https://arxiv.org/abs/2506.05999.
