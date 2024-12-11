---
permalink: /
title: "Climate Change AI Nordics"
excerpt: "Climate Change AI Nordics"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
img {
  width: 8em;
  float: right;
}
</style>

Welcome to _Climate Change AI Nordics_.

We are a [network of researchers](/people/) dedicated to developing and utilizing AI technologies to address the urgent global challenge of climate change. Our researchers focus on creating and promoting AI solutions that support both climate change mitigation, reducing the severity of climate change, and adaptation, adjusting to the effects of climate change. We are already in a climate emergency which is causing biodiversity loss, extreme weather events, and human suffering, and this necessitates a multifaceted approach involving both policy change, limitations on activities contributing to climate change, and bolstering societal resilience against climate-related events.

CCAI Nordics strongly supports the pioneering work of the global non-profit organization *Climate Change AI* ([climatechange.ai](https://climatechange.ai)). However, there is no affiliation between the two. CCAI Nordics shares similar goals, but is a regional network for researchers in the Nordic countries.

{% for p in site.posts %}
{% if p.first_page %}
> ## {{ p.title }}
{% if p.image %}
> ![]({{ p.image }})
{ endif }
> {{ p.shortversion | replace: '\n', '\n> ' }}
> **[(Read more)]({{ p.url }})**
{% endif %}
{% endfor %}


CCAI Nordics promotes the development of AI-based analytical tools and optimization techniques that can inform decision-making processes crucial for ensuring a sustainable future for generations to come. In particular, we recognize that technology, particularly AI-based solutions, can play a role in supporting efforts such as rewilding, rewetting, and reducing emissions and the reliance on fossil fuels.

By bringing together researchers in the Nordic countries, CCAI Nordics aims to:

* Foster collaboration and knowledge exchange through seminars and workshops.
* Help develop AI-driven solutions that contribute to the creation of climate-friendly products and services, optimize processes for efficiency and sustainability, and promote justice in addressing the impacts of climate change.

We hope that the collaborative nature of CCAI Nordics will accelerate progress in this critical field, enabling the sharing of expertise and resources to develop impactful AI solutions for climate change mitigation and adaptation.

[Join Climate Change AI Nordics now!](/join/)

## [News](/news/)

{% for p in site.categories.news limit: 5 %}
* {{p.date | date: '%Y-%m-%d'}}: {{ p.title }}\
[(Read more)]({{ p.url }})
{% endfor %}


## [Events](/events/)

{% for p in site.categories.events limit: 5 %}
* {{p.event_date | date: '%Y-%m-%d'}}: {{ p.title }}\
[(Read more)]({{ p.url }})
{% endfor %}


