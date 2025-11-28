---
title: "Climate AI Nordics Newsletter"
excerpt: "Climate AI Nordics Newsletter"
permalink: /generate-newsletter/
---
{% assign previous_newsletter = site.categories['newsletter'] | sort: 'date' | map: 'date' | last | date: "%Y-%m-%d" %}

{% capture nowtime %}{{'now' | date: '%s'}}{% endcapture %}
{% capture december %}{{'2025-12-01' | date: '%s'}}{% endcapture %}
{% capture previous_newsletter_time %}{{ previous_newsletter | date: '%s' }}{% endcapture %}
{% capture newsletter_start_time %}{{ previous_newsletter_time | plus: 86400 }}{% endcapture %}

<style>
body{font-family: arial, sans-serif;} img{ float: right; width: 8em; margin: 0.4em;} p{margin: .6em 0.2em .6em 0.2em;} h1{margin: .6em 0.2em .6em 0.2em;} h2{margin: .6em 0.2em .6em 0.2em;} h3{margin: .6em 0.2em .6em 0.2em;} h4{margin: .6em 0.2em .6em 0.2em;}
</style>

Welcome to the {{ "now" | date: "%B" }} edition of the Climate AI Nordics Newsletter!

{% if nowtime < december %}
This month, we are celebrating a major milestone that highlights the true power of this community. Our partner Klimatkollen has secured 3 million SEK from the Postcode Lottery Foundation for a project on AI-driven climate plan analysis—a collaboration with NORCE that was formed explicitly through connections made right here in this network.

In addition to this success story, we are marking our one-year anniversary with the launch of our official YouTube channel, giving you open access to our full archive of workshops and webinars.

As our network grows to 199 members across the Nordics and 72 international supporters, we look forward to seeing many of you in Copenhagen next month for EurIPS 2025. Until then, explore our latest updates, job opportunities, and featured research below.

