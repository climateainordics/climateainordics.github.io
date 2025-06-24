---
permalink: /
title: "Climate AI Nordics"
excerpt: "Climate AI Nordics"
---

<style>
img {
  width: 8em;
  float: right;
}
table {
border-width: 0;
}
tr {
border-width: 0;
}
td {
border-width: 0;
}
</style>

Welcome to _Climate AI Nordics_. We are a [network of researchers](/people/) dedicated to developing and utilizing AI technologies to address the urgent global challenge of climate change. Our researchers focus on creating and promoting AI solutions that support both climate change mitigation, reducing the severity of climate change, and adaptation, adjusting to the effects of climate change. We are already in a climate emergency which is causing biodiversity loss, extreme weather events, and human suffering, and this necessitates a multifaceted approach involving both policy change, limitations on activities contributing to climate change, and bolstering societal resilience against climate-related events.

{% for p in site.posts %}
{% if p.first_page %}> ## {{ p.title }}
{% if p.image %}> ![]({{ p.image }}){% else %}>{% endif %}
> {{ p.shortversion | replace: '\n', '\n> ' }}
> **[(Read more)]({{ p.url }})**
{% endif %}
{% endfor %}


Climate AI Nordics promotes the development of AI-based analytical tools and optimization techniques that can inform decision-making processes crucial for ensuring a sustainable future for generations to come. In particular, we recognize that technology, particularly AI-based solutions, can play a role in supporting efforts such as rewilding, rewetting, and reducing emissions and the reliance on fossil fuels.

By bringing together researchers in the Nordic countries, Climate AI Nordics aims to accelerate progress in this critical field, enabling the sharing of expertise and resources to develop impactful AI solutions for climate change mitigation and adaptation.

<!--
* Foster collaboration and knowledge exchange through seminars and workshops.
* Help develop AI-driven solutions that contribute to the creation of climate-friendly products and services, optimize processes for efficiency and sustainability, and promote justice in addressing the impacts of climate change.
We hope that the collaborative nature of Climate AI Nordics will accelerate progress in this critical field, enabling the sharing of expertise and resources to develop impactful AI solutions for climate change mitigation and adaptation.-->

[Join Climate AI Nordics now!](/join/)

## [News](/news/)


{% for p in site.categories.news limit: 3 %}
| &bull; | {{p.date | date: '%Y-%m-%d'}}: {{ p.title }} <br /> [(Read more)]({{ p.url }}) | {% if p.image %} ![]({{ p.image }}){% endif %} |
{%- endfor %}


## [Events](/events/)

{% for p in site.categories.events limit: 3 %}
| &bull; | {{p.event_date | date: '%Y-%m-%d'}}: {{ p.title }} <br /> [(Read more)]({{ p.url }}) | {% if p.image %} ![]({{ p.image }}){% endif %} |
{%- endfor %}


## [Job openings](/news/)

{% for p in site.categories.job-openings limit: 3 %}
| &bull; | {{p.event_date | date: '%Y-%m-%d'}}: {{ p.title }} <br /> [(Read more)]({{ p.url }}) | {% if p.image %} ![]({{ p.image }}){% endif %} |
{%- endfor %}


