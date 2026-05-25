import streamlit as st

st.set_page_config(
    page_title="Anand Sant | AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #050914;
    color: #e8eaf6;
    font-family: 'Space Grotesk', sans-serif;
    scroll-behavior: smooth;
}

/* hide Streamlit chrome */
#MainMenu, footer, header, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stAppViewContainer"] > .main { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }

/* ── Noise overlay ── */
body::before {
    content: '';
    position: fixed; inset: 0; z-index: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
}

/* ── Ambient blobs ── */
.blob-container {
    position: fixed; inset: 0; z-index: 0; overflow: hidden; pointer-events: none;
}
.blob {
    position: absolute; border-radius: 50%; filter: blur(120px); opacity: 0.18; animation: drift 20s ease-in-out infinite alternate;
}
.blob-1 { width: 600px; height: 600px; background: #5c6bc0; top: -200px; left: -100px; animation-duration: 25s; }
.blob-2 { width: 500px; height: 500px; background: #0097a7; top: 40%; right: -150px; animation-duration: 18s; animation-delay: -8s; }
.blob-3 { width: 400px; height: 400px; background: #7c4dff; bottom: -100px; left: 30%; animation-duration: 22s; animation-delay: -4s; }
@keyframes drift { 0% { transform: translate(0,0) scale(1); } 100% { transform: translate(40px, 30px) scale(1.05); } }

/* ── Page wrapper ── */
.page { position: relative; z-index: 1; }

/* ── HERO ── */
.hero {
    min-height: 100vh;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    text-align: center; padding: 60px 24px;
    position: relative;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(92,107,192,0.15); border: 1px solid rgba(92,107,192,0.4);
    border-radius: 999px; padding: 6px 18px; margin-bottom: 32px;
    font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #9fa8da;
    letter-spacing: 0.05em; backdrop-filter: blur(8px);
    animation: fadeUp 0.8s ease both;
}
.hero-badge::before { content: ''; width: 8px; height: 8px; background: #5c6bc0; border-radius: 50%; animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%,100% { opacity: 1; box-shadow: 0 0 0 0 rgba(92,107,192,0.6); } 50% { opacity: 0.7; box-shadow: 0 0 0 8px rgba(92,107,192,0); } }

.hero-name {
    font-family: 'Syne', sans-serif; font-size: clamp(56px, 9vw, 120px); font-weight: 800;
    line-height: 0.9; letter-spacing: -0.03em;
    background: linear-gradient(135deg, #ffffff 0%, #9fa8da 40%, #5c6bc0 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    margin-bottom: 24px; animation: fadeUp 0.8s 0.2s ease both;
}
.hero-title {
    font-size: clamp(18px, 3vw, 28px); font-weight: 400; color: #90a4ae;
    letter-spacing: 0.02em; margin-bottom: 40px;
    animation: fadeUp 0.8s 0.4s ease both;
}
.hero-title span { color: #80cbc4; font-weight: 600; }

.hero-meta {
    display: flex; flex-wrap: wrap; gap: 16px; justify-content: center;
    margin-bottom: 48px; animation: fadeUp 0.8s 0.6s ease both;
}
.meta-chip {
    display: flex; align-items: center; gap: 8px;
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px; padding: 8px 16px; font-size: 14px; color: #b0bec5;
    backdrop-filter: blur(6px);
}
.meta-chip svg { width:16px; height:16px; opacity: 0.7; }

.hero-cta {
    display: flex; gap: 16px; flex-wrap: wrap; justify-content: center;
    animation: fadeUp 0.8s 0.8s ease both;
}
.cta-primary, .cta-secondary {
    padding: 14px 32px; border-radius: 10px; font-size: 15px; font-weight: 600;
    cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;
    transition: all 0.25s ease; font-family: 'Space Grotesk', sans-serif;
}
.cta-primary {
    background: linear-gradient(135deg, #5c6bc0, #7c4dff);
    color: #fff; border: none;
    box-shadow: 0 4px 24px rgba(92,107,192,0.4);
}
.cta-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(92,107,192,0.6); }
.cta-secondary {
    background: transparent; color: #9fa8da;
    border: 1px solid rgba(92,107,192,0.4);
}
.cta-secondary:hover { background: rgba(92,107,192,0.1); transform: translateY(-2px); }

.scroll-hint {
    position: absolute; bottom: 36px; left: 50%; transform: translateX(-50%);
    display: flex; flex-direction: column; align-items: center; gap: 8px;
    color: #546e7a; font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase;
    animation: fadeUp 1s 1.2s ease both;
}
.scroll-hint::after {
    content: ''; width: 1px; height: 40px;
    background: linear-gradient(to bottom, #5c6bc0, transparent);
    animation: scrollLine 1.5s ease-in-out infinite;
}
@keyframes scrollLine { 0%,100% { transform: scaleY(1); opacity: 1; } 50% { transform: scaleY(0.5); opacity: 0.4; } }

@keyframes fadeUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }

/* ── Section base ── */
.section {
    padding: 100px 24px; max-width: 1100px; margin: 0 auto;
}
.section-tag {
    font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #5c6bc0;
    letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 12px;
    display: flex; align-items: center; gap: 12px;
}
.section-tag::before { content: '//'; color: #37474f; }
.section-title {
    font-family: 'Syne', sans-serif; font-size: clamp(32px, 5vw, 56px);
    font-weight: 800; line-height: 1.05; letter-spacing: -0.02em;
    color: #eceff1; margin-bottom: 64px;
}
.section-title span { color: #5c6bc0; }

/* ── Divider ── */
.divider {
    width: 100%; height: 1px; margin: 0;
    background: linear-gradient(90deg, transparent, rgba(92,107,192,0.3), transparent);
}

/* ── JOURNEY / TIMELINE ── */
.timeline { position: relative; padding-left: 40px; }
.timeline::before {
    content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px;
    background: linear-gradient(to bottom, #5c6bc0, #0097a7, #7c4dff, #5c6bc0);
    border-radius: 1px;
}
.timeline-item { position: relative; margin-bottom: 64px; }
.timeline-item:last-child { margin-bottom: 0; }
.timeline-dot {
    position: absolute; left: -47px; top: 6px;
    width: 16px; height: 16px; border-radius: 50%;
    border: 2px solid; display: flex; align-items: center; justify-content: center;
}
.timeline-dot.school { background: rgba(92,107,192,0.2); border-color: #5c6bc0; }
.timeline-dot.college { background: rgba(0,151,167,0.2); border-color: #0097a7; }
.timeline-dot.pg { background: rgba(124,77,255,0.2); border-color: #7c4dff; }
.timeline-dot.work1 { background: rgba(76,175,80,0.2); border-color: #4caf50; }
.timeline-dot.work2 { background: rgba(255,152,0,0.2); border-color: #ff9800; }
.timeline-dot::after { content: ''; width: 6px; height: 6px; border-radius: 50%; background: currentColor; }
.timeline-dot.school::after { color: #5c6bc0; }
.timeline-dot.college::after { color: #0097a7; }
.timeline-dot.pg::after { color: #7c4dff; }
.timeline-dot.work1::after { color: #4caf50; }
.timeline-dot.work2::after { color: #ff9800; }

.timeline-year {
    font-family: 'JetBrains Mono', monospace; font-size: 12px;
    color: #546e7a; margin-bottom: 6px; letter-spacing: 0.08em;
}
.timeline-card {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px; padding: 28px 32px;
    transition: border-color 0.3s ease, background 0.3s ease;
    backdrop-filter: blur(4px);
}
.timeline-card:hover { background: rgba(255,255,255,0.055); border-color: rgba(92,107,192,0.35); }
.timeline-org { font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 700; color: #eceff1; margin-bottom: 4px; }
.timeline-role { font-size: 14px; color: #80cbc4; font-weight: 500; margin-bottom: 14px; }
.timeline-desc { font-size: 15px; color: #78909c; line-height: 1.7; }
.timeline-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 16px; }
.t-tag {
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    background: rgba(92,107,192,0.12); border: 1px solid rgba(92,107,192,0.25);
    color: #9fa8da; border-radius: 6px; padding: 4px 10px;
}

/* ── SKILLS ── */
.skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
.skill-card {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px; padding: 28px; transition: all 0.3s ease;
    position: relative; overflow: hidden;
}
.skill-card::before {
    content: ''; position: absolute; inset: 0; opacity: 0;
    transition: opacity 0.3s ease;
}
.skill-card:hover { transform: translateY(-4px); }
.skill-card:hover::before { opacity: 1; }

.skill-card.ai::before { background: radial-gradient(circle at top left, rgba(92,107,192,0.12), transparent 70%); }
.skill-card.backend::before { background: radial-gradient(circle at top left, rgba(0,151,167,0.12), transparent 70%); }
.skill-card.frontend::before { background: radial-gradient(circle at top left, rgba(124,77,255,0.12), transparent 70%); }
.skill-card.data::before { background: radial-gradient(circle at top left, rgba(76,175,80,0.12), transparent 70%); }
.skill-card.cloud::before { background: radial-gradient(circle at top left, rgba(255,152,0,0.12), transparent 70%); }

.skill-icon { font-size: 32px; margin-bottom: 16px; }
.skill-name { font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; color: #eceff1; margin-bottom: 8px; }
.skill-items { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
.s-item {
    font-size: 12px; font-family: 'JetBrains Mono', monospace;
    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
    color: #90a4ae; border-radius: 6px; padding: 4px 10px;
}

/* ── PROJECTS ── */
.projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; }
.project-card {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px; padding: 32px; position: relative; overflow: hidden;
    transition: all 0.3s ease;
}
.project-card:hover { transform: translateY(-6px); border-color: rgba(92,107,192,0.4); }
.project-number {
    font-family: 'Syne', sans-serif; font-size: 72px; font-weight: 800;
    color: rgba(255,255,255,0.04); position: absolute; top: 12px; right: 20px;
    line-height: 1; user-select: none; letter-spacing: -0.04em;
}
.project-accent {
    width: 40px; height: 3px; border-radius: 2px; margin-bottom: 20px;
}
.project-title { font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 700; color: #eceff1; margin-bottom: 12px; }
.project-desc { font-size: 14px; color: #78909c; line-height: 1.7; margin-bottom: 20px; }
.project-tech { display: flex; flex-wrap: wrap; gap: 6px; }
.p-tech {
    font-size: 11px; font-family: 'JetBrains Mono', monospace;
    border-radius: 6px; padding: 4px 10px; border: 1px solid;
}

/* ── IMPACT ── */
.impact-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
.impact-card {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px; padding: 32px 24px; text-align: center;
    transition: all 0.3s ease;
}
.impact-card:hover { transform: translateY(-4px); background: rgba(255,255,255,0.055); }
.impact-number {
    font-family: 'Syne', sans-serif; font-size: 48px; font-weight: 800;
    line-height: 1; margin-bottom: 8px;
    background: linear-gradient(135deg, #5c6bc0, #80cbc4);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.impact-label { font-size: 14px; color: #546e7a; line-height: 1.4; }

/* ── CONTACT ── */
.contact-section {
    background: rgba(92,107,192,0.07); border: 1px solid rgba(92,107,192,0.2);
    border-radius: 24px; padding: 72px 40px; text-align: center;
    position: relative; overflow: hidden;
}
.contact-section::before {
    content: ''; position: absolute; top: -60px; left: 50%; transform: translateX(-50%);
    width: 300px; height: 300px; background: radial-gradient(circle, rgba(92,107,192,0.15), transparent 70%);
    pointer-events: none;
}
.contact-title { font-family: 'Syne', sans-serif; font-size: clamp(28px, 5vw, 48px); font-weight: 800; color: #eceff1; margin-bottom: 16px; }
.contact-sub { font-size: 16px; color: #78909c; margin-bottom: 40px; max-width: 500px; margin-left: auto; margin-right: auto; }
.contact-links { display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; }
.contact-link {
    display: inline-flex; align-items: center; gap: 10px;
    padding: 14px 28px; border-radius: 12px; font-size: 15px; font-weight: 600;
    text-decoration: none; transition: all 0.25s ease;
    font-family: 'Space Grotesk', sans-serif;
}
.contact-link.email { background: linear-gradient(135deg, #5c6bc0, #7c4dff); color: white; box-shadow: 0 4px 20px rgba(92,107,192,0.35); }
.contact-link.email:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(92,107,192,0.55); }
.contact-link.linkedin { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); color: #9fa8da; }
.contact-link.linkedin:hover { background: rgba(255,255,255,0.1); transform: translateY(-2px); }
.contact-link.phone { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); color: #9fa8da; }
.contact-link.phone:hover { background: rgba(255,255,255,0.1); transform: translateY(-2px); }

/* ── NAV ── */
.nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    padding: 16px 32px; display: flex; align-items: center; justify-content: space-between;
    background: rgba(5,9,20,0.7); backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.nav-logo { font-family: 'Syne', sans-serif; font-size: 20px; font-weight: 800; color: #eceff1; letter-spacing: -0.02em; }
.nav-logo span { color: #5c6bc0; }
.nav-links { display: flex; gap: 32px; }
.nav-link { font-size: 14px; color: #546e7a; text-decoration: none; letter-spacing: 0.03em; transition: color 0.2s; }
.nav-link:hover { color: #9fa8da; }

/* ── SPOT AWARD CALLOUT ── */
.callout {
    background: linear-gradient(135deg, rgba(255,152,0,0.1), rgba(255,193,7,0.05));
    border: 1px solid rgba(255,152,0,0.25); border-radius: 14px;
    padding: 20px 24px; display: flex; align-items: center; gap: 16px;
    margin-top: 16px;
}
.callout-icon { font-size: 28px; flex-shrink: 0; }
.callout-text { font-size: 14px; color: #ffcc80; line-height: 1.5; }

/* ── Footer ── */
.footer { text-align: center; padding: 40px 24px; font-size: 13px; color: #263238; }
</style>

<div class="blob-container">
    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>
    <div class="blob blob-3"></div>
</div>

<!-- NAV -->
<nav class="nav">
    <div class="nav-logo">A<span>.</span>Sant</div>
    <div class="nav-links">
        <a href="#journey" class="nav-link">Journey</a>
        <a href="#skills" class="nav-link">Skills</a>
        <a href="#projects" class="nav-link">Projects</a>
        <a href="#contact" class="nav-link">Contact</a>
    </div>
</nav>

<div class="page">

<!-- ════════════════════════════ HERO ════════════════════════════ -->
<section class="hero">
    <div class="hero-badge">Available for Opportunities · Mumbai, India</div>
    <h1 class="hero-name">Anand<br>Sant</h1>
    <p class="hero-title">Full-Stack <span>AI Engineer</span> · Building the Future with LLMs & RAG</p>
    <div class="hero-meta">
        <div class="meta-chip">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
            Mumbai, India
        </div>
        <div class="meta-chip">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>
            2 yrs 5 months experience
        </div>
        <div class="meta-chip">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
            Python · React · GenAI
        </div>
    </div>
    <div class="hero-cta">
        <a href="mailto:anandsant1212@gmail.com" class="cta-primary">✉ Get in Touch</a>
        <a href="https://linkedin.com/in/anandsant1212" target="_blank" class="cta-secondary">↗ LinkedIn</a>
    </div>
    <div class="scroll-hint">Scroll</div>
</section>

<div class="divider"></div>

<!-- ════════════════════════════ IMPACT ════════════════════════════ -->
<div class="section" style="padding-bottom: 60px;">
    <div class="impact-grid">
        <div class="impact-card">
            <div class="impact-number">90%</div>
            <div class="impact-label">Manual effort reduced in alt text generation</div>
        </div>
        <div class="impact-card">
            <div class="impact-number">75%</div>
            <div class="impact-label">Faster document processing via AI pipelines</div>
        </div>
        <div class="impact-card">
            <div class="impact-number">50%</div>
            <div class="impact-label">Reduction in fraudulent charges for clients</div>
        </div>
        <div class="impact-card">
            <div class="impact-number">6+</div>
            <div class="impact-label">AI proof-of-concepts shipped independently</div>
        </div>
    </div>
</div>

<div class="divider"></div>

<!-- ════════════════════════════ JOURNEY ════════════════════════════ -->
<a name="journey"></a>
<div class="section">
    <div class="section-tag">01 Origin Story</div>
    <h2 class="section-title">The Road<br>That <span>Shaped Me</span></h2>

    <div class="timeline">

        <!-- School -->
        <div class="timeline-item">
            <div class="timeline-dot school"></div>
            <div class="timeline-year">2016 · Akola, Maharashtra</div>
            <div class="timeline-card">
                <div class="timeline-org">Govt. Agarkar College, Akola</div>
                <div class="timeline-role">Higher Secondary · Science Stream</div>
                <div class="timeline-desc">
                    The foundation years. Science became my lens — mathematics, physics, and a growing curiosity about how things work under the hood. Akola taught me discipline and the hunger to explore beyond textbooks.
                </div>
                <div class="timeline-tags">
                    <span class="t-tag">Science</span>
                    <span class="t-tag">Mathematics</span>
                    <span class="t-tag">Foundation</span>
                </div>
            </div>
        </div>

        <!-- Engineering -->
        <div class="timeline-item">
            <div class="timeline-dot college"></div>
            <div class="timeline-year">2018 – 2022 · Nashik, Maharashtra</div>
            <div class="timeline-card">
                <div class="timeline-org">KK Wagh Institute of Engineering, Nashik</div>
                <div class="timeline-role">Bachelor of Engineering</div>
                <div class="timeline-desc">
                    Four transformative years where curiosity became craft. I dove deep into computer science fundamentals — algorithms, data structures, and system design. Here I wrote my first lines of Python, built my first projects, and fell in love with the idea of machines that think. Engineering wasn't just a degree; it was a mindset shift.
                </div>
                <div class="timeline-tags">
                    <span class="t-tag">Computer Science</span>
                    <span class="t-tag">Python (first steps)</span>
                    <span class="t-tag">System Design</span>
                    <span class="t-tag">Algorithms</span>
                </div>
            </div>
        </div>

        <!-- PG Diploma -->
        <div class="timeline-item">
            <div class="timeline-dot pg"></div>
            <div class="timeline-year">Mar 2023 – Nov 2023 · CDAC</div>
            <div class="timeline-card">
                <div class="timeline-org">CDAC — Centre for Development of Advanced Computing</div>
                <div class="timeline-role">PG Diploma · Big Data Analytics</div>
                <div class="timeline-desc">
                    The pivot. This intensive program was my deliberate leap into data and AI. Eight focused months immersing in Big Data ecosystems, machine learning pipelines, and cloud infrastructure. CDAC compressed years of learning into months — and launched my trajectory into the AI space.
                </div>
                <div class="timeline-tags">
                    <span class="t-tag">Big Data</span>
                    <span class="t-tag">Machine Learning</span>
                    <span class="t-tag">Cloud</span>
                    <span class="t-tag">Analytics</span>
                </div>
            </div>
        </div>

        <!-- LearningMate -->
        <div class="timeline-item">
            <div class="timeline-dot work1"></div>
            <div class="timeline-year">Dec 2023 – Sep 2025 · Mumbai</div>
            <div class="timeline-card">
                <div class="timeline-org">LearningMate Solutions</div>
                <div class="timeline-role">Associate Software Developer</div>
                <div class="timeline-desc">
                    First corporate chapter — and it hit the ground running. I built production-grade AI systems serving real clients across multiple pipelines. From GPT-4o powered image accessibility tools to automating California's educational analytics, I shipped work that mattered at scale. Led POCs, owned cross-functional delivery, and proved that a fresh mind can ship senior-level impact.
                </div>
                <div class="callout">
                    <span class="callout-icon">🏆</span>
                    <span class="callout-text"><strong>SPOT Award Recipient</strong> — Recognized for outstanding initiative, cross-functional ownership, and high-impact delivery across backend and AI systems.</span>
                </div>
                <div class="timeline-tags">
                    <span class="t-tag">GPT-4o</span>
                    <span class="t-tag">FastAPI</span>
                    <span class="t-tag">React</span>
                    <span class="t-tag">AWS S3</span>
                    <span class="t-tag">RAG</span>
                    <span class="t-tag">Azure OpenAI</span>
                </div>
            </div>
        </div>

        <!-- Telemerge -->
        <div class="timeline-item">
            <div class="timeline-dot work2"></div>
            <div class="timeline-year">Oct 2025 – Present · Mumbai</div>
            <div class="timeline-card">
                <div class="timeline-org">Telemerge</div>
                <div class="timeline-role">Software Engineer</div>
                <div class="timeline-desc">
                    Current chapter. Building a Test Case Generation platform for State Bank of India (SBI) — automating QA workflows with Generative AI at banking scale. Architecting secure full-stack applications with JWT auth, multi-database RAG (Postgres + Chroma), and GPT-4.1 powered intelligent document processing. This is where enterprise reliability meets cutting-edge AI.
                </div>
                <div class="timeline-tags">
                    <span class="t-tag">GPT-4.1</span>
                    <span class="t-tag">PostgreSQL</span>
                    <span class="t-tag">ChromaDB</span>
                    <span class="t-tag">JWT Auth</span>
                    <span class="t-tag">SIT/UAT</span>
                    <span class="t-tag">OCR Pipelines</span>
                </div>
            </div>
        </div>

    </div>
</div>

<div class="divider"></div>

<!-- ════════════════════════════ SKILLS ════════════════════════════ -->
<a name="skills"></a>
<div class="section">
    <div class="section-tag">02 Arsenal</div>
    <h2 class="section-title">Skills &<br><span>Tech Stack</span></h2>

    <div class="skills-grid">
        <div class="skill-card ai">
            <div class="skill-icon">🤖</div>
            <div class="skill-name">AI / GenAI</div>
            <div class="skill-items">
                <span class="s-item">LLMs</span>
                <span class="s-item">RAG</span>
                <span class="s-item">Azure OpenAI</span>
                <span class="s-item">GPT-4o / 4.1</span>
                <span class="s-item">Gemini 1.5</span>
                <span class="s-item">DALL-E</span>
                <span class="s-item">Chroma</span>
                <span class="s-item">OCR</span>
            </div>
        </div>
        <div class="skill-card backend">
            <div class="skill-icon">⚙️</div>
            <div class="skill-name">Backend</div>
            <div class="skill-items">
                <span class="s-item">Python</span>
                <span class="s-item">FastAPI</span>
                <span class="s-item">REST API</span>
                <span class="s-item">System Design</span>
                <span class="s-item">JWT Auth</span>
                <span class="s-item">Microservices</span>
            </div>
        </div>
        <div class="skill-card frontend">
            <div class="skill-icon">🎨</div>
            <div class="skill-name">Frontend</div>
            <div class="skill-items">
                <span class="s-item">React JS</span>
                <span class="s-item">React MUI</span>
                <span class="s-item">Streamlit</span>
                <span class="s-item">Microfrontend</span>
            </div>
        </div>
        <div class="skill-card data">
            <div class="skill-icon">🗄️</div>
            <div class="skill-name">Databases</div>
            <div class="skill-items">
                <span class="s-item">PostgreSQL</span>
                <span class="s-item">MongoDB</span>
                <span class="s-item">MySQL</span>
                <span class="s-item">SQLite</span>
                <span class="s-item">Vector DBs</span>
            </div>
        </div>
        <div class="skill-card cloud">
            <div class="skill-icon">☁️</div>
            <div class="skill-name">Cloud & DevOps</div>
            <div class="skill-items">
                <span class="s-item">AWS S3</span>
                <span class="s-item">Docker</span>
                <span class="s-item">Kubernetes</span>
                <span class="s-item">Cloud Architecture</span>
                <span class="s-item">Git</span>
                <span class="s-item">GitHub Copilot</span>
            </div>
        </div>
    </div>
</div>

<div class="divider"></div>

<!-- ════════════════════════════ PROJECTS ════════════════════════════ -->
<a name="projects"></a>
<div class="section">
    <div class="section-tag">03 Work</div>
    <h2 class="section-title">Featured<br><span>Projects</span></h2>

    <div class="projects-grid">

        <div class="project-card">
            <span class="project-number">01</span>
            <div class="project-accent" style="background: linear-gradient(90deg,#5c6bc0,#7c4dff);"></div>
            <div class="project-title">LCAP Data Extraction Platform</div>
            <div class="project-desc">
                Built for California CCEE — an AI pipeline that transforms complex LCAP educational documents into structured KPIs. Features human-in-the-loop validation and seamless Snowflake integration via S3. Achieved 75% faster processing.
            </div>
            <div class="project-tech">
                <span class="p-tech" style="color:#9fa8da;border-color:rgba(92,107,192,0.3);background:rgba(92,107,192,0.08);">Azure OpenAI</span>
                <span class="p-tech" style="color:#9fa8da;border-color:rgba(92,107,192,0.3);background:rgba(92,107,192,0.08);">RAG</span>
                <span class="p-tech" style="color:#9fa8da;border-color:rgba(92,107,192,0.3);background:rgba(92,107,192,0.08);">Kubernetes</span>
                <span class="p-tech" style="color:#9fa8da;border-color:rgba(92,107,192,0.3);background:rgba(92,107,192,0.08);">MongoDB Atlas</span>
                <span class="p-tech" style="color:#9fa8da;border-color:rgba(92,107,192,0.3);background:rgba(92,107,192,0.08);">AWS S3</span>
            </div>
        </div>

        <div class="project-card">
            <span class="project-number">02</span>
            <div class="project-accent" style="background: linear-gradient(90deg,#0097a7,#4caf50);"></div>
            <div class="project-title">AI Alt Text Generation Platform</div>
            <div class="project-desc">
                End-to-end accessibility platform powering image descriptions across client pipelines. Multimodal AI (GPT-4o + Gemini 1.5) with OCR, keyword extraction, and classification. Reduced manual effort by 90% and cut fraudulent charges by 50%.
            </div>
            <div class="project-tech">
                <span class="p-tech" style="color:#80cbc4;border-color:rgba(0,151,167,0.3);background:rgba(0,151,167,0.08);">GPT-4o</span>
                <span class="p-tech" style="color:#80cbc4;border-color:rgba(0,151,167,0.3);background:rgba(0,151,167,0.08);">Gemini 1.5</span>
                <span class="p-tech" style="color:#80cbc4;border-color:rgba(0,151,167,0.3);background:rgba(0,151,167,0.08);">FastAPI</span>
                <span class="p-tech" style="color:#80cbc4;border-color:rgba(0,151,167,0.3);background:rgba(0,151,167,0.08);">React MUI</span>
                <span class="p-tech" style="color:#80cbc4;border-color:rgba(0,151,167,0.3);background:rgba(0,151,167,0.08);">AWS S3</span>
            </div>
        </div>

        <div class="project-card">
            <span class="project-number">03</span>
            <div class="project-accent" style="background: linear-gradient(90deg,#7c4dff,#e040fb);"></div>
            <div class="project-title">SBI Test Case Generation Platform</div>
            <div class="project-desc">
                Automating QA workflows for India's largest bank. Ingests BRD/Solution documents, converts pages to images, and generates intelligent test cases for SIT/UAT using GPT-4.1 with dual vector database RAG.
            </div>
            <div class="project-tech">
                <span class="p-tech" style="color:#ce93d8;border-color:rgba(124,77,255,0.3);background:rgba(124,77,255,0.08);">GPT-4.1</span>
                <span class="p-tech" style="color:#ce93d8;border-color:rgba(124,77,255,0.3);background:rgba(124,77,255,0.08);">Chroma</span>
                <span class="p-tech" style="color:#ce93d8;border-color:rgba(124,77,255,0.3);background:rgba(124,77,255,0.08);">PostgreSQL</span>
                <span class="p-tech" style="color:#ce93d8;border-color:rgba(124,77,255,0.3);background:rgba(124,77,255,0.08);">JWT Auth</span>
                <span class="p-tech" style="color:#ce93d8;border-color:rgba(124,77,255,0.3);background:rgba(124,77,255,0.08);">OCR</span>
            </div>
        </div>

        <div class="project-card">
            <span class="project-number">04</span>
            <div class="project-accent" style="background: linear-gradient(90deg,#ff9800,#f44336);"></div>
            <div class="project-title">Real-time Facial Analysis System</div>
            <div class="project-desc">
                Computer vision application with multi-dimensional facial analysis: emotion recognition, attention monitoring, drowsiness detection (Eye Aspect Ratio), and 3D head pose estimation using solvePnP — all on a real-time analytics dashboard.
            </div>
            <div class="project-tech">
                <span class="p-tech" style="color:#ffcc80;border-color:rgba(255,152,0,0.3);background:rgba(255,152,0,0.08);">Python</span>
                <span class="p-tech" style="color:#ffcc80;border-color:rgba(255,152,0,0.3);background:rgba(255,152,0,0.08);">OpenCV</span>
                <span class="p-tech" style="color:#ffcc80;border-color:rgba(255,152,0,0.3);background:rgba(255,152,0,0.08);">MediaPipe</span>
                <span class="p-tech" style="color:#ffcc80;border-color:rgba(255,152,0,0.3);background:rgba(255,152,0,0.08);">Computer Vision</span>
            </div>
        </div>

    </div>
</div>

<div class="divider"></div>

<!-- ════════════════════════════ CONTACT ════════════════════════════ -->
<a name="contact"></a>
<div class="section">
    <div class="contact-section">
        <div class="contact-title">Let's Build<br>Something Together</div>
        <p class="contact-sub">Open to full-time roles, freelance AI projects, and interesting conversations about LLMs, RAG, and the future of software.</p>
        <div class="contact-links">
            <a href="mailto:anandsant1212@gmail.com" class="contact-link email">✉ anandsant1212@gmail.com</a>
            <a href="https://linkedin.com/in/anandsant1212" target="_blank" class="contact-link linkedin">↗ LinkedIn</a>
            <a href="tel:+919423586586" class="contact-link phone">📞 +91 94235 86586</a>
        </div>
    </div>
</div>

<div class="footer">
    Crafted with ⚡ by Anand Sant · Mumbai, India · 2026
</div>

</div>
""", unsafe_allow_html=True)