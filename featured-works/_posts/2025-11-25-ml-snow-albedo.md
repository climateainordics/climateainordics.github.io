---
title: "Featured paper: Separating the Albedo-Reducing Effect of Snow Impurities Using Machine Learning"
people:
- Alouette van Hove
summary: "This study presents an AI-driven inversion framework that uses a deep-learning emulator of a radiative transfer model to estimate snow albedo and quantify the impact of light-absorbing particles (LAPs) such as dust, black carbon, and algae. Trained on 5.8 million simulations, the method accelerates computations by 30× while maintaining accuracy, enabling large-scale mapping from drone or satellite data. Applied to field observations, it revealed strong but variable LAP effects on albedo and complex interactions between multiple impurities, offering a powerful tool for improving melt forecasts and climate projections."
---

![](/images/posts/2025-11-14-featured-paper-chevrollier-figure1.jpg)

*Lou-Anne Chevrollier from Aarhus University and Adrien Wehrlé from Zurich University collecting snow reflectance data at the Finse Research Station.*

**Authors:** Lou-Anne Chevrollier, Adrien Wehrlé, Joseph M. Cook, Norbert Pirk, Liane G. Benning, Alexandre M. Anesio, and Martyn Tranter.

**Paper:** [https:doi.org/10.5194/tc-19-1527-2025](https:doi.org/10.5194/tc-19-1527-2025), The Cryosphere, 2025, 19, 1527–1538.

Snow albedo—the fraction of sunlight reflected by snow—plays a key role in Earth’s energy balance. When snow is contaminated by light-absorbing particles (LAPs) such as mineral dust, black carbon, or pigmented algae, its albedo decreases, leading to enhanced absorption of solar radiation. This process influences glacier mass balance and represents an important source of uncertainty in melt forecasts because it varies greatly in time and space, and remote detection methods able to identify the different types of LAPs are lacking. 

To address this challenge, the study introduces an AI-based inversion framework using a deep-learning emulator of a radiative transfer model. Trained on over 5.8 million simulations, the emulator predicts spectral albedo from key surface parameters such as snow grain size, liquid water content, and LAP concentrations. Coupled with a gradient-based inversion algorithm, this approach simultaneously quantifies the role of each individual LAP type in surface darkening. The use of AI in this study enabled a speed up of the original model by 30 times while maintaining high accuracy, making it suitable for large-scale applications using drone or satellite imagery.

![](/images/posts/2025-11-14-featured-paper-chevrollier-figure2.jpg)

*Figure 2 reproduced from the original study, showing the agreement between model and observations as well as the retrieved surface parameters for different surface types (from left to right): clean snow, algal-loaded snow, dust-loaded snow, black particles-loaded snow.*

Applied to 180 observations collected at the Finse Research Station, the method revealed strong and variable impacts of LAPs on snow albedo. Red algal blooms reduced albedo by up to 0.13, mineral dust by 0.21, and dark particles by 0.25, corresponding to daily radiative forcing values as high as 44 W/m². Importantly, the presence of multiple LAPs attenuated individual effects by up to a factor of three, highlighting complex interactions that must be considered in predictive models. This open-source method enables high-resolution mapping of snow impurities and initiates progress toward improved climate projections and melt assessments.
