---
title: News
permalink: /news/
---
{% if author.googlescholar %}
{% endif %}
{% include base_path %}

<!-- NOTE! NEW NEWS ARE ADDED AS POSTS IN news/_posts! //-->
<!-- THIS FILE NEEDS EDITING ONLY IF THE PRESENTATION OF THE PROJECTS NEED TO CHANGE. //-->

{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}

{% for p in site.categories.news %}

## {{ p.title }}
<span style="color:grey;">*{{p.date | date: '%Y-%m-%d'}}*</span>

{% if p.image %}
<img src="{{ p.image }}" style="float: right; width: 25%;" />
{% endif %}

{% if p.shortversion %}{{ p.shortversion }}{% endif %}

{% if p.content  %}**[Read more!]({{ p.url }})**{% endif %}

{% endfor %}

