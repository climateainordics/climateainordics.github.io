---
title: Featured members
permalink: /job-openings/
---
{% include base_path %}

<!-- NOTE! NEW NEWS ARE ADDED AS POSTS IN news/_posts! //-->
<!-- THIS FILE NEEDS EDITING ONLY IF THE PRESENTATION OF THE PROJECTS NEED TO CHANGE. //-->

On this page, you will find the history of job openings (i.e. AI-climate-environment relevant jobs across the Nordics) posted at Climate AI Nordics. Note that we do **not** maintain the links, which may become obsolete as application deadlines pass. These are also posted in our newsletter; [join us to recieve the newsletter](https://climateainordics.com/join/)!

[Click here to see the newsletter archive](https://climateainordics.com/newsletter/).

{% capture nowunix %}{{'now' | date: '%s'}}{% endcapture %}

{% for p in site.posts %}
  {% if p.categories contains "job-openings" %}

<!--## {{ p.people | first }}--> KEEP SOME OF THIS THAT I COMMENTED OUT?
{% if p.image %}<img src="{{ p.image }}" style="float: right; width: 25%;" />{% endif %}


<span style="color:grey;">*{{p.date | date: '%Y-%m-%d'}}{% if p.categories contains "job-openings" %}; Job Opening{% endif %}*</span>

{% if p.summary %}{{ p.summary }}{% endif %}

{% if p.content  %}**[Read more!]({{ p.url }})**{% endif %}

{% endif %}

{% endfor %}
