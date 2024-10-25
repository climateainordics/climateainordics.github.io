---
permalink: /
title: "Climate Change AI Nordics"
excerpt: "Climate Change AI Nordics"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


Welcome to _Climate Change AI Nordics_.
We're a [network of researchers](https://ccai.cc/people/) who work on problems related to tackling climate change using AI and machine learning. We also host seminars and workshops, and send an occasional email.

[Sign up to receive invitations to seminars and workshops, and to mark your affiliation with Climate Change AI Nordics](https://forms.gle/RJ6HgucfwR1eKFfM6)!

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSds9NcE7-f_6ynh_abDOzhwp-DdRoWpiof204UTVTJXcgNvxw/viewform?embedded=true" width="640" height="1505" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>

## [News](/news/)

{% for p in site.categories.news limit: 5 %}
* {{p.date | date: '%Y-%m-%d'}}: {{ p.title }} [(Read more)]({{ p.url }})
{% endfor %}


