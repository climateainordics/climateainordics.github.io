---
title: Events
permalink: /recorded-events/
---
{% include base_path %}

Welcome to our list of recordings from previous talks! [Click here](/recorded-events/) to see  a list of coming events!

<!-- NOTE! NEW NEWS ARE ADDED AS POSTS IN events/_posts! //-->
<!-- THIS FILE NEEDS EDITING ONLY IF THE PRESENTATION OF THE EVENTS NEED TO CHANGE. //-->

{% capture nowtime %}{{'now' | date: '%s'}}{% endcapture %}

{% capture posts %}
  {% for post in site.categories.events %}
    {% unless post.youtube == blank %}
    |||||{{post.event_date}}#####{{ post.event_time }}#####{{ post.title }}#####{{ post.image }}#####{{ post.summary }}#####{{ post.url  }}#####{{ post.youtube }}
    {% endunless %}
  {% endfor %}
{% endcapture %}

{% assign sorted_posts = posts | split: '|||||' | shift |  sort_natural | reverse %}

{% for p in sorted_posts %}
{% assign postarray = p | split: '#####' %}
{% assign event_date = postarray[0] %}
{% assign event_time = postarray[1] %}
{% assign title = postarray[2] %}
{% assign image = postarray[3] %}
{% assign summary = postarray[4] %}
{% assign url = postarray[5] | strip %}
{% assign youtube = postarray[6] | strip %}

{% capture eventtimestamp %}{{ event_date | date: '%s'}}{% endcapture %}

## {{ title }}

<span style="color:grey;">**Event date:** *{{event_date | date: '%Y-%m-%d'}}* {% unless event_time == blank %}*{{ event_time }}*{% endunless %}</span>

<iframe width="560" height="315" src="https://www.youtube.com/embed/{{ page.youtube }}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<br />

**[Read more!]({{ url }})**

{% endfor %}

