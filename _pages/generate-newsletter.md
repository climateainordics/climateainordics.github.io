---
title: "Climate Change AI Nordics Newsletter"
excerpt: "Climate Change AI Nordics Newsletter"
permalink: /generate-newsletter/
previous_newsletter: 2024-10-01
---

<style>
img{
width: 8em;
float: right;
}
</style>

Welcome to the *Climate Change AI Nordics* Newsletter {{ "now" | date: "%B %Y" }}.

During the last month, *Climate Change AI Nordics* was launched! The founding team is very excited about the future of this network.

**Reply to this email address to contribute your own relevant news! We will include news on our web page, [ccainordics.com](https://ccainordics.com) and in our newsletter. Take the chance of showcasing your work or your events to the community!**

Do you know researchers who works in the intersection of AI and Climate Change? Tell them about Climate Change AI Nordics! [ccainordics.com/join](https://ccainordics.com/join)

{% capture nowtime %}{{'now' | date: '%s'}}{% endcapture %}
{% capture previous_newsletter_time %}{{ page.previous_newsletter | date: '%s' }}{% endcapture %}

{% for p in site.posts %}
{% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}
{% if posttime < previous_newsletter_time %}
{% continue %}
{% endif %}

{% if p.first_page %}
## {{ p.title }}

{% if p.image %}
![]({{ p.image  }})
{% endif %}

{% if p.event_date %}
{% capture eventtime %}{{ p.event_date | date: '%s'}}{% endcapture %}
{% if eventtime < nowtime %}*This event happened {{ p.event_date }}.*{% endif %}
{% endif %}

{{ p.shortversion }}<br />
**[(Read more)]({{ p.url }})**
{% endif %}
{% endfor %}

{% for p in site.posts %}
{% capture posttime %}{{ p.date | date: '%s'}}{% endcapture %}
{% if posttime < previous_newsletter_time %}
{% continue %}
{% endif %}

{% unless p.first_page %}
## {{ p.title }}

{% if p.image %}
![]({{ p.image  }})
{% endif %}

{% if p.event_date %}
{% capture eventtime %}{{ p.event_date | date: '%s'}}{% endcapture %}
{% if eventtime < nowtime %}*This event happened {{ p.event_date }}.*{% endif %}
{% endif %}

{{ p.shortversion }}<br />
**[(Read more)]({{ p.url }})**
{% endunless %}
{% endfor %}

*CCAI Nordics are a [network of researchers](/people/) dedicated to developing and utilizing AI technologies to address the urgent global challenge of climate change. Our researchers focus on creating and promoting AI solutions that support both climate change mitigation, reducing the severity of climate change, and adaptation, adjusting to the effects of climate change. We are already in a climate emergency which is causing biodiversity loss, extreme weather events, and human suffering, and this necessitates a multifaceted approach involving both policy change, limitations on activities contributing to climate change, and bolstering societal resilience against climate-related events.*

*CCAI Nordics promotes the development of AI-based analytical tools and optimization techniques that can inform decision-making processes crucial for ensuring a sustainable future for generations to come. In particular, we recognize that technology, particularly AI-based solutions, can play a role in supporting efforts such as rewilding, rewetting, and reducing emissions and the reliance on fossil fuels.*

*By bringing together researchers in the Nordic countries, CCAI Nordics aims to:*

* *Foster collaboration and knowledge exchange through seminars and workshops.*
* *Help develop AI-driven solutions that contribute to the creation of climate-friendly products and services, optimize processes for efficiency and sustainability, and promote justice in addressing the impacts of climate change.*

*We hope that the collaborative nature of CCAI Nordics will accelerate progress in this critical field, enabling the sharing of expertise and resources to develop impactful AI solutions for climate change mitigation and adaptation.*

