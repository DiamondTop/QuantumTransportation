import streamlit as st

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Quantum Transportation LLC | Intermodal & Container Storage – Los Angeles, CA",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Syne:wght@600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

[data-testid="stAppViewContainer"] {
    background: #04111f;
    font-family: 'DM Sans', sans-serif;
    color: #d6e4f0;
}
[data-testid="stHeader"], footer { display: none !important; }
[data-testid="block-container"] {
    padding: 0 !important;
    max-width: 100% !important;
}
section[data-testid="stVerticalBlock"] > div { gap: 0 !important; }

/* ═══════════ NAV ═══════════ */
.qt-nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 56px; height: 74px;
    background: rgba(4,17,31,0.88);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(0,210,190,0.15);
}
.qt-logo {
    display: flex; align-items: center; gap: 10px;
}
.qt-logo-mark {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #00D2BE 0%, #007BFF 100%);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; font-weight: 800; color: #fff;
    font-family: 'Syne', sans-serif; letter-spacing: -0.03em;
}
.qt-logo-text {
    font-family: 'Syne', sans-serif;
    font-size: 1.2rem; font-weight: 700;
    color: #fff; letter-spacing: 0.04em;
}
.qt-logo-text span { color: #00D2BE; }
.qt-nav-links { display: flex; align-items: center; gap: 36px; }
.qt-nav-links a {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.88rem; font-weight: 500; letter-spacing: 0.04em;
    color: #8aa8c0; text-decoration: none; transition: color 0.2s;
}
.qt-nav-links a:hover { color: #00D2BE; }
.qt-nav-cta {
    background: transparent !important;
    border: 1.5px solid #00D2BE !important;
    color: #00D2BE !important;
    padding: 9px 22px; border-radius: 6px;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.88rem !important; font-weight: 600 !important;
    transition: all 0.2s !important;
}
.qt-nav-cta:hover {
    background: #00D2BE !important;
    color: #04111f !important;
}

/* ═══════════ HERO ═══════════ */
.hero-wrap {
    position: relative; width: 100%;
    height: 100vh; min-height: 700px;
    overflow: hidden; display: flex; align-items: center;
}
.hero-bg {
    position: absolute; inset: 0;
    background-image:
        linear-gradient(to bottom, rgba(4,17,31,0.5) 0%, rgba(4,17,31,0.85) 100%),
        linear-gradient(to right, rgba(4,17,31,0.95) 38%, rgba(4,17,31,0.3) 100%),
        url('https://images.unsplash.com/photo-1494412651409-8963ce7935a7?w=1900&q=85&auto=format&fit=crop&crop=center');
    background-size: cover; background-position: center;
}
.hero-glow {
    position: absolute; top: -200px; right: -200px;
    width: 700px; height: 700px;
    background: radial-gradient(circle, rgba(0,210,190,0.07) 0%, transparent 70%);
    pointer-events: none;
}
.hero-glow-2 {
    position: absolute; bottom: -100px; left: 30%;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(0,123,255,0.05) 0%, transparent 70%);
    pointer-events: none;
}
.hero-grid-lines {
    position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(0,210,190,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,210,190,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
}
.hero-content {
    position: relative; z-index: 2;
    padding: 0 80px; margin-top: 74px;
    max-width: 780px;
}
.hero-eyebrow {
    display: inline-flex; align-items: center; gap: 10px;
    margin-bottom: 30px;
}
.hero-eyebrow-dot {
    width: 8px; height: 8px;
    background: #00D2BE; border-radius: 50%;
    box-shadow: 0 0 10px rgba(0,210,190,0.6);
    animation: pulse-dot 2s ease-in-out infinite;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.6; transform: scale(0.8); }
}
.hero-eyebrow-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.78rem; font-weight: 600; letter-spacing: 0.2em;
    text-transform: uppercase; color: #00D2BE;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(3rem, 5.5vw, 5.5rem);
    font-weight: 800; line-height: 1.0; letter-spacing: -0.02em;
    color: #fff; margin-bottom: 26px;
}
.hero-title .teal { color: #00D2BE; }
.hero-title .blue { color: #4da6ff; }
.hero-sub {
    font-size: 1.1rem; font-weight: 400; line-height: 1.75;
    color: #b8cfe0; max-width: 500px; margin-bottom: 44px;
}
.hero-btns { display: flex; gap: 14px; flex-wrap: wrap; }
.btn-teal {
    display: inline-block;
    background: linear-gradient(135deg, #00D2BE, #00a8a0);
    color: #04111f;
    padding: 15px 36px; border-radius: 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.95rem; font-weight: 700; letter-spacing: 0.04em;
    text-decoration: none; transition: all 0.25s;
    box-shadow: 0 8px 32px rgba(0,210,190,0.25);
}
.btn-teal:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(0,210,190,0.35);
    color: #04111f;
}
.btn-ghost {
    display: inline-block;
    border: 1.5px solid rgba(255,255,255,0.2);
    color: #d6e4f0;
    padding: 14px 32px; border-radius: 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.95rem; font-weight: 500;
    text-decoration: none; transition: all 0.25s;
}
.btn-ghost:hover {
    border-color: #00D2BE; color: #00D2BE;
    background: rgba(0,210,190,0.05);
}
.hero-stat-row {
    position: absolute; bottom: 0; left: 0; right: 0;
    display: flex; z-index: 2;
}
.stat-block {
    flex: 1; padding: 32px 40px;
    background: rgba(10,25,45,0.7);
    backdrop-filter: blur(12px);
    border-top: 1px solid rgba(0,210,190,0.12);
    border-right: 1px solid rgba(255,255,255,0.04);
    text-align: left;
}
.stat-block:last-child { border-right: none; }
.stat-n {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem; font-weight: 800; color: #00D2BE;
    line-height: 1; margin-bottom: 4px;
}
.stat-l {
    font-size: 0.78rem; font-weight: 400;
    color: #7a9ab5; letter-spacing: 0.06em;
    text-transform: uppercase;
}

/* ═══════════ TICKER STRIP ═══════════ */
.ticker-wrap {
    background: linear-gradient(90deg, #00D2BE 0%, #007BFF 100%);
    padding: 14px 0; overflow: hidden;
    white-space: nowrap;
}
.ticker-inner {
    display: inline-flex; gap: 0;
    animation: ticker 30s linear infinite;
}
@keyframes ticker {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
}
.ticker-item {
    display: inline-flex; align-items: center; gap: 12px;
    padding: 0 36px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.82rem; font-weight: 600; letter-spacing: 0.12em;
    text-transform: uppercase; color: #04111f;
}
.ticker-sep { opacity: 0.4; }

/* ═══════════ SECTION BASE ═══════════ */
.section { padding: 100px 80px; }
.section-dark { background: #04111f; }
.section-mid { background: #071828; }
.section-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.24em;
    text-transform: uppercase; color: #00D2BE;
    margin-bottom: 12px;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2rem, 3.6vw, 3.2rem);
    font-weight: 700; color: #fff;
    line-height: 1.12; letter-spacing: -0.02em;
    margin-bottom: 18px;
}
.section-sub {
    font-size: 1rem; font-weight: 400; color: #94b4c8;
    line-height: 1.75; max-width: 520px;
}

/* ═══════════ SERVICES ═══════════ */
.services-header {
    display: flex; align-items: flex-end;
    justify-content: space-between; margin-bottom: 56px;
}
.services-flex {
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    grid-template-rows: auto auto auto;
    gap: 16px;
}
.svc-card {
    position: relative; border-radius: 12px; overflow: hidden;
    cursor: default;
}
.svc-card.featured {
    grid-row: 1 / 4;
}
.svc-card img {
    width: 100%; height: 100%; min-height: 220px;
    object-fit: cover;
    transition: transform 0.6s ease;
    display: block;
}
.svc-card.featured img { min-height: 680px; }
.svc-card:hover img { transform: scale(1.05); }
.svc-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(to top, rgba(4,17,31,0.97) 30%, rgba(4,17,31,0.15) 100%);
    padding: 28px 26px;
    display: flex; flex-direction: column; justify-content: flex-end;
    transition: background 0.3s;
}
.svc-card:hover .svc-overlay {
    background: linear-gradient(to top, rgba(4,17,31,1) 45%, rgba(4,17,31,0.4) 100%);
}
.svc-tag {
    display: inline-block;
    background: rgba(0,210,190,0.15);
    border: 1px solid rgba(0,210,190,0.3);
    color: #00D2BE;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.68rem; font-weight: 600; letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 4px 10px; border-radius: 4px;
    margin-bottom: 10px; align-self: flex-start;
}
.svc-name {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem; font-weight: 700; color: #fff;
    margin-bottom: 8px; letter-spacing: -0.01em;
}
.svc-card.featured .svc-name { font-size: 1.9rem; }
.svc-desc {
    font-size: 0.86rem; font-weight: 400; color: #c8dce8;
    line-height: 1.6;
    max-height: 0; overflow: hidden; opacity: 0;
    transition: max-height 0.4s ease, opacity 0.4s ease;
}
.svc-card:hover .svc-desc { max-height: 100px; opacity: 1; }
.svc-arrow {
    color: #00D2BE; font-size: 1.1rem;
    margin-top: 12px; opacity: 0.3;
    transition: opacity 0.3s, transform 0.3s;
}
.svc-card:hover .svc-arrow { opacity: 1; transform: translateX(4px); }

/* ═══════════ RATES HIGHLIGHT ═══════════ */
.rates-banner {
    margin: 0 80px 0;
    background: linear-gradient(135deg, #071828 0%, #0a2038 100%);
    border: 1px solid rgba(0,210,190,0.15);
    border-radius: 16px;
    padding: 56px 64px;
    display: flex; align-items: center;
    gap: 60px;
    position: relative; overflow: hidden;
}
.rates-banner::before {
    content: '';
    position: absolute; top: -80px; right: -80px;
    width: 320px; height: 320px;
    background: radial-gradient(circle, rgba(0,210,190,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.rates-text { flex: 1; }
.rates-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.22em;
    text-transform: uppercase; color: #00D2BE;
    margin-bottom: 10px;
}
.rates-heading {
    font-family: 'Syne', sans-serif;
    font-size: 2rem; font-weight: 800; color: #fff;
    letter-spacing: -0.02em; margin-bottom: 12px;
}
.rates-body {
    font-size: 0.95rem; font-weight: 400; color: #a0bfd4;
    line-height: 1.7; max-width: 500px;
}
.rates-badges {
    display: flex; flex-direction: column; gap: 14px; flex-shrink: 0;
}
.rate-badge {
    display: flex; align-items: center; gap: 12px;
    background: rgba(0,210,190,0.06);
    border: 1px solid rgba(0,210,190,0.15);
    padding: 12px 20px; border-radius: 8px;
    white-space: nowrap;
}
.rate-badge-icon { color: #00D2BE; font-size: 1rem; }
.rate-badge-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.85rem; font-weight: 500; color: #c0d8e8;
}

/* ═══════════ ABOUT ═══════════ */
.about-wrap {
    display: grid; grid-template-columns: 1fr 1fr; gap: 0;
}
.about-visual {
    position: relative; overflow: hidden;
    min-height: 560px;
}
.about-visual img {
    width: 100%; height: 100%; object-fit: cover;
}
.about-visual-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(to right, transparent 60%, #071828 100%);
}
.about-visual-card {
    position: absolute; bottom: 48px; left: 40px;
    background: rgba(4,17,31,0.9);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(0,210,190,0.2);
    border-radius: 12px; padding: 24px 28px;
    max-width: 260px;
}
.avc-num {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem; font-weight: 800; color: #00D2BE;
    line-height: 1; letter-spacing: -0.03em;
}
.avc-label {
    font-size: 0.82rem; font-weight: 400; color: #8aaec4;
    margin-top: 4px; line-height: 1.4;
}
.about-copy {
    background: #071828; padding: 80px 64px;
    display: flex; flex-direction: column; justify-content: center;
}
.about-copy p {
    font-size: 0.97rem; font-weight: 400; color: #a0bfd4;
    line-height: 1.8; margin-bottom: 18px;
}
.about-pills {
    display: flex; flex-wrap: wrap; gap: 10px; margin-top: 28px;
}
.pill {
    display: inline-flex; align-items: center; gap: 7px;
    background: rgba(0,210,190,0.06);
    border: 1px solid rgba(0,210,190,0.18);
    padding: 8px 16px; border-radius: 999px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.82rem; font-weight: 500; color: #9dcce0;
}
.pill-dot { width: 6px; height: 6px; background: #00D2BE; border-radius: 50%; }

/* ═══════════ PORTS SECTION ═══════════ */
.ports-section {
    padding: 100px 80px;
    background: #04111f;
}
.ports-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px; margin-top: 56px;
}
.port-card {
    position: relative; border-radius: 12px; overflow: hidden;
    border: 1px solid rgba(255,255,255,0.05);
    transition: all 0.3s;
}
.port-card:hover {
    border-color: rgba(0,210,190,0.25);
    transform: translateY(-4px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
}
.port-card-img { height: 200px; overflow: hidden; }
.port-card-img img {
    width: 100%; height: 100%; object-fit: cover;
    transition: transform 0.5s ease;
}
.port-card:hover .port-card-img img { transform: scale(1.06); }
.port-card-body {
    background: #0a1e30; padding: 24px 26px;
}
.port-badge {
    display: inline-block;
    background: rgba(0,210,190,0.1);
    color: #00D2BE;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.65rem; font-weight: 600; letter-spacing: 0.14em;
    text-transform: uppercase; padding: 3px 9px; border-radius: 4px;
    margin-bottom: 10px;
}
.port-name {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem; font-weight: 700; color: #fff;
    margin-bottom: 6px;
}
.port-detail {
    font-size: 0.84rem; font-weight: 400; color: #7a9ab5;
    line-height: 1.5;
}

/* ═══════════ STORAGE FEATURE ═══════════ */
.storage-section {
    display: grid; grid-template-columns: 1fr 1fr; gap: 0;
    background: #071828;
}
.storage-copy {
    padding: 100px 72px;
    display: flex; flex-direction: column; justify-content: center;
}
.storage-copy p {
    font-size: 0.97rem; font-weight: 400; color: #a0bfd4;
    line-height: 1.8; margin-bottom: 18px;
}
.storage-features {
    display: flex; flex-direction: column; gap: 16px;
    margin: 32px 0;
}
.sf-row {
    display: flex; align-items: flex-start; gap: 16px;
    padding: 18px 20px;
    background: rgba(0,210,190,0.03);
    border: 1px solid rgba(0,210,190,0.08);
    border-radius: 8px;
    transition: all 0.25s;
}
.sf-row:hover {
    background: rgba(0,210,190,0.07);
    border-color: rgba(0,210,190,0.2);
}
.sf-icon {
    width: 52px; height: 52px; min-width: 52px;
    border-radius: 6px; overflow: hidden; margin-top: 2px; flex-shrink: 0;
}
.sf-icon img {
    width: 100%; height: 100%; object-fit: cover;
}
.sf-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.92rem; font-weight: 600; color: #c0d8e8;
    margin-bottom: 3px;
}
.sf-detail {
    font-size: 0.82rem; font-weight: 400; color: #7a9ab5; line-height: 1.5;
}
.storage-visual {
    position: relative; overflow: hidden;
}
.storage-visual img {
    width: 100%; height: 100%; object-fit: cover;
    filter: brightness(0.6) saturate(0.8);
}
.storage-visual::after {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(to right, #071828 0%, transparent 30%);
}
.storage-stat-overlay {
    position: absolute; top: 50%; right: 48px;
    transform: translateY(-50%);
    z-index: 2;
    display: flex; flex-direction: column; gap: 16px;
}
.sso-card {
    background: rgba(4,17,31,0.85);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(0,210,190,0.2);
    border-radius: 10px; padding: 20px 26px;
    text-align: center; min-width: 150px;
}
.sso-n {
    font-family: 'Syne', sans-serif;
    font-size: 2rem; font-weight: 800;
    color: #00D2BE; line-height: 1;
}
.sso-l {
    font-size: 0.75rem; font-weight: 400;
    color: #7a9ab5; margin-top: 4px;
    text-transform: uppercase; letter-spacing: 0.1em;
}

/* ═══════════ WHY QUANTUM ═══════════ */
.why-section { padding: 100px 80px; background: #04111f; }
.why-grid {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 20px; margin-top: 56px;
}
.wq-card {
    background: #071828;
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 12px; padding: 36px 32px;
    position: relative; overflow: hidden;
    transition: all 0.3s;
}
.wq-card:hover {
    border-color: rgba(0,210,190,0.2);
    transform: translateY(-4px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}
.wq-card::after {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #00D2BE, #007BFF);
    transform: scaleX(0); transform-origin: left;
    transition: transform 0.35s ease;
    border-radius: 2px 2px 0 0;
}
.wq-card:hover::after { transform: scaleX(1); }
.wq-num {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem; font-weight: 700; letter-spacing: 0.2em;
    color: #00D2BE; margin-bottom: 18px;
    display: flex; align-items: center; gap: 12px;
}
.wq-num::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(90deg, rgba(0,210,190,0.3), transparent);
}
.wq-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem; font-weight: 700; color: #fff;
    margin-bottom: 12px; letter-spacing: -0.01em;
}
.wq-body {
    font-size: 0.88rem; font-weight: 400; color: #7a9ab5; line-height: 1.75;
}

/* ═══════════ CONTACT ═══════════ */
.contact-wrap {
    display: grid; grid-template-columns: 1fr 1.2fr; gap: 0;
}
.contact-left {
    background: #071828; padding: 100px 64px;
    display: flex; flex-direction: column; justify-content: center;
}
.contact-right {
    background: #04111f; padding: 100px 80px;
}
.contact-item {
    display: flex; gap: 18px; align-items: flex-start;
    margin-bottom: 32px; padding-bottom: 32px;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.contact-item:last-of-type { border-bottom: none; }
.contact-icon {
    width: 46px; height: 46px; min-width: 46px;
    background: rgba(0,210,190,0.08);
    border: 1px solid rgba(0,210,190,0.2);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
}
.contact-lbl {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.7rem; font-weight: 600; letter-spacing: 0.18em;
    text-transform: uppercase; color: #00D2BE; margin-bottom: 4px;
}
.contact-val {
    font-size: 0.95rem; font-weight: 400; color: #b0cce0; line-height: 1.5;
}
.contact-val a { color: #b0cce0; text-decoration: none; }
.contact-val a:hover { color: #00D2BE; }
.form-label {
    display: block;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.16em;
    text-transform: uppercase; color: #7a9ab5;
    margin-bottom: 8px;
}
.form-group { margin-bottom: 18px; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.form-input, .form-select, .form-textarea {
    width: 100%;
    background: #071828;
    border: 1px solid rgba(0,210,190,0.1);
    border-radius: 8px; padding: 12px 16px;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.93rem; color: #c0d8e8;
    outline: none; transition: border-color 0.2s, box-shadow 0.2s;
    -webkit-appearance: none;
}
.form-input:focus, .form-select:focus, .form-textarea:focus {
    border-color: rgba(0,210,190,0.45);
    box-shadow: 0 0 0 3px rgba(0,210,190,0.06);
}
.form-textarea { resize: vertical; min-height: 110px; }
.submit-btn {
    width: 100%;
    background: linear-gradient(135deg, #00D2BE 0%, #007BFF 100%);
    color: #04111f; border: none;
    padding: 16px 32px; border-radius: 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.95rem; font-weight: 700; letter-spacing: 0.04em;
    cursor: pointer; transition: all 0.25s;
    box-shadow: 0 8px 28px rgba(0,210,190,0.2);
}
.submit-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 40px rgba(0,210,190,0.3);
}

/* ═══════════ FOOTER ═══════════ */
.qt-footer {
    background: #020c17;
    padding: 64px 80px 32px;
    border-top: 1px solid rgba(0,210,190,0.1);
}
.footer-grid {
    display: grid; grid-template-columns: 1.6fr 1fr 1fr;
    gap: 60px; margin-bottom: 48px;
}
.footer-logo-wrap .qt-logo-text { font-size: 1.3rem; margin-bottom: 16px; }
.footer-tagline {
    font-size: 0.88rem; font-weight: 400; color: #4a6a84;
    line-height: 1.75; max-width: 300px;
}
.footer-head {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.7rem; font-weight: 600; letter-spacing: 0.2em;
    text-transform: uppercase; color: #00D2BE; margin-bottom: 20px;
}
.footer-links { list-style: none; display: flex; flex-direction: column; gap: 10px; }
.footer-links li a {
    font-size: 0.88rem; color: #4a6a84; text-decoration: none;
    transition: color 0.2s;
}
.footer-links li a:hover { color: #00D2BE; }
.footer-bottom {
    border-top: 1px solid rgba(255,255,255,0.04);
    padding-top: 24px;
    display: flex; align-items: center; justify-content: space-between;
}
.footer-copy { font-size: 0.78rem; color: #3a5570; }
.footer-sep { color: #00D2BE; margin: 0 8px; }
.gradient-line {
    width: 100%; height: 2px;
    background: linear-gradient(90deg, transparent, #00D2BE 30%, #007BFF 70%, transparent);
    margin-bottom: 32px; opacity: 0.4;
}
</style>
""", unsafe_allow_html=True)


# ── NAVIGATION ────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="qt-nav">
  <div class="qt-logo">
    <div class="qt-logo-mark">Q</div>
    <div class="qt-logo-text">Quantum <span>Transportation</span></div>
  </div>
  <div class="qt-nav-links">
    <a href="#services">Services</a>
    <a href="#storage">Container Storage</a>
    <a href="#ports">Coverage</a>
    <a href="#about">About</a>
    <a href="#contact">Contact</a>
    <a href="#contact" class="qt-nav-cta">Get a Quote</a>
  </div>
</nav>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap" id="home">
  <div class="hero-bg"></div>
  <div class="hero-glow"></div>
  <div class="hero-glow-2"></div>
  <div class="hero-grid-lines"></div>
  <div class="hero-content">
    <div class="hero-eyebrow">
      <div class="hero-eyebrow-dot"></div>
      <div class="hero-eyebrow-text">Los Angeles &amp; Long Beach Port Specialist</div>
    </div>
    <h1 class="hero-title">
      West Coast<br>Logistics,<br><span class="teal">Redefined.</span>
    </h1>
    <p class="hero-sub">
      Quantum Transportation LLC delivers competitive rates, dependable intermodal drayage, 
      and flexible container storage solutions across the Southern California supply chain.
    </p>
    <div class="hero-btns">
      <a href="#contact" class="btn-teal">Request a Rate</a>
      <a href="#services" class="btn-ghost">Explore Services</a>
    </div>
  </div>
  <div class="hero-stat-row">
    <div class="stat-block">
      <div class="stat-n">Best</div>
      <div class="stat-l">Market Rates — Guaranteed</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">24/7</div>
      <div class="stat-l">Dispatch & Operations</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">2</div>
      <div class="stat-l">Mega-Port Terminals Covered</div>
    </div>
    <div class="stat-block">
      <div class="stat-n">100%</div>
      <div class="stat-l">On-Time Commitment</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── TICKER ────────────────────────────────────────────────────────────────────
ticker_items = [
    "Port of Los Angeles", "Port of Long Beach", "Intermodal Drayage",
    "Container Storage", "Competitive Rates", "Reliable Service",
    "TWIC Compliant", "Bonded & Insured",
    "Same-Day Dispatch", "24/7 Operations", "Southern California",
]
items_html = "".join([
    f'<div class="ticker-item">◈ &nbsp;{item}</div>' for item in ticker_items * 2
])
st.markdown(f"""
<div class="ticker-wrap">
  <div class="ticker-inner">{items_html}</div>
</div>
""", unsafe_allow_html=True)


# ── SERVICES ─────────────────────────────────────────────────────────────────
st.markdown('<div id="services"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-dark">
  <div class="services-header">
    <div>
      <div class="section-label">What We Do</div>
      <div class="section-title">End-to-End Freight Solutions</div>
    </div>
    <p class="section-sub" style="max-width:360px; text-align:right;">
      From the port gate to your warehouse door — every mile handled with precision and care.
    </p>
  </div>
  <div class="services-flex">
    <div class="svc-card featured">
      <img src="https://images.unsplash.com/photo-1605745341112-85968b19335b?w=900&q=85&auto=format&fit=crop" alt="Port Drayage LA" />
      <div class="svc-overlay">
        <div class="svc-tag">Flagship Service</div>
        <div class="svc-name">Port Drayage</div>
        <div class="svc-desc">Direct container pickup and delivery at the Port of Los Angeles and Port of Long Beach — the two largest container ports in North America. We hold terminal appointments and move your freight fast.</div>
        <div class="svc-arrow">→</div>
      </div>
    </div>
    <div class="svc-card">
      <img src="https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=800&q=80&auto=format&fit=crop" alt="Container Transport" />
      <div class="svc-overlay">
        <div class="svc-tag">Core Service</div>
        <div class="svc-name">Container Transport</div>
        <div class="svc-desc">All ISO container types — standard, high cube, reefer, and flat rack — moved efficiently across Southern California.</div>
        <div class="svc-arrow">→</div>
      </div>
    </div>
    <div class="svc-card">
      <img src="https://images.unsplash.com/photo-1553413077-190dd305871c?w=800&q=80&auto=format&fit=crop" alt="Container Storage" />
      <div class="svc-overlay">
        <div class="svc-tag">Unique Offering</div>
        <div class="svc-name">Container Storage</div>
        <div class="svc-desc">Secure, flexible container storage near LA/LB ports. Short-term and long-term options available.</div>
        <div class="svc-arrow">→</div>
      </div>
    </div>
    <div class="svc-card">
      <img src="https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?w=800&q=80&auto=format&fit=crop" alt="Expedited" />
      <div class="svc-overlay">
        <div class="svc-tag">Rush Service</div>
        <div class="svc-name">Expedited Moves</div>
        <div class="svc-desc">Time-critical freight handled by dedicated drivers. Hot-shot and same-day delivery available.</div>
        <div class="svc-arrow">→</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── RATES BANNER ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 0 0 80px 0; background: #04111f;">
  <div class="rates-banner">
    <div class="rates-text">
      <div class="rates-label">Our Promise</div>
      <div class="rates-heading">Competitive Rates. No Hidden Fees.</div>
      <p class="rates-body">
        At Quantum, we built our reputation on offering the most competitive drayage and storage rates in the 
        Southern California market — without cutting corners on service. Every quote is transparent, 
        itemized, and honored.
      </p>
    </div>
    <div class="rates-badges">
      <div class="rate-badge">
        <div class="rate-badge-icon">✓</div>
        <div class="rate-badge-text">All-In Pricing</div>
      </div>
      <div class="rate-badge">
        <div class="rate-badge-icon">✓</div>
        <div class="rate-badge-text">No Fuel Surcharge Games</div>
      </div>
      <div class="rate-badge">
        <div class="rate-badge-icon">✓</div>
        <div class="rate-badge-text">Instant Rate Quotes</div>
      </div>
      <div class="rate-badge">
        <div class="rate-badge-icon">✓</div>
        <div class="rate-badge-text">Volume Discounts Available</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── CONTAINER STORAGE ─────────────────────────────────────────────────────────
st.markdown('<div id="storage"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="storage-section">
  <div class="storage-copy">
    <div class="section-label">Container Storage</div>
    <div class="section-title">Secure Storage Near the Port</div>
    <p>
      Need to hold your containers before final delivery? Quantum Transportation offers 
      flexible, secure container storage solutions at our Southern California facility — 
      conveniently located minutes from the ports of LA and Long Beach.
    </p>
    <p>
      Whether you need a few days of overflow storage or a long-term yard solution, 
      we have the capacity and the team to manage your equipment safely.
    </p>
    <div class="storage-features">
      <div class="sf-row">
        <div class="sf-icon"><img src="https://images.unsplash.com/photo-1566576721346-d4a3b4eaeb55?w=120&q=80&auto=format&fit=crop" alt="Secure Facility" /></div>
        <div>
          <div class="sf-title">Secure, Fenced Facility</div>
          <div class="sf-detail">24/7 monitored yard with gated access and on-site personnel</div>
        </div>
      </div>
      <div class="sf-row">
        <div class="sf-icon"><img src="https://images.unsplash.com/photo-1605745341112-85968b19335b?w=120&q=80&auto=format&fit=crop&crop=right" alt="Container Types" /></div>
        <div>
          <div class="sf-title">All Container Types</div>
          <div class="sf-detail">Standard, high cube, reefer (with power), flat rack, and tank containers</div>
        </div>
      </div>
      <div class="sf-row">
        <div class="sf-icon"><img src="https://images.unsplash.com/photo-1565688534245-05d6b5be184a?w=120&q=80&auto=format&fit=crop" alt="Flexible Terms" /></div>
        <div>
          <div class="sf-title">Flexible Terms</div>
          <div class="sf-detail">Daily, weekly, and monthly storage options — no long-term commitment required</div>
        </div>
      </div>
      <div class="sf-row">
        <div class="sf-icon"><img src="https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?w=120&q=80&auto=format&fit=crop" alt="Drayage Integration" /></div>
        <div>
          <div class="sf-title">Seamless Drayage Integration</div>
          <div class="sf-detail">Store and dispatch from the same yard — zero re-handling costs</div>
        </div>
      </div>
    </div>
    <a href="#contact" class="btn-teal" style="display:inline-block; align-self:flex-start;">Inquire About Storage</a>
  </div>
  <div class="storage-visual">
    <img src="https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=900&q=85&auto=format&fit=crop" alt="Container storage yard" />
    <div class="storage-stat-overlay">
      <div class="sso-card">
        <div class="sso-n">Port</div>
        <div class="sso-l">Proximity Location</div>
      </div>
      <div class="sso-card">
        <div class="sso-n">All</div>
        <div class="sso-l">Container Types</div>
      </div>
      <div class="sso-card">
        <div class="sso-n">24/7</div>
        <div class="sso-l">Yard Monitoring</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── PORTS ─────────────────────────────────────────────────────────────────────
st.markdown('<div id="ports"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="ports-section">
  <div class="section-label">Service Coverage</div>
  <div class="section-title">California's Busiest Port Gateways</div>
  <p class="section-sub">We operate daily at the terminals that move the most containers on the Pacific Coast.</p>
  <div class="ports-grid">
    <div class="port-card">
      <div class="port-card-img">
        <img src="https://images.unsplash.com/photo-1494412651409-8963ce7935a7?w=800&q=85&auto=format&fit=crop&crop=top" alt="Port of Los Angeles" />
      </div>
      <div class="port-card-body">
        <div class="port-badge">Terminal Access</div>
        <div class="port-name">Port of Los Angeles</div>
        <div class="port-detail">San Pedro, CA · APM, Yusen, TraPac, China Shipping, West Basin terminals</div>
      </div>
    </div>
    <div class="port-card">
      <div class="port-card-img">
        <img src="https://images.unsplash.com/photo-1565688534245-05d6b5be184a?w=800&q=80&auto=format&fit=crop" alt="Port of Long Beach" />
      </div>
      <div class="port-card-body">
        <div class="port-badge">Terminal Access</div>
        <div class="port-name">Port of Long Beach</div>
        <div class="port-detail">Long Beach, CA · Pier T, G, F, J, A — all major container terminals</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── ABOUT ─────────────────────────────────────────────────────────────────────
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="about-wrap">
  <div class="about-visual">
    <img src="https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=900&q=85&auto=format&fit=crop&crop=center" alt="Semi truck on highway" />
    <div class="about-visual-overlay"></div>
    <div class="about-visual-card">
      <div class="avc-num">#1</div>
      <div class="avc-label">Priority: Your cargo moves on time, every time</div>
    </div>
  </div>
  <div class="about-copy">
    <div class="section-label">About Quantum</div>
    <div class="section-title">Built on Reliability. Driven by Value.</div>
    <p>
      Quantum Transportation LLC is a Los Angeles–based intermodal trucking company 
      built from the ground up on two principles: unbeatable rates and dependable execution. 
      We service the two largest container ports in the United States daily.
    </p>
    <p>
      Our lean owner-operator model means we eliminate the middlemen and pass the cost 
      savings directly to our customers. From freight brokers to direct importers and exporters, 
      Quantum has become the reliable, go-to drayage partner in the SoCal market.
    </p>
    <div class="about-pills">
      <div class="pill"><div class="pill-dot"></div> TWIC Credentialed</div>
      <div class="pill"><div class="pill-dot"></div> DOT Licensed</div>
      <div class="pill"><div class="pill-dot"></div> Fully Insured</div>
      <div class="pill"><div class="pill-dot"></div> Hazmat Ready</div>
      <div class="pill"><div class="pill-dot"></div> Owner-Operated</div>
      <div class="pill"><div class="pill-dot"></div> LA / LB Native</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── WHY QUANTUM ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="why-section">
  <div class="section-label">Why Choose Us</div>
  <div class="section-title">The Quantum Advantage</div>
  <div class="why-grid">
    <div class="wq-card">
      <div class="wq-num">01 ─ RATES</div>
      <div class="wq-title">Market-Best Rates</div>
      <div class="wq-body">Our lean structure means we consistently undercut the market without sacrificing service quality. Get more for your freight budget.</div>
    </div>
    <div class="wq-card">
      <div class="wq-num">02 ─ DELIVERY</div>
      <div class="wq-title">On-Time, Every Time</div>
      <div class="wq-body">We built our reputation one delivery at a time. Our on-time record speaks for itself — and we hold our drivers to it every day.</div>
    </div>
    <div class="wq-card">
      <div class="wq-num">03 ─ TRACKING</div>
      <div class="wq-title">Real-Time Visibility</div>
      <div class="wq-body">Track your container from port pickup to final delivery. You'll never wonder where your freight is again.</div>
    </div>
    <div class="wq-card">
      <div class="wq-num">04 ─ STORAGE</div>
      <div class="wq-title">Storage + Drayage</div>
      <div class="wq-body">The only Southern California carrier offering integrated port storage and drayage under one roof — no coordination headaches.</div>
    </div>
    <div class="wq-card">
      <div class="wq-num">05 ─ PARTNERSHIP</div>
      <div class="wq-title">Relationship-First</div>
      <div class="wq-body">We're not a load board. We build long-term partnerships and learn your freight patterns to serve you better every month.</div>
    </div>
    <div class="wq-card">
      <div class="wq-num">06 ─ QUOTING</div>
      <div class="wq-title">Fast Quote Response</div>
      <div class="wq-body">Submit a request and get a competitive, fully-itemized rate within the hour. We know your time is money.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── CONTACT ──────────────────────────────────────────────────────────────────
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-wrap">
  <div class="contact-left">
    <div class="section-label">Get In Touch</div>
    <div class="section-title" style="margin-bottom: 44px;">Ready to Move Smarter?</div>
    <div class="contact-item">
      <div class="contact-icon" style="font-size:0.75rem;font-weight:700;font-family:'Space Grotesk',sans-serif;color:#00D2BE;letter-spacing:0.04em;">LOC</div>
      <div>
        <div class="contact-lbl">Location</div>
        <div class="contact-val">Los Angeles, CA<br><span style="color:#2d4460; font-size:0.85rem;">Serving LA / Long Beach Port Complex</span></div>
      </div>
    </div>
    <div class="contact-item">
      <div class="contact-icon" style="font-size:0.75rem;font-weight:700;font-family:'Space Grotesk',sans-serif;color:#00D2BE;letter-spacing:0.04em;">TEL</div>
      <div>
        <div class="contact-lbl">Phone</div>
        <div class="contact-val"><a href="#">Contact via form for direct line</a></div>
      </div>
    </div>
    <div class="contact-item">
      <div class="contact-icon" style="font-size:0.75rem;font-weight:700;font-family:'Space Grotesk',sans-serif;color:#00D2BE;letter-spacing:0.04em;">24H</div>
      <div>
        <div class="contact-lbl">Hours</div>
        <div class="contact-val">24 / 7 Dispatch — 365 Days</div>
      </div>
    </div>
    <div class="contact-item">
      <div class="contact-icon" style="font-size:0.75rem;font-weight:700;font-family:'Space Grotesk',sans-serif;color:#00D2BE;letter-spacing:0.04em;">ETA</div>
      <div>
        <div class="contact-lbl">Quote Response Time</div>
        <div class="contact-val">Within 1 hour during business hours</div>
      </div>
    </div>
    <div style="margin-top: 40px; padding: 24px; background: rgba(0,210,190,0.05); border: 1px solid rgba(0,210,190,0.15); border-radius: 10px;">
      <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700; color:#fff; margin-bottom:8px;">Storage Inquiries</div>
      <div style="font-size:0.88rem; font-weight:400; color:#94b8cc; line-height:1.7;">Mention container storage in your message and our team will provide availability and rate information same day.</div>
    </div>
  </div>
  <div class="contact-right">
    <div class="section-label">Request a Rate</div>
    <div class="section-title" style="margin-bottom:36px;">Tell Us About Your Freight</div>
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">First Name</label>
        <input type="text" class="form-input" placeholder="Jane" />
      </div>
      <div class="form-group">
        <label class="form-label">Last Name</label>
        <input type="text" class="form-input" placeholder="Chen" />
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Company</label>
        <input type="text" class="form-input" placeholder="Your Company Name" />
      </div>
      <div class="form-group">
        <label class="form-label">Phone</label>
        <input type="text" class="form-input" placeholder="(310) 000-0000" />
      </div>
    </div>
    <div class="form-group">
      <label class="form-label">Email Address</label>
      <input type="email" class="form-input" placeholder="you@company.com" />
    </div>
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Service Needed</label>
        <select class="form-select">
          <option>Port Drayage – LA</option>
          <option>Port Drayage – Long Beach</option>
          <option>Container Storage</option>
          <option>Expedited / Hot-Shot</option>
          <option>Storage + Drayage Combo</option>
          <option>Other</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Container Type</label>
        <select class="form-select">
          <option>20' Standard (Dry)</option>
          <option>40' Standard (Dry)</option>
          <option>40' High Cube</option>
          <option>45' High Cube</option>
          <option>Reefer / Refrigerated</option>
          <option>Flat Rack</option>
          <option>Tank Container</option>
        </select>
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Origin Terminal / Ramp</label>
        <input type="text" class="form-input" placeholder="e.g. APM LA, Pier T LB" />
      </div>
      <div class="form-group">
        <label class="form-label">Delivery ZIP / City</label>
        <input type="text" class="form-input" placeholder="e.g. City of Industry, CA" />
      </div>
    </div>
    <div class="form-group">
      <label class="form-label">Additional Details</label>
      <textarea class="form-textarea" placeholder="Pickup date, container weight, overweight status, storage duration, any special requirements…"></textarea>
    </div>
    <button class="submit-btn">Submit Rate Request →</button>
  </div>
</div>
""", unsafe_allow_html=True)


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<footer class="qt-footer">
  <div class="gradient-line"></div>
  <div class="footer-grid">
    <div class="footer-logo-wrap">
      <div class="qt-logo" style="margin-bottom:16px;">
        <div class="qt-logo-mark">Q</div>
        <div class="qt-logo-text">Quantum <span>Transportation</span></div>
      </div>
      <p class="footer-tagline">
        Intermodal drayage, container storage, and port logistics serving the 
        Port of Los Angeles and Port of Long Beach — competitive rates, reliable execution.
      </p>
    </div>
    <div>
      <div class="footer-head">Services</div>
      <ul class="footer-links">
        <li><a href="#">Port Drayage – LA/LB</a></li>
        <li><a href="#">Container Transport</a></li>
        <li><a href="#">Container Storage</a></li>
        <li><a href="#">Expedited Delivery</a></li>
        <li><a href="#">Storage + Drayage Combo</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-head">Company</div>
      <ul class="footer-links">
        <li><a href="#">About Quantum</a></li>
        <li><a href="#">Why Choose Us</a></li>
        <li><a href="#">Port Coverage</a></li>
        <li><a href="#">Request a Rate</a></li>
        <li><a href="#">Contact Us</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-copy">
      © 2025 Quantum Transportation LLC
      <span class="footer-sep">·</span>Los Angeles, CA
      <span class="footer-sep">·</span>All rights reserved
    </div>
    <div class="footer-copy">
      DOT Licensed <span class="footer-sep">·</span> TWIC Compliant <span class="footer-sep">·</span> Fully Insured
    </div>
  </div>
</footer>
""", unsafe_allow_html=True)
