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
    column-gap: clamp(1.5rem, 4vw, 3.5rem);
    row-gap: 0.65rem;
    align-items: center;
    margin: 3.25rem 0;
    padding: clamp(1rem, 2vw, 1.35rem) clamp(1.25rem, 4vw, 2.6rem);
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
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 0.75rem;
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

  .scai-speaker-labels {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin: 0 0 0.5rem;
  }

  .scai-speaker-label {
    display: inline-flex;
    margin: 0;
    padding: 0.28rem 0.48rem;
    border-radius: 999px;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.06em;
    line-height: 1;
    text-transform: uppercase;
  }

  .scai-speaker-label-speaker {
    background: rgba(47, 107, 79, 0.11);
    color: var(--scai-green) !important;
  }

  .scai-speaker-label-panelist {
    background: rgba(5, 105, 151, 0.1);
    color: var(--scai-blue) !important;
  }

  .scai-speaker-details {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, max-content));
    gap: 0.45rem;
    margin-top: 0.75rem;
    padding-top: 0.7rem;
    border-top: 1px solid rgba(29, 37, 44, 0.1);
  }

  .scai-talk {
    min-width: 0;
  }

  .scai-speaker-details .scai-talk[open] {
    grid-column: 1 / -1;
  }

  .scai-speaker-details-single {
    grid-template-columns: minmax(0, max-content);
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

  .scai-talk.is-active summary {
    border-color: var(--scai-green);
    background: var(--scai-green);
    color: #fff !important;
  }

  .scai-talk.is-active summary::after {
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

  .scai-talk-panel a {
    overflow-wrap: anywhere;
  }

  .scai-talk-panel p + p {
    margin-top: 0.65rem;
  }

  .scai-speakers.is-wide-details .scai-talk-panel {
    display: none;
  }

  .scai-speaker.is-reader-active {
    border-color: rgba(47, 107, 79, 0.62);
    box-shadow: 0 0 0 2px rgba(47, 107, 79, 0.12), 0 0.65rem 1.5rem rgba(45, 38, 32, 0.1);
  }

  .scai-speaker-reader {
    position: relative;
    display: grid;
    grid-column: 1 / -1;
    grid-template-columns: minmax(180px, 0.7fr) minmax(0, 2.3fr);
    gap: clamp(1.25rem, 3vw, 2.4rem);
    margin: 0.15rem 0 0.6rem;
    padding: clamp(1.25rem, 2.8vw, 2rem);
    border: 1px solid rgba(47, 107, 79, 0.28);
    border-radius: 0.85rem;
    background:
      radial-gradient(circle at 100% 0%, rgba(5, 105, 151, 0.08), transparent 32%),
      linear-gradient(145deg, #f8fbf9 0%, #f1f7f3 100%);
    box-shadow: 0 0.7rem 1.7rem rgba(45, 38, 32, 0.08);
  }

  .scai-speaker-reader[hidden] {
    display: none;
  }

  .scai-speaker-reader-meta {
    padding-right: clamp(1rem, 2.5vw, 2rem);
    border-right: 1px solid rgba(47, 107, 79, 0.18);
  }

  .scai-speaker-reader-kicker {
    margin: 0 0 0.5rem;
    color: var(--scai-green) !important;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .scai-speaker-reader h3 {
    margin: 0 0 0.45rem;
    padding-right: 1.75rem;
    color: var(--scai-navy);
    font-size: clamp(1.35rem, 2vw, 1.75rem);
    line-height: 1.15;
  }

  .scai-speaker-reader-role {
    margin: 0;
    color: var(--scai-muted) !important;
    font-size: 0.86rem;
    line-height: 1.5;
  }

  .scai-speaker-reader-content {
    width: 100%;
    max-width: 82ch;
    align-self: start;
  }

  .scai-speaker-reader-content h4 {
    margin: 0 2.4rem 0.8rem 0;
    color: var(--scai-navy);
    font-size: clamp(1.1rem, 1.6vw, 1.35rem);
    line-height: 1.35;
  }

  .scai-speaker-reader-content p {
    margin: 0;
    color: #344650 !important;
    font-size: 0.96rem;
    line-height: 1.68;
  }

  .scai-speaker-reader-content p + p {
    margin-top: 0.9rem;
  }

  .scai-speaker-reader-content a {
    overflow-wrap: anywhere;
  }

  .scai-speaker-reader-close {
    position: absolute;
    top: 0.85rem;
    right: 0.9rem;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.38rem 0.55rem;
    border: 1px solid rgba(29, 37, 44, 0.16);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.82);
    color: var(--scai-muted);
    cursor: pointer;
    font: inherit;
    font-size: 0.75rem;
    font-weight: 750;
  }

  .scai-speaker-reader-close:hover,
  .scai-speaker-reader-close:focus {
    border-color: var(--scai-green);
    color: var(--scai-green);
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

  .scai-session-person strong a {
    color: var(--scai-navy) !important;
    text-decoration: underline;
    text-decoration-color: rgba(5, 105, 151, 0.35);
    text-underline-offset: 0.15em;
  }

  .scai-session-person strong a:hover,
  .scai-session-person strong a:focus {
    color: var(--scai-green) !important;
    text-decoration-color: currentColor;
  }

  .scai-session-description {
    margin: 0.45rem 0 0 !important;
    color: #3f4e57 !important;
    font-size: 0.76rem !important;
    line-height: 1.5 !important;
  }

  .scai-session-group-label {
    margin-top: 0.2rem;
    padding-top: 0.7rem;
    border-top: 1px solid rgba(5, 105, 151, 0.16);
    color: var(--scai-green) !important;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.07em;
    text-transform: uppercase;
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

  .scai-codec .scai-back-to-top {
    margin-top: 0;
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

    .scai-speaker-reader {
      grid-template-columns: 1fr;
      gap: 1rem;
    }

    .scai-speaker-reader-meta {
      padding: 0 2.5rem 0.9rem 0;
      border-right: 0;
      border-bottom: 1px solid rgba(47, 107, 79, 0.18);
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

    .scai-speaker-reader {
      padding: 1.1rem;
    }

    .scai-speaker-reader-content p {
      font-size: 0.91rem;
    }

  }
</style>

<div class="scai-page" id="page-top">
  <div class="scai-opening">
    <section class="scai-hero" aria-labelledby="scai-hero-title">
      <div class="scai-hero-inner">
        <div>
          <p class="scai-eyebrow">Sustainable Compute &amp; AI Infrastructure (SCAI) Research Symposium</p>
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

  <section class="scai-section" id="speakers" aria-labelledby="speakers-heading">
    <div class="scai-section-header scai-section-header-single">
      <h2 id="speakers-heading">Invited speakers/panelists</h2>
    </div>

    <div class="scai-speakers">
      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/erin-baker.png" alt="Erin Baker" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.umass.edu/engineering/about/directory/erin-baker" target="_blank" rel="noopener noreferrer">Erin Baker</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Distinguished Professor of Mechanical and Industrial Engineering and Faculty Director of the Energy Transition Institute, UMass Amherst</p>
          <div class="scai-speaker-details scai-speaker-details-single">
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Erin Baker is a Distinguished Professor of Mechanical and Industrial Engineering at UMass Amherst and Faculty Director of the Energy Transition Institute. Her research applies operations research and economics to decision-making under uncertainty in energy and the environment, with an emphasis on energy justice and publicly funded energy-technology research and development in the face of climate change.</p>
                <p>Her modeling work addresses energy policy and planning across geographic and temporal scales and uses multiple parallel models to derive robust insights. She also studies the sustainability of electricity grids in New England and developing countries, as well as the environmental costs and benefits of offshore wind energy.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/mosharaf-chowdhury.jpg" alt="Mosharaf Chowdhury" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://eecs.engin.umich.edu/people/chowdhury-mosharaf/" target="_blank" rel="noopener noreferrer">Mosharaf Chowdhury</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Associate Professor of Computer Science and Engineering, University of Michigan</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>Toward Energy-Optimal AI</h4>
                <p>Generative AI adoption and its energy consumption are skyrocketing. Training a single frontier model can consume tens of GWh, and inference is rapidly outpacing training in aggregate energy demand. This surge is inflating operational costs, and power delivery is now the gating factor for bringing new GPU capacity online.</p>
                <p>In this talk, I will introduce the ML.ENERGY Initiative, our effort to understand and curtail AI's runaway energy demands on three fronts. First, understanding where energy goes: I will present tools to precisely measure AI energy consumption and findings from benchmarking open-weight models across hardware and serving configurations via the ML.ENERGY Leaderboard. Second, optimizing energy use: I will describe how identifying computations on and off the critical path in distributed training enables precise GPU frequency control, saving energy on non-critical work without slowing down training. Third, exposing tradeoffs: I will present how co-optimizing static and dynamic energy through better kernel scheduling reveals the Pareto frontier between energy and performance, enabling practitioners to make informed deployment decisions under diverse constraints. All tools and systems are open-sourced through the Zeus project. I will conclude with open problems in building energy-optimal AI systems.</p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Mosharaf Chowdhury is an Associate Professor of Computer Science and Engineering at the University of Michigan, Ann Arbor, where he leads the SymbioticLab. His research focuses on making AI/ML workloads more efficient, with a particular emphasis on reducing their energy consumption through the ML Energy Initiative. Major open-source projects from his team include Infiniswap, the first scalable memory disaggregation solution; FedScale, a planetary-scale AI/ML platform; TPP, a tiered memory manager integrated into the Linux kernel (v5.18+); and Zeus, the first energy-optimal generative AI stack. Previously, Mosharaf invented the concept of coflows and was one of the original creators of Apache Spark. He has received numerous individual honors, including fellowships and paper awards from NSDI, OSDI, ATC, and MICRO.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/ayse-coskun.jpg" alt="Ayse K. Coskun" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.bu.edu/peaclab/people/faculty/" target="_blank" rel="noopener noreferrer">Ayse K. Coskun</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Professor of Electrical and Computer Engineering and Systems Engineering and Director of CISE, Boston University; Chief Scientist, Emerald AI</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>AI Data Centers as Flexible Grid Assets</h4>
                <p>This talk explores how the rapid growth of AI is transforming data centers into major power consumers—and how, with the right technologies, data centers can become valuable grid resources instead. The talk will discuss emerging approaches to making AI workloads "power-flexible" and enabling data centers to dynamically adjust consumption in response to grid conditions while meeting performance constraints. Drawing from real-world deployments, the talk highlights how grid-interactive data centers can accelerate interconnection and support a more resilient and affordable power grid.</p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Professor Ayse Coskun is the Chief Scientist at Emerald AI, a startup focused on enabling power flexibility in data centers. She is also a full professor in the Electrical and Computer Engineering Department at Boston University, where she leads the Center for Information and Systems Engineering and serves as Associate Dean for Research at the College of Engineering (currently on leave from BU).</p>
                <p>Prof. Coskun is widely recognized as a leading academic authority on orchestrating data center power demand in response to power grid needs. Her broader research applies AI and machine learning to optimize cloud and high-performance computing systems. She has received many honors for her contributions, including the Ernest Kuh Award for energy-efficient system-level design and an IBM Faculty Award for applying AI-based methods in DevSecOps. Earlier in her career, Prof. Coskun worked in industry at Sun Microsystems (now Oracle). She recently served as Deputy Editor-in-Chief of IEEE Transactions on Computer-Aided Design and holds a PhD in Computer Science and Engineering from the University of California, San Diego.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/john-goodhue.jpg" alt="John Goodhue" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://mghpcc.org/executive-director/" target="_blank" rel="noopener noreferrer">John Goodhue</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span></div>
          <p class="scai-speaker-role">Executive Director, Massachusetts Green High Performance Computing Center</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>Massachusetts Green High Performance Computing Center</h4>
                <p>A talk introducing MGHPCC facilities, capabilities, and opportunities for research collaboration </p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>John Goodhue is Executive Director of the Massachusetts Green High Performance Computing Center, an energy-efficient data center and consortium serving more than 20,000 researchers, students, and educators at Boston University, Harvard University, MIT, Northeastern University, the University of Massachusetts, and other institutions across the Northeast. His work focuses on regional and national collaboration around research-computing infrastructure, broadening access to advanced computing for researchers at small and mid-sized institutions, and developing a diverse next generation of computing professionals.</p>
                <p>His research-infrastructure leadership includes the Northeast Storage Exchange, Open Storage Network, Northeast Big Data Hub, Eastern Regional Network, and Northeast Cyberteam. He also brings 30 years of industry experience in networking and high-performance computing, including technology leadership, engineering management, and general management roles at Cisco Systems and BBN Technologies, along with work on the management teams of several Boston-area startups. He holds a B.S. in Computer Science and Engineering from MIT.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/fabio-grimaldi.jpg" alt="Fabio Grimaldi" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.linkedin.com/in/fabio-grimaldi-530796ba/" target="_blank" rel="noopener noreferrer">Fabio Grimaldi</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Senior Sustainability Scientist, Amazon Web Services</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>The Sustainability Stack for AI at Scale: An Industry Perspective</h4>
                <p>AI infrastructure presents one of the single biggest opportunities of our time to align large-scale computing with sustainability goals — but realizing that opportunity requires scientific rigor, operational integration, and cross-industry collaboration that match the complexity of the underlying systems. From embodied carbon in accelerator chips to operational energy across globally distributed fleets, quantifying and reducing the environmental footprint of AI compute demands work across materials science, systems engineering, power systems, and policy.
This talk describes how AWS approaches this challenge across interconnected layers. Measurement: building lifecycle assessment methodologies for AI hardware and operations, addressing data availability gaps, and working with service teams to quantify emissions from training and inference at the most granular level. Decarbonization of hardware and operations: making carbon metrics visible to service teams, integrating with financial and planning systems, co-owning reduction goals with infrastructure owners, and embedding sustainability into early-stage hardware and service design. Customer engagement: providing emissions reporting through public-facing tools and supporting responsible use of cloud and AI services. Cross-industry research and standardization: publishing methodology openly, contributing to Product Category Rule development, providing technical input to public policy teams on regulatory frameworks, and collaborating with partners across the full value chain — from manufacturers to academia to initiatives like SCAI — to advance the science of sustainable computing.</p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Fabio Grimaldi is a Senior Sustainability Scientist at AWS, where he leads the development of methodologies and large-scale models to track and improve the sustainability performance of AWS cloud services. He drives the adoption of sustainability metrics across AWS services, translating data into actionable insights that help AWS and its customers meet their sustainability goals. Fabio joined Amazon in 2022. He holds a PhD in Chemical Engineering from the University College London.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/laura-haas.jpg" alt="Laura Haas" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.cics.umass.edu/about/directory/laura-haas" target="_blank" rel="noopener noreferrer">Laura Haas</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Professor, Manning College of Information and Computer Sciences, UMass Amherst</p>
          <div class="scai-speaker-details scai-speaker-details-single">
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Laura Haas is a Professor in the Manning College of Information and Computer Sciences at UMass Amherst. She joined UMass in 2017 after a distinguished career at IBM, where she was an IBM Fellow and held leadership roles including Director of the Accelerated Discovery Lab, Director of Computer Science at the Almaden Research Center, and head of IBM Research’s worldwide exploratory science program.</p>
                <p>Her foundational contributions to database systems include the Starburst query processor, which became the basis for DB2 LUW; Garlic, an early system for integrating heterogeneous data sources; and Clio, the first semi-automatic tool for heterogeneous schema mapping. As the first permanent dean of Manning CICS, she led substantial growth in the college, expanded faculty and student diversity, oversaw the design and construction of a new academic building, and helped raise more than $100 million from public, industry, and philanthropic sources. Haas is an ACM Fellow, a member of the National Academy of Engineering and IBM Academy of Technology, and a Fellow of the American Academy of Arts and Sciences. She earned her Ph.D. in Computer Science from the University of Texas at Austin and her A.B. in Computer Science from Harvard University.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/deepak-rajagopal.webp" alt="Deepak Rajagopal" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.ioes.ucla.edu/person/deepak-rajagopal/" target="_blank" rel="noopener noreferrer">Deepak Rajagopal</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Professor and Co-Chair, Environmental Science and Engineering (D.Env.) Program, UCLA Institute of the Environment and Sustainability</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>The Challenges of Measuring AI's Environmental Footprint: An Industrial Ecology Perspective</h4>
                <p>We can increasingly measure what AI systems consume directly, but it remains difficult to determine their lifecycle environmental impacts. For instance, operational energy and water use can often be measured with relatively direct activity data and established emissions factors. Yet for major AI infrastructure providers, much of the reported greenhouse-gas footprint appears to lie upstream—in semiconductor fabrication, server manufacturing, construction, and other capital goods or downstream (end-of-life treatment) —where data and estimates tend to be incomplete and uncertain. Beyond the own lifecycle of AI systems, their may arise major impacts, both positive and negative, on the broader economy and society that tended to be even harder to isolate and quantify, The result is a measurement asymmetry: some of the impacts that are easiest to quantify might not necessarily be the largest and most uncertain.</p>
                <p>Industrial ecology, life-cycle assessment, and energy economics provide mature conceptual frameworks for addressing such issues. They distinguish attributional from consequential effects, embodied from operational impacts, and direct from indirect and economy-wide rebound. They also provide a disciplined way to ask a question often neglected in AI sustainability debates: how far should the system boundary expand before additional precision ceases to justify its cost?</p>
                <p>From a public policy standpoint, California’s SB 253 is a first-of-a-kind policy going into effect in 2027 which requires large firms doing business in California to disclose Scope 1, 2, and eventually Scope 3 GHG emissions under standardized rules and phased third-party assurance. Such regulations necessitate consistency, transparency, and accountability in measuring and reporting lifecycle emissions of AI. But disclosure alone will not eliminate uncertainty where underlying supply-chain data remain modeled or incomplete. The central challenge, therefore, is not simply more measurement but distinguish what is directly observed from what is estimated, make uncertainty explicit, and design reporting systems that improve decision-relevant accuracy without creating a false impression of precision.</p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Deepak Rajagopal is a Professor in the UCLA Institute of the Environment and Sustainability and Dept. of Urban Planning in the UCLA Luskin School of Public Affairs. His fields of research include Industrial Ecology and Life cycle assessment, applied economic analysis of energy and environmental policies. He is also a faculty Scientist in the Energy Analysis Division at the Lawrence Berkeley National Laboratory. He has a Ph.D. in Energy and Resources from UC Berkeley, MS degrees in Ag. and Resource Economics (UC Berkeley), and Mechanical Engineering (U. of Maryland, College Park) and B.Tech. in Mechanical Engineering (Indian Institute. of Technology, Madras). He has been a post-doctoral researcher at the Energy Biosciences Institute, UC Berkeley and also worked as a Structural Engineer at United Technologies Research Center, E.Hartford, Connecticut. </p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/shaolei-ren.jpg" alt="Shaolei Ren" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://shaoleiren.github.io/" target="_blank" rel="noopener noreferrer">Shaolei Ren</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Professor of Electrical and Computer Engineering, University of California, Riverside</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>Powering AI in a Thirsty World</h4>
                <p>The rapid growth of artificial intelligence (AI) is driving the construction of gigawatt-scale data centers, placing increasing demands on both power grids and water infrastructure. Yet power and water are tightly coupled: water-intensive cooling can compete for local water resources and create risks to data center resilience, while waterless cooling can increase electricity demand and further stress the local grid. This tradeoff is particularly significant on the hottest days of the year, when both power and water systems are under stress. Despite these interdependencies, power and water are often planned and managed separately, overlooking important opportunities for coordination.</p>
                <p>This talk explores how responsible AI infrastructure design and operations can address coupled power-water challenges. I will discuss water-aware computing and cooling, coordination with power systems, and approaches for managing resource tradeoffs while strengthening infrastructure resilience and reducing impacts on surrounding communities.</p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Shaolei Ren is a Professor of Electrical and Computer Engineering at the University of California, Riverside. His research broadly focuses on developing modeling frameworks, algorithms, and empirical methodologies to address challenges at the intersection of AI, computing systems, and communities. He is a recipient of the U.S. National Science Foundation CAREER Award (2015) and several paper awards, including at ACM e-Energy (2024, 2016) and IEEE ICC (2016). He received his Ph.D. degree from the University of California, Los Angeles.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/jeremy-rice.jpeg" alt="Jeremy Rice" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.linkedin.com/in/jeremy-rice-9a015b12/" target="_blank" rel="noopener noreferrer">Jeremy Rice</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Mechanical Systems Lead, Verrus</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>Direct and Indirect Energy Resources Enabling the Data Center as a Grid Asset</h4>
                <p>As data centers become increasingly integrated into the modern power grid, the demand for operational flexibility has never been greater. This talk explores the multi-faceted power and energy impacts of a flexible data center, specifically focusing on the complex interactions between direct energy resources, such as battery energy storage systems (BESS) and dynamic IT loads and indirect energy resources, such as water usage and flexible temperature interfaces. By examining these variables in concert, we can better understand how data centers can become grid assets, while maintaining the required availability of the IT workloads and constraining the use of the indirect energy resources.</p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Jeremy Rice, Ph.D., is a seasoned engineering leader with over two decades of experience spanning the "chip to chiller" stack. Currently, he serves as the Mechanical Systems Lead at Verrus LLC.</p>
                <p>Prior to Verrus, Jeremy held a significant tenure at Google within their data center organization, where he focused on asset utilization, system simplification, and acted as a technical liaison between the IT and data center teams. He also brings extensive experience in IT-side hardware, having advanced the state of the art in both air and liquid cooling technologies.</p>
                <p>Jeremy holds a Bachelor of Science and a Ph.D. in Mechanical Engineering from the University of Connecticut.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/yuanrui-sang.png" alt="Yuanrui Sang" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.umass.edu/engineering/about/directory/assistant-professor" target="_blank" rel="noopener noreferrer">Yuanrui Sang</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span></div>
          <p class="scai-speaker-role">Assistant Professor of Electrical and Computer Engineering, UMass Amherst</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>Flexible Data Centers Scheduling: Economic, Environmental, and Transmission Congestion Impacts</h4>
                <p>Simultaneously considering optimization of operating cost, greenhouse gas, and toxic emissions, this talk discusses a tri-objective, multi-period, power system-constrained framework to schedule flexible data center load. The framework Models data center power consumption as the sum of latency-critical and best-effort loads and considers the temporal flexibility of best-effort workload. The framework was implemented on standard power system test systems with data centers, and pareto fronts were obtained from the solutions. Trade-offs between different objectives are analyzed, and the impacts on electricity prices and system congestions were discussed.</p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Yuanrui Sang is an assistant professor in the Department of Electrical and Computer Engineering at the University of Massachusetts Amherst. Before joining UMass in 2024, she was an assistant professor at The University of Texas at El Paso, and she received her Ph.D. in electrical and computer engineering from The University of Utah in 2019. Her research interests include power system operation and planning, grid-enhancing technologies, and the integration of flexible load, such as data centers and electric vehicles, in power systems.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/prashant-shenoy.jpg" alt="Prashant Shenoy" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://people.cs.umass.edu/~shenoy/" target="_blank" rel="noopener noreferrer">Prashant Shenoy</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span></div>
          <p class="scai-speaker-role">Distinguished Professor of Computer Science and Director of the NSF CoDec Expedition, UMass Amherst</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>Data Centers, AI Workloads, and Efficiency: A Systems Perspective</h4>
                <p>The exponential growth of cloud computing has been a defining trend of our time, fueled by rapidly growing demands from online and data-intensive  workloads. Despite the end of Denard scaling, the cloud's energy demand grew more slowly than expected over the past decade due to the aggressive implementation of energy-efficiency optimizations. However, the rise of AI workloads, which are often more resource-intensive than traditional cloud workloads, has led to rapid growth in data centers with power-hungry accelerators such as GPUs and TPUs, leading to a resurgence in the cloud's energy consumption and a strain on our electric grids.</p>
                <p>In this talk, I will provide a systems perspective on the challenges and opportunities in enhancing the efficiency and sustainability of cloud platforms in the face of rising AI demand. I will discuss how resource management techniques such as workload shifting can enhance the efficiency of cloud platforms by exploiting the spatio-temporal variability in grid demand, energy availability, and electricity prices. I will present initial directions in making current computing systems grid-friendly and discuss approaches for navigating performance, efficiency, and cost tradeoffs that arise in their operations. I will end with several open research challenges that the research community needs to tackle to make AI-driven cloud platforms grid-friendly and ensure their continued growth.</p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Prashant Shenoy is currently a Distinguished Professor  in the College of Information and Computer Sciences at the University of Massachusetts Amherst. He received the B.Tech degree in Computer Science and Engineering from the Indian Institute of Technology, Bombay and the M.S and Ph.D degrees in Computer Science from the University of Texas, Austin. His research interests lie in distributed systems and networking, with a recent emphasis on cloud and sustainable computing. He has been the recipient of several best paper awards at leading conferences, including two ACM Test of Time Awards. He is a fellow of the ACM, IEEE, AAAS, and AAIA.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/ramesh-sitaraman.jpg" alt="Ramesh Sitaraman" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.cics.umass.edu/about/directory/ramesh-sitaraman" target="_blank" rel="noopener noreferrer">Ramesh Sitaraman</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Distinguished Professor, Manning College of Information and Computer Sciences, UMass Amherst; Chief Consulting Scientist, Akamai Technologies</p>
          <div class="scai-speaker-details scai-speaker-details-single">
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Ramesh Sitaraman is a Distinguished Professor in the Manning College of Information and Computer Sciences at UMass Amherst and Chief Consulting Scientist at Akamai Technologies. His research spans Internet-scale distributed systems, including algorithms, architectures, performance, energy efficiency, and user behavior. During his time in industry, he helped create the world’s first major content delivery network and pioneered distributed systems that deliver web content, video, applications, and online services to billions of users.</p>
                <p>He is the founding director of UMass Amherst’s interdisciplinary Informatics undergraduate program and a Fellow of both ACM and IEEE. His honors include the inaugural ACM SIGCOMM Networking Systems Award for his work on the Akamai CDN, an Excellence in DASH Award for adaptive-bitrate algorithms used in commercial video streaming, the UMass Amherst Distinguished Teaching Award, and NSF Research Initiation and CAREER awards. He earned his Ph.D. in Computer Science from Princeton University and his B.Tech. from the Indian Institute of Technology Madras.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/karin-strauss.jpg" alt="Karin Strauss" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.microsoft.com/en-us/research/people/kstrauss/" target="_blank" rel="noopener noreferrer">Karin Strauss</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Innovation Strategist and Senior Principal Research Manager, Microsoft Research</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>AI Needs a Dose of Its Own Cure to Cut the Carbon. Let’s Do It!</h4>
                <p>As we ride the Cambrian explosion of AI, gains in the efficiency of resource use have become ever more important. They make the technology more accessible, enabling more models, features, products, and applications, increasing the value of AI. But as this community has pointed out, efficiency could backfire as a climate strategy: making AI more efficient could spur so much additional use that total consumption and absolute emissions might keep climbing. So if efficiency’s shadow twin, the availability of low carbon supply, is neglected, increasing value may come with rising environmental cost. After celebrating the progress this community has made on using resources efficiently, on carbon-aware computing, and on measuring embodied carbon, I will turn to increasing that low carbon supply of electricity and materials to build on, and I will share some of the work we are doing in this space. AI, so often seen as adding pressure against reaching net zero, can instead be a positive force to achieve it. Together, AI that makes resource use more efficient and AI that expands low carbon supply can drive a virtuous cycle, and this community can, and I will argue should, participate in both.</p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Karin Strauss is a Senior Principal Research Manager and Innovation Strategist at Microsoft Research and an Affiliate Professor in the Paul G. Allen School of Computer Science &amp; Engineering at the University of Washington. Her work spans computer systems, synthetic biology and environmental sustainability, with research ranging from machine learning hardware and emerging memory technologies to biologically inspired computing. She is best known for pioneering DNA data storage systems, a project that received broad industry and media recognition. More recently, she has focused on making AI and IT infrastructure more sustainable. </p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/adam-wierman.png" alt="Adam Wierman" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.cms.caltech.edu/people/adamw" target="_blank" rel="noopener noreferrer">Adam Wierman</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Carl F Braun Professor of Computing and Mathematical Sciences, Caltech</p>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/le-xie.jpg" alt="Le Xie" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://xielab.seas.harvard.edu/le-xie/" target="_blank" rel="noopener noreferrer">Le Xie</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Gordon McKay Professor of Electrical Engineering and Faculty Director of the Power and AI Initiative, Harvard University</p>
          <div class="scai-speaker-details scai-speaker-details-single">
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Le Xie is the Gordon McKay Professor of Electrical Engineering at the Harvard John A. Paulson School of Engineering and Applied Sciences and Faculty Director of the Power and AI Initiative at Harvard SEAS. Before joining Harvard, he served on the faculty of Texas A&amp;M University from 2010 to 2024. He earned his B.E. in Electrical Engineering from Tsinghua University, S.M. in Engineering Sciences from Harvard, and Ph.D. in Electrical and Computer Engineering from Carnegie Mellon University. His industry experience includes work at ISO New England and Edison Mission Energy Marketing and Trading.</p>
                <p>His research interests include modeling and control in data-rich large-scale systems, the grid integration of clean-energy resources, and electricity markets. He is an IEEE Fellow and IEEE Power &amp; Energy Society Distinguished Lecturer, and is the lead author of <em>Data Science and Applications for Modern Power Systems</em>.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/juncheng-yang.jpg" alt="Juncheng Yang" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://seas.harvard.edu/person/juncheng-yang" target="_blank" rel="noopener noreferrer">Juncheng Yang</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span></div>
          <p class="scai-speaker-role">Assistant Professor of Computer Science, Harvard University</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>Rethinking Storage for Sustainable AI: From Models to Generated Data</h4>
                <p>The rapid growth of AI is creating a new storage sustainability challenge. Modern AI systems produce and retain enormous amounts of data—from billions of model checkpoints and fine-tuned variants to an ever-growing volume of AI-generated content. Yet today’s storage systems largely treat these objects as conventional byte streams, ignoring the rich structure and semantics introduced by AI workloads.</p>
                <p>In this talk, I will present our recent work on rethinking storage systems for AI data. I will first discuss ZipLLM, which exploits relationships among models and combines model-aware compression with deduplication to substantially reduce the footprint of large model repositories. I will then present TensorDex, which pushes this idea further by treating tensors, rather than files or models, as first-class storage objects and exploiting relationships among tensors across an entire model ecosystem. Finally, I will discuss LatentStore, which revisits a more fundamental question for AI-generated data: do we need to store the generated object at all? By storing compact model-native representations and reconstructing data on demand, LatentStore trades increasingly inexpensive computation for reductions in long-term storage.</p>
                <p>Together, these systems illustrate a broader opportunity: rather than applying traditional storage techniques directly to rapidly growing AI data, we can redesign the storage stack around the structure, semantics, and regenerability of AI workloads. I will conclude with a broader vision for sustainable AI storage, where computation and storage are jointly optimized to reduce the growing resource and environmental footprint of AI. </p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Juncheng Yang is an Assistant Professor in Harvard John A. Paulson School of Engineering and Applied Sciences. His research interests broadly cover the efficiency, performance, reliability, and sustainability of large-scale data systems and machine learning systems.</p>
                <p>Juncheng's works have received best paper awards or honorable mention at VLDB'26, VALUETOOLS'24, NSDI'24, NSDI'21, SOSP'21, and SYSTOR'16. Juncheng was a Facebook Fellow, recognized as a Rising Star in machine learning and systems, and a Google Cloud Research Innovator. His dissertation on designing efficient and scalable cache management systems received the CMU SCS Doctoral Dissertation Award and the ACM SIGOPS Dennis M. Ritchie Doctoral Dissertation Award. </p>
                <p>His works have been widely adopted. For example, S3-FIFO and SIEVE are adopted for production at hundreds of companies with more than 60 open-source libraries and packages in 18 programming languages. Moreover, his group maintains libCacheSim, the most popular cache simulation library, and freeinference, a free LLM inference service. </p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/minlan-yu.jpg" alt="Minlan Yu" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://minlanyu.seas.harvard.edu/" target="_blank" rel="noopener noreferrer">Minlan Yu</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-speaker">Speaker</span><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Gordon McKay Professor of Computer Science, Harvard University</p>
          <div class="scai-speaker-details">
            <details class="scai-talk">
              <summary>Talk</summary>
              <div class="scai-talk-panel">
                <h4>Resilient AI Infrastructure: From the GPU to the Grid</h4>
                <p>Modern AI systems run on massive, costly infrastructure that must operate under three kinds of change: workload changes, as agentic request rates, output lengths, and tool-calling times vary continuously; infrastructure interruptions, as GPU and network failures, preemptions, and maintenance repeatedly halt training at scale; and power changes, as available grid power fluctuates. In this talk, I will present our recent work on resilient AI infrastructure that adapts to all three. For workload changes, we use internal LLM signals to schedule inference requests, from standalone inferences to agentic workflows, cutting latency and improving efficiency. For infrastructure interruptions, we introduce TrainMover, a resilient LLM training runtime which leverages elastic and standby machines to handle interruptions with minimal downtime. For power changes, we started the Harvard Power and AI Initiative to rethink the coordination between the power grid and AI infrastructure—making AI workloads flexible and making grid planning matching such flexibility. </p>
              </div>
            </details>
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Minlan Yu is a Gordon McKay professor at the Harvard School of Engineering and Applied Science. She’s the assistant director of the SRC/DARPA JUMP 2.0 ACE Center for Evolvable Computing, and the co-director for the Harvard power and AI initiative. She received her B.A. in computer science and mathematics from Peking University and her M.A. and PhD in computer science from Princeton University. She received the ACM-W rising star award, NSF CAREER award, and ACM SIGCOMM doctoral dissertation award. She served as PC co-chair for SIGCOMM, NSDI, HotNets, and several other conferences and workshops.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <article class="scai-speaker">
        <img class="scai-speaker-photo" src="{{ site.base }}/img/scai-speakers/golbon-zakeri.jpg" alt="Golbon Zakeri" loading="lazy">
        <div class="scai-speaker-body">
          <h3><a href="https://www.umass.edu/engineering/about/directory/golbon-zakeri" target="_blank" rel="noopener noreferrer">Golbon Zakeri</a></h3>
          <div class="scai-speaker-labels"><span class="scai-speaker-label scai-speaker-label-panelist">Panelist</span></div>
          <p class="scai-speaker-role">Professor of Mechanical and Industrial Engineering and Director of the Northeast Power Economics and Analytics Research Lab, UMass Amherst</p>
          <div class="scai-speaker-details scai-speaker-details-single">
            <details class="scai-talk">
              <summary>Biography</summary>
              <div class="scai-talk-panel">
                <p>Golbon Zakeri is a Professor of Operations Research in the Department of Mechanical and Industrial Engineering at UMass Amherst and Director of the Northeast Power Economics and Analytics Research Lab. Her research develops analytics, economic models, and optimization methods for decision-making under uncertainty, with particular emphasis on electricity markets and power systems. She uses mathematical modeling to study policies and system designs that support efficient, reliable, resilient, and equitable energy procurement.</p>
                <p>Before joining UMass Amherst, Zakeri was a faculty member at the University of Auckland, where she directed the Electric Power Optimization Centre, served as Deputy Director of the University of Auckland Energy Centre, and was President of the Operations Research Society of New Zealand from 2013 to 2017. Her prior experience also includes research at Argonne National Laboratory. She serves as an Area Editor for Energy and Environment at <em>Operations Research</em>, an editor of the INFORMS-Springer book series, and an associate editor for <em>Computational Management Science</em>. She earned her Ph.D. in Mathematics and Computer Science from the University of Wisconsin–Madison.</p>
              </div>
            </details>
          </div>
        </div>
      </article>

      <aside class="scai-speaker-reader" id="scai-speaker-reader" aria-labelledby="scai-speaker-reader-name" aria-live="polite" hidden>
        <div class="scai-speaker-reader-meta">
          <p class="scai-speaker-reader-kicker"></p>
          <h3 id="scai-speaker-reader-name"></h3>
          <p class="scai-speaker-reader-role"></p>
        </div>
        <div class="scai-speaker-reader-content"></div>
        <button class="scai-speaker-reader-close" type="button" aria-label="Close speaker details">Close <span aria-hidden="true">&times;</span></button>
      </aside>
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
            <p>Brian Levine</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Brian Levine</strong><span>Associate Dean of Research &amp; Engagement; Distinguished Professor, Manning College of Information and Computer Sciences, UMass Amherst</span><em>Welcome remarks</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T13:10">1:10&ndash;2:00 pm</time>
          <div class="scai-program-session">
            <strong>Panel I: What Should Academia Solve for the Future of AI Infrastructure?</strong>
            <p>Karin Strauss, Fabio Grimaldi, Adam Wierman, and Ramesh Sitaraman &middot; Moderator: Laura Haas</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Karin Strauss</strong><span>Innovation Strategist and Senior Principal Research Manager, Microsoft Research</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Fabio Grimaldi</strong><span>Senior Sustainability Scientist, Amazon Web Services</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Adam Wierman</strong><span>Carl F Braun Professor of Computing and Mathematical Sciences, Caltech</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Ramesh Sitaraman</strong><span>Distinguished Professor, Manning College of Information and Computer Sciences, UMass Amherst; Chief Consulting Scientist, Akamai Technologies</span><em>Panelist</em></div>
                <div class="scai-session-person"><strong>Laura Haas</strong><span>Professor, Manning College of Information and Computer Sciences, UMass Amherst</span><em>Moderator</em></div>
              </div>
            </details>
          </div>
        </div>
        <div class="scai-program-row">
          <time class="scai-program-time" datetime="2026-09-17T14:00">2:00&ndash;3:00 pm</time>
          <div class="scai-program-session">
            <strong>Faculty and emerging-researcher highlights</strong>
            <p>Faculty talks: Juncheng Yang and Yuanrui Sang &middot; Job-market talks: Walid Abdelrahman Hanafy, Can Hankendi, Adam Lechowicz, Qingsong Liu, Talha Mehboob, and Christopher Yeh</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>Juncheng Yang</strong><span>Assistant Professor of Computer Science, Harvard University</span><em>Talk: Rethinking Storage for Sustainable AI: From Models to Generated Data</em></div>
                <div class="scai-session-person"><strong>Yuanrui Sang</strong><span>Assistant Professor of Electrical and Computer Engineering, UMass Amherst</span><em>Talk: Flexible Data Centers Scheduling: Economic, Environmental, and Transmission Congestion Impacts</em></div>
                <div class="scai-session-group-label">Job-market talks</div>
                <div class="scai-session-person">
                  <strong><a href="https://people.cs.umass.edu/~whanafy/" target="_blank" rel="noopener noreferrer">Walid Abdelrahman Hanafy</a></strong>
                  <span>UMass Amherst</span>
                  <em>Talk: Flex: Grid-Responsive Provisioning and Scheduling for Elastic Cloud Clusters</em>
                  <p class="scai-session-description">The talk will explain the workload and temporal coupling inherent in carbon-aware resource provisioning and scheduling for data centers, and why effective management must account for (i) the cluster’s current and anticipated demand and its elasticity, (ii) exogenous grid signals and their variability, and (iii) the trade-off between delaying work and the potential savings enabled by waiting.</p>
                  <p class="scai-session-description">To address these challenges, I proposed Flex, a grid-responsive resource manager that jointly provisions cluster capacity and schedules elastic batch jobs. Flex addresses this coupling by computing optimal provisioning and scheduling decisions over recent historical conditions and reusing those decisions at runtime. I show that this approach provides an effective and practical method for grid-responsive management of elastic batch workloads</p>
                </div>
                <div class="scai-session-person">
                  <strong><a href="https://www.hankendi.com" target="_blank" rel="noopener noreferrer">Can Hankendi</a></strong>
                  <span>Boston University</span>
                  <em>Talk: PALS: Power-Aware LLM Serving for Grid-Interactive AI</em>
                  <p class="scai-session-description">Large-scale LLM inference is becoming a significant and increasingly dynamic data-center load, yet today’s serving systems largely treat GPU power as a fixed hardware constraint. This talk presents PALS, a power-aware LLM serving framework that makes GPU power a first-class runtime control knob. At runtime, PALS selects GPU power caps, batch sizes, and tensor-parallel configurations based on profiled power–performance tradeoffs, adapting the serving configuration as the available power budget changes. Implemented within vLLM, PALS shows how inference workloads can respond to changing power constraints while maintaining application-level performance and QoS. I will discuss results across dense and Mixture-of-Experts models and show how application-aware power management can connect LLM serving objectives with data-center and grid-level power requirements. More broadly, PALS illustrates how AI workloads can expose controllable flexibility rather than behaving as fixed electrical loads.</p>
                </div>
                <div class="scai-session-person">
                  <strong><a href="https://adamlechowicz.github.io" target="_blank" rel="noopener noreferrer">Adam Lechowicz</a></strong>
                  <span>University of Massachusetts Amherst</span>
                  <em>Talk: Unlocking System Control Benefits of AI using Theoretical Modeling</em>
                  <p class="scai-session-description">AI and machine learning can improve decision-making in complex systems, but their unreliability remains a major barrier in settings where feasibility and worst-case guarantees matter. This lightning talk presents a perspective on how theoretical modeling can help bridge that gap. Focusing on online decision-making under uncertainty, I describe a “robust algorithm learning” approach: first analytically characterize a certificate set of algorithms that provably satisfy a robustness guarantee, such as a competitive-ratio bound; then use data-driven learning to optimize performance within that "safe" search space. This combines classical theoretical tools for identifying structural guarantees with modern learning methods that adapt algorithms to real problem instances. I illustrate the idea through our SIGMETRICS 2026 work on online smoothed demand management, where the approach is instantiated and evaluated. More broadly, the talk argues that theory can make AI-driven control schemes practical in systems such as data centers and power grids by constraining learning without giving up its performance benefits.</p>
                </div>
                <div class="scai-session-person">
                  <strong><a href="https://qingsong-liu.github.io/" target="_blank" rel="noopener noreferrer">Qingsong Liu</a></strong>
                  <span>Caltech &amp; UMass Amherst</span>
                  <em>Talk: Decisions That Reshape the System: Closed-Loop Learning and Resource Allocation for Stateful AI Infrastructure</em>
                  <p class="scai-session-description">Modern computing systems must learn and allocate resources under uncertainty while meeting operational constraints. Yet their decisions often have persistent effects: configuration changes take time to settle, admitted workloads occupy capacity and shape future feedback, and repeated use can alter resource performance. These effects violate standard assumptions that feedback is immediate, resources are consumed only once, or system dynamics are fixed. My research develops algorithmic foundations with provable guarantees for such stateful online decision-making and translates them into closed-loop control for AI infrastructure. I will highlight three themes—convergence-aware learning, reusable capacity management, and deterioration-aware allocation—and show how they motivate a future agenda in capacity management for heterogeneous AI clusters, multi-timescale LLM serving, and agentic infrastructure.</p>
                </div>
                <div class="scai-session-person">
                  <strong><a href="https://talhamehboob10.github.io" target="_blank" rel="noopener noreferrer">Talha Mehboob</a></strong>
                  <span>University of Massachusetts Amherst</span>
                  <em>Talk: Optimizing the Performance and Efficiency of Distributed Model Training under Resource Constraint</em>
                  <p class="scai-session-description">This talk explores methods for efficiently distributing large-scale machine learning workloads across geographically dispersed, power-constrained data centers. As foundational models exceed single-site capacities, training infrastructure must adapt to dynamic power availability and heterogeneous network conditions. The presentation outlines systems like PowerTrip and PowerScale which utilize dynamic site selection and hierarchical aggregation to balance aggregate computing power against WAN communication overhead. These frameworks improve efficiency by adjusting synchronization frequencies based on runtime network constraints and cluster topologies. Carbon-aware execution architectures, including EcoLearn, mitigate environmental impacts by aligning workload schedules with time-varying grid carbon intensities. By combining computation-communication overlap with adaptive scheduling, these systems significantly reduce training energy and inference carbon footprints while maintaining strict time-to-accuracy objectives.</p>
                </div>
                <div class="scai-session-person">
                  <strong><a href="https://chrisyeh96.github.io" target="_blank" rel="noopener noreferrer">Christopher Yeh</a></strong>
                  <span>Harvard University</span>
                  <em>Talk: Online conformal risk control for energy applications</em>
                  <p class="scai-session-description">Integrating AI into modern energy systems requires ensuring safety, even under distribution shift. Online conformal risk control presents a promising approach to achieve long-run online safety guarantees including under distribution shift, but typically without accounting for decision costs. In this work, we demonstrate that the trade-off between decision costs and long-run risk control is naturally formulated as an instance of constrained online convex optimization (COCO) with long-term constraints: the safety loss defines the per-round constraint, while the decision loss defines the per-round objective. Building upon results from the COCO literature, we derive the first sublinear static regret guarantees for online conformal prediction, including in settings where the safety constraint functions are either convex or monotone. We demonstrate the utility of our approach on battery storage arbitrage settings.</p>
                </div>
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
            <p>James Allan and Caitlyn Butler</p>
            <details class="scai-session-details">
              <summary>Full session details</summary>
              <div class="scai-session-details-panel">
                <div class="scai-session-person"><strong>James Allan</strong><span>Senior Associate Dean of Operations; Distinguished Professor, Manning College of Information and Computer Sciences, UMass Amherst</span><em>Welcome remarks</em></div>
                <div class="scai-session-person"><strong>Caitlyn Butler</strong><span>Associate Dean for Research and Graduate Affairs, Riccio College of Engineering; Professor of Civil and Environmental Engineering, UMass Amherst</span><em>Welcome remarks</em></div>
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
                <div class="scai-session-person"><strong>John Goodhue</strong><span>Executive Director, Massachusetts Green High Performance Computing Center</span><em>Talk: Massachusetts Green High Performance Computing Center</em></div>
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
    var grid = document.querySelector(".scai-speakers");
    if (!grid) return;

    var cards = Array.prototype.slice.call(grid.querySelectorAll(".scai-speaker"));
    var disclosures = Array.prototype.slice.call(grid.querySelectorAll(".scai-talk"));
    var reader = grid.querySelector(".scai-speaker-reader");
    if (!cards.length || !disclosures.length || !reader) return;

    var readerKicker = reader.querySelector(".scai-speaker-reader-kicker");
    var readerName = reader.querySelector(".scai-speaker-reader h3");
    var readerRole = reader.querySelector(".scai-speaker-reader-role");
    var readerContent = reader.querySelector(".scai-speaker-reader-content");
    var closeButton = reader.querySelector(".scai-speaker-reader-close");
    var activeDisclosure = null;
    var activeCard = null;
    var resizeTimer = null;

    function getColumnCount() {
      var columns = window.getComputedStyle(grid).gridTemplateColumns;
      return Math.max(1, columns.split(/\s+/).filter(Boolean).length);
    }

    function placeReader(card) {
      var cardIndex = cards.indexOf(card);
      var rowEnd = Math.min(cards.length, Math.ceil((cardIndex + 1) / getColumnCount()) * getColumnCount());
      var nextCard = cards[rowEnd];
      if (nextCard) {
        grid.insertBefore(reader, nextCard);
      } else {
        grid.appendChild(reader);
      }
    }

    function closeReader(restoreFocus) {
      var focusTarget = activeDisclosure ? activeDisclosure.querySelector("summary") : null;
      disclosures.forEach(function (item) {
        item.classList.remove("is-active");
        item.open = false;
        item.querySelector("summary").setAttribute("aria-expanded", "false");
      });
      cards.forEach(function (card) { card.classList.remove("is-reader-active"); });
      reader.hidden = true;
      activeDisclosure = null;
      activeCard = null;
      if (restoreFocus && focusTarget) focusTarget.focus();
    }

    function openReader(disclosure) {
      var card = disclosure.closest(".scai-speaker");
      var summary = disclosure.querySelector("summary");
      var panel = disclosure.querySelector(".scai-talk-panel");
      var name = card.querySelector("h3");
      var role = card.querySelector(".scai-speaker-role");
      var isSameDisclosure = disclosure === activeDisclosure && !reader.hidden;

      if (isSameDisclosure) {
        closeReader(false);
        return;
      }

      closeReader(false);
      readerKicker.textContent = summary.textContent.trim() === "Talk" ? "Talk" : "Biography";
      readerName.textContent = name ? name.textContent.trim() : "Speaker details";
      readerRole.textContent = role ? role.textContent.trim() : "";
      readerContent.innerHTML = panel.innerHTML;
      placeReader(card);
      reader.hidden = false;
      disclosure.classList.add("is-active");
      summary.setAttribute("aria-expanded", "true");
      card.classList.add("is-reader-active");
      activeDisclosure = disclosure;
      activeCard = card;
    }

    disclosures.forEach(function (disclosure) {
      var summary = disclosure.querySelector("summary");
      disclosure.open = false;
      summary.setAttribute("aria-controls", "scai-speaker-reader");
      summary.setAttribute("aria-expanded", "false");
      summary.addEventListener("click", function (event) {
        event.preventDefault();
        openReader(disclosure);
      });
    });

    closeButton.addEventListener("click", function () { closeReader(true); });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && !reader.hidden) closeReader(true);
    });
    window.addEventListener("resize", function () {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(function () {
        if (activeCard && !reader.hidden) placeReader(activeCard);
      }, 120);
    });

    grid.classList.add("is-wide-details");
  }());

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
- Laura Haas: https://www.cics.umass.edu/about/directory/laura-haas
- Ramesh Sitaraman: https://www.cics.umass.edu/about/directory/ramesh-sitaraman
- Golbon Zakeri: https://www.umass.edu/engineering/about/directory/golbon-zakeri
- Deepak Rajagopal: https://www.ioes.ucla.edu/person/deepak-rajagopal/
- Le Xie: https://xielab.seas.harvard.edu/le-xie/
- Yuanrui Sang: https://www.umass.edu/engineering/about/directory/assistant-professor
-->
