---
title: People
permalink: /people/
---
{% include base_path %}

<style>
img {
  width: 8em;
  float: right;
  padding: 1em 0em 1em 1em;
}
.hidden {
  display: none;
}
.content {
  overflow: auto;
}
</style>



Welcome to _Climate AI Nordics_.
We're a network of researchers who work on problems related to tackling climate change using AI and machine learning. Climate AI Nordics acts as a hub, hosting and announcing news, seminars, and workshops. [Join us](/join/)!

## This month's featured member

{% for p in site.categories.featured-member limit: 1 %}
{% if p.image %} ![]({{ p.image }}){% endif %}

**{{ p.people | first }}** 

{{ p.summary }}

[Read more about {{ p.people | first }}!]({{ p.url }})
{%- endfor %}

[List all monthly featured members!](/featured-member/)


{% include people-from-form-count.md %}

{% include people-dropdown.md %}

{% include board-from-form.md %}

{% include people-from-form.md %}

