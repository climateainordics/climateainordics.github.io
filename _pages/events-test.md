---
title: Events
permalink: /events-test/
---
{% if author.googlescholar %}
{% endif %}
{% include base_path %}

<!-- NOTE! NEW NEWS ARE ADDED AS POSTS IN events/_posts! //-->
<!-- THIS FILE NEEDS EDITING ONLY IF THE PRESENTATION OF THE PROJECTS NEED TO CHANGE. //-->

{% capture nowtime %}{{'now' | date: '%s'}}{% endcapture %}

{% capture posts %}
  {% for post in site.categories.events %}
    |{{ post.title }}#{{ post.event_date }}#{{ post.shortversion }}#{{ post.url  }}
  {% endfor %}
{% endcapture %}

{% assign sorted_posts = posts | split: '|' | sort | shift %}

{% for p in sorted_posts %}
{% assign postarray = p | split: '#' %}
{% assign title = postarray[0] %}
{% assign event_date = postarray[1] %}
{% assign shortversion = postarray[2] %}
{% assign url = postarray[3] %}

{% capture eventtime %}{{ event_date | date: '%s'}}{% endcapture %}

## {{ title }}
{% if image %}<img src="{{ image }}" style="float: right; width: 25%;" />{% endif %}

<span style="color:grey;">**Event date:** *{{event_date | date: '%Y-%m-%d'}}*</span>

{% if eventtime < nowtime %}This event has already happened. Stay tuned for more events like these!{% endif %}
{{ shortversion }}

**[Read more!]({{ url }})**

{% endfor %}

