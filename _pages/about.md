---
permalink: /
title: "Climate Change AI Nordics"
excerpt: "Climate Change AI Nordics"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


Welcome to _Climate Change AI Nordics_.
We're a [network of researchers](https://ccai.cc/people/) who work on problems related to tackling climate change using AI and machine learning. We also host seminars and workshops, and send an occasional email.

## [News](/news/)

{% for p in site.categories.news limit: 5 %}
* {{p.date | date: '%Y-%m-%d'}}: {{ p.title }} [(Read more)]({{ p.url }})
{% endfor %}


## [People](/people/)

* [Olof Mogren, PhD, RISE Research Institutes of Sweden](https://mogren.one/)


