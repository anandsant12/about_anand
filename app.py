import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Anand Sant | AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove all Streamlit default padding/margins
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    section[data-testid="stSidebar"] {display: none;}
    .stApp {
        margin: 0;
        padding: 0;
    }
</style>
""", unsafe_allow_html=True)

html_code = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&family=JetBrains+Mono:wght@400;500&display=swap');

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

html{
    scroll-behavior:smooth;
}

body{
    background:#050914;
    color:white;
    font-family:'Space Grotesk',sans-serif;
    overflow-x:hidden;
}

/* NAVBAR */
.nav{
    position:fixed;
    top:0;
    width:100%;
    padding:20px 50px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:rgba(5,9,20,0.8);
    backdrop-filter:blur(10px);
    z-index:999;
    border-bottom:1px solid rgba(255,255,255,0.05);
}

.logo{
    font-size:28px;
    font-weight:800;
    font-family:'Syne',sans-serif;
}

.logo span{
    color:#7c4dff;
}

.nav-links{
    display:flex;
    gap:30px;
}

.nav-links a{
    text-decoration:none;
    color:#9fa8da;
    transition:0.3s;
}

.nav-links a:hover{
    color:white;
}

/* HERO SECTION */
.hero{
    height:100vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:20px;
}

.badge{
    padding:10px 20px;
    border-radius:30px;
    border:1px solid rgba(255,255,255,0.1);
    margin-bottom:30px;
    color:#9fa8da;
    background:rgba(255,255,255,0.03);
}

.hero h1{
    font-size:110px;
    line-height:1;
    font-family:'Syne',sans-serif;
    background:linear-gradient(to right,#ffffff,#7c4dff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero p{
    margin-top:25px;
    font-size:24px;
    color:#90a4ae;
}

.buttons{
    margin-top:40px;
    display:flex;
    gap:20px;
}

.btn{
    padding:14px 30px;
    border-radius:10px;
    text-decoration:none;
    font-weight:600;
    transition:0.3s;
}

.btn-primary{
    background:linear-gradient(135deg,#5c6bc0,#7c4dff);
    color:white;
}

.btn-secondary{
    border:1px solid rgba(255,255,255,0.15);
    color:#9fa8da;
}

.btn:hover{
    transform:translateY(-3px);
}

/* SECTION */
.section{
    max-width:1200px;
    margin:auto;
    padding:120px 20px;
}

.section-tag{
    color:#5c6bc0;
    font-size:13px;
    margin-bottom:10px;
    letter-spacing:2px;
    text-transform:uppercase;
}

.section-title{
    font-size:60px;
    font-family:'Syne',sans-serif;
    margin-bottom:60px;
}

.section-title span{
    color:#7c4dff;
}

/* TIMELINE */
.timeline{
    border-left:2px solid rgba(255,255,255,0.1);
    padding-left:40px;
}

.timeline-item{
    margin-bottom:50px;
    position:relative;
}

.timeline-item::before{
    content:'';
    position:absolute;
    left:-49px;
    top:5px;
    width:14px;
    height:14px;
    background:#7c4dff;
    border-radius:50%;
}

.timeline-card{
    background:rgba(255,255,255,0.03);
    padding:30px;
    border-radius:18px;
    border:1px solid rgba(255,255,255,0.06);
    transition:0.3s;
}

.timeline-card:hover{
    transform:translateY(-5px);
    border-color:#7c4dff;
}

.timeline-year{
    color:#90a4ae;
    margin-bottom:10px;
}

.timeline-org{
    font-size:24px;
    font-weight:700;
    margin-bottom:8px;
}

.timeline-role{
    color:#80cbc4;
    margin-bottom:15px;
}

.timeline-desc{
    color:#90a4ae;
    line-height:1.7;
}

/* SKILLS */
.skills-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
    gap:20px;
}

.skill-card{
    background:rgba(255,255,255,0.03);
    border-radius:18px;
    padding:30px;
    border:1px solid rgba(255,255,255,0.06);
    transition:0.3s;
}

.skill-card:hover{
    transform:translateY(-5px);
    border-color:#7c4dff;
}

.skill-card h3{
    margin-bottom:20px;
    font-size:22px;
}

.skill-items{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
}

.skill-items span{
    background:rgba(255,255,255,0.06);
    padding:8px 12px;
    border-radius:8px;
    font-size:13px;
    color:#b0bec5;
}

/* PROJECTS */
.projects-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
    gap:25px;
}

.project-card{
    background:rgba(255,255,255,0.03);
    padding:30px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.06);
    transition:0.3s;
}

.project-card:hover{
    transform:translateY(-5px);
    border-color:#7c4dff;
}

.project-card h3{
    font-size:24px;
    margin-bottom:15px;
}

.project-card p{
    color:#90a4ae;
    line-height:1.7;
}

/* CONTACT */
.contact{
    text-align:center;
    padding:100px 20px;
}

.contact h2{
    font-size:60px;
    font-family:'Syne',sans-serif;
}

.contact p{
    margin-top:20px;
    color:#90a4ae;
}

.contact-links{
    margin-top:40px;
    display:flex;
    justify-content:center;
    gap:20px;
    flex-wrap:wrap;
}

/* FOOTER */
.footer{
    text-align:center;
    padding:40px;
    color:#546e7a;
}

/* RESPONSIVE */
@media(max-width:768px){
    .hero h1{
        font-size:60px;
    }
    .section-title{
        font-size:40px;
    }
    .nav{
        padding:20px;
    }
    .nav-links{
        display:none;
    }
}
</style>
</head>

<body>

<nav class="nav">
    <div class="logo">A<span>.</span>Sant</div>
    <div class="nav-links">
        <a href="#journey">Journey</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </div>
</nav>

<section class="hero">
    <div class="badge">Available for Opportunities &middot; Mumbai, India</div>
    <h1>Anand<br>Sant</h1>
    <p>Full Stack AI Engineer &middot; Building AI Systems with LLMs &amp; RAG</p>
    <div class="buttons">
        <a class="btn btn-primary" href="mailto:anandsant1212@gmail.com">Contact Me</a>
        <a class="btn btn-secondary" href="https://linkedin.com/in/anandsant1212" target="_blank">LinkedIn</a>
    </div>
</section>

<section class="section" id="journey">
    <div class="section-tag">01 JOURNEY</div>
    <h2 class="section-title">The Road That <span>Shaped Me</span></h2>
    <div class="timeline">

        <div class="timeline-item">
            <div class="timeline-card">
                <div class="timeline-year">2025 - Present</div>
                <div class="timeline-org">Telemerge</div>
                <div class="timeline-role">Software Engineer</div>
                <div class="timeline-desc">
                    Building AI-powered Test Case Generation platform for SBI using GPT-4.1, RAG, PostgreSQL, ChromaDB and FastAPI.
                </div>
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-card">
                <div class="timeline-year">2023 - 2025</div>
                <div class="timeline-org">LearningMate Solutions</div>
                <div class="timeline-role">Associate Software Developer</div>
                <div class="timeline-desc">
                    Built production-grade AI systems using GPT-4o, OCR, React MUI, AWS S3 and Azure OpenAI.
                </div>
            </div>
        </div>

    </div>
</section>

<section class="section" id="skills">
    <div class="section-tag">02 SKILLS</div>
    <h2 class="section-title">Tech <span>Stack</span></h2>
    <div class="skills-grid">

        <div class="skill-card">
            <h3>AI / GenAI</h3>
            <div class="skill-items">
                <span>LLMs</span>
                <span>RAG</span>
                <span>GPT-4o</span>
                <span>Azure OpenAI</span>
                <span>ChromaDB</span>
            </div>
        </div>

        <div class="skill-card">
            <h3>Backend</h3>
            <div class="skill-items">
                <span>Python</span>
                <span>FastAPI</span>
                <span>JWT</span>
                <span>REST APIs</span>
            </div>
        </div>

        <div class="skill-card">
            <h3>Frontend</h3>
            <div class="skill-items">
                <span>React JS</span>
                <span>MUI</span>
                <span>Streamlit</span>
            </div>
        </div>

    </div>
</section>

<section class="section" id="projects">
    <div class="section-tag">03 PROJECTS</div>
    <h2 class="section-title">Featured <span>Projects</span></h2>
    <div class="projects-grid">

        <div class="project-card">
            <h3>AI Alt Text Platform</h3>
            <p>Built accessibility-focused multimodal AI platform using GPT-4o and Gemini 1.5.</p>
        </div>

        <div class="project-card">
            <h3>LCAP Data Extraction</h3>
            <p>Automated KPI extraction pipeline with Azure OpenAI and RAG.</p>
        </div>

        <div class="project-card">
            <h3>SBI Test Case Generator</h3>
            <p>AI-powered SIT/UAT test case generation using GPT-4.1 and dual vector DB RAG.</p>
        </div>

    </div>
</section>

<section class="contact" id="contact">
    <h2>Let's Build Something Together</h2>
    <p>Open to AI Engineering opportunities and freelance projects.</p>
    <div class="contact-links">
        <a class="btn btn-primary" href="mailto:anandsant1212@gmail.com">Email Me</a>
        <a class="btn btn-secondary" href="https://linkedin.com/in/anandsant1212" target="_blank">LinkedIn</a>
    </div>
</section>

<div class="footer">Crafted with &#x26A1; by Anand Sant</div>

</body>
</html>"""

components.html(
    html_code,
    height=3500,
    scrolling=True
)
