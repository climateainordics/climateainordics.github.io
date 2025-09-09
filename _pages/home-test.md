---
permalink: /test/
title: ""
excerpt: "AI for Climate action across the Nordics"
---

<!-- -------------------------  PAGE STYLES  ------------------------- -->
<style>
:root{
  --cai-primary:#007b83;
  --cai-dark:#0f172a;
  --cai-muted:#6b7280;
  --cai-bg:#ffffff;
  --cai-card:#f8fafc;
  --cai-accent:#10b981;
}
@media (prefers-color-scheme: dark){
  :root{ --cai-bg:#0b1020; --cai-card:#0f172a; --cai-muted:#a3a3a3; --cai-dark:#e5e7eb; }
}
.page{
  font-size:1.05rem;
}
.hero{
  position:relative; margin: 0 0 2rem; border-radius:18px; overflow:hidden;
  /*background:linear-gradient(180deg, rgba(0,0,0,.35), rgba(0,0,0,.55)),
             url(/images/backgrounds/hero.png) center/cover no-repeat;*/
  background: url(/images/backgrounds/hero.png) center/cover no-repeat;
  min-height:360px; color:#fff; display:flex; align-items:center;
}
.hero .inner{ padding:3.5rem 2rem; }
.hero h1{ font-size:2.2rem; margin:.2rem 0 .6rem; line-height:1.1; }
.hero p{ font-size:1.15rem; max-width:760px; opacity:.95; }
.hero .cta{ margin-top:1.1rem; display:flex; gap:.75rem; flex-wrap:wrap; }
.hero .btn{
  display:inline-block; padding:.7rem 1rem; border-radius:999px; font-weight:700;
  text-decoration:none; transition:.15s transform ease, .15s box-shadow ease;
  background:#fff; color:#0f172a; box-shadow:0 2px 14px rgba(0,0,0,.18);
}
.hero .btn:hover{ transform:translateY(-2px) }
.hero .btn--ghost{ background:transparent; border:2px solid rgba(255,255,255,.9); color:#fff; }

.section {
  margin: 2rem 0;   /* center it */
  padding: 0 1rem;     /* breathing room */
}
.section h2{ font-size:1.5rem; margin-bottom:.75rem }

.grid{ display:grid; gap:1rem }
.grid-3{ grid-template-columns:repeat(3, minmax(0,1fr)) }
.grid-2{ grid-template-columns:repeat(2, minmax(0,1fr)) }
@media (max-width: 860px){ .grid-3, .grid-2{ grid-template-columns:1fr } }

.card{
  background:#ffffff;          /* pure white cards */
  color:#0f172a;               /* dark text */
  border-radius:14px;
  border:1px solid rgba(0,0,0,.08);
  box-shadow:0 2px 6px rgba(0,0,0,.05);
  overflow:hidden;                 /* clip child corners */
}
.card__meta{ color:#475569; }   /* slate gray */
.lede{ color:#334155; }
.card__body{ padding:1rem 1rem 1.1rem }
.card__img{ width:100%; aspect-ratio:16/9; object-fit:cover; background:#e5e7eb; }
.tags{ margin-top:.25rem; font-size:.85rem; color:var(--cai-muted) }

.divider{ height:1px; background:rgba(0,0,0,.08); margin:1.25rem 0 }

.badges{ display:flex; gap:.5rem; flex-wrap:wrap; margin-top:.5rem }
.badges a{
  text-decoration:none; padding:.45rem .7rem; border-radius:999px; font-weight:700;
  background:#eef2ff; color:#1e293b; border:1px solid rgba(0,0,0,.05);
}
.badges a:hover{ opacity:.85 }

.strip{
  margin-top:1.5rem; display:flex; gap:1rem; flex-wrap:wrap; align-items:center;
  color:var(--cai-muted);
}
.strip img{ height:30px; opacity:.9; }

.cta-banner{
  margin-top:2rem; padding:1.2rem 1.1rem; border-radius:14px; color:#fff;
  background:linear-gradient(120deg, var(--cai-primary), #0ea5e9);
  display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between;
}
.cta-banner a{ color:#fff; font-weight:800; text-decoration:underline }
.kicker{
  color:#0ea5e9;   /* bright cyan accent */
}
.readmore, .card__title a{
  color:#007b83;   /* your brand teal */
  text-decoration:none;
}
.readmore:hover, .card__title a:hover{
  text-decoration:underline;
}

@media (prefers-color-scheme: dark){
    .card {
      background: #1e293b;       /* slate blue */
      color: #f1f5f9;
      border: 1px solid rgba(255,255,255,.05);
    }
    a, .readmore, .card__title a { color: #22d3ee; }
    a:hover, .readmore:hover, .card__title a:hover { color: #67e8f9; }
    .card__meta, .lede { color: #cbd5e1; }
}

</style>

<div class="page">

  <!-- -------------------------  HERO  ------------------------- -->
  <section class="hero" role="banner" aria-label="Climate AI Nordics">
    <div class="inner">
      <span class="kicker">Climate AI Nordics</span>
      <h1>Supporting AI climate action across the Nordic region</h1>
      <p>
        We are a network of researchers developing AI to accelerate
        mitigation and adaptation — from biodiversity monitoring to
        resilient cities and nature-based solutions.
      </p>
      <div class="cta">
        <a class="btn" href="/join/">Join the network</a>
        <a class="btn btn--ghost" href="/people/">Meet the people</a>
        <a class="btn btn--ghost" href="/events/">Upcoming events</a>
        <a class="btn btn--ghost" href="/news/">Latest news</a>
      </div>
    </div>
  </section>

  <!-- -------------------------  WHAT WE DO  ------------------------- -->
  <section class="section">
    <h2>What we do</h2>
    <div class="grid grid-3">
      <div class="card">
        <div class="card__body">
          <div class="kicker">Research & Methods</div>
          <h3 class="card__title">Earth observation + AI</h3>
          <p class="lede">Remote sensing, ML, and decision support for wetlands, urban green, hazards, and biodiversity.</p>
        </div>
      </div>
      <div class="card">
        <div class="card__body">
          <div class="kicker">Collaboration</div>
          <h3 class="card__title">Nordic network</h3>
          <p class="lede">We connect labs and agencies to co-create open tools, datasets, and reproducible workflows.</p>
        </div>
      </div>
      <div class="card">
        <div class="card__body">
          <div class="kicker">Impact</div>
          <h3 class="card__title">From pilots to policy</h3>
          <p class="lede">Turning models into decisions for mitigation, rewetting/rewilding, and climate resilience.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- -------------------------  SPOTLIGHT  ------------------------- -->
  {% assign spotlight = site.posts | where: "first_page", true | slice: 0, 1 %}
  {% if spotlight.size > 0 %}
  <section class="section">
    <h2>Spotlight</h2>
    {% for p in spotlight %}
      <div class="card">
        {% if p.image %}<img class="card__img" src="{{ p.image }}" alt="Cover image for {{ p.title }}">{% endif %}
        <div class="card__body">
          <div class="card__meta">{{ p.date | date: "%Y-%m-%d" }}</div>
          <h3 class="card__title">{{ p.title }}</h3>
          <p>{{ p.summary }}</p>
          <a class="readmore" href="{{ p.url }}">Read the story →</a>
        </div>
      </div>
    {% endfor %}
  </section>
  {% endif %}

  <!-- -------------------------  LATEST  ------------------------- -->
  <section class="section">
    <h2>Latest news</h2>
    <div class="grid grid-3">
      {% for p in site.categories.news limit: 3 %}
      <article class="card">
        {% if p.image %}<img class="card__img" src="{{ p.image }}" alt="Image for {{ p.title }}">{% endif %}
        <div class="card__body">
          <div class="card__meta">{{ p.date | date: "%Y-%m-%d" }}</div>
          <h3 class="card__title"><a href="{{ p.url }}">{{ p.title }}</a></h3>
          {% if p.summary %}<p>{{ p.summary | truncate: 150 }}</p>{% endif %}
          <a class="readmore" href="{{ p.url }}">Read more →</a>
        </div>
      </article>
      {% endfor %}
    </div>
    <div class="badges"><a href="/news/">All news</a></div>
  </section>

  <section class="section">
    <h2>Upcoming events</h2>
    <div class="grid grid-3">
      {% for p in site.categories.events limit: 3 %}
      <article class="card">
        {% if p.image %}<img class="card__img" src="{{ p.image }}" alt="Image for {{ p.title }}">{% endif %}
        <div class="card__body">
          <div class="card__meta">{{ p.event_date | default: p.date | date: "%Y-%m-%d" }}</div>
          <h3 class="card__title"><a href="{{ p.url }}">{{ p.title }}</a></h3>
          {% if p.summary %}<p>{{ p.summary | truncate: 150 }}</p>{% endif %}
          <a class="readmore" href="{{ p.url }}">Event details →</a>
        </div>
      </article>
      {% endfor %}
    </div>
    <div class="badges"><a href="/events/">All events</a></div>
  </section>

  <section class="section">
    <h2>Job openings</h2>
    <div class="grid grid-3">
      {% for p in site.categories["job-openings"] limit: 3 %}
      <article class="card">
        {% if p.image %}<img class="card__img" src="{{ p.image }}" alt="Image for {{ p.title }}">{% endif %}
        <div class="card__body">
          <div class="card__meta">{{ p.date | date: "%Y-%m-%d" }}</div>
          <h3 class="card__title"><a href="{{ p.url }}">{{ p.title }}</a></h3>
          <a class="readmore" href="{{ p.url }}">How to apply →</a>
        </div>
      </article>
      {% endfor %}
    </div>
    <div class="badges"><a href="/news/#job-openings">More jobs</a></div>
  </section>

  <!-- -------------------------  SOCIALS / PARTNERS / CTA  ------------------------- -->
  <section class="section">
    <div class="divider"></div>
    <div class="strip" aria-label="Follow and partners">
      <strong>Follow:</strong>
      <a href="https://bsky.app/profile/climateainordics.bsky.social">Bluesky</a> ·
      <a href="https://github.com/climate-ai-nordics">GitHub</a> ·
      <a href="/join/">Email list</a>
    </div>
    {% if site.data.partners %}
      <div class="strip" style="opacity:.9">
        <strong>Partners:</strong>
        {% for org in site.data.partners %}
          {% if org.logo %}<img src="{{ org.logo }}" alt="{{ org.name }} logo">{% endif %}
        {% endfor %}
      </div>
    {% endif %}
    <div class="cta-banner">
      <div><strong>Want to collaborate?</strong> We welcome new members, projects, and datasets across the Nordics.</div>
      <a href="/join/">Join us →</a>
    </div>
  </section>

</div>

