---
layout: default
title: "SCAI Research Symposium"
permalink: /scai-symposium/
---

<style>
  .scai-page {
    --scai-maroon: #881c1c;
    --scai-ink: #1d252c;
    --scai-muted: #5f6b73;
    --scai-green: #2f6b4f;
    --scai-lime: #67b42c;
    --scai-teal: #008f86;
    --scai-blue: #056997;
    --scai-navy: #073666;
    --scai-cream: #f7f3ed;
    --scai-line: #ded7cc;
    color: var(--scai-ink);
  }

  .scai-page a {
    color: var(--scai-green);
  }

  .scai-page h2,
  .scai-page h3,
  .scai-page p,
  .scai-page span,
  .scai-page li,
  .scai-page strong {
    color: inherit;
  }

  .scai-opening {
    display: grid;
    grid-template-columns: minmax(0, 3fr) minmax(235px, 1fr);
    gap: clamp(1rem, 2vw, 1.5rem);
    align-items: stretch;
    margin: 0 0 2.75rem;
  }

  .scai-hero {
    position: relative;
    overflow: hidden;
    padding: clamp(1.85rem, 3vw, 2.8rem);
    border: 1px solid rgba(5, 105, 151, 0.13);
    border-radius: 1rem;
    background:
      radial-gradient(circle at 96% 4%, rgba(5, 105, 151, 0.18), transparent 33%),
      radial-gradient(circle at 17% 106%, rgba(103, 180, 44, 0.18), transparent 36%),
      linear-gradient(118deg, #fbfefc 0%, #eff9f5 46%, #edf7fb 100%);
    box-shadow: 0 1rem 2.8rem rgba(7, 54, 102, 0.12);
  }

  .scai-hero::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 0.42rem;
    background: linear-gradient(90deg, var(--scai-lime), var(--scai-teal) 52%, var(--scai-navy));
  }

  .scai-hero::after {
    content: "";
    position: absolute;
    right: -13rem;
    bottom: -24rem;
    width: 42rem;
    height: 42rem;
    border: 1.35rem solid rgba(5, 105, 151, 0.045);
    border-radius: 50%;
    box-shadow:
      0 0 0 2rem rgba(0, 143, 134, 0.035),
      0 0 0 4rem rgba(103, 180, 44, 0.025);
  }

  .scai-hero-inner {
    position: relative;
    z-index: 1;
    display: grid;
    grid-template-columns: minmax(0, 1.35fr) minmax(220px, 0.65fr);
    gap: clamp(1rem, 2.2vw, 2rem);
    align-items: center;
  }

  .scai-logo-card {
    position: relative;
    justify-self: end;
    width: 100%;
    max-width: 350px;
    aspect-ratio: 1.92 / 1;
  }

  .scai-logo-card::before {
    content: "";
    position: absolute;
    inset: 14% 1%;
    border-radius: 50%;
    background: linear-gradient(105deg, rgba(103, 180, 44, 0.2), rgba(0, 143, 134, 0.18) 48%, rgba(5, 105, 151, 0.18));
    filter: blur(2rem);
  }

  .scai-logo-card img {
    position: relative;
    display: block;
    width: 100%;
    max-width: 100%;
    height: auto;
    filter: drop-shadow(0 0.8rem 0.8rem rgba(7, 54, 102, 0.1));
  }

  .scai-eyebrow {
    position: relative;
    z-index: 1;
    margin: 0 0 0.55rem;
    color: var(--scai-green) !important;
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
  }

  .scai-hero h2 {
    position: relative;
    z-index: 1;
    max-width: 770px;
    margin: 0 0 0.75rem;
    color: var(--scai-navy);
    font-size: clamp(1.9rem, 3.8vw, 3.15rem);
    line-height: 1.02;
    letter-spacing: -0.038em;
  }

  .scai-hero-copy {
    position: relative;
    z-index: 1;
    max-width: 690px;
    margin: 0;
    color: #24485b !important;
    font-size: clamp(0.94rem, 1.4vw, 1.08rem);
    line-height: 1.52;
  }

  .scai-hero-context {
    position: relative;
    z-index: 1;
    margin-top: clamp(1.25rem, 2vw, 1.7rem);
    padding-top: clamp(1rem, 1.8vw, 1.35rem);
    border-top: 1px solid rgba(5, 105, 151, 0.18);
  }

  .scai-hero-context p {
    margin: 0;
    color: #294b5c !important;
    font-size: 0.88rem;
    line-height: 1.62;
  }

  .scai-factbox {
    position: relative;
    overflow: hidden;
    padding: clamp(1.25rem, 2vw, 1.55rem);
    border: 1px solid rgba(5, 105, 151, 0.14);
    border-radius: 1rem;
    background: #fff;
    box-shadow: 0 1rem 2.8rem rgba(7, 54, 102, 0.09);
  }

  .scai-factbox::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 0.42rem;
    background: linear-gradient(90deg, var(--scai-lime), var(--scai-teal) 52%, var(--scai-navy));
  }

  .scai-factbox h3 {
    margin: 0 0 1rem;
    color: var(--scai-navy);
    font-size: 1.05rem;
    letter-spacing: 0.07em;
    text-transform: uppercase;
  }

  .scai-factbox dl {
    margin: 0;
  }

  .scai-factbox dt {
    margin-top: 0.82rem;
    color: var(--scai-green);
    font-size: 0.74rem;
    font-weight: 750;
    letter-spacing: 0.09em;
    text-transform: uppercase;
  }

  .scai-factbox dd {
    margin: 0.18rem 0 0;
    color: #243b4a;
    font-size: 0.9rem;
    font-weight: 620;
    line-height: 1.42;
  }

  .scai-section {
    margin: 3.5rem 0;
  }

  .scai-codec {
    display: grid;
    grid-template-columns: minmax(0, 1.25fr) minmax(220px, 0.75fr);
    gap: clamp(1.5rem, 4vw, 3.5rem);
    align-items: center;
    margin: 3.25rem 0;
    padding: clamp(1.5rem, 4vw, 2.6rem);
    border-left: 5px solid var(--scai-green);
    border-radius: 0 0.75rem 0.75rem 0;
    background: #eef4f0;
  }

  .scai-codec h2 {
    margin: 0 0 0.65rem;
    font-size: clamp(1.45rem, 3vw, 2.05rem);
  }

  .scai-codec p {
    margin: 0;
    line-height: 1.65;
  }

  .scai-codec-link {
    display: inline-block;
    justify-self: end;
    padding: 0.7rem 1rem;
    border: 1px solid var(--scai-green);
    border-radius: 999px;
    font-weight: 700;
    text-decoration: none;
    white-space: nowrap;
  }

  .scai-codec-link:hover,
  .scai-codec-link:focus {
    background: var(--scai-green);
    color: #fff;
    text-decoration: none;
  }

  .scai-section-header {
    display: grid;
    grid-template-columns: 0.58fr 1.42fr;
    gap: clamp(1.25rem, 4vw, 3.75rem);
    align-items: start;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--scai-line);
  }

  .scai-section-header h2 {
    margin: 0;
    font-size: clamp(1.55rem, 3vw, 2.25rem);
    letter-spacing: -0.025em;
  }

  .scai-section-header p {
    margin: 0;
    color: var(--scai-muted);
    font-size: 1.03rem;
    line-height: 1.65;
  }

  .scai-layers {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }

  .scai-layer {
    min-height: 100%;
    padding: 1.4rem;
    border: 1px solid var(--scai-line);
    border-radius: 0.7rem;
    background: #fff;
  }

  .scai-layer-number {
    display: inline-grid;
    width: 2.3rem;
    height: 2.3rem;
    place-items: center;
    margin-bottom: 0.85rem;
    border-radius: 50%;
    background: var(--scai-maroon);
    color: #fff !important;
    font-size: 0.8rem;
    font-weight: 700;
  }

  .scai-layer h3 {
    margin: 0 0 0.55rem;
    font-size: 1.12rem;
  }

  .scai-layer p {
    margin: 0;
    color: var(--scai-muted);
    line-height: 1.6;
  }

  .scai-speakers {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.15rem;
  }

  .scai-speaker {
    overflow: hidden;
    min-width: 0;
    border: 1px solid var(--scai-line);
    border-radius: 0.75rem;
    background: #fff;
    box-shadow: 0 0.45rem 1.2rem rgba(45, 38, 32, 0.07);
  }

  .scai-speaker-photo {
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    object-position: center 25%;
    background: #ebe7e2;
  }

  .scai-speaker-body {
    padding: 1rem 1.1rem 1.15rem;
  }

  .scai-speaker h3 {
    margin: 0 0 0.3rem;
    font-size: 1.17rem;
    line-height: 1.25;
  }

  .scai-speaker h3 a {
    color: var(--scai-ink);
    text-decoration: none;
  }

  .scai-speaker h3 a:hover,
  .scai-speaker h3 a:focus {
    color: var(--scai-maroon);
    text-decoration: underline;
  }

  .scai-speaker-role {
    margin: 0;
    color: var(--scai-muted) !important;
    font-size: 0.92rem;
    line-height: 1.48;
  }

  .scai-note {
    margin-top: 1.15rem;
    color: var(--scai-muted) !important;
    font-size: 0.82rem;
  }

  .scai-callout {
    display: grid;
    grid-template-columns: 1.4fr auto;
    gap: 1.5rem;
    align-items: center;
    margin: 3.75rem 0 1rem;
    padding: clamp(1.5rem, 4vw, 2.75rem);
    border-radius: 0.75rem;
    background: var(--scai-ink);
  }

  .scai-callout h2 {
    margin: 0 0 0.55rem;
    color: #fff;
    font-size: clamp(1.45rem, 3vw, 2.1rem);
  }

  .scai-callout p {
    max-width: 710px;
    margin: 0;
    color: #dce3e6 !important;
    line-height: 1.6;
  }

  .scai-status {
    display: inline-block;
    padding: 0.62rem 0.9rem;
    border: 1px solid #a8bab4;
    border-radius: 999px;
    color: #fff !important;
    font-size: 0.84rem;
    font-weight: 700;
    white-space: nowrap;
  }

  @media (max-width: 980px) {
    .scai-opening {
      grid-template-columns: 1fr;
    }

    .scai-factbox dl {
      display: grid;
      grid-template-columns: minmax(90px, 0.28fr) minmax(0, 1fr);
      column-gap: 1.25rem;
    }

    .scai-factbox dt,
    .scai-factbox dd {
      margin-top: 0.8rem;
    }
  }

  @media (max-width: 800px) {
    .scai-hero-inner {
      grid-template-columns: 1fr;
    }

    .scai-logo-card {
      justify-self: start;
      width: min(100%, 390px);
      max-width: none;
    }

    .scai-codec,
    .scai-section-header,
    .scai-callout {
      grid-template-columns: 1fr;
    }

    .scai-codec-link {
      justify-self: start;
    }

    .scai-layers,
    .scai-speakers {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 520px) {
    .scai-hero {
      border-radius: 0.55rem;
    }

    .scai-factbox dl {
      display: block;
    }

    .scai-layers,
    .scai-speakers {
      grid-template-columns: 1fr;
    }

  }
</style>

<div class="scai-page">
  <div class="scai-opening">
    <section class="scai-hero" aria-labelledby="scai-hero-title">
      <div class="scai-hero-inner">
        <div>
          <p class="scai-eyebrow">SCAI Research Symposium</p>
          <h2 id="scai-hero-title">Building flexible, sustainable AI infrastructure for a resource-constrained world</h2>
          <p class="scai-hero-copy">A UMass-led forum at the intersection of AI systems, computing infrastructure, and energy.</p>
        </div>
        <div class="scai-logo-card">
          <img src="{{ site.base }}/img/scai-logo-banner.png" alt="SCAI Sustainable Compute and AI logo">
        </div>
      </div>
      <div class="scai-hero-context">
        <p>Frontier AI infrastructure is becoming a coupled cyber-physical system in which model behavior, compute platforms, and the electric grid can no longer be optimized independently. The symposium will convene researchers, infrastructure builders, energy experts, public-interest partners, UMass campus leadership, and state officials to examine how training, inference, placement, cooling, and service design can adapt safely to power, capacity, reliability, and grid constraints while preserving the latency, availability, progress, and quality guarantees that make AI services useful.</p>
      </div>
    </section>
    <aside class="scai-factbox" aria-label="Event details">
      <h3>Event details</h3>
      <dl>
        <dt>When</dt>
        <dd>September 17&ndash;18, 2026</dd>
        <dt>Where</dt>
        <dd><a href="https://www.google.com/maps/search/?api=1&amp;query=Computer+Science+Laboratories%2C+140+Governors+Dr%2C+Amherst%2C+MA+01003">Computer Science Laboratories<br>140 Governors Dr<br>Amherst, MA 01003<br>United States</a></dd>
        <dt>Format</dt>
        <dd>Invitation-only talks, panels, and working sessions</dd>
        <dt>Audience</dt>
        <dd>Academic, industry, government, utility, and campus leadership communities</dd>
        <dt>Agenda</dt>
        <dd>Available soon</dd>
      </dl>
    </aside>
  </div>

  <section class="scai-codec" aria-labelledby="codec-heading">
    <div>
      <h2 id="codec-heading">Building on the NSF CoDec Expedition</h2>
      <p>SCAI grows from the UMass-led <strong>NSF CoDec Expedition in Computational Decarbonization</strong>, an interdisciplinary collaboration spanning six universities and bringing together expertise in theory, AI, systems, energy systems, the built environment, and economics. The symposium extends this foundation toward the coupled AI compute-and-energy infrastructure stack.</p>
    </div>
    <a class="scai-codec-link" href="https://codecexp.us/">Visit NSF CoDec</a>
  </section>

  <section class="scai-section" aria-labelledby="agenda-heading">
    <div class="scai-section-header">
      <h2 id="agenda-heading">A coupled research agenda</h2>
      <p>SCAI is a UMass-led, compute-first initiative focused on service-guarantee-preserving infrastructure control: coordinating AI workloads, computing systems, and energy constraints as one integrated stack.</p>
    </div>
    <div class="scai-layers">
      <article class="scai-layer">
        <span class="scai-layer-number" aria-hidden="true">01</span>
        <h3>AI workloads</h3>
        <p>Training cadence, checkpointing, inference tiers, latency, availability, quality, and progress objectives.</p>
      </article>
      <article class="scai-layer">
        <span class="scai-layer-number" aria-hidden="true">02</span>
        <h3>Compute infrastructure</h3>
        <p>Accelerators, interconnects, placement, memory and storage bottlenecks, queues, utilization, cooling, and reliability headroom.</p>
      </article>
      <article class="scai-layer">
        <span class="scai-layer-number" aria-hidden="true">03</span>
        <h3>Energy context</h3>
        <p>Power availability, demand response, cost, carbon, curtailment and recovery events, siting constraints, and grid risk.</p>
      </article>
    </div>
  </section>

  <section class="scai-section" aria-labelledby="speakers-heading">
    <div class="scai-section-header">
      <h2 id="speakers-heading">Invited speakers</h2>
      <p>Perspectives spanning sustainable computing, hyperscale infrastructure, systems, computer architecture, AI, and grid-responsive data centers.</p>
    </div>

    <div class="scai-speakers">
      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/adam-wierman.png" alt="Adam Wierman" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://heritageproject.caltech.edu/interviews/adam-wierman">Adam Wierman</a></h3>
          <p class="scai-speaker-role">Professor of Computing and Mathematical Sciences, Caltech</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/prashant-shenoy.jpg" alt="Prashant Shenoy" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://people.cs.umass.edu/~shenoy/">Prashant Shenoy</a></h3>
          <p class="scai-speaker-role">Distinguished Professor and Director of the NSF CoDec Expedition, UMass Amherst</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/karin-strauss.jpg" alt="Karin Strauss" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.microsoft.com/en-us/research/people/kstrauss/">Karin Strauss</a></h3>
          <p class="scai-speaker-role">Senior Principal Research Manager, Microsoft Research</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/fabio-grimaldi.jpg" alt="Fabio Grimaldi" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.linkedin.com/in/fabio-grimaldi-530796ba/">Fabio Grimaldi</a></h3>
          <p class="scai-speaker-role">Cloud technology and sustainability, Amazon Web Services</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/ayse-coskun.jpg" alt="Ayse K. Coskun" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.bu.edu/peaclab/people/faculty/">Ayse K. Coskun</a></h3>
          <p class="scai-speaker-role">Professor of Electrical and Computer Engineering and Director of CISE, Boston University; Chief Scientist, Emerald AI</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/jeremy-rice.jpeg" alt="Jeremy Rice" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.linkedin.com/in/jeremy-rice-9a015b12/">Jeremy Rice</a></h3>
          <p class="scai-speaker-role">Mechanical Systems Lead, Verrus</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/shaolei-ren.jpg" alt="Shaolei Ren" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://shaoleiren.github.io/">Shaolei Ren</a></h3>
          <p class="scai-speaker-role">Professor of Electrical and Computer Engineering, University of California, Riverside</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/ramesh-sitaraman.jpg" alt="Ramesh Sitaraman" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.cics.umass.edu/events/distinguished-faculty-lecturer-ramesh-sitaraman">Ramesh Sitaraman</a></h3>
          <p class="scai-speaker-role">Distinguished Professor, UMass Amherst; Chief Consulting Scientist, Akamai Technologies</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/mosharaf-chowdhury.jpg" alt="Mosharaf Chowdhury" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://cse.engin.umich.edu/stories/mosharaf-chowdhury-receives-david-e-liddle-research-excellence-award">Mosharaf Chowdhury</a></h3>
          <p class="scai-speaker-role">Associate Professor of Computer Science and Engineering, University of Michigan</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/minlan-yu.jpg" alt="Minlan Yu" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://minlanyu.seas.harvard.edu/">Minlan Yu</a></h3>
          <p class="scai-speaker-role">Gordon McKay Professor of Computer Science, Harvard University</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/john-goodhue.jpg" alt="John Goodhue" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://mghpcc.org/executive-director/">John Goodhue</a></h3>
          <p class="scai-speaker-role">Executive Director, Massachusetts Green High Performance Computing Center</p>
        </div>
      </article>
    </div>
    <p class="scai-note">Speaker participation is subject to confirmation. The symposium agenda will be available soon.</p>
  </section>

  <section class="scai-callout" aria-labelledby="participate-heading">
    <div>
      <h2 id="participate-heading">Invitation-only symposium</h2>
      <p>The symposium will bring together invited researchers, infrastructure practitioners, utilities, policymakers, UMass campus leadership, state officials, and partners interested in the future of reliable, grid-aware AI systems. If you are interested in attending, please email <a href="mailto:hajiesmaili@cs.umass.edu" style="color: #fff; text-decoration: underline;">Mohammad Hajiesmaili</a> at <a href="mailto:hajiesmaili@cs.umass.edu" style="color: #fff; text-decoration: underline;">hajiesmaili@cs.umass.edu</a>. The agenda will be available soon.</p>
    </div>
    <span class="scai-status">Agenda coming soon</span>
  </section>
</div>

<!--
Speaker image sources:
- Adam Wierman: https://heritageproject.caltech.edu/interviews/adam-wierman
- Prashant Shenoy: https://people.cs.umass.edu/~shenoy/
- Karin Strauss: https://www.microsoft.com/en-us/research/people/kstrauss/
- Fabio Grimaldi: https://www.linkedin.com/in/fabio-grimaldi-530796ba/
- Ayse K. Coskun: https://www.bu.edu/peaclab/people/faculty/
- Jeremy Rice: portrait supplied by the symposium organizer.
- Shaolei Ren: https://shaoleiren.github.io/
- Ramesh Sitaraman: https://www.cics.umass.edu/events/distinguished-faculty-lecturer-ramesh-sitaraman
- Mosharaf Chowdhury: https://cse.engin.umich.edu/stories/mosharaf-chowdhury-receives-david-e-liddle-research-excellence-award
- Minlan Yu: https://minlanyu.seas.harvard.edu/
- John Goodhue: https://mghpcc.org/executive-director/
-->
