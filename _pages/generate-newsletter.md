---
title: "Climate AI Nordics Newsletter"
excerpt: "Climate AI Nordics Newsletter"
permalink: /generate-newsletter/
previous_newsletter: 2025-03-27
---

<style>
body{font-family: arial, sans-serif;} img{ float: right; width: 8em; margin: 0.4em;} p{margin: .6em 0.2em .6em 0.2em;} h1{margin: .6em 0.2em .6em 0.2em;} h2{margin: .6em 0.2em .6em 0.2em;} h3{margin: .6em 0.2em .6em 0.2em;} h4{margin: .6em 0.2em .6em 0.2em;}
</style>

Welcome to the *Climate AI Nordics* Newsletter {{ "now" | date: "%B %Y" }}.

Since the launch in October, the network has grown to 
{% include people_from_form_count_number_only_nordics.md %}
people spread over the Nordic countries
({% include people_from_form_count_number_total.md %} including international supporting affiliates).
Do you know researchers who works in the intersection of AI and Climate Change? Tell them about Climate AI Nordics! [climateainordics.com/join](https://climateainordics.com/join).

{% capture nowtime %}{{'now' | date: '%s'}}{% endcapture %}
{% capture previous_newsletter_time %}{{ page.previous_newsletter | date: '%s' }}{% endcapture %}
{% capture newsletter_start_time %}{{ previous_newsletter_time | plus: 86400 }}{% endcapture %}

{% assign items_listed = false %}

{% comment %} FIRST, first_page ITEMS!!! {% endcomment %}

# News

{% for p in site.posts %}
{% if p.categories contains 'newsletter' %}{% continue %}{% endif %}
{% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}

{% if p.first_page %}
{% assign items_listed = true %}

<br clear=all />

## {{ p.title }}

{% if p.image %}
![](https://climateainordics.com{{ p.image  }})
{% endif %}

{% if p.event_date %}*{{ p.event_date }}*{% else %}*{{ p.date | date: '%Y-%m-%d' }}*{% endif %} {{ p.shortversion }}<br />
**[(Read more)](https://climateainordics.com{{ p.url }})**
{% endif %}
{% endfor %}

{% comment %} NEXT, NEWS!!! {% endcomment %}

{% for p in site.posts %}
{% if p.categories contains 'newsletter' %}{% continue %}{% endif %}
{% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}
{% if posttime < newsletter_start_time %}
{% continue %}
{% endif %}

{% if p.event_date %}
{% continue %}
{% else %}
{% capture printdate %}*{{ p.date | date: '%Y-%m-%d' }}*{% endcapture %}
{% endif %}

{% unless p.first_page %}
{% assign items_listed = true %}

<br clear=all />

## {{ p.title }}

{% if p.image %}
![](https://climateainordics.com{{ p.image  }})
{% endif %}

{{printdate}} {{ p.shortversion }}<br />
**[(Read more)](https://climateainordics.com{{ p.url }})**
{% endunless %}
{% endfor %}

{% unless items_listed %}No current news.{% endunless %}

{% comment %} NEXT, EVENTS THAT HAS NOT YET HAPPENED!!! {% endcomment %}

<br clear=all />

# Coming events

{% assign items_listed = false %}

{% for p in site.posts %}
{% if p.categories contains 'newsletter' %}{% continue %}{% endif %}

{% if p.event_date %}
{% capture eventtime %}{{ p.event_date | date: '%s'}}{% endcapture %}
{% if eventtime < nowtime %}
{% continue %}
{% endif %}
{% capture printdate %}*Event date: {{ p.event_date }}.*{% endcapture %}
{% else %}
{% continue %}
{% endif %}

{% unless p.first_page %}
{% assign items_listed = true %}

<br clear=all />

## {{ p.title }}

{% if p.image %}
![](https://climateainordics.com{{ p.image  }})
{% endif %}

{{printdate}}

{{ p.shortversion }}<br />
**[(Read more)](https://climateainordics.com{{ p.url }})**
{% endunless %}
{% endfor %}

{% unless items_listed %}There are no coming events at this time.{% endunless %}

{% comment %} FINALLY, EVENTS THAT HAS ALREADY HAPPENED!!! {% endcomment %}

{% for i in (1..2) %}
  {% comment %} TWO ITERATIONS, FIRST TO CHECK IF ANY POSTS AVAILABLE {% endcomment %}

  {% if i == 2 %}
    {% if items_listed %}
<br clear=all />

# Recent events
    {% else %}
      {% comment %} There are no recent events at this time.{% endcomment %}
      {% break %}
    {% endif %}
  {% endif %}
  {% assign items_listed = false %}

  {% for p in site.posts %}
    {% if p.categories contains 'newsletter' %}{% continue %}{% endif %}
    {% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}
    {% if posttime < newsletter_start_time %}
      {% continue %}
    {% endif %}

    {% if p.event_date %}
      {% capture eventtime %}{{ p.event_date | date: '%s'}}{% endcapture %}
      {% if eventtime > nowtime %}
        {% continue %}
      {% endif %}
      {% capture printdate %}*This event took place {{ p.event_date }}.*{% endcapture %}
    {% else %}
      {% continue %}
    {% endif %}

    {% unless p.first_page %}
      {% assign items_listed = true %}

      <br clear=all />

      ## {{ p.title }}

      {% if p.image %}
        ![](https://climateainordics.com{{ p.image  }})
      {% endif %}

      {{ printdate }} {{ p.shortversion }}<br />
      **[(Read more)](https://climateainordics.com{{ p.url }})**
    {% endunless %}
  {% endfor %}

{% endfor %}


# Your news in the newsletter!

**Make sure to share your work with us, by sending us an email ([contact@climateainordics.com](mailto:contact@climateainordics.com)), posting in our Slack or some other channel, and we'll add it to the news feed! Take the chance of showcasing your work or your events to the community!**

Also be sure to follow us on [LinkedIn](https://www.linkedin.com/company/climate-ai-nordics/) and [BlueSky](https://bsky.app/profile/climateainordics.com). Climate AI Nordics will have the most impact if you repost and like our stories!

**[Climate AI Nordics](https://climateainordics.com/)** is a network of [researchers](https://climateainordics.com//people/) working to harness AI in tackling the climate crisis through both mitigation and adaptation.

We promote AI-based tools and optimization methods that support sustainable decision-making—helping reduce emissions, restore ecosystems, and build climate resilience.

