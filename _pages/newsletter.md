---
permalink: /newsletter/
title: "Climate AI Nordics Newsletter"
excerpt: "Climate AI Nordics Newsletter"
---


Welcome to the _Climate AI Nordics_ Newsletter!

The newsletter is distributed to all members of Climate AI Nordics.

[Join Climate AI Nordics now!](/join/)

# Issues

{% for p in site.categories.newsletter %}
## {{p.date | date: '%Y-%m-%d'}}: {{ p.title }}
{% if p.image %}<img src="{{ p.image }}" style="float: right; width: 25%;" />{% endif %}

{{ p.shortversion }}

[**Read more**]({{ p.url }})
{% endfor %}


