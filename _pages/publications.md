---
layout: page
title: Working Papers
permalink: /publications/
description: Job market paper and working papers.
gscholar_badge: true 
inline_citations: true
nav: true
nav_order: 2
---

<!-- Pure CSS to drop year headings and collapse empty image margins -->
<style>
  /* Completely hides the massive auto-generated year headers (e.g., 2025, 2026) */
  .publications h2.year {
      display: none !important; 
  }
  
  /* Compresses the vertical gap between individual papers */
  .publications .row {
      margin-bottom: 0.5rem !important; 
  }
  
  /* Deletes the empty image/thumbnail margin box on the left */
  .publications .col-sm-2 {
      display: none !important; 
  }
  
  /* Stretches your text to use the full page width elegantly */
  .publications .col-sm-8 {
      max-width: 100% !important; 
      flex: 0 0 100% !important;
  }
  
  /* Cleans up list grouping gaps */
  .publications ol.bibliography li {
      margin-bottom: 1rem !important; 
  }
</style>

<div class="publications">
  {% bibliography %}
</div>
