import streamlit as st

st.set_page_config(
    page_title="Anand Sant | AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Init session state ────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "exp_tab" not in st.session_state:
    st.session_state.exp_tab = "telemerge"
if "proj_open" not in st.session_state:
    st.session_state.proj_open = None

def nav(p):
    st.session_state.page = p
    st.session_state.proj_open = None

# ── Global styles ─────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Playfair+Display:wght@700;800&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: #f5f3ef;
    font-family: 'DM Sans', sans-serif;
    color: #1a1a1a;
}
#MainMenu, footer, header, [data-testid="stToolbar"] { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }

/* ── Streamlit button reset ── */
.stButton > button {
    background: none !important;
    border: none !important;
    padding: 0 !important;
    font-family: 'DM Sans', sans-serif !important;
    cursor: pointer !important;
    box-shadow: none !important;
    color: inherit !important;
    width: auto !important;
}
.stButton > button:hover, .stButton > button:focus {
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    color: inherit !important;
}

/* ── NAV ── */
.topnav {
    position: sticky; top: 0; z-index: 100;
    background: rgba(245,243,239,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid #e0ddd8;
    padding: 0 48px;
    display: flex; align-items: center; justify-content: space-between;
    height: 64px;
}
.nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 22px; font-weight: 800;
    color: #1a1a1a; letter-spacing: -0.02em;
}
.nav-logo em { color: #c84b31; font-style: normal; }
.nav-menu { display: flex; gap: 4px; }
.nav-btn {
    padding: 8px 18px; border-radius: 8px;
    font-size: 14px; font-weight: 500;
    color: #555; cursor: pointer;
    transition: all 0.2s;
    background: none; border: none;
    font-family: 'DM Sans', sans-serif;
    text-decoration: none;
}
.nav-btn:hover { background: #ece9e3; color: #1a1a1a; }
.nav-btn.active { background: #1a1a1a; color: #f5f3ef; }

/* ── HERO ── */
.hero-wrap {
    min-height: calc(100vh - 64px);
    display: flex; flex-direction: column; justify-content: center;
    max-width: 900px; margin: 0 auto; padding: 60px 24px 80px;
}
.hero-label {
    display: inline-flex; align-items: center; gap: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px; color: #c84b31; letter-spacing: 0.08em;
    text-transform: uppercase; margin-bottom: 24px;
}
.hero-label::before {
    content: ''; width: 24px; height: 1px; background: #c84b31;
}
.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(52px, 8vw, 96px);
    font-weight: 800; line-height: 1.0;
    letter-spacing: -0.03em; color: #1a1a1a;
    margin-bottom: 28px;
}
.hero-name em { color: #c84b31; font-style: normal; }
.hero-sub {
    font-size: 20px; color: #666; line-height: 1.6;
    max-width: 580px; margin-bottom: 40px; font-weight: 400;
}
.hero-sub strong { color: #1a1a1a; font-weight: 600; }
.hero-chips { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 48px; }
.chip {
    padding: 8px 16px; border-radius: 999px;
    border: 1px solid #d4d0c9; background: white;
    font-size: 13px; color: #555; font-weight: 500;
}
.hero-ctas { display: flex; gap: 12px; flex-wrap: wrap; }
.cta-main {
    padding: 14px 28px; border-radius: 10px;
    background: #1a1a1a; color: #f5f3ef;
    font-size: 15px; font-weight: 600;
    text-decoration: none; transition: all 0.2s;
    font-family: 'DM Sans', sans-serif;
}
.cta-main:hover { background: #c84b31; }
.cta-sec {
    padding: 14px 28px; border-radius: 10px;
    background: white; color: #1a1a1a;
    font-size: 15px; font-weight: 600;
    border: 1px solid #d4d0c9; text-decoration: none;
    transition: all 0.2s; font-family: 'DM Sans', sans-serif;
}
.cta-sec:hover { border-color: #1a1a1a; }

/* ── STAT ROW ── */
.stats-row {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 1px; background: #d4d0c9;
    border: 1px solid #d4d0c9; border-radius: 14px;
    overflow: hidden; margin-top: 64px;
}
.stat-box {
    background: white; padding: 28px 24px; text-align: center;
}
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 40px; font-weight: 800;
    color: #c84b31; line-height: 1;
}
.stat-lbl { font-size: 13px; color: #888; margin-top: 6px; line-height: 1.4; }

/* ── PAGE CONTAINER ── */
.page-wrap { max-width: 900px; margin: 0 auto; padding: 56px 24px 80px; }
.page-heading {
    font-family: 'Playfair Display', serif;
    font-size: clamp(36px, 5vw, 56px); font-weight: 800;
    letter-spacing: -0.03em; color: #1a1a1a;
    margin-bottom: 8px; line-height: 1.1;
}
.page-heading em { color: #c84b31; font-style: normal; }
.page-sub { font-size: 16px; color: #888; margin-bottom: 48px; font-weight: 400; }

/* ── ABOUT ── */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-bottom: 48px; }
.about-card {
    background: white; border-radius: 14px;
    border: 1px solid #e0ddd8; padding: 28px;
}
.about-card h3 {
    font-size: 13px; text-transform: uppercase; letter-spacing: 0.08em;
    color: #999; margin-bottom: 14px;
    font-family: 'JetBrains Mono', monospace;
}
.about-card p { font-size: 15px; color: #444; line-height: 1.7; }
.interest-grid { display: flex; flex-wrap: wrap; gap: 8px; }
.interest-tag {
    padding: 6px 14px; border-radius: 999px;
    background: #f5f3ef; border: 1px solid #e0ddd8;
    font-size: 13px; color: #555;
}

/* ── EXPERIENCE TABS ── */
.exp-tabs { display: flex; gap: 4px; margin-bottom: 28px; }
.exp-tab-btn {
    padding: 10px 22px; border-radius: 8px;
    font-size: 14px; font-weight: 600;
    cursor: pointer; border: 1px solid #d4d0c9;
    background: white; color: #777;
    font-family: 'DM Sans', sans-serif;
    transition: all 0.2s;
}
.exp-tab-btn.active { background: #1a1a1a; color: white; border-color: #1a1a1a; }

.exp-company {
    background: white; border: 1px solid #e0ddd8;
    border-radius: 14px; padding: 32px;
    margin-bottom: 24px;
}
.exp-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; }
.exp-org {
    font-family: 'Playfair Display', serif;
    font-size: 28px; font-weight: 800; color: #1a1a1a;
}
.exp-period {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px; color: #999; padding-top: 6px;
}
.exp-role { font-size: 15px; color: #c84b31; font-weight: 600; margin-bottom: 20px; }
.exp-bullets { list-style: none; padding: 0; }
.exp-bullets li {
    padding: 8px 0; font-size: 14px; color: #555;
    line-height: 1.6; border-bottom: 1px solid #f0ede8;
    padding-left: 18px; position: relative;
}
.exp-bullets li:last-child { border-bottom: none; }
.exp-bullets li::before {
    content: '→'; position: absolute; left: 0;
    color: #c84b31; font-size: 12px; top: 9px;
}
.award-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: #fff8f0; border: 1px solid #ffd090;
    border-radius: 8px; padding: 10px 16px;
    font-size: 13px; color: #b06000; margin-top: 16px; font-weight: 500;
}

/* ── PROJECT CARDS ── */
.proj-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.proj-card {
    background: white; border: 1px solid #e0ddd8;
    border-radius: 14px; padding: 28px;
    cursor: pointer; transition: all 0.2s;
    position: relative; overflow: hidden;
}
.proj-card:hover { border-color: #c84b31; transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.07); }
.proj-card::after {
    content: '↗'; position: absolute; top: 20px; right: 20px;
    font-size: 18px; color: #d4d0c9; transition: 0.2s;
}
.proj-card:hover::after { color: #c84b31; }
.proj-company-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em;
    color: #c84b31; margin-bottom: 10px;
}
.proj-title { font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; color: #1a1a1a; margin-bottom: 10px; line-height: 1.2; }
.proj-summary { font-size: 13px; color: #888; line-height: 1.6; margin-bottom: 16px; }
.proj-tags { display: flex; flex-wrap: wrap; gap: 6px; }
.proj-tag {
    font-size: 11px; font-family: 'JetBrains Mono', monospace;
    background: #f5f3ef; border: 1px solid #e0ddd8;
    color: #777; border-radius: 6px; padding: 3px 8px;
}

/* ── PROJECT DETAIL ── */
.proj-detail {
    background: white; border: 1px solid #e0ddd8;
    border-radius: 14px; padding: 40px;
}
.back-btn {
    display: inline-flex; align-items: center; gap: 8px;
    font-size: 14px; color: #888; cursor: pointer;
    margin-bottom: 28px; font-weight: 500;
    background: none; border: none; font-family: 'DM Sans', sans-serif;
}
.back-btn:hover { color: #c84b31; }
.detail-title { font-family: 'Playfair Display', serif; font-size: 32px; font-weight: 800; margin-bottom: 6px; }
.detail-company { font-size: 14px; color: #c84b31; font-weight: 600; margin-bottom: 24px; }
.detail-section { margin-bottom: 28px; }
.detail-section h4 {
    font-size: 12px; text-transform: uppercase; letter-spacing: 0.1em;
    color: #999; font-family: 'JetBrains Mono', monospace;
    margin-bottom: 12px;
}
.detail-bullets { list-style: none; padding: 0; }
.detail-bullets li {
    font-size: 14px; color: #555; line-height: 1.7;
    padding: 6px 0 6px 20px; position: relative;
    border-bottom: 1px solid #f5f3ef;
}
.detail-bullets li:last-child { border: none; }
.detail-bullets li::before { content: '→'; position: absolute; left: 0; color: #c84b31; }
.tech-stack { display: flex; flex-wrap: wrap; gap: 8px; }
.tech-item {
    padding: 6px 14px; border-radius: 8px;
    background: #f5f3ef; border: 1px solid #e0ddd8;
    font-size: 13px; color: #555; font-weight: 500;
}

/* ── SKILLS ── */
.skill-group { margin-bottom: 32px; }
.skill-group-title {
    font-size: 13px; font-family: 'JetBrains Mono', monospace;
    text-transform: uppercase; letter-spacing: 0.1em;
    color: #999; margin-bottom: 12px;
}
.skill-pills { display: flex; flex-wrap: wrap; gap: 8px; }
.skill-pill {
    padding: 9px 18px; border-radius: 999px;
    border: 1px solid #d4d0c9; background: white;
    font-size: 14px; color: #444; font-weight: 500;
    transition: all 0.2s;
}
.skill-pill:hover { border-color: #c84b31; color: #c84b31; }

/* ── JOURNEY TIMELINE ── */
.journey-line { position: relative; padding-left: 32px; }
.journey-line::before {
    content: ''; position: absolute; left: 7px; top: 0; bottom: 0;
    width: 1px; background: #e0ddd8;
}
.jitem { position: relative; margin-bottom: 36px; }
.jdot {
    position: absolute; left: -29px; top: 4px;
    width: 14px; height: 14px; border-radius: 50%;
    border: 2px solid #c84b31; background: white;
}
.jdot.filled { background: #c84b31; }
.jyear {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; color: #aaa; margin-bottom: 6px;
}
.jcard {
    background: white; border: 1px solid #e0ddd8;
    border-radius: 12px; padding: 20px 24px;
}
.jcard h3 { font-size: 17px; font-weight: 700; color: #1a1a1a; margin-bottom: 4px; }
.jcard .jrole { font-size: 13px; color: #c84b31; font-weight: 600; margin-bottom: 8px; }
.jcard p { font-size: 13px; color: #888; line-height: 1.6; }

/* ── CONTACT ── */
.contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.contact-card {
    background: white; border: 1px solid #e0ddd8;
    border-radius: 14px; padding: 28px;
    display: flex; align-items: center; gap: 16px;
    text-decoration: none; color: inherit;
    transition: all 0.2s;
}
.contact-card:hover { border-color: #c84b31; transform: translateY(-2px); }
.contact-icon { font-size: 28px; }
.contact-label { font-size: 12px; color: #aaa; text-transform: uppercase; letter-spacing: 0.06em; font-family: 'JetBrains Mono', monospace; }
.contact-value { font-size: 15px; color: #1a1a1a; font-weight: 600; margin-top: 2px; }

/* mobile */
@media(max-width:700px){
    .stats-row { grid-template-columns: 1fr 1fr; }
    .about-grid, .proj-grid, .contact-grid { grid-template-columns: 1fr; }
    .topnav { padding: 0 16px; }
    .hero-wrap, .page-wrap { padding: 40px 16px 60px; }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────── DATA ───────────────────────────────────────────

PROJECTS = {
    "lcap": {
        "title": "LCAP Data Extraction & Analytics Platform",
        "company": "LearningMate",
        "summary": "AI pipeline that transforms complex educational policy documents into structured KPIs for California.",
        "tags": ["Azure OpenAI", "RAG", "Kubernetes", "MongoDB", "AWS S3"],
        "bullets": [
            "Developed a sophisticated AI-powered data extraction platform for California Collaborative for Educational Excellence (CCEE) to automate processing of LCAP documents.",
            "Implemented complete pipeline from document ingestion and intelligent KPI extraction to final data delivery, featuring a human-in-the-loop approval workflow.",
            "Reduced document processing time by 75% through AI pipelines and human-in-the-loop validation, enabling data-driven educational insights.",
            "Enabled seamless integration with client infrastructure via standardized JSON outputs to S3 for Snowflake ingestion.",
            "Streamlined data delivery allowing stakeholders to effectively monitor and enhance educational outcomes.",
        ],
        "tech": ["Azure OpenAI", "Vector Databases", "Kubernetes", "MongoDB Atlas", "AWS S3", "RAG", "OCR", "Python", "FastAPI"],
        "impact": "75% faster processing"
    },
    "alttext": {
        "title": "AI-Powered Alt Text Generation Platform",
        "company": "LearningMate",
        "summary": "End-to-end accessibility platform automating high-quality image descriptions across multiple client pipelines.",
        "tags": ["GPT-4o", "Gemini 1.5", "FastAPI", "React MUI", "AWS S3"],
        "bullets": [
            "Delivered an AI-powered alt text generation platform, enhancing accessibility and SEO; integrated across multiple pipelines and client environments.",
            "Reduced manual effort in alt text generation by 90% using AI-based vision models for OCR, classification, and keyword extraction.",
            "Built a full-stack solution using FastAPI and React MUI, enabling seamless interaction and image processing with multimodal AI models.",
            "The solution features microservice architecture, cloud storage integration, automated email notifications, and a modern React MUI interface within a microfrontend framework.",
            "Supports multiple input methods (file uploads, URLs, S3) with configurable generation parameters and detailed image analysis capabilities.",
            "Reduced fraudulent charges by 50% through accurate AI-generated metadata.",
        ],
        "tech": ["Python", "FastAPI", "React", "Material UI", "AWS S3", "GPT-4o", "Gemini 1.5", "Ollama", "Email Services", "Microfrontend"],
        "impact": "90% effort reduction · 50% fewer fraudulent charges"
    },
    "sbi": {
        "title": "SBI Test Case Generation Platform",
        "company": "Telemerge",
        "summary": "Generative AI platform automating QA workflows for India's largest bank — State Bank of India.",
        "tags": ["GPT-4.1", "ChromaDB", "PostgreSQL", "FastAPI", "React MUI"],
        "bullets": [
            "Working on a Test Case Generation platform for State Bank of India (SBI), automating QA workflows using Generative AI.",
            "Built a full-stack application using Python FastAPI as backend, React MUI as frontend, and SQLite as database.",
            "Implemented BRD and Solution Document processing by ingesting PDF/DOCX files and converting pages into images for selective test case generation.",
            "Implemented Retrieval Augmented Generation (RAG) utilizing Postgres and Chroma as vector databases for enhanced context retrieval.",
            "Designed pipelines to extract OCR text and image descriptions from document pages to form complete contextual inputs for GPT-4.1 based test case generation.",
            "Implemented environment-specific prompting logic (SIT/UAT) to dynamically generate relevant test cases.",
            "Developed secure user registration with password hashing and JWT-based authentication for session management.",
        ],
        "tech": ["GPT-4.1", "Python", "FastAPI", "React MUI", "PostgreSQL", "ChromaDB", "SQLite", "JWT", "OCR", "RAG"],
        "impact": "Automated QA for India's largest bank"
    },
    "facial": {
        "title": "Real-time Facial Analysis System",
        "company": "Personal Project",
        "summary": "Computer vision app with emotion recognition, drowsiness detection, and 3D head pose estimation.",
        "tags": ["Python", "OpenCV", "MediaPipe", "Computer Vision"],
        "bullets": [
            "Developed a comprehensive computer vision application using Python, OpenCV, and MediaPipe for multi-dimensional facial analysis in real-time.",
            "Incorporated emotion recognition, attention monitoring, drowsiness detection using Eye Aspect Ratio (EAR) algorithm.",
            "Implemented 3D head pose estimation using solvePnP with facial landmark detection.",
            "Visualized all metrics on a real-time analytics dashboard.",
        ],
        "tech": ["Python", "OpenCV", "MediaPipe", "solvePnP", "Computer Vision"],
        "impact": "Real-time multi-metric analysis"
    },
    "pocs": {
        "title": "AI Proof of Concepts (6 POCs)",
        "company": "LearningMate",
        "summary": "Six independent AI experiments spanning vision, audio, evaluation, and multimodal understanding.",
        "tags": ["GPT-4o", "DALL-E", "Gemini", "Multimodal"],
        "bullets": [
            "Image Metadata Generation: Utilized gpt-4-vision-preview, gpt-4o, and gemini-1.5-flash to automatically generate descriptive metadata for images.",
            "Audio/Video Description & Summarization: Created a tool using gpt-4o to generate concise summaries from audio and video content.",
            "AI Evaluation Tool: Built an evaluation framework using gpt-3.5-turbo to assess student responses against correct answers for automated grading.",
            "Text-to-Image Generator: Developed a generator using DALL-E model to create images from textual descriptions.",
            "Multimodal Summarization Tool: Engineered a solution to summarize content from combinations of text, image, audio, and video media.",
        ],
        "tech": ["GPT-4o", "GPT-3.5-turbo", "DALL-E", "Gemini 1.5 Flash", "gpt-4-vision-preview", "Python"],
        "impact": "6 shipped POCs · Cross-functional impact"
    },
}

LM_PROJ_KEYS = ["alttext", "lcap", "pocs"]
TM_PROJ_KEYS = ["sbi"]
ALL_PROJ_KEYS = ["sbi", "alttext", "lcap", "facial", "pocs"]

# ─────────────────── NAV BAR ────────────────────────────────────────

pages = ["home", "about", "experience", "projects", "skills", "contact"]
labels = {"home": "Home", "about": "About", "experience": "Experience", "projects": "Projects", "skills": "Skills", "contact": "Contact"}

st.markdown('<div class="topnav"><div class="nav-logo">Anand<em>.</em></div><div class="nav-menu" id="navmenu"></div></div>', unsafe_allow_html=True)

nav_cols = st.columns(len(pages) + 2)
with nav_cols[0]:
    pass  # spacer
for i, p in enumerate(pages):
    with nav_cols[i + 1]:
        active_cls = "active" if st.session_state.page == p else ""
        if st.button(labels[p], key=f"nav_{p}"):
            nav(p)
            st.rerun()

st.markdown("<style>.stButton{display:inline;} .stButton>button{padding:8px 18px!important;border-radius:8px!important;font-size:14px!important;font-weight:500!important;color:#555!important;cursor:pointer!important;transition:all 0.2s!important;background:none!important;border:none!important;}</style>", unsafe_allow_html=True)

# ─────────────────── PAGES ──────────────────────────────────────────

page = st.session_state.page

# ══════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════
if page == "home":
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-label">Full-Stack AI Engineer · Mumbai</div>
        <h1 class="hero-name">Hi, I'm<br>Anand<em>.</em></h1>
        <p class="hero-sub">
            I build <strong>production-grade AI systems</strong> — from LLM pipelines and RAG architectures
            to full-stack applications that solve real problems at scale.
            Currently at <strong>Telemerge</strong>, previously at <strong>LearningMate</strong>.
        </p>
        <div class="hero-chips">
            <span class="chip">🤖 Generative AI</span>
            <span class="chip">⚙️ Python · FastAPI</span>
            <span class="chip">⚛️ React · MUI</span>
            <span class="chip">☁️ AWS · Azure</span>
            <span class="chip">🗄️ RAG · Vector DBs</span>
        </div>
        <div class="hero-ctas">
            <a class="cta-main" href="mailto:anandsant1212@gmail.com">Get in touch</a>
            <a class="cta-sec" href="https://linkedin.com/in/anandsant1212" target="_blank">LinkedIn ↗</a>
        </div>

        <div class="stats-row">
            <div class="stat-box">
                <div class="stat-num">2.5</div>
                <div class="stat-lbl">Years experience</div>
            </div>
            <div class="stat-box">
                <div class="stat-num">90%</div>
                <div class="stat-lbl">Manual effort reduced</div>
            </div>
            <div class="stat-box">
                <div class="stat-num">75%</div>
                <div class="stat-lbl">Faster doc processing</div>
            </div>
            <div class="stat-box">
                <div class="stat-num">6+</div>
                <div class="stat-lbl">AI POCs shipped</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# ABOUT
# ══════════════════════════════════════════════════════════════
elif page == "about":
    st.markdown("""
    <div class="page-wrap">
        <div class="page-heading">About <em>Me</em></div>
        <p class="page-sub">Beyond the code — the person, the passions, the journey.</p>

        <div class="about-grid">
            <div class="about-card">
                <h3>Origin</h3>
                <p>
                    Born and raised in <strong>Daryapur, Amravati, Maharashtra</strong> — a small town that taught
                    me resilience, curiosity, and the value of working hard for what you want.
                    Now based in <strong>Mumbai</strong>, chasing big ideas in AI and software.
                </p>
            </div>
            <div class="about-card">
                <h3>Who I Am</h3>
                <p>
                    AI engineer by profession, athlete by passion. I believe the discipline from sport
                    directly feeds into how I approach engineering — patience, precision, and never settling for "good enough."
                </p>
            </div>
            <div class="about-card">
                <h3>Sport & Outdoors</h3>
                <div class="interest-grid">
                    <span class="interest-tag">🏀 Basketball (District level)</span>
                    <span class="interest-tag">🏹 Archery (District · 3rd Rank)</span>
                    <span class="interest-tag">🏏 Cricket</span>
                    <span class="interest-tag">🥾 Trekking</span>
                    <span class="interest-tag">✈️ Travel</span>
                    <span class="interest-tag">💪 Gym</span>
                </div>
            </div>
            <div class="about-card">
                <h3>Life Outside Work</h3>
                <div class="interest-grid">
                    <span class="interest-tag">🏍️ Royal Enfield Hunter 350</span>
                    <span class="interest-tag">💡 Fog lights enthusiast</span>
                    <span class="interest-tag">🚗 Cars & Bikes</span>
                    <span class="interest-tag">🍜 Anime</span>
                    <span class="interest-tag">🍽️ Food explorer</span>
                    <span class="interest-tag">🥗 Home cook</span>
                </div>
            </div>
        </div>

        <div class="about-card" style="margin-bottom:32px;">
            <h3>In My Own Words</h3>
            <p style="font-size:16px;line-height:1.8;">
                I'm the kind of person who mounts fog lights on their Hunter 350 because details matter —
                the same philosophy I bring to engineering. I love eating out and exploring food,
                but I cook my own lunch and dinner every day to stay disciplined with calories (gym is non-negotiable 🏋️).
                I watch anime to decompress, trek to reset, and ride to feel free.
                District-level basketball and a 3rd-rank finish in archery taught me that consistency beats talent —
                a lesson I carry into every sprint and every system I build.
            </p>
        </div>

        <div class="about-card">
            <h3>Education Path</h3>
            <div class="journey-line">
                <div class="jitem">
                    <div class="jdot filled"></div>
                    <div class="jyear">2016 – 2018</div>
                    <div class="jcard">
                        <h3>Govt. Agarkar College, Akola</h3>
                        <div class="jrole">Higher Secondary · Science</div>
                        <p>Where curiosity for science began — the foundation of everything.</p>
                    </div>
                </div>
                <div class="jitem">
                    <div class="jdot filled"></div>
                    <div class="jyear">2018 – 2022</div>
                    <div class="jcard">
                        <h3>KK Wagh Institute, Nashik</h3>
                        <div class="jrole">Bachelor of Engineering</div>
                        <p>Four years of CS fundamentals, first Python programs, and the realization that software could change everything.</p>
                    </div>
                </div>
                <div class="jitem">
                    <div class="jdot filled"></div>
                    <div class="jyear">Mar – Nov 2023</div>
                    <div class="jcard">
                        <h3>CDAC</h3>
                        <div class="jrole">PG Diploma · Big Data Analytics</div>
                        <p>The deliberate pivot into AI and data. Eight intense months that launched the trajectory into Generative AI.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# EXPERIENCE
# ══════════════════════════════════════════════════════════════
elif page == "experience":
    st.markdown("""
    <div class="page-wrap">
        <div class="page-heading"><em>Experience</em></div>
        <p class="page-sub">2 years 5 months · 2 companies · real-world AI at scale.</p>
    """, unsafe_allow_html=True)

    # Tab buttons
    col1, col2, col3 = st.columns([2, 2, 6])
    with col1:
        tm_active = "active" if st.session_state.exp_tab == "telemerge" else ""
        if st.button("⚡ Telemerge", key="tab_tm"):
            st.session_state.exp_tab = "telemerge"
            st.rerun()
    with col2:
        lm_active = "active" if st.session_state.exp_tab == "learningmate" else ""
        if st.button("🎓 LearningMate", key="tab_lm"):
            st.session_state.exp_tab = "learningmate"
            st.rerun()

    if st.session_state.exp_tab == "telemerge":
        st.markdown("""
        <div class="exp-company">
            <div class="exp-header">
                <div>
                    <div class="exp-org">Telemerge</div>
                    <div class="exp-role">Software Engineer</div>
                </div>
                <div class="exp-period">Oct 2025 – Present</div>
            </div>
            <ul class="exp-bullets">
                <li>Working on a Test Case Generation platform for <strong>State Bank of India (SBI)</strong>, automating QA workflows using Generative AI.</li>
                <li>Built a full-stack application using <strong>Python FastAPI</strong> as backend, <strong>React MUI</strong> as frontend, and SQLite as database.</li>
                <li>Implemented BRD and Solution Document processing by ingesting PDF/DOCX files and converting pages into images for selective test case generation.</li>
                <li>Implemented <strong>Retrieval Augmented Generation (RAG)</strong> utilizing Postgres and Chroma as vector databases for enhanced context retrieval.</li>
                <li>Designed pipelines to extract OCR text and image descriptions from document pages to form complete contextual inputs for <strong>GPT-4.1</strong> based test case generation.</li>
                <li>Implemented environment-specific prompting logic (SIT/UAT) to dynamically generate relevant test cases.</li>
                <li>Developed secure user registration with <strong>password hashing and JWT-based authentication</strong> for session management.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='font-size:14px;color:#888;font-weight:600;margin-bottom:12px;padding:0 0 4px;'>Projects at Telemerge</div>", unsafe_allow_html=True)
        for key in TM_PROJ_KEYS:
            p = PROJECTS[key]
            if st.button(f"**{p['title']}** — {p['summary']}", key=f"proj_{key}_exp"):
                st.session_state.proj_open = key
                st.session_state.page = "projects"
                st.rerun()

    else:
        st.markdown("""
        <div class="exp-company">
            <div class="exp-header">
                <div>
                    <div class="exp-org">LearningMate Solutions</div>
                    <div class="exp-role">Associate Software Developer</div>
                </div>
                <div class="exp-period">Dec 2023 – Sep 2025</div>
            </div>
            <ul class="exp-bullets">
                <li>Delivered an AI-powered alt text generation platform, enhancing accessibility and SEO; integrated across multiple pipelines, <strong>reducing fraudulent charges by 50%</strong>.</li>
                <li>Built a full-stack solution using FastAPI and React MUI, enabling seamless interaction with multimodal AI models like <strong>GPT-4o and Gemini 1.5</strong>.</li>
                <li>Increased team productivity by setting up scalable React-based internal tool frameworks, improving onboarding speed.</li>
                <li>Accelerated innovation by leading POCs in image processing, gamification, and automation.</li>
                <li>Reduced manual effort in alt text generation by <strong>90%</strong>, using AI-based vision models for OCR, classification, and keyword extraction.</li>
                <li>Automated document analysis for California CCEE, transforming LCAP documents into structured KPIs.</li>
                <li>Reduced document processing time by <strong>75%</strong> through AI pipelines and human-in-the-loop validation.</li>
                <li>Streamlined data delivery via S3 and standardized JSON, enabling efficient analytics for education stakeholders.</li>
            </ul>
            <div class="award-badge">🏆 SPOT Award — Recognized for initiative, cross-functional ownership, and impactful delivery in backend and AI systems.</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='font-size:14px;color:#888;font-weight:600;margin-bottom:12px;'>Projects at LearningMate</div>", unsafe_allow_html=True)
        for key in LM_PROJ_KEYS:
            p = PROJECTS[key]
            if st.button(f"**{p['title']}** — {p['summary']}", key=f"proj_{key}_exp"):
                st.session_state.proj_open = key
                st.session_state.page = "projects"
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PROJECTS
# ══════════════════════════════════════════════════════════════
elif page == "projects":

    if st.session_state.proj_open:
        p = PROJECTS[st.session_state.proj_open]
        st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

        if st.button("← Back to Projects", key="back_proj"):
            st.session_state.proj_open = None
            st.rerun()

        tags_html = "".join(f'<span class="tech-item">{t}</span>' for t in p["tech"])
        bullets_html = "".join(f"<li>{b}</li>" for b in p["bullets"])

        st.markdown(f"""
        <div class="proj-detail">
            <div class="detail-title">{p['title']}</div>
            <div class="detail-company">{p['company']} · {p.get('impact','')}</div>
            <div class="detail-section">
                <h4>What I built</h4>
                <ul class="detail-bullets">{bullets_html}</ul>
            </div>
            <div class="detail-section">
                <h4>Tech Stack</h4>
                <div class="tech-stack">{tags_html}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="page-wrap">
            <div class="page-heading"><em>Projects</em></div>
            <p class="page-sub">Click any card to see the full breakdown.</p>
        """, unsafe_allow_html=True)

        keys = ALL_PROJ_KEYS
        # render in rows of 2
        for i in range(0, len(keys), 2):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if i + j < len(keys):
                    key = keys[i + j]
                    p = PROJECTS[key]
                    tags_html = "".join(f'<span class="proj-tag">{t}</span>' for t in p["tags"])
                    with col:
                        st.markdown(f"""
                        <div class="proj-card" style="cursor:pointer;">
                            <div class="proj-company-tag">{p['company']}</div>
                            <div class="proj-title">{p['title']}</div>
                            <div class="proj-summary">{p['summary']}</div>
                            <div class="proj-tags">{tags_html}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        if st.button("Open →", key=f"open_{key}"):
                            st.session_state.proj_open = key
                            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════════════════════
elif page == "skills":
    st.markdown("""
    <div class="page-wrap">
        <div class="page-heading"><em>Skills</em></div>
        <p class="page-sub">Everything I work with, day in and day out.</p>

        <div class="skill-group">
            <div class="skill-group-title">AI / Generative AI</div>
            <div class="skill-pills">
                <span class="skill-pill">LLMs</span>
                <span class="skill-pill">RAG</span>
                <span class="skill-pill">GPT-4o / 4.1</span>
                <span class="skill-pill">Gemini 1.5</span>
                <span class="skill-pill">Azure OpenAI</span>
                <span class="skill-pill">DALL-E</span>
                <span class="skill-pill">ChromaDB</span>
                <span class="skill-pill">Vector Databases</span>
                <span class="skill-pill">OCR</span>
                <span class="skill-pill">Prompt Engineering</span>
            </div>
        </div>

        <div class="skill-group">
            <div class="skill-group-title">Backend</div>
            <div class="skill-pills">
                <span class="skill-pill">Python</span>
                <span class="skill-pill">FastAPI</span>
                <span class="skill-pill">REST APIs</span>
                <span class="skill-pill">System Design</span>
                <span class="skill-pill">JWT Authentication</span>
                <span class="skill-pill">Password Hashing</span>
                <span class="skill-pill">Microservices</span>
            </div>
        </div>

        <div class="skill-group">
            <div class="skill-group-title">Frontend</div>
            <div class="skill-pills">
                <span class="skill-pill">React JS</span>
                <span class="skill-pill">React MUI</span>
                <span class="skill-pill">Streamlit</span>
                <span class="skill-pill">Microfrontend Architecture</span>
            </div>
        </div>

        <div class="skill-group">
            <div class="skill-group-title">Databases</div>
            <div class="skill-pills">
                <span class="skill-pill">PostgreSQL</span>
                <span class="skill-pill">MongoDB Atlas</span>
                <span class="skill-pill">MySQL</span>
                <span class="skill-pill">SQLite</span>
                <span class="skill-pill">Chroma</span>
            </div>
        </div>

        <div class="skill-group">
            <div class="skill-group-title">Cloud & DevOps</div>
            <div class="skill-pills">
                <span class="skill-pill">AWS S3</span>
                <span class="skill-pill">Azure</span>
                <span class="skill-pill">Docker</span>
                <span class="skill-pill">Kubernetes</span>
                <span class="skill-pill">Cloud Architecture</span>
                <span class="skill-pill">Scalability</span>
            </div>
        </div>

        <div class="skill-group">
            <div class="skill-group-title">Tools</div>
            <div class="skill-pills">
                <span class="skill-pill">Git</span>
                <span class="skill-pill">Bitbucket</span>
                <span class="skill-pill">GitHub Copilot</span>
                <span class="skill-pill">OpenCV</span>
                <span class="skill-pill">MediaPipe</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════
elif page == "contact":
    st.markdown("""
    <div class="page-wrap">
        <div class="page-heading">Let's <em>Talk</em></div>
        <p class="page-sub">Open to full-time AI engineering roles, freelance projects, and interesting conversations.</p>

        <div class="contact-grid">
            <a class="contact-card" href="mailto:anandsant1212@gmail.com">
                <div class="contact-icon">✉️</div>
                <div>
                    <div class="contact-label">Email</div>
                    <div class="contact-value">anandsant1212@gmail.com</div>
                </div>
            </a>
            <a class="contact-card" href="https://linkedin.com/in/anandsant1212" target="_blank">
                <div class="contact-icon">💼</div>
                <div>
                    <div class="contact-label">LinkedIn</div>
                    <div class="contact-value">linkedin.com/in/anandsant1212</div>
                </div>
            </a>
            <a class="contact-card" href="tel:+919423586586">
                <div class="contact-icon">📞</div>
                <div>
                    <div class="contact-label">Phone</div>
                    <div class="contact-value">+91 94235 86586</div>
                </div>
            </a>
            <div class="contact-card">
                <div class="contact-icon">📍</div>
                <div>
                    <div class="contact-label">Location</div>
                    <div class="contact-value">Mumbai, Maharashtra, India</div>
                </div>
            </div>
        </div>

        <div class="about-card" style="margin-top:32px;text-align:center;">
            <h3 style="text-align:center;">Currently at</h3>
            <p style="font-size:18px;font-weight:600;color:#1a1a1a;margin-top:8px;">Telemerge · Software Engineer</p>
            <p style="margin-top:6px;">Building AI-powered QA automation for State Bank of India · Oct 2025 – Present</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
