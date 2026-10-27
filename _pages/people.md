---
title: People
permalink: /people/
layout: home
---
{% include base_path %}
{% comment %}
  The board and member lists are auto-generated includes (board-from-form.md, people-from-form.md):
  never edit them. This page only wraps them; styles are in _sass/_people.scss and
  assets/js/people-directory.js tidies each entry and adds search + topic filters.
  Bios stay as hover tooltips (the title attribute in the generated markup).
{% endcomment %}
{% capture people_nordics %}{% include people_from_form_count_number_only_nordics.md %}{% endcapture %}
{% capture people_orgs %}{% include people_from_form_count_number_organizations.md %}{% endcapture %}
{% capture people_outside %}{% include people_from_form_count_number_outside_nordics.md %}{% endcapture %}
{% assign people_nordics_rounded = people_nordics | strip | plus: 0 | divided_by: 10 | times: 10 %}
{% assign people_orgs_rounded = people_orgs | strip | plus: 0 | divided_by: 10 | times: 10 %}
{% assign people_outside_rounded = people_outside | strip | plus: 0 | divided_by: 10 | times: 10 %}

<header class="list-header">
  <h1 class="list-header__title">People</h1>
  <p class="list-header__lead">
    We're a network of researchers & practitioners across the Nordics who work on problems related to tackling
    climate change using AI and machine learning. Climate AI Nordics acts as a hub, hosting and
    announcing news, seminars and workshops.
  </p>
  <div class="page-actions">
    <a class="home-btn home-btn--primary" href="/join/">Join the network</a>
  </div>
</header>

<section class="home-stats people-stats" aria-label="The network in numbers">
  <div class="home-stat"><span class="home-stat__num">{{ people_nordics_rounded }}+</span><span class="home-stat__label">researchers in the Nordics</span></div>
  <div class="home-stat"><span class="home-stat__num">{{ people_orgs_rounded }}+</span><span class="home-stat__label">organisations across the network</span></div>
  <div class="home-stat"><span class="home-stat__num">{{ people_outside_rounded }}+</span><span class="home-stat__label">supporting affiliates outside the Nordics</span></div>
</section>

{% for p in site.categories.featured-member limit: 1 %}
{% assign person = p.people | first | default: p.title %}
{% assign img = site.data.card_images[p.path] | default: p.image_small | default: p.image %}
<section class="people-featured">
  {% if img %}<a class="people-featured__media" href="{{ p.url }}" tabindex="-1" aria-hidden="true"><img src="{{ img }}" alt=""></a>{% endif %}
  <div class="people-featured__body">
    <p class="home-card__meta">Featured member · {{ p.date | date: "%B %Y" }}</p>
    <h2 class="people-featured__title"><a href="{{ p.url }}">{{ person }}</a></h2>
    {% if p.summary %}<p>{{ p.summary | markdownify | strip_html | truncatewords: 50 }}</p>{% endif %}
    <div class="page-actions">
      <a class="home-btn home-btn--primary" href="{{ p.url }}">Meet {{ person | split: " " | first }}</a>
      <a class="home-btn home-btn--outline" href="/featured-member/">All featured members</a>
    </div>
  </div>
</section>
{% endfor %}

<div class="people-filter" id="people-filter" hidden>
  <label class="people-search">
    <i class="fas fa-magnifying-glass" aria-hidden="true"></i>
    <input type="search" id="people-search" placeholder="Search by name, organisation or topic" aria-label="Search people by name, organisation or topic" autocomplete="off">
  </label>
  <div class="list-filters people-topics" id="people-topics" role="group" aria-label="Filter people by topic"></div>
  <p class="people-count" id="people-count" aria-live="polite"></p>
</div>

<div class="people-board" markdown="1">

{% include board-from-form.md %}

</div>

<div class="people-list" markdown="1">

{% include people-from-form.md %}

</div>

<p class="list-empty" id="people-empty" hidden>No one matches your search. Try another name, organisation or topic, or <a href="/join/">join the network</a> yourself!</p>

<script src="{{ base_path }}/assets/js/people-directory.js?v={{ site.time | date: '%s' }}" defer></script>
