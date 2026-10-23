---
abstract: Physics-guided AI for high-resolution air quality forecasting that explicitly models how wind and terrain influence pollutant transport.
image: /images/posts/topoflow-figure.png
image_small: /images/posts/topoflow-figure.png
people:
- Helmi Toropainen
- Michael Boy
- Zhi-Song Liu
summary: "This month's Climate AI Nordics featured paper is \"TopoFlow: topography-aware pollutant Flow learning for high-resolution air quality prediction\". This work introduces a physics-guided transformer that incorporates wind and topography directly into the model to improve air quality forecasting."
title: 'Featured paper: TopoFlow: topography-aware pollutant Flow learning for high-resolution air quality prediction'
---

Authors: Ammar Kheder, Helmi Toropainen, Wenqing Peng, Samuel Antão, Jia Chen, Michael Boy*, Zhi-Song Liu

The latest Climate AI Nordics featured paper is [_TopoFlow: Topography-Aware Pollutant Flow Learning for High-Resolution Air Quality Prediction_](https://doi.org/10.1038/s41612-026-01417-5),
published in NPJ Climate and Atmospheric Science.

Accurately forecasting air pollution remains challenging, especially in regions with complex terrain where mountains and valleys strongly influence how pollutants move and accumulate.
This paper introduces [_TopoFlow_](https://github.com/AmmarKheder/TopoFlow), a physics-guided transformer model that explicitly incorporates two key drivers of pollutant transport:
wind direction and topography. Rather than treating these factors as just additional inputs, they are built directly into the model architecture.

Using six years of air quality and weather data across China, _TopoFlow_ achieves state-of-the-art performance, reducing prediction errors by 13% compared to leading ML baselines and by
71-80% compared to operational forecasting systems for PM₂.₅ pollution. The model also demonstrates strong performance across multiple pollutants and forecast horizons up to four days ahead.

**Why it matters for climate and the environment:** Better air quality forecasts support public health, environmental management, and policy decisions. By bringing physical knowledge directly
into AI architectures, TopoFlow highlights how domain-aware machine learning can provide more reliable predictions for complex environmental systems, helping societies respond more
effectively to pollution and environmental risks.

For more details, explore:
- [Paper](https://doi.org/10.1038/s41612-026-01417-5)
- [Code](https://github.com/AmmarKheder/TopoFlow)
- [Project page](https://ammarkheder.github.io/TopoFlow/)
