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
    |{{post.event_date}}#{{ post.title }}#{{ post.image }}#{{ post.shortversion }}#{{ post.url  }}#{{ post.youtube }}
  {% endfor %}
{% endcapture %}

{% assign sorted_posts = posts | split: '|' | sort_natural %}

{% for p in sorted_posts %}
{% assign postarray = p | split: '#' %}
{% assign event_date = postarray[0] %}
{% assign event_time = postarray[1] %}
{% assign title = postarray[2] %}
{% assign image = postarray[3] %}
{% assign shortversion = postarray[4] %}
{% assign url = postarray[5] | strip %}
{% assign youtube = postarray[6] | strip %}

{% capture eventtimestamp %}{{ event_date | date: '%s'}}{% endcapture %}

## {{ title }}
{% if image %}<img src="{{ image }}" style="float: right; width: 25%;" />{% endif %}

<span style="color:grey;">**Event date:** *{{event_date | date: '%Y-%m-%d'}} {{ event_time }}*</span>

{% if eventtimestamp < nowtime %}
{% if youtube != "" %}
Click below to view the recording of this seminar!
{% else %}
This event has already happened. Stay tuned for more events like these!
{% endif %}
{% endif %}
{{ shortversion }}

{% if youtube %}
**[View recorded seminar!]({{ url }})**
{% else %}
**[Read more!]({{ url }})**
{% endif %}

{% endfor %}

