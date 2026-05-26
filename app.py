import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Anand Sant | AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "home"
if "exp_tab" not in st.session_state:
    st.session_state.exp_tab = "telemerge"
if "proj_open" not in st.session_state:
    st.session_state.proj_open = None

# Hide streamlit chrome
st.markdown("""
<style>
#MainMenu, footer, header, [data-testid="stToolbar"] { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }
.stApp { background: #f5f3ef; }
/* nav button row */
div[data-testid="stHorizontalBlock"] .stButton > button {
    background: none !important;
    border: 1px solid #d4d0c9 !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #444 !important;
    padding: 6px 14px !important;
    width: 100% !important;
    transition: all 0.2s !important;
    box-shadow: none !important;
}
div[data-testid="stHorizontalBlock"] .stButton > button:hover {
    background: #1a1a1a !important;
    color: #f5f3ef !important;
    border-color: #1a1a1a !important;
}
</style>
""", unsafe_allow_html=True)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&family=Playfair+Display:wght@700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#f5f3ef;color:#1a1a1a;font-family:'DM Sans',sans-serif;}
a{text-decoration:none;color:inherit;}

/* NAV STRIP */
.topbar{background:#f5f3ef;border-bottom:1px solid #e0ddd8;padding:14px 48px;display:flex;align-items:center;justify-content:space-between;}
.logo{font-family:'Playfair Display',serif;font-size:22px;font-weight:900;color:#1a1a1a;}
.logo em{color:#c84b31;font-style:normal;}

/* PAGE */
.wrap{max-width:860px;margin:0 auto;padding:48px 24px 72px;}

/* HERO */
.hero-label{display:inline-flex;align-items:center;gap:10px;font-family:'JetBrains Mono',monospace;font-size:11px;color:#c84b31;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:20px;}
.hero-label::before{content:'';width:20px;height:1px;background:#c84b31;}
.hero-name{font-family:'Playfair Display',serif;font-size:clamp(56px,9vw,100px);font-weight:900;line-height:1.0;letter-spacing:-0.03em;color:#1a1a1a;margin-bottom:22px;}
.hero-name em{color:#c84b31;font-style:normal;}
.hero-sub{font-size:18px;color:#666;line-height:1.7;max-width:560px;margin-bottom:32px;}
.hero-sub strong{color:#1a1a1a;font-weight:600;}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:36px;}
.chip{padding:7px 15px;border-radius:999px;border:1px solid #d4d0c9;background:white;font-size:13px;color:#555;font-weight:500;}
.ctas{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:60px;}
.btn-main{padding:13px 28px;border-radius:10px;background:#1a1a1a;color:#f5f3ef;font-size:15px;font-weight:600;transition:background 0.2s;}
.btn-main:hover{background:#c84b31;}
.btn-sec{padding:13px 28px;border-radius:10px;background:white;color:#1a1a1a;font-size:15px;font-weight:600;border:1px solid #d4d0c9;transition:border-color 0.2s;}
.btn-sec:hover{border-color:#1a1a1a;}

/* STATS */
.stats{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid #e0ddd8;border-radius:14px;overflow:hidden;background:#e0ddd8;gap:1px;}
.stat{background:white;padding:24px 16px;text-align:center;}
.stat-n{font-family:'Playfair Display',serif;font-size:38px;font-weight:900;color:#c84b31;line-height:1;}
.stat-l{font-size:12px;color:#999;margin-top:5px;line-height:1.3;}

/* PAGE HEADING */
.ph{font-family:'Playfair Display',serif;font-size:clamp(40px,6vw,64px);font-weight:900;letter-spacing:-0.03em;color:#1a1a1a;margin-bottom:6px;line-height:1.05;}
.ph em{color:#c84b31;font-style:normal;}
.ps{font-size:15px;color:#999;margin-bottom:40px;}

/* CARDS */
.card{background:white;border:1px solid #e0ddd8;border-radius:14px;padding:28px;}
.card+.card{margin-top:16px;}
.card h3{font-size:12px;text-transform:uppercase;letter-spacing:0.1em;color:#bbb;margin-bottom:12px;font-family:'JetBrains Mono',monospace;}
.card p{font-size:15px;color:#555;line-height:1.75;}
.card strong{color:#1a1a1a;}

/* ABOUT GRID */
.ag{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;}
.ig{display:flex;flex-wrap:wrap;gap:7px;}
.itag{padding:6px 13px;border-radius:999px;background:#f5f3ef;border:1px solid #e0ddd8;font-size:13px;color:#555;}

/* TIMELINE */
.tl{position:relative;padding-left:28px;margin-top:4px;}
.tl::before{content:'';position:absolute;left:6px;top:0;bottom:0;width:1px;background:#e0ddd8;}
.ti{position:relative;margin-bottom:24px;}
.ti:last-child{margin-bottom:0;}
.tdot{position:absolute;left:-25px;top:5px;width:13px;height:13px;border-radius:50%;border:2px solid #c84b31;background:white;}
.tdot.f{background:#c84b31;}
.ty{font-family:'JetBrains Mono',monospace;font-size:10px;color:#bbb;margin-bottom:5px;letter-spacing:0.06em;}
.tc{background:#f9f8f6;border:1px solid #e8e5e0;border-radius:10px;padding:16px 20px;}
.tc h4{font-size:15px;font-weight:700;color:#1a1a1a;margin-bottom:3px;}
.tc .role{font-size:13px;color:#c84b31;font-weight:600;margin-bottom:6px;}
.tc p{font-size:13px;color:#888;line-height:1.6;}

/* EXP */
.exp-hdr{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px;}
.exp-org{font-family:'Playfair Display',serif;font-size:26px;font-weight:900;color:#1a1a1a;}
.exp-period{font-family:'JetBrains Mono',monospace;font-size:11px;color:#aaa;padding-top:5px;}
.exp-role{font-size:14px;color:#c84b31;font-weight:600;margin-bottom:18px;}
.bullets{list-style:none;padding:0;}
.bullets li{font-size:14px;color:#555;line-height:1.65;padding:7px 0 7px 18px;position:relative;border-bottom:1px solid #f5f3ef;}
.bullets li:last-child{border:none;}
.bullets li::before{content:'→';position:absolute;left:0;color:#c84b31;font-size:11px;top:9px;}
.bullets li strong{color:#1a1a1a;}
.award{display:inline-flex;align-items:center;gap:8px;background:#fff8f0;border:1px solid #ffd090;border-radius:8px;padding:10px 16px;font-size:13px;color:#b06000;margin-top:16px;font-weight:500;}
.sec-label{font-size:12px;text-transform:uppercase;letter-spacing:0.08em;color:#aaa;font-family:'JetBrains Mono',monospace;margin:24px 0 12px;font-weight:500;}
.proj-link{display:flex;align-items:center;justify-content:space-between;background:#f9f8f6;border:1px solid #e8e5e0;border-radius:10px;padding:14px 18px;margin-bottom:8px;cursor:pointer;transition:all 0.2s;}
.proj-link:hover{border-color:#c84b31;background:white;}
.proj-link-title{font-size:14px;font-weight:600;color:#1a1a1a;}
.proj-link-sub{font-size:12px;color:#aaa;margin-top:2px;}
.proj-link-arr{color:#c84b31;font-size:18px;}

/* PROJECTS GRID */
.pg{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.pc{background:white;border:1px solid #e0ddd8;border-radius:14px;padding:24px;transition:all 0.2s;position:relative;}
.pc:hover{border-color:#c84b31;transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,0.06);}
.pc-co{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:0.1em;color:#c84b31;margin-bottom:8px;}
.pc-title{font-family:'Playfair Display',serif;font-size:18px;font-weight:800;color:#1a1a1a;margin-bottom:8px;line-height:1.2;}
.pc-sum{font-size:13px;color:#999;line-height:1.6;margin-bottom:14px;}
.pc-tags{display:flex;flex-wrap:wrap;gap:5px;}
.pc-tag{font-size:10px;font-family:'JetBrains Mono',monospace;background:#f5f3ef;border:1px solid #e0ddd8;color:#777;border-radius:5px;padding:3px 8px;}
.open-btn{display:inline-flex;align-items:center;gap:5px;margin-top:14px;font-size:12px;color:#c84b31;font-weight:600;font-family:'JetBrains Mono',monospace;}

/* DETAIL */
.detail-title{font-family:'Playfair Display',serif;font-size:30px;font-weight:900;margin-bottom:4px;line-height:1.2;}
.detail-co{font-size:13px;color:#c84b31;font-weight:600;margin-bottom:24px;font-family:'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:0.06em;}
.ds h4{font-size:11px;text-transform:uppercase;letter-spacing:0.1em;color:#bbb;font-family:'JetBrains Mono',monospace;margin-bottom:10px;}
.ds{margin-bottom:24px;}
.dbugs{list-style:none;padding:0;}
.dbugs li{font-size:14px;color:#555;line-height:1.7;padding:6px 0 6px 18px;position:relative;border-bottom:1px solid #f9f8f6;}
.dbugs li:last-child{border:none;}
.dbugs li::before{content:'→';position:absolute;left:0;color:#c84b31;font-size:11px;top:8px;}
.dbugs li strong{color:#1a1a1a;}
.tech-row{display:flex;flex-wrap:wrap;gap:8px;}
.tech-item{padding:7px 14px;border-radius:8px;background:#f5f3ef;border:1px solid #e0ddd8;font-size:13px;color:#555;font-weight:500;}
.back-link{display:inline-flex;align-items:center;gap:6px;font-size:13px;color:#aaa;cursor:pointer;margin-bottom:24px;font-family:'JetBrains Mono',monospace;background:none;border:none;}
.back-link:hover{color:#c84b31;}

/* SKILLS */
.sg{margin-bottom:28px;}
.sg-t{font-size:11px;font-family:'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:0.12em;color:#bbb;margin-bottom:10px;}
.sp{display:flex;flex-wrap:wrap;gap:8px;}
.spill{padding:9px 18px;border-radius:999px;border:1px solid #d4d0c9;background:white;font-size:14px;color:#444;font-weight:500;transition:all 0.2s;}
.spill:hover{border-color:#c84b31;color:#c84b31;}

/* CONTACT */
.cg{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.cc{background:white;border:1px solid #e0ddd8;border-radius:14px;padding:24px;display:flex;align-items:center;gap:16px;transition:all 0.2s;}
.cc:hover{border-color:#c84b31;transform:translateY(-2px);}
.cc-icon{font-size:26px;}
.cc-lbl{font-size:11px;color:#bbb;text-transform:uppercase;letter-spacing:0.08em;font-family:'JetBrains Mono',monospace;}
.cc-val{font-size:14px;color:#1a1a1a;font-weight:600;margin-top:3px;}

@media(max-width:680px){
  .stats{grid-template-columns:1fr 1fr;}
  .ag,.pg,.cg{grid-template-columns:1fr;}
  .topbar{padding:14px 16px;}
  .wrap{padding:32px 16px 60px;}
}
"""

PROJECTS = {
    "lcap": {
        "title": "LCAP Data Extraction & Analytics",
        "company": "LearningMate",
        "summary": "AI pipeline transforming California educational policy documents into structured KPIs.",
        "tags": ["Azure OpenAI", "RAG", "Kubernetes", "MongoDB", "AWS S3"],
        "bullets": [
            "Developed an AI-powered data extraction platform for <strong>California CCEE</strong> to automate processing of Local Control Accountability Plan (LCAP) documents.",
            "Implemented complete pipeline from document ingestion and intelligent KPI extraction to final delivery, featuring a <strong>human-in-the-loop approval workflow</strong>.",
            "Reduced document processing time by <strong>75%</strong> through AI pipelines and human-in-the-loop validation.",
            "Enabled seamless integration with client infrastructure via standardized JSON outputs to <strong>S3 for Snowflake ingestion</strong>.",
            "Streamlined data delivery allowing stakeholders to effectively monitor and enhance educational outcomes.",
        ],
        "tech": ["Azure OpenAI", "Vector Databases", "Kubernetes", "MongoDB Atlas", "AWS S3", "RAG", "OCR", "Python", "FastAPI"],
        "impact": "75% faster processing"
    },
    "alttext": {
        "title": "AI Alt Text Generation Platform",
        "company": "LearningMate",
        "summary": "End-to-end accessibility platform automating image descriptions across multiple client pipelines.",
        "tags": ["GPT-4o", "Gemini 1.5", "FastAPI", "React MUI", "AWS S3"],
        "bullets": [
            "Delivered an AI-powered alt text platform, now <strong>integrated across multiple pipelines and client environments</strong>, reducing fraudulent charges by 50%.",
            "Reduced manual effort in alt text generation by <strong>90%</strong> using AI-based vision models for OCR, classification, and keyword extraction.",
            "Built full-stack solution using <strong>FastAPI and React MUI</strong> for seamless interaction with multimodal AI models.",
            "Features microservice architecture, cloud storage integration, automated email notifications, and a microfrontend React MUI interface.",
            "Supports multiple input methods — <strong>file uploads, URLs, S3</strong> — with configurable generation parameters.",
        ],
        "tech": ["Python", "FastAPI", "React", "Material UI", "AWS S3", "GPT-4o", "Gemini 1.5", "Ollama", "Email Services", "Microfrontend"],
        "impact": "90% effort reduction · 50% fewer fraudulent charges"
    },
    "sbi": {
        "title": "SBI Test Case Generation Platform",
        "company": "Telemerge",
        "summary": "Generative AI platform automating QA workflows for India's largest bank.",
        "tags": ["GPT-4.1", "ChromaDB", "PostgreSQL", "FastAPI", "React MUI"],
        "bullets": [
            "Building a Test Case Generation platform for <strong>State Bank of India (SBI)</strong>, automating QA workflows using Generative AI.",
            "Built full-stack application using <strong>Python FastAPI</strong> backend, <strong>React MUI</strong> frontend, and SQLite database.",
            "Implemented BRD and Solution Document processing by ingesting PDF/DOCX files and <strong>converting pages into images</strong> for selective test case generation.",
            "Implemented <strong>RAG using Postgres + Chroma</strong> as vector databases for enhanced context retrieval.",
            "Designed OCR pipelines to extract text and image descriptions from document pages as contextual inputs for <strong>GPT-4.1</strong>.",
            "Implemented environment-specific prompting logic <strong>(SIT/UAT)</strong> to dynamically generate relevant test cases.",
            "Developed secure user registration with <strong>password hashing and JWT authentication</strong> for session management.",
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
            "Developed a computer vision application using <strong>Python, OpenCV, and MediaPipe</strong> for multi-dimensional facial analysis in real-time.",
            "Incorporated <strong>emotion recognition, attention monitoring, drowsiness detection</strong> using Eye Aspect Ratio (EAR) algorithm.",
            "Implemented <strong>3D head pose estimation</strong> using solvePnP with facial landmark detection.",
            "Visualized all metrics on a <strong>real-time analytics dashboard</strong>.",
        ],
        "tech": ["Python", "OpenCV", "MediaPipe", "solvePnP", "Computer Vision"],
        "impact": "Real-time multi-metric analysis"
    },
    "pocs": {
        "title": "AI Proof of Concepts (6 POCs)",
        "company": "LearningMate",
        "summary": "Six independent AI experiments — vision, audio, evaluation, and multimodal understanding.",
        "tags": ["GPT-4o", "DALL-E", "Gemini", "Multimodal"],
        "bullets": [
            "<strong>Image Metadata Generation:</strong> Used gpt-4-vision-preview, gpt-4o, and gemini-1.5-flash to automatically generate descriptive metadata for images.",
            "<strong>Audio/Video Summarization:</strong> Created a tool using gpt-4o to generate concise summaries from audio and video content.",
            "<strong>AI Evaluation Tool:</strong> Built an evaluation framework using gpt-3.5-turbo to assess student responses against correct answers for automated grading.",
            "<strong>Text-to-Image Generator:</strong> Developed a generator using DALL-E to create images from textual descriptions.",
            "<strong>Multimodal Summarization:</strong> Engineered a solution to summarize content from combinations of text, image, audio, and video media.",
        ],
        "tech": ["GPT-4o", "GPT-3.5-turbo", "DALL-E", "Gemini 1.5 Flash", "gpt-4-vision-preview", "Python"],
        "impact": "6 shipped POCs"
    },
}

LM_KEYS = ["alttext", "lcap", "pocs"]
TM_KEYS = ["sbi"]
ALL_KEYS = ["sbi", "alttext", "lcap", "facial", "pocs"]

def make_chips(items):
    return "".join(f'<span class="chip">{i}</span>' for i in items)

def make_bullets(items, cls="bullets"):
    return "".join(f"<li>{b}</li>" for b in items)

def make_tech(items):
    return "".join(f'<span class="tech-item">{t}</span>' for t in items)

def make_proj_tags(items):
    return "".join(f'<span class="pc-tag">{t}</span>' for t in items)

def render(html_body, height=900):
    full = f"""<!DOCTYPE html>
<html lang='en'><head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<style>{CSS}</style>
</head><body>{html_body}</body></html>"""
    components.html(full, height=height, scrolling=True)

# ── NAV ─────────────────────────────────────────────────────
st.markdown("""
<div style='background:#f5f3ef;border-bottom:1px solid #e0ddd8;padding:14px 48px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:99;'>
<span style='font-family:Georgia,serif;font-size:21px;font-weight:900;color:#1a1a1a;'>Anand<span style="color:#c84b31;">.</span></span>
</div>
""", unsafe_allow_html=True)

pages = ["home","about","experience","projects","skills","contact"]
labels = {"home":"Home","about":"About","experience":"Experience","projects":"Projects","skills":"Skills","contact":"Contact"}
cols = st.columns(len(pages))
for i,p in enumerate(pages):
    with cols[i]:
        if st.button(labels[p], key=f"nav_{p}"):
            st.session_state.page = p
            st.session_state.proj_open = None
            st.rerun()

st.markdown("<div style='height:4px;background:linear-gradient(90deg,#c84b31,#f5a88a,#f5f3ef);margin-bottom:0;'></div>", unsafe_allow_html=True)

page = st.session_state.page

# ══════════════ HOME ══════════════
if page == "home":
    render(f"""
<div class='wrap'>
  <div class='hero-label'>Full-Stack AI Engineer · Mumbai</div>
  <h1 class='hero-name'>Hi, I'm<br>Anand<em>.</em></h1>
  <p class='hero-sub'>
    I build <strong>production-grade AI systems</strong> — LLM pipelines, RAG architectures,
    and full-stack apps that solve real problems at scale.
    Currently at <strong>Telemerge</strong>, previously at <strong>LearningMate</strong>.
  </p>
  <div class='chips'>
    {make_chips(['🤖 Generative AI','⚙️ Python · FastAPI','⚛️ React · MUI','☁️ AWS · Azure','🗄️ RAG · Vector DBs'])}
  </div>
  <div class='ctas'>
    <a class='btn-main' href='mailto:anandsant1212@gmail.com'>Get in touch</a>
    <a class='btn-sec' href='https://linkedin.com/in/anandsant1212' target='_blank'>LinkedIn ↗</a>
  </div>
  <div class='stats'>
    <div class='stat'><div class='stat-n'>2.5</div><div class='stat-l'>Years experience</div></div>
    <div class='stat'><div class='stat-n'>90%</div><div class='stat-l'>Manual effort reduced</div></div>
    <div class='stat'><div class='stat-n'>75%</div><div class='stat-l'>Faster doc processing</div></div>
    <div class='stat'><div class='stat-n'>6+</div><div class='stat-l'>AI POCs shipped</div></div>
  </div>
</div>
""", height=780)

# ══════════════ ABOUT ══════════════
elif page == "about":
    render(f"""
<div class='wrap'>
  <div class='ph'>About <em>Me</em></div>
  <p class='ps'>Beyond the code — the person, the passions, the journey.</p>

  <div class='ag'>
    <div class='card'>
      <h3>Origin</h3>
      <p>Born and raised in <strong>Daryapur, Amravati, Maharashtra</strong> — a small town that taught me resilience and curiosity. Now based in <strong>Mumbai</strong>, chasing big ideas in AI.</p>
    </div>
    <div class='card'>
      <h3>Who I Am</h3>
      <p>AI engineer by profession, athlete by passion. The discipline from sport feeds directly into how I approach engineering — patience, precision, never settling.</p>
    </div>
    <div class='card'>
      <h3>Sport &amp; Outdoors</h3>
      <div class='ig'>
        <span class='itag'>🏀 Basketball (District)</span>
        <span class='itag'>🏹 Archery (District · 3rd Rank)</span>
        <span class='itag'>🏏 Cricket</span>
        <span class='itag'>🥾 Trekking</span>
        <span class='itag'>✈️ Travel</span>
        <span class='itag'>💪 Gym</span>
      </div>
    </div>
    <div class='card'>
      <h3>Life Outside Work</h3>
      <div class='ig'>
        <span class='itag'>🏍️ Royal Enfield Hunter 350</span>
        <span class='itag'>💡 Fog lights mod</span>
        <span class='itag'>🚗 Cars &amp; Bikes</span>
        <span class='itag'>🍜 Anime</span>
        <span class='itag'>🍽️ Food explorer</span>
        <span class='itag'>🥗 Home cook</span>
      </div>
    </div>
  </div>

  <div class='card' style='margin-bottom:20px;'>
    <h3>In My Own Words</h3>
    <p style='font-size:15px;line-height:1.8;'>
      I'm the kind of person who mounts fog lights on a Hunter 350 because details matter —
      the same philosophy I bring to engineering. I love eating out and exploring food, but cook my own
      lunch and dinner daily to stay disciplined with calories (gym is non-negotiable 🏋️).
      I watch anime to decompress, trek to reset, and ride to feel free.
      District-level basketball and a <strong>3rd-rank finish in archery</strong> taught me that
      consistency beats talent — a lesson I carry into every sprint and every system I build.
    </p>
  </div>

  <div class='card'>
    <h3>Education Path</h3>
    <div class='tl'>
      <div class='ti'>
        <div class='tdot f'></div>
        <div class='ty'>2016 – 2018 · Akola</div>
        <div class='tc'><h4>Govt. Agarkar College, Akola</h4><div class='role'>Higher Secondary · Science</div><p>Where curiosity for science began — the foundation of everything.</p></div>
      </div>
      <div class='ti'>
        <div class='tdot f'></div>
        <div class='ty'>2018 – 2022 · Nashik</div>
        <div class='tc'><h4>KK Wagh Institute of Engineering</h4><div class='role'>Bachelor of Engineering</div><p>Four years of CS fundamentals, first Python programs, and the realization that software can change everything.</p></div>
      </div>
      <div class='ti'>
        <div class='tdot f'></div>
        <div class='ty'>Mar – Nov 2023 · CDAC</div>
        <div class='tc'><h4>CDAC — Centre for Development of Advanced Computing</h4><div class='role'>PG Diploma · Big Data Analytics</div><p>The deliberate pivot into AI. Eight intense months that launched the trajectory into Generative AI.</p></div>
      </div>
    </div>
  </div>
</div>
""", height=1400)

# ══════════════ EXPERIENCE ══════════════
elif page == "experience":
    tab = st.session_state.exp_tab
    c1, c2, c3 = st.columns([2,2,6])
    with c1:
        if st.button("⚡ Telemerge", key="etm"):
            st.session_state.exp_tab = "telemerge"; st.rerun()
    with c2:
        if st.button("🎓 LearningMate", key="elm"):
            st.session_state.exp_tab = "learningmate"; st.rerun()

    if tab == "telemerge":
        proj_links = "".join(f"""
        <div class='proj-link' onclick="window.parent.postMessage({{type:'proj',key:'{k}'}},'*')">
          <div><div class='proj-link-title'>{PROJECTS[k]['title']}</div><div class='proj-link-sub'>{PROJECTS[k]['summary']}</div></div>
          <div class='proj-link-arr'>↗</div>
        </div>""" for k in TM_KEYS)
        render(f"""
<div class='wrap'>
  <div class='ph'><em>Experience</em></div>
  <p class='ps'>2 years 5 months · 2 companies · real-world AI at scale.</p>
  <div class='card'>
    <div class='exp-hdr'>
      <div><div class='exp-org'>Telemerge</div><div class='exp-role'>Software Engineer</div></div>
      <div class='exp-period'>Oct 2025 – Present</div>
    </div>
    <ul class='bullets'>
      <li>Working on a Test Case Generation platform for <strong>State Bank of India (SBI)</strong>, automating QA workflows using Generative AI.</li>
      <li>Built full-stack application using <strong>Python FastAPI</strong> backend, <strong>React MUI</strong> frontend, and SQLite database.</li>
      <li>Implemented BRD and Solution Document processing by ingesting PDF/DOCX files, converting pages to images for selective test case generation.</li>
      <li>Implemented <strong>RAG using Postgres + ChromaDB</strong> as vector databases for enhanced context retrieval.</li>
      <li>Designed OCR pipelines for contextual inputs to <strong>GPT-4.1</strong> based test case generation.</li>
      <li>Implemented environment-specific prompting logic <strong>(SIT/UAT)</strong> to dynamically generate relevant test cases.</li>
      <li>Developed secure user registration with <strong>JWT-based authentication</strong> and password hashing.</li>
    </ul>
  </div>
  <div class='sec-label'>Projects at Telemerge</div>
  {proj_links}
</div>
""", height=820)
    else:
        proj_links = "".join(f"""
        <div class='proj-link' onclick="window.parent.postMessage({{type:'proj',key:'{k}'}},'*')">
          <div><div class='proj-link-title'>{PROJECTS[k]['title']}</div><div class='proj-link-sub'>{PROJECTS[k]['summary']}</div></div>
          <div class='proj-link-arr'>↗</div>
        </div>""" for k in LM_KEYS)
        render(f"""
<div class='wrap'>
  <div class='ph'><em>Experience</em></div>
  <p class='ps'>2 years 5 months · 2 companies · real-world AI at scale.</p>
  <div class='card'>
    <div class='exp-hdr'>
      <div><div class='exp-org'>LearningMate Solutions</div><div class='exp-role'>Associate Software Developer</div></div>
      <div class='exp-period'>Dec 2023 – Sep 2025</div>
    </div>
    <ul class='bullets'>
      <li>Delivered an AI-powered alt text generation platform integrated across multiple pipelines, <strong>reducing fraudulent charges by 50%</strong>.</li>
      <li>Built full-stack solution using <strong>FastAPI and React MUI</strong> with multimodal AI models like GPT-4o and Gemini 1.5.</li>
      <li>Increased team productivity by setting up scalable React-based internal tool frameworks, improving onboarding speed.</li>
      <li>Led POCs in image processing, gamification, and automation — fostering rapid cross-functional experimentation.</li>
      <li>Reduced manual effort in alt text generation by <strong>90%</strong> using AI-based vision models for OCR, classification, and keyword extraction.</li>
      <li>Automated document analysis for <strong>California CCEE</strong>, transforming LCAP documents into structured KPIs.</li>
      <li>Reduced document processing time by <strong>75%</strong> through AI pipelines and human-in-the-loop validation.</li>
      <li>Streamlined data delivery via S3 and standardized JSON for Snowflake ingestion.</li>
    </ul>
    <div class='award'>🏆 SPOT Award — Recognized for initiative, cross-functional ownership, and impactful delivery.</div>
  </div>
  <div class='sec-label'>Projects at LearningMate</div>
  {proj_links}
</div>
""", height=960)

# ══════════════ PROJECTS ══════════════
elif page == "projects":
    if st.session_state.proj_open:
        k = st.session_state.proj_open
        p = PROJECTS[k]
        if st.button("← Back to Projects", key="back"):
            st.session_state.proj_open = None; st.rerun()
        bullets = "".join(f"<li>{b}</li>" for b in p["bullets"])
        render(f"""
<div class='wrap'>
  <div class='detail-title'>{p['title']}</div>
  <div class='detail-co'>{p['company']} · {p['impact']}</div>
  <div class='ds'><h4>What I Built</h4><ul class='dbugs'>{bullets}</ul></div>
  <div class='ds'><h4>Tech Stack</h4><div class='tech-row'>{make_tech(p['tech'])}</div></div>
</div>
""", height=800)
    else:
        # Check for project key passed via query or button
        rows = [ALL_KEYS[i:i+2] for i in range(0, len(ALL_KEYS), 2)]
        cards_html = ""
        for row in rows:
            cards_html += "<div style='display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;'>"
            for k in row:
                p = PROJECTS[k]
                tags = "".join(f'<span class="pc-tag">{t}</span>' for t in p["tags"])
                cards_html += f"""
                <div class='pc'>
                  <div class='pc-co'>{p['company']}</div>
                  <div class='pc-title'>{p['title']}</div>
                  <div class='pc-sum'>{p['summary']}</div>
                  <div class='pc-tags'>{tags}</div>
                </div>"""
            cards_html += "</div>"

        render(f"""
<div class='wrap'>
  <div class='ph'><em>Projects</em></div>
  <p class='ps'>Select a project below to see the full breakdown.</p>
  {cards_html}
</div>
""", height=900)
        # Buttons below for opening projects
        st.markdown("<div style='max-width:860px;margin:0 auto;padding:0 24px;'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:13px;color:#aaa;font-family:monospace;margin-bottom:8px;'>OPEN PROJECT →</p>", unsafe_allow_html=True)
        btn_cols = st.columns(len(ALL_KEYS))
        for i, k in enumerate(ALL_KEYS):
            with btn_cols[i]:
                if st.button(PROJECTS[k]["title"][:18]+"…", key=f"open_{k}"):
                    st.session_state.proj_open = k; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ══════════════ SKILLS ══════════════
elif page == "skills":
    render(f"""
<div class='wrap'>
  <div class='ph'><em>Skills</em></div>
  <p class='ps'>Everything I work with, day in and day out.</p>
  <div class='sg'><div class='sg-t'>AI / Generative AI</div><div class='sp'>
    {''.join(f"<span class='spill'>{s}</span>" for s in ['LLMs','RAG','GPT-4o / 4.1','Gemini 1.5','Azure OpenAI','DALL-E','ChromaDB','Vector Databases','OCR','Prompt Engineering'])}
  </div></div>
  <div class='sg'><div class='sg-t'>Backend</div><div class='sp'>
    {''.join(f"<span class='spill'>{s}</span>" for s in ['Python','FastAPI','REST APIs','System Design','JWT Authentication','Microservices'])}
  </div></div>
  <div class='sg'><div class='sg-t'>Frontend</div><div class='sp'>
    {''.join(f"<span class='spill'>{s}</span>" for s in ['React JS','React MUI','Streamlit','Microfrontend Architecture'])}
  </div></div>
  <div class='sg'><div class='sg-t'>Databases</div><div class='sp'>
    {''.join(f"<span class='spill'>{s}</span>" for s in ['PostgreSQL','MongoDB Atlas','MySQL','SQLite','ChromaDB'])}
  </div></div>
  <div class='sg'><div class='sg-t'>Cloud & DevOps</div><div class='sp'>
    {''.join(f"<span class='spill'>{s}</span>" for s in ['AWS S3','Azure','Docker','Kubernetes','Cloud Architecture','Scalability'])}
  </div></div>
  <div class='sg'><div class='sg-t'>Tools</div><div class='sp'>
    {''.join(f"<span class='spill'>{s}</span>" for s in ['Git','Bitbucket','GitHub Copilot','OpenCV','MediaPipe'])}
  </div></div>
</div>
""", height=700)

# ══════════════ CONTACT ══════════════
elif page == "contact":
    render(f"""
<div class='wrap'>
  <div class='ph'>Let's <em>Talk</em></div>
  <p class='ps'>Open to full-time AI engineering roles, freelance projects, and interesting conversations.</p>
  <div class='cg'>
    <a class='cc' href='mailto:anandsant1212@gmail.com'>
      <div class='cc-icon'>✉️</div>
      <div><div class='cc-lbl'>Email</div><div class='cc-val'>anandsant1212@gmail.com</div></div>
    </a>
    <a class='cc' href='https://linkedin.com/in/anandsant1212' target='_blank'>
      <div class='cc-icon'>💼</div>
      <div><div class='cc-lbl'>LinkedIn</div><div class='cc-val'>linkedin.com/in/anandsant1212</div></div>
    </a>
    <a class='cc' href='tel:+919423586586'>
      <div class='cc-icon'>📞</div>
      <div><div class='cc-lbl'>Phone</div><div class='cc-val'>+91 94235 86586</div></div>
    </a>
    <div class='cc'>
      <div class='cc-icon'>📍</div>
      <div><div class='cc-lbl'>Location</div><div class='cc-val'>Mumbai, Maharashtra</div></div>
    </div>
  </div>
  <div class='card' style='margin-top:20px;text-align:center;'>
    <h3 style='text-align:center;margin-bottom:10px;'>Currently</h3>
    <p style='font-size:17px;font-weight:700;color:#1a1a1a;'>Telemerge · Software Engineer</p>
    <p style='margin-top:6px;'>Building AI-powered QA automation for State Bank of India · Oct 2025 – Present</p>
  </div>
</div>
""", height=620)
