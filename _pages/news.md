---
title: News
permalink: /news/
---
{% include base_path %}

<!-- NOTE! NEW NEWS ARE ADDED AS POSTS IN news/_posts! //-->
<!-- THIS FILE NEEDS EDITING ONLY IF THE PRESENTATION OF THE PROJECTS NEED TO CHANGE. //-->

On this page, you will find the news items communicated by Climate AI Nordics. Each month, we collect recent news and communicate them in a newsletter. [Join us to recieve the newsletter](https://climateainordics.com/join/)!

[Click here to see the newsletter archive](https://climateainordics.com/newsletter/).

{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}

{% for p in site.categories.news %}

## {{ p.title }}
{% if p.image %}<img src="{{ p.image }}" style="float: right; width: 25%;" />{% endif %}

<span style="color:grey;">*{{p.date | date: '%Y-%m-%d'}}*</span>

{% if p.shortversion %}{{ p.shortversion }}{% endif %}

{% if p.content  %}**[Read more!]({{ p.url }})**{% endif %}

{% endfor %}

