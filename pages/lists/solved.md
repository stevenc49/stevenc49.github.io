---
layout: page
title:  Solved Problems
---

{% for p in site.problems %}
- [{{ p.title }}]( {{ p.url }} )
{% endfor %}