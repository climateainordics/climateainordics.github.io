---
title: Featured projects and papers
permalink: /featured-project-paper/
---
{% include base_path %}

<!-- NOTE! NEW NEWS ARE ADDED AS POSTS IN news/_posts! //-->
<!-- THIS FILE NEEDS EDITING ONLY IF THE PRESENTATION OF THE PROJECTS NEED TO CHANGE. //-->

On this page, you will find the history of featured projects and papers in Climate AI Nordics. Each month, we feature one specific project or paper from members within Climate AI Nordics. [Join us to recieve the newsletter](https://climateainordics.com/join/)!

[Click here to see the newsletter archive](https://climateainordics.com/newsletter/).

{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}

{% for p in site.posts %}
  {% if p.categories contains "featured-paper" %}

<!--## {{ p.people | first }} -- TODO: KEEP SOME IN THIS COMMENT? -->
{% if p.image %}<img src="{{ p.image }}" style="float: right; width: 25%;" />{% endif %}

<span style="color:grey;">*{{p.date | date: '%Y-%m-%d'}}{% if p.categories contains "job-openings" %}; Job Opening{% endif %}*</span>

{% if p.summary %}{{ p.summary }}{% endif %}

{% if p.content  %}**[Read more!]({{ p.url }})**{% endif %}

{% endif %}

{% endfor %}
