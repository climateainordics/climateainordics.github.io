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
## {{ p.title }}
{% if p.image_small %}<img src="{{ p.image_small }}" style="float: right; width: 25%;" />{% elsif p.image %}<img src="{{ p.image }}" style="float: right; width: 25%;" />{% endif %}

{{ p.summary }}

[**Read more**]({{ p.url }})
{% endfor %}


