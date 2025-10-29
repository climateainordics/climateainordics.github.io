---
title: "Featured paper: Continuous Urban Change Detection From Satellite Image Time Series With Temporal Feature Refinement and Multitask Integration"
people:
- Sebastian Hafner
image: /images/posts/2025-10-29-continuous-urban-change.png
summary: "This paper presents a method to continuously detect urban changes in high-resolution satellite image time series (SITS). Traditional urban change detection models often rely on bi-temporal image pairs acquired multiple years apart, limiting their ability to capture gradual, ongoing urbanization processes. The paper introduces a deep learning framework, including two novel modules to enhance segmentation feature maps extracted from SITS and integrate multi-task model outputs (i.e., building segmentations and dense change information). The paper’s findings show the limitations of bi-temporal change detection methods, as they cannot exploit multitemporal information in SITS. In contrast, their continuous urban change detection method achieves accurate urbanization monitoring results even at short time intervals."
---

**Authors:** Sebastian Hafner, Heng Fang, Hossein Azizpour, and Yifang Ban

**Paper:** [arxiv.org/abs/2406.17458](https://arxiv.org/abs/2406.17458), published in  IEEE Transactions on Geoscience and Remote Sensing (Volume: 63).

Monitoring how cities grow over time is essential for managing urban sprawl and planning sustainable development. Most existing methods compare satellite image pairs acquired at two points in time, typically multiple years apart (i.e., bi-temporal change detection). Due to rapid ongoing urbanization, however, monitoring urban growth at short time intervals is becoming increasingly important. To that end, this paper presents a continuous urban change detection framework that captures changes between consecutive images in high-resolution satellite image time series (SITS).

The proposed model introduces two innovations: the Temporal Feature Refinement (TFR) and Multitask Integration (MTI) modules. The TFR module applies a transformer-based self-attention mechanism to model temporal dependencies in building representations extracted from SITS. Importantly, the TFR module preserves the time dimension, unlike existing SITS change detection methods that are limited to detecting changes between the first and last image of a time series. On the other hand, the MTI module uses Markov networks to fuse the outputs of building segmentation and change detection tasks. By applying belief propagation, the MTI module ensures temporal consistency and removes contradictions between change maps and building footprints.

The framework was tested on three challenging datasets, namely SpaceNet 7 (PlanetScope, 4 m), Wuhan Urban Semantic Understanding (Gaofen-2, 1 m), and Time Series Change Detection (WorldView-2, 0.5 m), and consistently outperformed bi-temporal change detection methods, as well as SITS change detection methods.

Ablation studies confirmed that modeling full temporal context through self-attention significantly improves performance over recurrent alternatives, and that dense temporal connections in the MTI module lead to more consistent and accurate urban change maps.
