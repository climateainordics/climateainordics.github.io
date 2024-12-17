---
title: "Climate AI Nordics Newsletter"
excerpt: "Climate AI Nordics Newsletter"
permalink: /generate-newsletter/
previous_newsletter: 2024-11-22
---

<style>
body{font-family: arial, sans-serif;} img{ float: right; width: 8em; margin: 0.4em;} p{margin: .6em 0.2em .6em 0.2em;} h1{margin: .6em 0.2em .6em 0.2em;} h2{margin: .6em 0.2em .6em 0.2em;} h3{margin: .6em 0.2em .6em 0.2em;} h4{margin: .6em 0.2em .6em 0.2em;}
</style>

Welcome to the *Climate AI Nordics* Newsletter {{ "now" | date: "%B %Y" }}.

**Email us at [contact@climateainordics.com](mailto:contact@climateainordics.com) to contribute your own relevant news! We will include news on our web page, [climateainordics.com](https://climateainordics.com), and in our newsletter. Some announcements will also be communicated in social media. Take the chance of showcasing your work or your events to the community!**

Since the launch in October, the network has grown to 53 people spread over the Nordic countries. Do you know researchers who works in the intersection of AI and Climate Change? Tell them about Climate AI Nordics! [climateainordics.com/join](https://climateainordics.com/join).

{% capture nowtime %}{{'now' | date: '%s'}}{% endcapture %}
{% capture previous_newsletter_time %}{{ page.previous_newsletter | date: '%s' }}{% endcapture %}
{% capture newsletter_start_time %}{{ previous_newsletter_time | plus: 86400 }}{% endcapture %}

{% assign items_listed = false %}

{% comment %} FIRST, first_page ITEMS!!! {% endcomment %}

# News

{% for p in site.posts %}
{% if p.categories contains 'newsletter' %}{% continue %}{% endif %}
{% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}
{% if posttime < newsletter_start_time %}
{% continue %}
{% endif %}

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
{% capture printdate %}*This event takes place {{ p.event_date }}.*{% endcapture %}
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

{{printdate}} {{ p.shortversion }}<br />
**[(Read more)](https://climateainordics.com{{ p.url }})**
{% endunless %}
{% endfor %}

{% unless items_listed %}There are no coming events at this time.{% endunless %}

{% comment %} FINALLY, EVENTS THAT HAS ALREADY HAPPENED!!! {% endcomment %}

<br clear=all />

# Recent events

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

{% unless items_listed %}There are no recent events at this time.{% endunless %}

# Some members of the network did not receive last month's newsletter.

Unfortunately, the November email got stuck in many people's spam folders. Either look there, or read the contents online: [climateainordics.com/newsletter/2024-11-22-november-2024/](https://climateainordics.com/newsletter/2024-11-22-november-2024/).

# Spread the word!

Climate AI Nordics is present on [LinkedIn](https://www.linkedin.com/company/climate-change-ai-nordics/) and [BlueSky](https://bsky.app/profile/climateainordics.com). Follow us and repost our stories so that we get the most impact! Also make sure to share your work with us, by sending us an email ([contact@climateainordics.com](mailto:contact@climateainordics.com)) or some other channel, and we'll add it to the news feed!

*Climate AI Nordics is a [network of researchers](/people/) dedicated to developing and utilizing AI technologies to address the urgent global challenge of climate change. Our researchers focus on creating and promoting AI solutions that support both climate change mitigation, reducing the severity of climate change, and adaptation, adjusting to the effects of climate change. We are already in a climate emergency which is causing biodiversity loss, extreme weather events, and human suffering, and this necessitates a multifaceted approach involving both policy change, limitations on activities contributing to climate change, and bolstering societal resilience against climate-related events.*

*Climate AI Nordics promotes the development of AI-based analytical tools and optimization techniques that can inform decision-making processes crucial for ensuring a sustainable future for generations to come. In particular, we recognize that technology, particularly AI-based solutions, can play a role in supporting efforts such as rewilding, rewetting, and reducing emissions and the reliance on fossil fuels.*

*By bringing together researchers in the Nordic countries, Climate AI Nordics aims to:*

* *Foster collaboration and knowledge exchange through seminars and workshops.*
* *Help develop AI-driven solutions that contribute to the creation of climate-friendly products and services, optimize processes for efficiency and sustainability, and promote justice in addressing the impacts of climate change.*

*We hope that the collaborative nature of Climate AI Nordics will accelerate progress in this critical field, enabling the sharing of expertise and resources to develop impactful AI solutions for climate change mitigation and adaptation.*

