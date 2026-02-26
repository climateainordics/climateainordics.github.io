---
title: "Featured Project: Open-Insect: Benchmarking Open-Set Recognition of Novel Species in Biodiversity Monitoring"
summary: "We propose a new open-set recognition dataset, Open-Insect, and evaluate 38 algorithms for new species detection on geographical open-set splits with varying difficulty."
abstract: "Researchers from Climate AI Nordics have introduced Open-Insect, a large-scale dataset designed to benchmark open-set recognition (OSR) by evaluating how machine learning models detect previously unseen insect species across different geographic regions. The study categorized and tested 38 different OSR algorithms, finding that while no single method was universally superior, simple post-hoc techniques remain surprisingly effective baselines.

A key discovery was that "local" unknown species are significantly harder to identify than non-local ones, though top-performing models still achieved a strong AUROC of over 85%. Ultimately, the benchmark demonstrates that OSR can effectively automate species discovery, providing a vital tool for monitoring and preserving global biodiversity."
people:
- Sigrid Passano Hellan
image: /images/posts/2026-02-26-open-insect.png
---
**Paper**: Open-Insect: Benchmarking Open-Set Recognition of Novel Species in Biodiversity Monitoring

**Authors**:  Yuyan Chen, Nico Lang, B. Christian Schmidt, Aditya Jain, Yves Basset, Sara Beery, Maxim Larrivée, David Rolnick

**Project page**: [https://yuyan-c.github.io/open-insect-project/](https://yuyan-c.github.io/open-insect-project/)

**TL;DR**: We propose a new open-set recognition dataset, Open-Insect, and evaluate 38 algorithms for new species detection on geographical open-set splits with varying difficulty.

Global biodiversity is declining at an unprecedented rate, yet little information is known about most species and how their populations are changing. Machine learning has recently emerged as a promising tool to facilitate biodiversity monitoring, including algorithms for fine-grained species recognition from images. However, such algorithms typically are not designed to detect examples from categories unseen during training – the problem of open-set recognition (OSR) – limiting their applicability for poorly studied taxa such as insects. To address this gap, we introduce Open-Insect, a large-scale, fine-grained dataset to evaluate unknown species detection across different geographic regions with varying difficulty.

Open-Insect consists of closed-, open-set, and auxiliary splits for three geographical regions: Northeastern North America, Western Europe, and Central America, utilizing geographical metadata to study local and non-local semantic shifts. Local open-set species may not only be harder to detect, but also reflect challenges encountered when deploying species-recognition models in practice. For each region, we also include a realistic auxiliary dataset for OSR methods that benefit from training with such data. 

We evaluated 38 OSR methods, and following OpenOOD v1.5, we categorized these methods into 1\) **post-hoc**; 2\) **training-time regularization**; and 3\) **training with auxiliary data**. Post-hoc methods can be combined with a trained classifier and do not require further training. For training-time regularization, these methods require further training, but they only utilize the closed-set during training time. Finally, for methods that require training with auxiliary data, they require both the closed-set and the auxiliary set. 

Though no method consistently outperforms the others across datasets, we observe that simple, efficient **post-hoc** methods, for example, maximum softmax probability, remain a strong baseline. Local open-set species are substantially more difficult to detect than non-local and non-moth open-set species. However, for all regions, the best performing method can achieve over 85% AUROC, indicating strong potential for automating species discovery with OSR in computer vision. 

One common concern of domain experts to adopt ML-based tools for species discovery is that models only use background features instead of species-level fine-grained features to determine whether the species are from the open-set or not. We conducted an experiment to empirically verify that background features are not enough to achieve good OSR performance on Open-Insect. 

We hope that the Open-Insect benchmark will draw attention to the problem of  species discovery and enable further work within the ML research community on OSR and OOD detection methods for biodiversity. Such work stands to benefit the preservation of ecosystem services on which humanity depends.

