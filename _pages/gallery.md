---
layout: page
title: gallery
permalink: /gallery/
description: Photos from my backpacking trips.
nav: true
nav_order: 6
images:
  lightbox2: true
---

<style>
  .trip-gallery {
    --row-h: 240px;
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  /* Each item grows in proportion to its aspect ratio, so every photo in a row
     ends up the same height while keeping its own shape (panoramas included). */
  .trip-gallery a {
    flex-basis: calc(var(--r) * var(--row-h));
    overflow: hidden;
    border-radius: 4px;
    background: var(--global-divider-color);
  }
  .trip-gallery img {
    display: block;
    width: 100%;
    height: auto;
    transition: transform 0.3s ease;
  }
  .trip-gallery a:hover img { transform: scale(1.03); }
  /* keeps the last row from stretching huge */
  .trip-gallery::after { content: ""; flex-grow: 1000000; }
  @media (max-width: 576px) { .trip-gallery { --row-h: 140px; } }
</style>

<div class="trip-gallery">
{%- for photo in site.data.gallery -%}
{%- assign ratio = photo.width | times: 1.0 | divided_by: photo.height | round: 4 -%}
<a href="{{ photo.full | relative_url }}" data-lightbox="trips" data-title="{{ photo.caption | escape }}" style="--r: {{ ratio }}; flex-grow: {{ ratio }};">
<img src="{{ photo.thumb | relative_url }}" width="{{ photo.width }}" height="{{ photo.height }}" alt="{{ photo.caption | default: 'Backpacking photo' | escape }}" loading="lazy">
</a>
{%- endfor -%}
</div>
