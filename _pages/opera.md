---
layout: page
title: opera
permalink: /opera/
description: Essays on the art form I love most.
nav: true
nav_order: 10
---

<ul class="post-list">
{% for post in site.categories.opera %}
  <li>
    <h3><a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p>{{ post.description }}</p>
    <p class="post-meta">{{ post.date | date: '%B %-d, %Y' }}</p>
  </li>
{% endfor %}
</ul>
