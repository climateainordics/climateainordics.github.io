---
title: "Featured Preprint: Continuous Ensemble Weather Forecasting with Diffusion Models"
summary: "In Featured Preprints, preprints from affiliated researchers are summarized and featured at Climate AI Nordics. This one features &quot;Continuous Ensemble Weather Forecasting with Diffusion Models&quot;, from Martin Andrae, Tomas Landelius, Joel Oskarsson, and Fredrik Lindsten."
people:
- Olof Mogren
image: /images/posts/2024-11-22-featured-preprint.png
---
Authors: Martin Andrae, Tomas Landelius, **Joel Oskarsson**, Fredrik Lindsten

Traditional numerical weather prediction (NWP) systems rely on complex physical models and extensive computational resources. Diffusion models have been proposed as a promising direction. This paper addresses some of the limitations of weather forecasting using diffusion models; they are computationally expensive and accumulate errors for high temporal resolution due to the many rollout steps. 

**Continuous Ensemble Forecasting**: The authors propose a method that generates temporally consistent ensemble trajectories in parallel, eliminating the need for autoregressive steps. This approach addresses the computational inefficiencies and error accumulation associated with high temporal resolution forecasts.

**Integration with Autoregressive Rollouts**: The method can be combined with autoregressive rollouts to produce forecasts at arbitrarily fine temporal resolutions without compromising accuracy.

**Probabilistic Modeling**: By employing diffusion models, the approach captures the inherent uncertainties in weather forecasting, providing a probabilistic framework that enhances the reliability of predictions.

This research signifies a shift towards more efficient and accurate weather forecasting methods, which are crucial for climate modeling and decision-making. The ability to generate ensemble forecasts with reduced computational resources aligns with the goals of Climate Change AI, promoting the development of scalable and effective tools to address climate challenges.

[Read the full paper at arxiv!](https://arxiv.org/abs/2410.05431)

