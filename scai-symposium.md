---
layout: default
title: "SCAI Research Symposium"
permalink: /scai-symposium/
---

<!-- SCAI symposium page reviewed August 17, 2026. -->

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
    font-size: clamp(1.75rem, 2.65vw, 2.2rem);
    line-height: 1.02;
    letter-spacing: -0.038em;
  }

  .scai-hero-line {
    display: block;
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

  .scai-hero-actions {
    position: relative;
    z-index: 1;
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
    margin-top: 1rem;
  }

  .scai-call-link {
    display: inline-flex;
    align-items: center;
    gap: 0.65rem;
    padding: 0.68rem 0.95rem;
    border-radius: 999px;
    background: var(--scai-navy);
    color: #fff !important;
    font-size: 0.86rem;
    font-weight: 750;
    line-height: 1.2;
    text-decoration: none;
    box-shadow: 0 0.45rem 1rem rgba(7, 54, 102, 0.16);
  }

  .scai-call-link span {
    padding-left: 0.65rem;
    border-left: 1px solid rgba(255, 255, 255, 0.38);
    color: #dbeef5 !important;
    font-size: 0.76rem;
    font-weight: 650;
  }

  .scai-call-link:hover,
  .scai-call-link:focus {
    background: var(--scai-green);
    color: #fff;
    text-decoration: none;
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

  .scai-agenda {
    scroll-margin-top: 1.5rem;
    padding: clamp(1.5rem, 3.5vw, 2.75rem);
    border: 1px solid rgba(5, 105, 151, 0.16);
    border-radius: 1rem;
    background:
      radial-gradient(circle at 100% 0%, rgba(5, 105, 151, 0.1), transparent 29%),
      linear-gradient(145deg, #fcfdf9 0%, #f3f8f5 50%, #f1f8fb 100%);
    box-shadow: 0 1rem 2.5rem rgba(7, 54, 102, 0.08);
  }

  .scai-section-header .scai-eyebrow {
    margin-bottom: 0.5rem;
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
    position: relative;
    overflow: hidden;
    min-height: 100%;
    padding: 1.4rem;
    border: 1px solid var(--scai-line);
    border-radius: 0.7rem;
    background: #fff;
  }

  .scai-layer::before {
    content: "";
    position: absolute;
    inset: 0 0 auto;
    height: 0.34rem;
    background: var(--scai-maroon);
  }

  .scai-layer:nth-child(1) {
    --layer-color: var(--scai-lime);
  }

  .scai-layer:nth-child(2) {
    --layer-color: var(--scai-teal);
  }

  .scai-layer:nth-child(3) {
    --layer-color: var(--scai-blue);
  }

  .scai-layer-number {
    display: inline-grid;
    width: 2.3rem;
    height: 2.3rem;
    place-items: center;
    margin-bottom: 0.85rem;
    border-radius: 50%;
    background: var(--layer-color);
    color: #fff !important;
    font-size: 0.8rem;
    font-weight: 700;
  }

  .scai-layer h3 {
    margin: 0 0 0.55rem;
    color: var(--scai-navy);
    font-size: 1.12rem;
  }

  .scai-layer > p {
    margin: 0;
    color: var(--scai-muted);
    line-height: 1.6;
  }

  .scai-layer ul {
    margin: 0.9rem 0 0;
    padding-left: 1.05rem;
  }

  .scai-layer li {
    margin-bottom: 0.5rem;
    color: #3f4e57 !important;
    font-size: 0.86rem;
    line-height: 1.47;
  }

  .scai-layer li:last-child {
    margin-bottom: 0;
  }

  .scai-agenda-coupling {
    display: grid;
    grid-template-columns: minmax(190px, 0.48fr) minmax(0, 1.52fr);
    gap: clamp(1rem, 3vw, 2rem);
    align-items: center;
    margin-top: 1rem;
    padding: 1.1rem 1.25rem;
    border-left: 5px solid var(--scai-teal);
    border-radius: 0 0.7rem 0.7rem 0;
    background: linear-gradient(105deg, #eef7f3, #edf6fa);
  }

  .scai-agenda-coupling strong {
    color: var(--scai-navy) !important;
    font-size: 1.02rem;
  }

  .scai-agenda-coupling p {
    margin: 0;
    color: #3c505c !important;
    font-size: 0.91rem;
    line-height: 1.58;
  }

  .scai-community-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin-top: 1rem;
  }

  .scai-community-row span {
    padding: 0.45rem 0.7rem;
    border: 1px solid rgba(5, 105, 151, 0.18);
    border-radius: 999px;
    background: #fff;
    color: var(--scai-navy) !important;
    font-size: 0.78rem;
    font-weight: 700;
  }

  .scai-speakers {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.85rem;
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
    padding: 0.78rem 0.85rem 0.9rem;
  }

  .scai-speaker h3 {
    margin: 0 0 0.22rem;
    font-size: 1.02rem;
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
    font-size: 0.82rem;
    line-height: 1.42;
  }

  .scai-note {
    margin-top: 1.15rem;
    color: var(--scai-muted) !important;
    font-size: 0.82rem;
  }

  .scai-participation-call {
    scroll-margin-top: 1.5rem;
    margin: 4rem 0 3.5rem;
    padding: clamp(1.5rem, 3.5vw, 2.75rem);
    border: 1px solid rgba(5, 105, 151, 0.16);
    border-radius: 1rem;
    background:
      radial-gradient(circle at 100% 0%, rgba(5, 105, 151, 0.11), transparent 30%),
      linear-gradient(145deg, #f9fcfa 0%, #f3f8f7 52%, #f2f8fb 100%);
    box-shadow: 0 1rem 2.5rem rgba(7, 54, 102, 0.08);
  }

  .scai-lightning-call {
    margin-top: 3.5rem;
    background:
      radial-gradient(circle at 0% 0%, rgba(103, 180, 44, 0.12), transparent 29%),
      linear-gradient(145deg, #fbfcf8 0%, #f2f8f4 48%, #eef7fa 100%);
  }

  .scai-call-header {
    display: grid;
    grid-template-columns: minmax(190px, 0.55fr) minmax(0, 1.45fr);
    gap: clamp(1.25rem, 4vw, 3.5rem);
    align-items: start;
    margin-bottom: 1.6rem;
    padding-bottom: 1.35rem;
    border-bottom: 1px solid rgba(5, 105, 151, 0.18);
  }

  .scai-call-kicker {
    margin: 0 0 0.4rem;
    color: var(--scai-green) !important;
    font-size: 0.74rem;
    font-weight: 750;
    letter-spacing: 0.14em;
    text-transform: uppercase;
  }

  .scai-call-header h2 {
    margin: 0;
    color: var(--scai-navy);
    font-size: clamp(1.75rem, 3vw, 2.4rem);
    letter-spacing: -0.03em;
  }

  .scai-call-intro p {
    margin: 0 0 0.7rem;
    color: #3c505c !important;
    line-height: 1.62;
  }

  .scai-call-intro p:last-child {
    margin-bottom: 0;
  }

  .scai-lightning-tagline {
    color: var(--scai-navy) !important;
    font-size: clamp(1.15rem, 2vw, 1.45rem);
    font-weight: 800;
    letter-spacing: -0.02em;
  }

  .scai-scope-reference {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    gap: 1.25rem;
    align-items: center;
    margin: 1rem 0 0;
    padding: 1rem 1.1rem;
    border-left: 4px solid var(--scai-teal);
    background: rgba(255, 255, 255, 0.78);
  }

  .scai-scope-reference p {
    margin: 0;
    color: #3c505c !important;
    font-size: 0.9rem;
    line-height: 1.55;
  }

  .scai-scope-reference strong {
    color: var(--scai-navy) !important;
  }

  .scai-scope-reference a {
    display: inline-block;
    padding: 0.58rem 0.8rem;
    border: 1px solid var(--scai-green);
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 750;
    text-decoration: none;
    white-space: nowrap;
  }

  .scai-scope-reference a:hover,
  .scai-scope-reference a:focus {
    background: var(--scai-green);
    color: #fff;
    text-decoration: none;
  }

  .scai-lightning-details {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
    margin-top: 1.2rem;
  }

  .scai-lightning-detail {
    min-width: 0;
    padding: 1.2rem;
    border: 1px solid rgba(29, 37, 44, 0.12);
    border-top: 0.3rem solid var(--detail-color);
    border-radius: 0.75rem;
    background: rgba(255, 255, 255, 0.92);
  }

  .scai-lightning-detail:nth-child(1) {
    --detail-color: var(--scai-lime);
  }

  .scai-lightning-detail:nth-child(2) {
    --detail-color: var(--scai-teal);
  }

  .scai-lightning-detail h3 {
    margin: 0 0 0.65rem;
    color: var(--scai-navy);
    font-size: 1.05rem;
    line-height: 1.3;
  }

  .scai-lightning-detail p {
    margin: 0;
    color: var(--scai-muted) !important;
    font-size: 0.9rem;
    line-height: 1.55;
  }

  .scai-lightning-detail p + p {
    margin-top: 0.7rem;
  }

  .scai-lightning-detail .scai-submission-note {
    margin-top: 0.8rem;
    padding-top: 0.75rem;
    border-top: 1px solid rgba(29, 37, 44, 0.1);
  }

  .scai-lightning-detail ul,
  .scai-submission-format ul {
    margin: 0;
    padding-left: 1.05rem;
  }

  .scai-lightning-detail li {
    margin-bottom: 0.45rem;
    color: #3f4e57 !important;
    font-size: 0.86rem;
    line-height: 1.47;
  }

  .scai-lightning-detail li:last-child {
    margin-bottom: 0;
  }

  .scai-submission-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.35fr) minmax(220px, 0.65fr);
    gap: clamp(1.25rem, 3vw, 2.5rem);
    margin-top: 1.7rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(5, 105, 151, 0.18);
  }

  .scai-submission-grid h3 {
    margin: 0 0 0.75rem;
    color: var(--scai-navy);
    font-size: 1.15rem;
  }

  .scai-submission-format li {
    margin-bottom: 0.45rem;
    color: #3f4e57 !important;
    font-size: 0.9rem;
    line-height: 1.5;
  }

  .scai-submission-note {
    margin: 0.9rem 0 0;
    color: var(--scai-muted) !important;
    font-size: 0.86rem;
    line-height: 1.55;
  }

  .scai-dates {
    padding: 1.15rem;
    border-radius: 0.7rem;
    background: var(--scai-navy);
    color: #fff;
  }

  .scai-dates h3 {
    color: #fff;
  }

  .scai-date-item {
    margin: 0;
    padding: 0.72rem 0;
    border-top: 1px solid rgba(255, 255, 255, 0.2);
  }

  .scai-date-item span {
    display: block;
    color: #bddbe8 !important;
    font-size: 0.7rem;
    font-weight: 750;
    letter-spacing: 0.09em;
    text-transform: uppercase;
  }

  .scai-date-item strong {
    display: block;
    margin-top: 0.15rem;
    color: #fff !important;
    font-size: 0.96rem;
  }

  .scai-submission-pending,
  .scai-submission-link {
    display: block;
    margin-top: 0.85rem;
    padding: 0.65rem 0.8rem;
    border: 1px solid rgba(255, 255, 255, 0.45);
    border-radius: 0.5rem;
    color: #fff !important;
    font-size: 0.8rem;
    font-weight: 700;
    text-align: center;
  }

  .scai-submission-link {
    background: #fff;
    color: var(--scai-navy) !important;
    text-decoration: none;
  }

  .scai-submission-link:hover,
  .scai-submission-link:focus {
    background: #dbeef5;
    color: var(--scai-navy) !important;
    text-decoration: none;
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
    .scai-call-header,
    .scai-scope-reference,
    .scai-submission-grid,
    .scai-agenda-coupling,
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

    .scai-layer:last-child {
      grid-column: 1 / -1;
    }

    .scai-lightning-details {
      grid-template-columns: 1fr;
    }

    .scai-scope-reference a {
      justify-self: start;
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

    .scai-layer:last-child {
      grid-column: auto;
    }

    .scai-call-link {
      align-items: flex-start;
      flex-direction: column;
      border-radius: 0.65rem;
    }

    .scai-call-link span {
      padding: 0;
      border-left: 0;
    }

  }
</style>

<div class="scai-page">
  <div class="scai-opening">
    <section class="scai-hero" aria-labelledby="scai-hero-title">
      <div class="scai-hero-inner">
        <div>
          <p class="scai-eyebrow">SCAI Research Symposium</p>
          <h2 id="scai-hero-title">
            <span class="scai-hero-line">Building sustainable</span>
            <span class="scai-hero-line">AI infrastructure for a</span>
            <span class="scai-hero-line">resource-constrained world</span>
          </h2>
          <p class="scai-hero-copy">A symposium imagining AI infrastructure as a flexible and responsible participant in the broader public-infrastructure ecosystem, designed to respect the resource constraints of existing infrastructure and serve the public good.</p>
          <div class="scai-hero-actions">
            <a class="scai-call-link" href="#call-for-posters">Call for posters <span>Deadline: August 28, 2026</span></a>
            <a class="scai-call-link" href="#call-for-lightning-talks">Call for lightning talks <span>Deadline: August 28, 2026</span></a>
          </div>
        </div>
        <div class="scai-logo-card">
          <img src="{{ site.base }}/img/scai-logo-banner.png" alt="SCAI Sustainable Compute and AI logo">
        </div>
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
        <dd>Invitation-only talks, panels, and poster sessions</dd>
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

  <section class="scai-section scai-agenda" id="research-agenda" aria-labelledby="agenda-heading">
    <div class="scai-section-header">
      <div>
        <p class="scai-eyebrow">The shared intellectual framework</p>
        <h2 id="agenda-heading">One research agenda, three coupled layers</h2>
      </div>
      <p>Frontier AI infrastructure is becoming a coupled cyber-physical system in which models, computing platforms, power systems, and public infrastructure can no longer be designed or operated independently. Models and workloads expose flexibility; computing systems translate it into safe operational decisions; and power systems and other public infrastructure define the physical, economic, and societal conditions within which training, inference, placement, cooling, and service design must adapt while preserving application-level guarantees.</p>
    </div>
    <div class="scai-layers">
      <article class="scai-layer">
        <span class="scai-layer-number" aria-hidden="true">01</span>
        <h3>AI and Workloads</h3>
        <p>How models and workloads can expose and use flexibility while preserving useful service and research outcomes.</p>
        <ul>
          <li>Flexible training and inference through checkpointing, pause and resume, batching, model selection, and precision scaling</li>
          <li>Trade-offs among accuracy, latency, throughput, availability, progress, cost, and resource consumption</li>
          <li>Efficient model techniques, including compression, sparsity, quantization, and workload-aware optimization</li>
          <li>Measurement and lifecycle analysis of energy, carbon, water, and material footprints</li>
        </ul>
      </article>
      <article class="scai-layer">
        <span class="scai-layer-number" aria-hidden="true">02</span>
        <h3>Computing Systems</h3>
        <p>How computing platforms can convert workload flexibility and changing resource conditions into reliable runtime action.</p>
        <ul>
          <li>Scheduling, placement, provisioning, and admission control across accelerators, clusters, clouds, and edge platforms</li>
          <li>Coordination across heterogeneous and geographically distributed computing resources</li>
          <li>Telemetry, forecasting, and feedback control across compute, network, storage, cooling, thermal, and power conditions</li>
          <li>Reliability, recovery, and controlled degradation that preserve application-level service objectives</li>
        </ul>
      </article>
      <article class="scai-layer">
        <span class="scai-layer-number" aria-hidden="true">03</span>
        <h3>Energy and Infrastructure</h3>
        <p>How large, dynamic AI loads interact with electric grids and the wider infrastructure systems that communities depend on.</p>
        <ul>
          <li>AI load modeling and forecasting, including effects on transmission, distribution, power quality, and stability</li>
          <li>Datacenter siting and interconnection, resource adequacy, capacity expansion, and coordinated infrastructure planning</li>
          <li>Grid-responsive control, demand response, ramp management, curtailment and recovery, ancillary services, and on-site resources</li>
          <li>Markets, tariffs, reliability, affordability, water, land, governance, and impacts on the public good</li>
        </ul>
      </article>
    </div>
    <div class="scai-agenda-coupling">
      <strong>Coupling is the research problem.</strong>
      <p>The agenda runs in both directions: infrastructure constraints must inform model and systems design, while workload capabilities and service objectives must inform datacenter, grid, and public-infrastructure planning and control.</p>
    </div>
    <div class="scai-community-row" aria-label="Research communities convened by the agenda">
      <span>AI and machine learning</span>
      <span>Computer and distributed systems</span>
      <span>Power systems and control</span>
      <span>Public infrastructure, planning, and policy</span>
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

  <section class="scai-participation-call scai-poster-call" id="call-for-posters" aria-labelledby="posters-heading">
    <div class="scai-call-header">
      <div>
        <p class="scai-call-kicker">Participate in the symposium</p>
        <h2 id="posters-heading">Call for Posters</h2>
      </div>
      <div class="scai-call-intro">
        <p>We invite poster submissions spanning AI, computing systems, sustainability, and public infrastructure.</p>
        <p>Published or accepted work, work in progress, new research directions, systems, datasets, testbeds, demonstrations, and interdisciplinary research are welcome. The session is designed to foster exchange across research and practitioner communities.</p>
      </div>
    </div>

    <div class="scai-scope-reference">
      <p><strong>Shared scope.</strong> Poster submissions may focus deeply on any one layer of the coupled research agenda or connect multiple layers. Cross-layer work that makes the relationship between AI, computing systems, and power or public infrastructure explicit is particularly encouraged.</p>
      <a href="#research-agenda">Review the research agenda</a>
    </div>

    <div class="scai-submission-grid">
      <div class="scai-submission-format">
        <h3>Submission format</h3>
        <ul>
          <li>A title, author list, affiliations, and contact information</li>
          <li>A brief abstract of up to 500 words describing the problem, motivation, approach, contribution, and current status of the work</li>
          <li>The most relevant layer or layers of the coupled research agenda</li>
          <li>For recently published or accepted work, the full citation and a link to the publication</li>
          <li>For work in progress, a brief description of preliminary findings, anticipated contributions, or questions on which feedback would be valuable</li>
        </ul>
        <p class="scai-submission-note">The poster session will be non-archival and is intended to encourage feedback, exchange, and collaboration. Selected authors will be invited to present their posters in person at the SCAI Research Symposium.</p>
      </div>

      <aside class="scai-dates" aria-label="Poster submission dates">
        <h3>Important dates</h3>
        <p class="scai-date-item"><span>Submission deadline</span><strong>August 28, 2026</strong></p>
        <p class="scai-date-item"><span>Acceptance notification</span><strong>September 1, 2026</strong></p>
        <p class="scai-date-item"><span>Symposium</span><strong>September 17&ndash;18, 2026</strong></p>
        <a class="scai-submission-link" href="https://forms.gle/Ayhcj3Z9JGedDrcY9" target="_blank" rel="noopener noreferrer">Submit a poster</a>
      </aside>
    </div>
  </section>

  <section class="scai-participation-call scai-lightning-call" id="call-for-lightning-talks" aria-labelledby="lightning-heading">
    <div class="scai-call-header">
      <div>
        <p class="scai-call-kicker">Contribute to the conversation</p>
        <h2 id="lightning-heading">Call for Lightning Talks</h2>
      </div>
      <div class="scai-call-intro">
        <p class="scai-lightning-tagline">New results, open questions, and emerging directions.</p>
        <p>The SCAI Research Symposium invites submissions for focused, 5-minute talks that introduce research or important challenges to an interdisciplinary community and spark further conversation.</p>
      </div>
    </div>

    <div class="scai-scope-reference">
      <p><strong>Shared scope.</strong> Talks may engage one layer of the coupled research agenda or connect several. Cross-layer questions, constraints, capabilities, and opportunities are especially welcome.</p>
      <a href="#research-agenda">Review the research agenda</a>
    </div>

    <div class="scai-lightning-details">
      <article class="scai-lightning-detail">
        <h3>Who should submit</h3>
        <p>Senior graduate students and postdoctoral researchers on the job market, early-career faculty, and mid-career faculty working across AI, computing systems, power systems and control, or other public-infrastructure domains.</p>
        <p>Published, accepted, ongoing, and preliminary work are all welcome; no paper is required.</p>
      </article>

      <article class="scai-lightning-detail">
        <h3>What works well</h3>
        <ul>
          <li>A recent or ongoing result</li>
          <li>An emerging direction, open problem, or provocative question</li>
          <li>A system, dataset, testbed, measurement effort, or deployment lesson</li>
          <li>A cross-layer technical or societal challenge</li>
        </ul>
        <p class="scai-submission-note">Keep the presentation focused rather than compressing a conventional conference talk.</p>
      </article>
    </div>

    <div class="scai-submission-grid">
      <div class="scai-submission-format">
        <h3>Submission format</h3>
        <ul>
          <li>Talk title, speaker name, and affiliation</li>
          <li>A brief description of the proposed talk, up to 150 words</li>
          <li>The most relevant layer or layers of the coupled research agenda</li>
          <li>A one-sentence answer to: <strong>What should the audience remember or discuss after your talk?</strong></li>
        </ul>
        <p class="scai-submission-note">The session is non-archival. Participation in the SCAI Research Symposium is by invitation.</p>
      </div>

      <aside class="scai-dates" aria-label="Lightning-talk submission dates">
        <h3>Important dates</h3>
        <p class="scai-date-item"><span>Submission deadline</span><strong>August 28, 2026</strong></p>
        <p class="scai-date-item"><span>Acceptance notification</span><strong>September 1, 2026</strong></p>
        <p class="scai-date-item"><span>Symposium</span><strong>September 17&ndash;18, 2026</strong></p>
        <a class="scai-submission-link" href="https://forms.gle/YaBgLckyGhicvvGp8" target="_blank" rel="noopener noreferrer">Submit a lightning talk</a>
      </aside>
    </div>
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
