---
title: Events
permalink: /events/
---
{% if author.googlescholar %}
{% endif %}
{% include base_path %}

<!-- NOTE! NEW NEWS ARE ADDED AS POSTS IN events/_posts! //-->
<!-- THIS FILE NEEDS EDITING ONLY IF THE PRESENTATION OF THE PROJECTS NEED TO CHANGE. //-->

{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}

{% for p in site.categories.events %}

## {{ p.title }}
{% if p.event_date %}
<span style="color:grey;">**Event date:** *{{p.event_date | date: '%Y-%m-%d'}}*</span>
{% endif %}

{% if p.image %}
<img src="{{ p.image }}" style="float: right; width: 25%;" />
{% endif %}

{% if p.shortversion %}{{ p.shortversion }}{% endif %}

*{% if p.people %}{{ p.people | join: ", " }}{% endif %}*

**[p.permalink](Read more!)**

{% endfor %}

