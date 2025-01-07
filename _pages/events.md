---
title: Events
permalink: /events/
---
{% if author.googlescholar %}
{% endif %}
{% include base_path %}

<!-- NOTE! NEW NEWS ARE ADDED AS POSTS IN events/_posts! //-->
<!-- THIS FILE NEEDS EDITING ONLY IF THE PRESENTATION OF THE PROJECTS NEED TO CHANGE. //-->

{% capture nowtime %}{{'now' | date: '%s'}}{% endcapture %}

{% assign sorted_posts = site.categories.events | sort: "event_date" %}

{% for p in sorted_posts %}
{% capture eventtime %}{{ p.event_date | date: '%s'}}{% endcapture %}

## {{ p.title }}
{% if p.image %}<img src="{{ p.image }}" style="float: right; width: 25%;" />{% endif %}

{% if p.event_date %}
<span style="color:grey;">**Event date:** *{{p.event_date | date: '%Y-%m-%d'}}*</span>
{% endif %}

{% if eventtime < nowtime %}This event has already happened. Stay tuned for more events like these!{% endif %}
{% if p.shortversion %}{{ p.shortversion }}{% endif %}

{% if p.content  %}**[Read more!]({{ p.url }})**{% endif %}

{% endfor %}

