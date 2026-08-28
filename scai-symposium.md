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

  .scai-opening > * {
    height: 100%;
  }

  .scai-hero {
    display: flex;
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
    width: 100%;
    min-height: 100%;
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

  .scai-hero-status {
    margin-top: 0.65rem;
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

  .scai-section-header-single {
    grid-template-columns: 1fr;
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

  .scai-talk {
    margin-top: 0.75rem;
    padding-top: 0.7rem;
    border-top: 1px solid rgba(29, 37, 44, 0.1);
  }

  .scai-talk summary {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.42rem 0.62rem;
    border: 1px solid rgba(47, 107, 79, 0.32);
    border-radius: 999px;
    color: var(--scai-green) !important;
    cursor: pointer;
    font-size: 0.76rem;
    font-weight: 750;
    line-height: 1.2;
    list-style: none;
  }

  .scai-talk summary::-webkit-details-marker {
    display: none;
  }

  .scai-talk summary::after {
    content: "+";
    font-size: 0.95rem;
    line-height: 1;
  }

  .scai-talk[open] summary::after {
    content: "\2212";
  }

  .scai-talk summary:hover,
  .scai-talk summary:focus {
    background: var(--scai-green);
    color: #fff !important;
  }

  .scai-talk-panel {
    margin-top: 0.7rem;
    padding: 0.8rem;
    border-radius: 0.55rem;
    background: #f1f7f3;
  }

  .scai-talk-panel h4 {
    margin: 0 0 0.5rem;
    color: var(--scai-navy);
    font-size: 0.88rem;
    line-height: 1.38;
  }

  .scai-talk-panel p {
    margin: 0;
    color: #3f4e57 !important;
    font-size: 0.78rem;
    line-height: 1.52;
  }

  .scai-talk-panel p + p {
    margin-top: 0.65rem;
  }

  .scai-note {
    margin-top: 1.15rem;
    color: var(--scai-muted) !important;
    font-size: 0.82rem;
  }

  .scai-program {
    scroll-margin-top: 1.5rem;
    margin: 4rem 0 3.5rem;
    padding: clamp(1.5rem, 3.5vw, 2.75rem);
    border: 1px solid rgba(5, 105, 151, 0.16);
    border-radius: 1rem;
    background:
      radial-gradient(circle at 100% 0%, rgba(5, 105, 151, 0.1), transparent 30%),
      linear-gradient(145deg, #fbfdfb 0%, #f3f8f5 50%, #f1f8fb 100%);
    box-shadow: 0 1rem 2.5rem rgba(7, 54, 102, 0.08);
  }

  .scai-draft-badge {
    display: inline-block;
    margin-bottom: 0.55rem;
    padding: 0.35rem 0.58rem;
    border-radius: 999px;
    background: #fff2cf;
    color: #72540a !important;
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .scai-program-days {
    display: grid;
    gap: 1.25rem;
  }

  .scai-agenda-view {
    display: none;
    align-items: center;
    justify-content: flex-end;
    gap: 0.4rem;
    margin: -0.25rem 0 1rem;
  }

  .scai-agenda-view.is-ready {
    display: flex;
  }

  .scai-agenda-view > span {
    margin-right: 0.25rem;
    color: var(--scai-muted) !important;
    font-size: 0.76rem;
    font-weight: 750;
  }

  .scai-agenda-view button {
    padding: 0.42rem 0.72rem;
    border: 1px solid rgba(5, 105, 151, 0.28);
    border-radius: 999px;
    background: #fff;
    color: var(--scai-navy);
    font: inherit;
    font-size: 0.74rem;
    font-weight: 750;
    line-height: 1;
    cursor: pointer;
  }

  .scai-agenda-view button:hover,
  .scai-agenda-view button:focus-visible,
  .scai-agenda-view button.is-active {
    border-color: var(--scai-green);
    background: var(--scai-green);
    color: #fff;
  }

  .scai-program-day {
    overflow: hidden;
    border: 1px solid rgba(29, 37, 44, 0.13);
    border-radius: 0.8rem;
    background: rgba(255, 255, 255, 0.94);
  }

  .scai-program-day h3 {
    margin: 0;
    padding: 0.95rem 1.1rem;
    background: var(--scai-navy);
    color: #fff;
    font-size: 1.05rem;
  }

  .scai-program-row {
    display: grid;
    grid-template-columns: 9rem minmax(0, 1fr);
    gap: 1rem;
    padding: 0.9rem 1.1rem;
    border-top: 1px solid rgba(29, 37, 44, 0.1);
  }

  .scai-program-row:nth-child(odd) {
    background: rgba(238, 247, 243, 0.54);
  }

  .scai-program-time {
    color: var(--scai-green) !important;
    font-size: 0.82rem;
    font-weight: 800;
    white-space: nowrap;
  }

  .scai-program-session strong {
    display: block;
    color: var(--scai-navy) !important;
    font-size: 0.94rem;
    line-height: 1.38;
  }

  .scai-program-session p {
    margin: 0.28rem 0 0;
    color: var(--scai-muted) !important;
    font-size: 0.82rem;
    line-height: 1.5;
  }

  .scai-session-details {
    margin-top: 0.5rem;
    border-top: 1px solid rgba(5, 105, 151, 0.14);
  }

  .scai-session-details summary {
    width: fit-content;
    padding-top: 0.45rem;
    color: var(--scai-green);
    font-size: 0.75rem;
    font-weight: 750;
    cursor: pointer;
  }

  .scai-session-details[open] summary {
    margin-bottom: 0.55rem;
  }

  .scai-session-details-panel {
    display: grid;
    gap: 0.55rem;
    padding: 0.7rem;
    border-radius: 0.55rem;
    background: rgba(241, 248, 246, 0.88);
  }

  .scai-session-person {
    padding-left: 0.7rem;
    border-left: 2px solid rgba(5, 105, 151, 0.3);
  }

  .scai-session-person strong,
  .scai-session-person span,
  .scai-session-person em {
    display: block;
  }

  .scai-session-person strong {
    font-size: 0.82rem;
  }

  .scai-session-person span {
    margin-top: 0.08rem;
    color: var(--scai-muted) !important;
    font-size: 0.76rem;
    line-height: 1.42;
  }

  .scai-session-person em {
    margin-top: 0.25rem;
    color: #243b4a !important;
    font-size: 0.76rem;
    font-style: normal;
    font-weight: 650;
    line-height: 1.42;
  }

  .scai-back-to-top {
    display: block;
    width: fit-content;
    margin: 1.25rem 0 0 auto;
    color: var(--scai-green) !important;
    font-size: 0.76rem;
    font-weight: 750;
    text-decoration: none;
  }

  .scai-back-to-top::before {
    content: "\2191";
    margin-right: 0.35rem;
  }

  .scai-back-to-top:hover,
  .scai-back-to-top:focus {
    text-decoration: underline;
  }

  .scai-codec .scai-back-to-top,
  .scai-callout .scai-back-to-top {
    grid-column: 1 / -1;
  }

  .scai-callout .scai-back-to-top {
    color: #bddbe8 !important;
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

  a.scai-status {
    text-decoration: none;
  }

  a.scai-status:hover,
  a.scai-status:focus {
    background: #fff;
    color: var(--scai-ink) !important;
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

    .scai-program-row {
      grid-template-columns: 1fr;
      gap: 0.25rem;
    }

    .scai-agenda-view {
      justify-content: flex-start;
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

<div class="scai-page" id="page-top">
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
          <div class="scai-hero-actions scai-hero-status">
            <a class="scai-call-link" href="#draft-agenda">Draft agenda <span>Subject to change</span></a>
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
        <dt>Organizer</dt>
        <dd><a href="https://groups.cs.umass.edu/hajiesmaili/">Mohammad Hajiesmaili</a></dd>
      </dl>
    </aside>
  </div>

  <section class="scai-codec" aria-labelledby="codec-heading">
    <div>
      <h2 id="codec-heading">Building on the NSF CoDec Expedition</h2>
      <p>SCAI grows from the UMass-led <strong>NSF CoDec Expedition in Computational Decarbonization</strong>, an interdisciplinary collaboration spanning six universities and bringing together expertise in theory, AI, systems, energy systems, the built environment, and economics. The symposium extends this foundation toward the coupled AI compute-and-energy infrastructure stack.</p>
    </div>
    <a class="scai-codec-link" href="https://codecexp.us/">Visit NSF CoDec</a>
    <a class="scai-back-to-top" href="#page-top">Back to top</a>
  </section>

  <section class="scai-section" aria-labelledby="speakers-heading">
    <div class="scai-section-header scai-section-header-single">
      <h2 id="speakers-heading">Invited speakers/panelists</h2>
    </div>

    <div class="scai-speakers">
      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/erin-baker.png" alt="Erin Baker" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.umass.edu/engineering/about/directory/erin-baker">Erin Baker</a></h3>
          <p class="scai-speaker-role">Distinguished Professor of Mechanical and Industrial Engineering and Faculty Director of the Energy Transition Institute, UMass Amherst</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/mosharaf-chowdhury.jpg" alt="Mosharaf Chowdhury" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://eecs.engin.umich.edu/people/chowdhury-mosharaf/">Mosharaf Chowdhury</a></h3>
          <p class="scai-speaker-role">Associate Professor of Computer Science and Engineering, University of Michigan</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>Toward Energy-Optimal AI</h4>
              <p>Generative AI adoption and its energy consumption are skyrocketing. Training a single frontier model can consume tens of GWh, while inference is rapidly outpacing training in aggregate energy demand. This talk introduces the ML.ENERGY Initiative and its work to measure where AI energy goes, optimize energy use without slowing training, and expose the tradeoffs between energy and performance. The tools and systems are open-sourced through the Zeus project.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/ayse-coskun.jpg" alt="Ayse K. Coskun" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.bu.edu/peaclab/people/faculty/">Ayse K. Coskun</a></h3>
          <p class="scai-speaker-role">Professor of Electrical and Computer Engineering and Systems Engineering and Director of CISE, Boston University; Chief Scientist, Emerald AI</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>AI Data Centers as Flexible Grid Assets</h4>
              <p>This talk explores how the rapid growth of AI is transforming data centers into major power consumers—and how, with the right technologies, they can become valuable grid resources. It discusses approaches to making AI workloads power-flexible and enabling data centers to dynamically adjust consumption in response to grid conditions while meeting performance constraints, drawing on real-world deployments.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/john-goodhue.jpg" alt="John Goodhue" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://mghpcc.org/executive-director/">John Goodhue</a></h3>
          <p class="scai-speaker-role">Executive Director, Massachusetts Green High Performance Computing Center</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/fabio-grimaldi.jpg" alt="Fabio Grimaldi" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.linkedin.com/in/fabio-grimaldi-530796ba/">Fabio Grimaldi</a></h3>
          <p class="scai-speaker-role">Senior Sustainability Scientist, Amazon Web Services</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>The Sustainability Stack for AI at Scale: An Industry Perspective</h4>
              <p>AI infrastructure offers a major opportunity to align large-scale computing with sustainability goals, but doing so requires scientific rigor, operational integration, and cross-industry collaboration. This talk describes AWS's approach across measurement, hardware and operational decarbonization, customer engagement, lifecycle assessment, research, and standardization.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/deepak-rajagopal.webp" alt="Deepak Rajagopal" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.ioes.ucla.edu/person/deepak-rajagopal/">Deepak Rajagopal</a></h3>
          <p class="scai-speaker-role">Professor and Co-Chair, Environmental Science and Engineering (D.Env.) Program, UCLA Institute of the Environment and Sustainability</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>The Challenges of Measuring AI's Environmental Footprint: An Industrial Ecology Perspective</h4>
              <p>We can increasingly measure what AI systems consume directly, but determining their lifecycle environmental impacts remains difficult. This talk uses industrial ecology, lifecycle assessment, and energy economics to examine operational and embodied impacts, system boundaries, uncertainty, rebound effects, supply-chain data gaps, and emerging disclosure requirements.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/shaolei-ren.jpg" alt="Shaolei Ren" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://shaoleiren.github.io/">Shaolei Ren</a></h3>
          <p class="scai-speaker-role">Professor of Electrical and Computer Engineering, University of California, Riverside</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>Powering AI in a Thirsty World</h4>
              <p>The rapid growth of AI is driving gigawatt-scale data centers and increasing demands on power grids and water infrastructure. This talk explores water-aware computing and cooling, coordination with power systems, and approaches for managing resource tradeoffs while strengthening infrastructure resilience and reducing impacts on surrounding communities.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/jeremy-rice.jpeg" alt="Jeremy Rice" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.linkedin.com/in/jeremy-rice-9a015b12/">Jeremy Rice</a></h3>
          <p class="scai-speaker-role">Mechanical Systems Lead, Verrus</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>Direct and Indirect Energy Resources Enabling the Data Center as a Grid Asset</h4>
              <p>This talk examines the operational flexibility of data centers through direct energy resources such as battery storage and dynamic IT loads, and indirect resources such as water use and flexible temperature interfaces. It considers how these variables can be coordinated so data centers support the grid while maintaining workload availability.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/yuanrui-sang.png" alt="Yuanrui Sang" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.umass.edu/engineering/about/directory/assistant-professor">Yuanrui Sang</a></h3>
          <p class="scai-speaker-role">Assistant Professor of Electrical and Computer Engineering, UMass Amherst</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/prashant-shenoy.jpg" alt="Prashant Shenoy" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://people.cs.umass.edu/~shenoy/">Prashant Shenoy</a></h3>
          <p class="scai-speaker-role">Distinguished Professor of Computer Science and Director of the NSF CoDec Expedition, UMass Amherst</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>Data Centers, AI Workloads, and Efficiency: A Systems Perspective</h4>
              <p>This talk offers a systems perspective on improving the efficiency and sustainability of cloud platforms as AI demand grows. It examines workload shifting across time and location, grid demand, energy availability, electricity prices, and the performance, efficiency, and cost tradeoffs involved in making computing systems grid-friendly.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/karin-strauss.jpg" alt="Karin Strauss" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.microsoft.com/en-us/research/people/kstrauss/">Karin Strauss</a></h3>
          <p class="scai-speaker-role">Innovation Strategist and Senior Principal Research Manager, Microsoft Research</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>AI Needs a Dose of Its Own Cure to Cut the Carbon. Let's Do It!</h4>
              <p>Efficiency makes AI more accessible and valuable, but it can also spur enough additional use that total consumption and emissions continue to rise. This talk connects efficient resource use with expanding low-carbon supplies of electricity and materials, and explores how AI itself can help create a virtuous cycle toward net zero.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/adam-wierman.png" alt="Adam Wierman" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.cms.caltech.edu/people/adamw">Adam Wierman</a></h3>
          <p class="scai-speaker-role">Carl F Braun Professor of Computing and Mathematical Sciences, Caltech</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/le-xie.jpg" alt="Le Xie" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://xielab.seas.harvard.edu/le-xie/">Le Xie</a></h3>
          <p class="scai-speaker-role">Gordon McKay Professor of Electrical Engineering and Faculty Director of the Power and AI Initiative, Harvard University</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/juncheng-yang.jpg" alt="Juncheng Yang" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://seas.harvard.edu/person/juncheng-yang">Juncheng Yang</a></h3>
          <p class="scai-speaker-role">Assistant Professor of Computer Science, Harvard University</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>Rethinking Storage for Sustainable AI: From Models to Generated Data</h4>
              <p>Modern AI systems create a growing storage sustainability challenge across model checkpoints, fine-tuned variants, and generated content. This talk presents ZipLLM, TensorDex, and LatentStore, illustrating how storage can be redesigned around the structure, semantics, and regenerability of AI data so computation and storage are jointly optimized.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/minlan-yu.jpg" alt="Minlan Yu" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://minlanyu.seas.harvard.edu/">Minlan Yu</a></h3>
          <p class="scai-speaker-role">Gordon McKay Professor of Computer Science, Harvard University</p>
          <details class="scai-talk">
            <summary>View talk</summary>
            <div class="scai-talk-panel">
              <h4>Resilient AI Infrastructure: From the GPU to the Grid</h4>
              <p>Modern AI infrastructure must operate through changing workloads, GPU and network interruptions, and fluctuating grid power. This talk presents work on scheduling inference with internal LLM signals, TrainMover for resilient large-model training, and the Harvard Power and AI Initiative's effort to coordinate flexible AI workloads with grid planning.</p>
            </div>
          </details>
        </div>
      </article>
    </div>
    <p class="scai-note">Participant and talk information reflects confirmations received to date and will be updated as additional details become available.</p>
    <a class="scai-back-to-top" href="#page-top">Back to top</a>
  </section>

  <section class="scai-section scai-agenda" id="research-agenda" aria-labelledby="agenda-heading">
    <div class="scai-section-header">
      <div>
        <p class="scai-eyebrow">The shared intellectual framework</p>
        <h2 id="agenda-heading">One research agenda, three coupled layers</h2>
      </div>
      <p>We envision AI infrastructure as a coupled cyber-physical system spanning three interdependent layers. In this vision, models and workloads expose flexibility, computing systems translate that flexibility into reliable operational decisions, and energy systems and public infrastructure shape the physical, economic, and societal conditions under which those decisions are made. This vision motivates a shared research agenda across three coupled layers: AI and workloads, computing systems, and energy and infrastructure.</p>
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
    <a class="scai-back-to-top" href="#page-top">Back to top</a>
  </section>

  <section class="scai-program" id="draft-agenda" aria-labelledby="draft-agenda-heading">
    <div class="scai-section-header">
      <div>
        <span class="scai-draft-badge">Draft &middot; Subject to change</span>
        <h2 id="draft-agenda-heading">Symposium agenda</h2>
      </div>
      <p>Two days of invited talks, panels, research highlights, poster presentations, and structured conversation across AI systems, data-center infrastructure, power systems, environmental impacts, and public priorities. Times, session titles, and participation may change as the program is finalized.</p>
    </div>

    <div class="scai-agenda-view" aria-label="Agenda detail level">
      <span>Agenda view</span>
      <button type="button" class="is-active" data-agenda-view="compact" aria-pressed="true">Compact</button>
      <button type="button" data-agenda-view="expanded" aria-pressed="false">Expanded</button>
    </div>

    <div class="scai-program-days">
      <section class="scai-program-day" aria-labelledby="day-one-heading">
        <h3 id="day-one-heading">Day 1 &mdash; Thursday, September 17</h3>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T08:30">8:30&ndash;9:00 am</time>
          <div class="scai-program-session"><strong>Registration, breakfast, and informal networking</strong></div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T09:00">9:00&ndash;9:20 am</time>
          <div class="scai-program-session">
            <strong>Welcome remarks</strong>
            <p>Mike Malone, Laura Vandenberg, and Sanjay Raman &middot; Chair: Mohammad Hajiesmaili</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Mike Malone</strong><span>Vice Chancellor for Research and Engagement, UMass Amherst</span><em>Welcome remarks</em></div>
                <div class="scai-session-person"><strong>Laura Vandenberg</strong><span>Associate Vice Chancellor and Vice Provost for Research and Engagement; Professor of Environmental Health Sciences, UMass Amherst</span><em>Welcome remarks</em></div>
                <div class="scai-session-person"><strong>Sanjay Raman</strong><span>Daniel J. Riccio Jr. Dean of Engineering; Professor of Electrical and Computer Engineering, UMass Amherst</span><em>Welcome remarks</em></div>
                <div class="scai-session-person"><strong>Mohammad Hajiesmaili</strong><span>Associate Professor, Manning College of Information and Computer Sciences, UMass Amherst</span><em>Session chair</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T09:20">9:20&ndash;10:30 am</time>
          <div class="scai-program-session">
            <strong>Expeditions Keynotes</strong>
            <p>Adam Wierman and Prashant Shenoy</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Adam Wierman</strong><span>Carl F Braun Professor of Computing and Mathematical Sciences, Caltech</span><em>Talk: TBD</em></div>
                <div class="scai-session-person"><strong>Prashant Shenoy</strong><span>Distinguished Professor of Computer Science and Director of the NSF CoDec Expedition, UMass Amherst</span><em>Talk: Data Centers, AI Workloads, and Efficiency: A Systems Perspective</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T10:30">10:30&ndash;10:45 am</time>
          <div class="scai-program-session"><strong>Break</strong></div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T10:45">10:45 am&ndash;12:00 pm</time>
          <div class="scai-program-session">
            <strong>Industry Session I</strong>
            <p>Karin Strauss and Fabio Grimaldi</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Karin Strauss</strong><span>Innovation Strategist and Senior Principal Research Manager, Microsoft Research</span><em>Talk: AI Needs a Dose of Its Own Cure to Cut the Carbon. Let&rsquo;s Do It!</em></div>
                <div class="scai-session-person"><strong>Fabio Grimaldi</strong><span>Senior Sustainability Scientist, Amazon Web Services</span><em>Talk: The Sustainability Stack for AI at Scale: An Industry Perspective</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T12:00">12:00&ndash;1:00 pm</time>
          <div class="scai-program-session"><strong>Lunch</strong></div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T13:00">1:00&ndash;1:10 pm</time>
          <div class="scai-program-session">
            <strong>Afternoon welcome remarks</strong>
            <p>Caitlyn Butler and Brian Levine</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Caitlyn Butler</strong><span>Associate Dean for Research and Graduate Affairs, Riccio College of Engineering; Professor of Civil and Environmental Engineering, UMass Amherst</span><em>Welcome remarks</em></div>
                <div class="scai-session-person"><strong>Brian Levine</strong><span>Associate Dean of IT and Facilities; Distinguished Professor, Manning College of Information and Computer Sciences, UMass Amherst</span><em>Welcome remarks</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T13:10">1:10&ndash;2:00 pm</time>
          <div class="scai-program-session">
            <strong>Panel I: What Should Academia Solve for the Future of AI Infrastructure?</strong>
            <p>Karin Strauss, Fabio Grimaldi, Adam Wierman, and Prashant Shenoy &middot; Moderator: Laura Haas</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Karin Strauss</strong><span>Innovation Strategist and Senior Principal Research Manager, Microsoft Research</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Fabio Grimaldi</strong><span>Senior Sustainability Scientist, Amazon Web Services</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Adam Wierman</strong><span>Carl F Braun Professor of Computing and Mathematical Sciences, Caltech</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Prashant Shenoy</strong><span>Distinguished Professor of Computer Science and Director of the NSF CoDec Expedition, UMass Amherst</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Laura Haas</strong><span>Professor, Manning College of Information and Computer Sciences, UMass Amherst</span><em>Moderator</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T14:00">2:00&ndash;3:00 pm</time>
          <div class="scai-program-session">
            <strong>Faculty and emerging-researcher highlights</strong>
            <p>Faculty talks: Juncheng Yang, Yuanrui Sang, and Nicolas Christianson &middot; Job-market talks: Speakers TBD</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Juncheng Yang</strong><span>Assistant Professor of Computer Science, Harvard University</span><em>Talk: Rethinking Storage for Sustainable AI: From Models to Generated Data</em></div>
                <div class="scai-session-person"><strong>Yuanrui Sang</strong><span>Assistant Professor of Electrical and Computer Engineering, UMass Amherst</span><em>Talk: TBD</em></div>
                <div class="scai-session-person"><strong>Nicolas Christianson</strong><span>Assistant Professor of Computer Science, Johns Hopkins University</span><em>Talk: TBD</em></div>
                <div class="scai-session-person"><strong>Job-market talks</strong><span>Speakers and affiliations TBD</span><em>Talks: TBD</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T15:00">3:00&ndash;3:15 pm</time>
          <div class="scai-program-session"><strong>Break and refreshments</strong></div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T15:15">3:15&ndash;4:00 pm</time>
          <div class="scai-program-session">
            <strong>Technical Session I: Responsible AI Infrastructure</strong>
            <p>Shaolei Ren and Deepak Rajagopal</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Shaolei Ren</strong><span>Professor of Electrical and Computer Engineering, University of California, Riverside</span><em>Talk: Powering AI in a Thirsty World</em></div>
                <div class="scai-session-person"><strong>Deepak Rajagopal</strong><span>Professor and Co-Chair, Environmental Science and Engineering Program, UCLA Institute of the Environment and Sustainability</span><em>Talk: The Challenges of Measuring AI&rsquo;s Environmental Footprint: An Industrial Ecology Perspective</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T16:00">4:00&ndash;5:00 pm</time>
          <div class="scai-program-session">
            <strong>Panel II: Can AI Infrastructure Scale Responsibly? Impacts on the Grid, Water, and Communities</strong>
            <p>Le Xie, Shaolei Ren, Deepak Rajagopal, and Erin Baker &middot; Moderator: Golbon Zakeri</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Le Xie</strong><span>Gordon McKay Professor of Electrical Engineering and Faculty Director of the Power and AI Initiative, Harvard University</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Shaolei Ren</strong><span>Professor of Electrical and Computer Engineering, University of California, Riverside</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Deepak Rajagopal</strong><span>Professor and Co-Chair, Environmental Science and Engineering Program, UCLA Institute of the Environment and Sustainability</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Erin Baker</strong><span>Distinguished Professor of Mechanical and Industrial Engineering and Faculty Director of the Energy Transition Institute, UMass Amherst</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Golbon Zakeri</strong><span>Professor of Mechanical and Industrial Engineering, UMass Amherst</span><em>Moderator</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T16:45">4:45&ndash;6:00 pm</time>
          <div class="scai-program-session"><strong>Poster session</strong></div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T18:00">6:00&ndash;7:30 pm</time>
          <div class="scai-program-session"><strong>Dinner and networking</strong></div>
        </div>
      </section>

      <section class="scai-program-day" aria-labelledby="day-two-heading">
        <h3 id="day-two-heading">Day 2 &mdash; Friday, September 18</h3>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-18T08:30">8:30&ndash;9:00 am</time>
          <div class="scai-program-session"><strong>Light breakfast and arrival</strong></div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-18T09:00">9:00&ndash;9:10 am</time>
          <div class="scai-program-session">
            <strong>Welcome remarks</strong>
            <p>James Allan</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>James Allan</strong><span>Associate Dean of Research and Engagement; Distinguished Professor, Manning College of Information and Computer Sciences, UMass Amherst</span><em>Welcome remarks</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-18T09:10">9:10&ndash;10:40 am</time>
          <div class="scai-program-session">
            <strong>Industry Session II: Flexible Data Centers</strong>
            <p>Ayse K. Coskun, Jeremy Rice, and John Goodhue</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Ayse K. Coskun</strong><span>Professor of Electrical and Computer Engineering and Systems Engineering; Director of the Center for Information and Systems Engineering, Boston University; Chief Scientist, Emerald AI</span><em>Talk: AI Data Centers as Flexible Grid Assets</em></div>
                <div class="scai-session-person"><strong>Jeremy Rice</strong><span>Mechanical Systems Lead, Verrus</span><em>Talk: Direct and Indirect Energy Resources Enabling the Data Center as a Grid Asset</em></div>
                <div class="scai-session-person"><strong>John Goodhue</strong><span>Executive Director, Massachusetts Green High Performance Computing Center</span><em>Talk: TBD</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-18T10:40">10:40&ndash;10:50 am</time>
          <div class="scai-program-session"><strong>Break</strong></div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-18T10:50">10:50 am&ndash;12:00 pm</time>
          <div class="scai-program-session">
            <strong>Technical Session II: Frontiers of AI Systems and Networking</strong>
            <p>Mosharaf Chowdhury and Minlan Yu</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Mosharaf Chowdhury</strong><span>Associate Professor of Computer Science and Engineering, University of Michigan</span><em>Talk: Toward Energy-Optimal AI</em></div>
                <div class="scai-session-person"><strong>Minlan Yu</strong><span>Gordon McKay Professor of Computer Science, Harvard University</span><em>Talk: Resilient AI Infrastructure: From the GPU to the Grid</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-18T12:00">12:00&ndash;1:00 pm</time>
          <div class="scai-program-session"><strong>Lunch and structured networking</strong></div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-18T13:00">1:00&ndash;2:00 pm</time>
          <div class="scai-program-session">
            <strong>Panel III: How Flexible Can AI Infrastructure Really Be?</strong>
            <p>Ayse K. Coskun, Jeremy Rice, Mosharaf Chowdhury, and Minlan Yu &middot; Moderator: David Irwin</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Ayse K. Coskun</strong><span>Professor of Electrical and Computer Engineering and Systems Engineering; Director of the Center for Information and Systems Engineering, Boston University; Chief Scientist, Emerald AI</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Jeremy Rice</strong><span>Mechanical Systems Lead, Verrus</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Mosharaf Chowdhury</strong><span>Associate Professor of Computer Science and Engineering, University of Michigan</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Minlan Yu</strong><span>Gordon McKay Professor of Computer Science, Harvard University</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>David Irwin</strong><span>Professor and Associate Department Head of Electrical and Computer Engineering; Adjunct Professor of Computer Science, UMass Amherst</span><em>Moderator</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-18T14:00">2:00&ndash;3:00 pm</time>
          <div class="scai-program-session"><strong>Additional speakers</strong><p>Speakers TBD &middot; Talks TBD</p></div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-18T15:00">3:00&ndash;3:15 pm</time>
          <div class="scai-program-session">
            <strong>Closing remarks</strong>
            <p>Prashant Shenoy and David Irwin</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Prashant Shenoy</strong><span>Distinguished Professor of Computer Science and Director of the NSF CoDec Expedition, UMass Amherst</span><em>Closing remarks</em></div>
                <div class="scai-session-person"><strong>David Irwin</strong><span>Professor and Associate Department Head of Electrical and Computer Engineering; Adjunct Professor of Computer Science, UMass Amherst</span><em>Closing remarks</em></div>
              </div>
            </details>
          </div>
        </div>
      </section>
    </div>
    <a class="scai-back-to-top" href="#page-top">Back to top</a>
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
        <p class="scai-date-item"><span>Acceptance notification</span><strong>August 31, 2026</strong></p>
        <p class="scai-date-item"><span>Registration deadline</span><strong>September 2, 2026</strong></p>
        <p class="scai-date-item"><span>Symposium</span><strong>September 17&ndash;18, 2026</strong></p>
        <a class="scai-submission-link" href="https://forms.gle/Ayhcj3Z9JGedDrcY9" target="_blank" rel="noopener noreferrer">Submit a poster</a>
      </aside>
    </div>
    <a class="scai-back-to-top" href="#page-top">Back to top</a>
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
        <p class="scai-date-item"><span>Acceptance notification</span><strong>August 31, 2026</strong></p>
        <p class="scai-date-item"><span>Registration deadline</span><strong>September 2, 2026</strong></p>
        <p class="scai-date-item"><span>Symposium</span><strong>September 17&ndash;18, 2026</strong></p>
        <a class="scai-submission-link" href="https://forms.gle/YaBgLckyGhicvvGp8" target="_blank" rel="noopener noreferrer">Submit a lightning talk</a>
      </aside>
    </div>
    <a class="scai-back-to-top" href="#page-top">Back to top</a>
  </section>

  <section class="scai-callout" aria-labelledby="participate-heading">
    <div>
      <h2 id="participate-heading">Invitation-only symposium</h2>
      <p>The symposium will bring together invited researchers, infrastructure practitioners, utilities, policymakers, UMass campus leadership, state officials, and partners interested in the future of reliable, grid-aware AI systems. If you are interested in attending, please email <a href="mailto:hajiesmaili@cs.umass.edu" style="color: #fff; text-decoration: underline;">Mohammad Hajiesmaili</a> at <a href="mailto:hajiesmaili@cs.umass.edu" style="color: #fff; text-decoration: underline;">hajiesmaili@cs.umass.edu</a>.</p>
    </div>
    <a class="scai-status" href="#draft-agenda">View draft agenda</a>
    <a class="scai-back-to-top" href="#page-top">Back to top</a>
  </section>
</div>

<script>
  (function () {
    var agenda = document.getElementById("draft-agenda");
    if (!agenda) return;

    var controls = agenda.querySelector(".scai-agenda-view");
    var buttons = agenda.querySelectorAll("[data-agenda-view]");
    var details = agenda.querySelectorAll(".scai-session-details");
    if (!controls || !buttons.length || !details.length) return;

    controls.classList.add("is-ready");
    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        var expanded = button.getAttribute("data-agenda-view") === "expanded";
        details.forEach(function (item) { item.open = expanded; });
        buttons.forEach(function (item) {
          var active = item === button;
          item.classList.toggle("is-active", active);
          item.setAttribute("aria-pressed", active ? "true" : "false");
        });
      });
    });
  }());
</script>

<!--
Speaker image sources:
- Erin Baker: https://www.umass.edu/engineering/about/directory/erin-baker
- Adam Wierman: https://heritageproject.caltech.edu/interviews/adam-wierman
- Prashant Shenoy: https://people.cs.umass.edu/~shenoy/
- Karin Strauss: https://www.microsoft.com/en-us/research/people/kstrauss/
- Fabio Grimaldi: https://www.linkedin.com/in/fabio-grimaldi-530796ba/
- Ayse K. Coskun: https://www.bu.edu/peaclab/people/faculty/
- Juncheng Yang: https://seas.harvard.edu/person/juncheng-yang
- Jeremy Rice: portrait supplied by the symposium organizer.
- Shaolei Ren: https://shaoleiren.github.io/
- Mosharaf Chowdhury: https://cse.engin.umich.edu/stories/mosharaf-chowdhury-receives-david-e-liddle-research-excellence-award
- Minlan Yu: https://minlanyu.seas.harvard.edu/
- John Goodhue: https://mghpcc.org/executive-director/
- Deepak Rajagopal: https://www.ioes.ucla.edu/person/deepak-rajagopal/
- Le Xie: https://xielab.seas.harvard.edu/le-xie/
- Yuanrui Sang: https://www.umass.edu/engineering/about/directory/assistant-professor
-->
