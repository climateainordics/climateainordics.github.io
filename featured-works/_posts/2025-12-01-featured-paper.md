---
title: "Featured Paper: ForestFormer3D: A Unified Framework for End-to-End Segmentation of Forest LiDAR 3D Point Clouds"
summary: "The new Climate AI Nordics Featured Paper is \"ForestFormer3D: Unified 3D Forest Segmentation from LiDAR\". This work introduces a transformer-based framework for accurate individual tree and semantic segmentation in complex forest environments."
abstract: "The segmentation of forest LiDAR 3D point clouds, including both individual tree and semantic segmentation, is fundamental for advancing forest management and ecological research. However, current approaches often struggle with the complexity and variability of natural forest environments. We present ForestFormer3D, a new unified and end-to-end framework designed for precise individual tree and semantic segmentation. ForestFormer3D incorporates ISA-guided query point selection, a score-based block merging strategy during inference, and a one-to-many association mechanism for effective training. By combining these new components, our model achieves state-of-the-art performance for individual tree segmentation on the newly introduced FOR-instanceV2 dataset, which spans diverse forest types and regions. Additionally, ForestFormer3D generalizes well to unseen test sets (Wytham Woods and LAUTx), showcasing its robustness across different forest conditions and sensor modalities. The FOR-instanceV2 dataset and the ForestFormer3D code are publicly available."
socialmedia: "ForestFormer3D introduces a unified transformer-based framework for individual tree and semantic segmentation of forest LiDAR point clouds."
people:
- Stefano Puliti
image: /images/posts/FF3D.PNG
---
Authors: Binbin Xiang, Maciej Wielgosz, **Stefano Puliti**, Kamil Král, Martin Krůček, Azim Missarov, Rasmus Astrup

The new Climate AI Nordics Featured Paper is **\"ForestFormer3D: Unified 3D Forest Segmentation from LiDAR\"**, presented as an **oral at ICCV 2025 in Honolulu, Hawaii**. The paper tackles a core challenge in forest remote sensing: accurate segmentation of complex forest LiDAR point clouds across diverse forest types and sensor configurations.

ForestFormer3D introduces a **unified, end-to-end transformer-based framework** that jointly addresses individual tree segmentation and semantic segmentation. The method integrates several key innovations, including ISA-guided query point selection to improve instance initialization, a score-based block merging strategy to handle large-scale point clouds during inference, and a one-to-many association mechanism that stabilizes training and improves segmentation quality.

The model achieves **state-of-the-art performance** on individual tree segmentation using the newly introduced **FOR-instanceV2 dataset**, which covers a wide range of forest structures and geographic regions. Importantly, ForestFormer3D demonstrates strong generalization to **unseen datasets**, including Wytham Woods and LAUTx, highlighting its robustness across different forest conditions and LiDAR sensor modalities.

This work represents a significant step forward for scalable and reliable 3D forest analysis, with direct relevance for forest inventory, ecological research, and forest management applications.

For more details, explore:
- [Full paper (arXiv):](https://www.arxiv.org/abs/2506.16991)  
- [Project page](https://bxiang233.github.io/FF3D/)
- [Data](https://zenodo.org/records/16742708)
