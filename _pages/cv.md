---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 4
---

<div class="cv-container">
  <div class="text-center mb-4">
    <a href="{{ '/assets/pdf/CV_Afshar.pdf' | relative_url }}" class="btn btn-primary" role="button" target="_blank">
      <i class="fa-solid fa-file-pdf"></i>&nbsp; Download CV (PDF)
    </a>
  </div>
  <iframe
    src="{{ '/assets/pdf/CV_Afshar.pdf' | relative_url }}#toolbar=0&navpanes=0"
    class="cv-frame"
    title="Curriculum Vitae">
  </iframe>
</div>

<style>
  .cv-frame {
    width: 100%;
    height: 85vh;                 /* scales to the viewport instead of a fixed 800px */
    border: 1px solid var(--global-divider-color);
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  }
  @media (max-width: 768px) {
    .cv-frame { height: 70vh; }
  }
</style>
