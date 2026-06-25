---
layout: page
title: "Definitions of Terms"
subtitle: "What we mean by some of the framework's more nuanced terms"
draft: true
---

<p class="text-muted">
This glossary explains terms used across the risk and mitigation catalogue that
carry a specific meaning in this framework, or that are easy to misread. It is a
living document.
</p>

{% assign terms = site.data.glossary | sort: "term" %}

<nav class="mb-4" aria-label="Glossary index">
  <div class="d-flex flex-wrap gap-2">
    {% for entry in terms %}
    <a href="#{{ entry.slug }}" class="badge rounded-pill bg-light text-dark border text-decoration-none">{{ entry.term }}</a>
    {% endfor %}
  </div>
</nav>

<dl class="glossary">
  {% for entry in terms %}
  <dt id="{{ entry.slug }}" class="h5 mt-4">{{ entry.term }}</dt>
  <dd class="mb-3">{{ entry.definition }}</dd>
  {% endfor %}
</dl>
