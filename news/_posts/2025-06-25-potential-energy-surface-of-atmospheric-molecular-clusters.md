---
title: "Featured paper: Accurate modeling of the potential energy surface of atmospheric molecular clusters boosted by neural networks"
people:
- Hilda Sandström
image: /images/posts/2025-06-25-atmospheric-molecular-clusters.png
shortversion: "This paper explores the potential for using neural networks to model atmospheric particle formation. The neural network-based model, tasked here to predict cluster binding energies, achieved the target chemical accuracy of less than 1 kcal/mol, although kernel ridge regression had a slightly lower error. Training was over an order of magnitude faster with the neural network compared to kernel ridge regression."
---

*Figure. The challenge of modeling atmospheric molecular clusters grows with increasing cluster size. The neural network PaiNN provides a way to avoid this computational barrier. Image from Kubečka et al., (2024). Licensed under CC BY 3.0.*

**Authors:** Jakub Kubečka, Daniel Ayoubi, Zeyuan Tang, Yosef Knattrup, Morten Engsvang, Haide Wu, and Jonas Elm, Aarhus University, Denmark.

**Paper:** [https:doi.org/10.1039/d4va00255e](https:doi.org/10.1039/d4va00255e), Environ. Sci. Adv., 2024, 3, 1438-1451.

Computational chemists tackle a key challenge in molecular atmospheric science by studying particle formation at different size scales that no single experimental technique can yet fully probe. Quantum chemistry methods that solve the Schrödinger equation allow chemists to study the molecular structure and interactions inside and on the surface of atmospheric particles with a bottom-up approach. The Aarhus University group led by Jonas Elm has built a large database of atmospheric molecular acid-base clusters, published in the Clusteromics I–V datasets. In total, the group has collected hundreds of thousands of structures. However, the computational cost of quantum chemistry calculations grows rapidly with cluster size and complexity, often forcing a trade-off between feasibility and accuracy.

Having previously tested kernel ridge regression for fast mapping of low-accuracy quantum chemistry energies to higher accuracy ones using delta learning, Kubečka and co-authors now report the first effort to replace kernel ridge regression with neural networks for this purpose. The machine learning community for molecular sciences offers several model architectures for predicting energies and forces needed to identify stable cluster structures and their properties. The model used here is PaiNN, the polarizable atom interaction neural network.

The PaiNN model was trained with the goal to predict cluster binding energies within the chemical accuracy threshold of 1 kcal/mol compared to quantum chemistry references. When predicting energies only, PaiNN achieved a mean absolute error (MAE) of 0.7 kcal/mol, compared to 0.5 kcal/mol for kernel ridge regression. An improved performance with an energy MAE below 0.3 kcal/mol was reached when training PaiNN on both energies and forces. Interestingly, the authors found that the model generalizes well to larger cluster sizes. They suggest this is because hydrogen bonds, which play a central role in determining cluster structure, are already well represented in smaller clusters.

One main motivation for moving away from kernel ridge regression is its poor scalability during training, which becomes critical when considering more diverse and larger datasets. The authors observed more than a tenfold speedup during training with PaiNN compared to kernel ridge regression.

In the long term, neural network models such as PaiNN could and likely will replace quantum chemistry methods for certain tasks in studying particle formation, including conformational sampling and molecular dynamics. This will enable researchers to study larger and more complex structures and reactions at the particle-gas interface. Such knowledge can improve models of new particle formation and how it affects climate and air quality.

The Clusteromics datasets and other atmospheric cluster data are freely available on [Jonas Elm’s GitHub page](https://github.com/elmjonas/ACDB).