If you know colleagues in academia, public agencies, or industry who should be part of this conversation, please invite them to join us at [climateainordics.com/join](https://climateainordics.com/join).

{% endif %}

Since launching in October 2024, our community has grown to 
{% include people_from_form_count_number_only_nordics.md %}
members across the Nordic region and 
{% include people_from_form_count_number_outside_nordics.md %} 
international supporters. Together, we connect researchers and practitioners working at the intersection of artificial intelligence and climate action—spanning mitigation, adaptation, and environmental monitoring.

If you know colleagues in academia, public agencies, or industry who share these interests, invite them to join us at
[climateainordics.com/join](https://climateainordics.com/join).

This month’s issue features community updates, job opportunities, and our featured member.


{% assign items_listed = false %}

{% comment %} FIRST, first_page ITEMS!!! {% endcomment %}

# News

{% for p in site.posts %}
{% unless p.categories contains 'news' %}{% continue %}{% endunless %}
{% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}

{% if p.first_page %}
{% assign items_listed = true %}

<br clear=all />

## {{ p.title }}

{% if p.image %}
![](https://climateainordics.com{{ p.image  }})
{% endif %}

{% if p.event_date %}*{{ p.event_date }}*{% else %}*{{ p.date | date: '%Y-%m-%d' }}*{% endif %} {{ p.summary }}<br />
**[Read more!](https://climateainordics.com{{ p.url }})**
{% endif %}
{% endfor %}

{% comment %} NEXT, NEWS!!! {% endcomment %}

{% for p in site.posts %}
{% unless p.categories contains 'news' %}{% continue %}{% endunless %}
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

{{printdate}} {{ p.summary }}<br />
**[Read more!](https://climateainordics.com{{ p.url }})**
{% endunless %}
{% endfor %}

{% unless items_listed %}No current news.{% endunless %}

{% comment %} ######### FEATURED WORK ########## {% endcomment %}

{% assign items_listed = false %}

{% for i in (1..2) %}
{% comment %} TWO ITERATIONS, FIRST TO CHECK IF ANY POSTS AVAILABLE {% endcomment %}

  {% if i == 2 %}
{% if items_listed %}

<br clear=all />

# Featured work

    {% else %}
      {% comment %} There is no featured work for this period.{% endcomment %}
      {% break %}
    {% endif %}
  {% endif %}
  {% assign items_listed = false %}

  {% for p in site.posts %}
    {% unless p.categories contains 'featured-works' %}{% continue %}{% endunless %}
    {% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}
    {% if posttime < newsletter_start_time %}
      {% continue %}
    {% endif %}

    {% assign items_listed = true %}
      {% if i == 2 %}
<br clear=all />

## {{ p.title }}

    {% if p.image %}
![](https://climateainordics.com{{ p.image  }})
    {% endif %}

{{ printdate }} {{ p.summary }}<br />
**[Read more!](https://climateainordics.com{{ p.url }})**
    {% endif %}
  {% endfor %}

{% endfor %}

{% comment %} ######### END, FEATURED WORK  ########## {% endcomment %}
{% comment %} ######### FEATURED MEMBER ########## {% endcomment %}

{% assign items_listed = false %}

{% for i in (1..2) %}
{% comment %} TWO ITERATIONS, FIRST TO CHECK IF ANY POSTS AVAILABLE {% endcomment %}

  {% if i == 2 %}
{% if items_listed %}


# Featured member

    {% else %}
      {% comment %} There are no featured members for this period.{% endcomment %}
      {% break %}
    {% endif %}
  {% endif %}
  {% assign items_listed = false %}

  {% for p in site.posts %}
    {% unless p.categories contains 'featured-member' %}{% continue %}{% endunless %}
    {% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}
    {% if posttime < newsletter_start_time %}
      {% continue %}
    {% endif %}

    {% assign items_listed = true %}
      {% if i == 2 %}
<br clear=all />

## {{ p.title }}

    {% if p.image %}
![](https://climateainordics.com{{ p.image  }})
    {% endif %}

{{ printdate }} {{ p.summary }}<br />
**[Read more!](https://climateainordics.com{{ p.url }})**
    {% endif %}
  {% endfor %}

{% endfor %}

{% comment %} ######### END, FEATURED MEMBER ########## {% endcomment %}

{% comment %} NEXT, EVENTS THAT HAS NOT YET HAPPENED!!! {% endcomment %}

<br clear=all />

# Coming events

{% assign items_listed = false %}

{% for p in site.posts reversed %}
  {% unless p.categories contains 'events' %}{% continue %}{% endunless %}

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

{{ p.summary }}<br />
**[Read more!](https://climateainordics.com{{ p.url }})**

  {% endunless %}
{% endfor %}

{% unless items_listed %}There are no coming events at this time.{% endunless %}

{% comment %} NEXT, EVENTS THAT HAS ALREADY HAPPENED!!! {% endcomment %}

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
    {% unless p.categories contains 'events' %}{% continue %}{% endunless %}
    {% capture eventtime %}{{ p.event_date | date: '%s'}}{% endcapture %}
    {% if eventtime < newsletter_start_time %}
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
        {% if i == 2 %}
<br clear=all />

## {{ p.title }}

      {% if p.image %}
![](https://climateainordics.com{{ p.image  }})
      {% endif %}

{{ printdate }} {{ p.summary }}<br />
        {% if p.youtube != "" %}
**[View recorded seminar!](https://climateainordics.com{{ p.url }})**
        {% else %}
**[Read more!](https://climateainordics.com{{ p.url }})**
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endfor %}

{% endfor %}

{% comment %} ######### OPEN POSITIONS ########## {% endcomment %}

{% assign items_listed = false %}

{% for i in (1..2) %}
{% comment %} TWO ITERATIONS, FIRST TO CHECK IF ANY POSTS AVAILABLE {% endcomment %}

  {% if i == 2 %}
{% if items_listed %}

<br clear=all />

# Job openings 

    {% else %}
      {% comment %} There are no job openings to show at this time.{% endcomment %}
      {% break %}
    {% endif %}
  {% endif %}
  {% assign items_listed = false %}

  {% for p in site.posts %}
    {% unless p.categories contains 'job-openings' %}{% continue %}{% endunless %}
    {% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}
    {% if p.deadline %}{% capture deadlinetime %}{{ p.deadline | date: '%s'}}{% endcapture %}{% else %}{% assign deadlinetime = "1970-01-01" | date: '%s' %}{% endif %}
    {% if posttime < newsletter_start_time and deadlinetime < nowtime %}
      {% continue %}
    {% endif %}

    {% assign items_listed = true %}
      {% if i == 2 %}
<br clear=all />

## {{ p.title }}

    {% if p.image %}
![](https://climateainordics.com{{ p.image  }})
    {% endif %}

{{ p.summary }}<br />

{% capture oneweektime %}{{ nowtime | plus: 604800 }}{% endcapture %}
{% if p.deadline != null and p.deadline != "" %}{% if deadlinetime < oneweektime %}<span style="font-weight: bold; color: #f00;">{% endif %}Deadline: {{ p.deadline }}{% if deadlinetime < oneweektime %}</span>{% endif %}<br />{% endif %}

**[Read more!](https://climateainordics.com{{ p.url }})**
    {% endif %}
  {% endfor %}

{% endfor %}

{% comment %} ######### END, OPEN POSITIONS ########## {% endcomment %}


# Your news in the newsletter!

**Make sure to share your work with us, by sending us an email ([contact@climateainordics.com](mailto:contact@climateainordics.com)), posting in our Slack or some other channel, and we'll add it to the news feed! Take the chance of showcasing your work or your events to the community!**

Also be sure to follow us on [LinkedIn](https://www.linkedin.com/company/climate-ai-nordics/) and [BlueSky](https://bsky.app/profile/climateainordics.com). Climate AI Nordics will have the most impact if you repost and like our stories!

**[Climate AI Nordics](https://climateainordics.com/)** is a network of [researchers](https://climateainordics.com//people/) working to harness AI in tackling the climate crisis through both mitigation and adaptation.

We promote the development of AI-based tools and optimization methods that support sustainable decision-making—helping reduce emissions, restore ecosystems, and build climate resilience.

