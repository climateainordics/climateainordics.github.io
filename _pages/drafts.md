---
permalink: /drafts/
title: "Climate AI Nordics Drafts"
excerpt: "Climate AI Nordics Drafts"
---


Welcome to the _Climate AI Nordics_ Drafts!

The list of posts below are not yet officially published.

# Posts

{% for p in site.categories.drafts %}
## {{ p.title }}
{% if p.image_small %}<img src="{{ p.image_small }}" style="float: right; width: 25%;" />{% elsif p.image %}<img src="{{ p.image }}" style="float: right; width: 25%;" />{% endif %}

{{ p.summary }}

[**Read more**]({{ p.url }})
{% endfor %}


