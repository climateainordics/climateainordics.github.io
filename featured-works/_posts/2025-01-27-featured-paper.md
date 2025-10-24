---
title: "Featured Paper: Deep learning-enhanced detection of road culverts in high-resolution digital elevation models: Improving stream network accuracy in Sweden"
summary: "The new Climate AI Nordics Featured Paper is \"Deep learning-enhanced detection of road culverts in high-resolution digital elevation models: Improving stream network accuracy in Sweden\" by William Lidberg. In this work, Lidberg combines LiDAR data and aerial imagery with deep learning to detect 87 % of all road culverts in Sweden. These culverts are in turn used to increase the accuracy of maps featuring small watercourses."
abstract: "In this work, Lidberg combines LiDAR data and aerial imagery with deep learning to detect 87 % of all road culverts in Sweden. These culverts are in turn used to increase the accuracy of maps featuring small watercourses."
socialmedia: "Deep learning-enhanced detection of road culverts in high-resolution digital elevation models: Improving stream network accuracy in Sweden."
people:
- Aleksis Pirinen
image: /images/posts/2025-01-29-featured-paper.png
---
Authors: **William Lidberg**

The new Climate AI Nordics Featured Paper is "Deep learning-enhanced detection of road culverts in high-resolution digital elevation models: Improving stream network accuracy in Sweden" by William Lidberg. In this work, Lidberg combines LiDAR data and aerial imagery with deep learning to detect 87 % of all road culverts in Sweden. These culverts are in turn used to increase the accuracy of maps featuring small watercourses.

The paper focuses on using deep learning to detect road culverts and improve stream network mapping in Sweden. It addresses challenges posed by road embankments that disrupt hydrological modeling in high-resolution digital elevation models (DEMs). By training a Residual Attention UNet (RA-UNet) architecture on data from 28,512 field-mapped culverts and combining LiDAR-derived topographical indices with aerial imagery, the study achieved an 87% detection rate for culverts in test datasets. These detections were incorporated into DEMs to enhance the accuracy of extracted stream networks.

The inclusion of detected culverts in DEM preprocessing improved hydrological modeling by correcting artificial barriers in the digital landscape. This approach enhanced stream-road intersections, with the RA-UNet performing better than traditional DEM pre-processing methods like least-cost breaching and road removal. Overall, this research demonstrates the feasibility of deep learning for large-scale culvert detection and stream network enhancement, offering practical applications for hydrological modeling, land use planning, and forestry management. Future work could explore reducing false positives, incorporating additional data sources like infrared imagery, and optimizing stream initiation thresholds across diverse landscapes.

For a comprehensive understanding, we encourage readers to explore [the full paper](https://www.sciencedirect.com/science/article/pii/S221458182400497X).

Code is available [here](https://github.com/williamlidberg/DeepBreach).

Lidberg's work on culvert mapping is already being used by several Swedish agencies.
