---
image: /images/posts/wikimpacts-img.png
image_small: /images/posts/wikimpacts-img_small.png
people:
- Shorouq Zahra
- Murathan Kurfalı
summary: Wikimpacts 1.0 is an open-access global database of extreme climate event impacts built by extracting structured data from Wikipedia using large language models and natural language processing. Developed with contributions from RISE researchers as part of the CLIMES Center of Excellence (a partner organisation to Climate AI Nordics), Wikimpacts covers over 2,700 historical events and introduces granular sub-national impact data to empower climate resilience research.
title: 'Featured project: Wikimpacts - Automated global climate impact database'
---

**Authors:** Ni Li, Wim Thiery, *Shorouq Zahra*, Mariana Madruga de Brito, Koffi Worou, *Murathan Kurfalı*, Seppe Lampe, Paul Muñoz, Clare Flynn, Camila Trigoso, *Joakim Nivre*, Jakob Zscheischler, and *Gabriele Messori*

**Project website:** [https://www.wikimpacts.eu/](https://www.wikimpacts.eu/)  
**Data repository:** [https://bolin.su.se/data/li-2025-wikimpacts-1.0.final](https://bolin.su.se/data/li-2025-wikimpacts-1.0.final)  
**Research paper:** [https://doi.org/10.5194/nhess-26-2609-2026](https://doi.org/10.5194/nhess-26-2609-2026)  
**Recorded talk:** [Shorouq Zahra on Wikimpacts on YouTube](https://www.youtube.com/watch?v=O9jZz1V_ktA)

# The climate impact data gap

Understanding the socioeconomic damage caused by climate extremes, such as storms, floods, heatwaves, wildfires, and droughts, is essential for climate adaptation, loss-and-damage assessment, and disaster risk reduction. However, existing global disaster databases often suffer from significant geographical coverage gaps, reporting discrepancies, and limited spatial resolution. For instance, benchmark datasets frequently miss severe extreme events across regions such as Africa or Latin America, or report widely conflicting damage figures for the same event.

Traditionally, curating disaster impact records has required laborious manual human extraction from disaster reports and news articles, severely constraining how fast and comprehensively databases can be updated.

# How Wikimpacts is solving it

**Wikimpacts 1.0** tackles this bottleneck by utilizing Natural Language Processing (NLP) and Large Language Models (LLMs) to automatically extract, structure, and geocode disaster impact data from Wikipedia. Important contributions have been made by Climate AI Nordics researchers **Shorouq Zahra**, **Murathan Kurfalı**, **Joakim Nivre**, and **Gabriele Messori**, under **CLIMES** (The Swedish Centre for Impacts of Climate Extremes), a [partner organisation to **Climate AI Nordics**](/partners/).

The resulting database contains:
* **2,726 extreme climate events** spanning historical records from 1034 to 2024.
* **Multi-level spatial granularity**, including 17,912 national-level records and 32,343 sub-national (regional, county, and city) impact entries.
* **Systematic impact indicators**, capturing fatalities, injuries, displaced persons, homelessness, damaged or destroyed buildings, and economic/insured losses.

# The NLP and LLM pipeline

Extracting reliable tabular data from unstructured free-form text requires far more than just prompting an LLM. The Wikimpacts team designed a resilient multi-stage pipeline:

1. **Document retrieval & filtering:** Wikipedia articles are initially retrieved through keyword filtering and then screened using a fine-tuned BERT text classifier to remove false positives (e.g., sports teams like the Miami Hurricanes).
2. **Information extraction:** Target articles are processed with LLMs (including GPT-4o as well as fine-tuned open-weight models such as Mistral and Qwen) to extract event parameters, distinction of true zeros versus missing values (`null`), numerical uncertainty ranges, and geographic entities.
3. **Rigorous post-processing:** A deterministic pipeline using rule-based parsing, part-of-speech tagging, and regular expressions resolves JSON formatting errors, normalizes complex international date formats, converts numerical text intervals, and standardizes currency and inflation metrics.
4. **Geocoding:** Extracted place names are mapped to standardized spatial borders and OpenStreetMap coordinates, outputting GeoJSON polygon and point geometries directly suited for spatial climate modeling.

In rigorous benchmark evaluations against expert-annotated events, Wikimpacts 1.0 achieved low error rates—particularly for event timing (0.05), fatalities (0.03), and economic damage (0.12).

# What's next

While Wikimpacts 1.0 significantly expands the coverage and sub-national detail of disaster records, the team is working on several next-generation improvements:
* **Multi-lingual expansion:** Extending the extraction pipeline beyond English to Wikipedia editions in Spanish, Chinese, French, and local news sources to counteract systemic geographical coverage biases.
* **Open-source local deployments:** Transitioning further toward fine-tuned open-source LLMs (such as Mistral) so that research institutions can run and reproduce impact extraction pipelines locally without relying on closed proprietary APIs.
* **Compound events:** Developing modeling capabilities to handle cascading and compound hazards (such as hurricanes triggering compounding flash floods and landslides).

