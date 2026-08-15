"""ATS-clean sample renderer, one-off preview.

Builds a single ATS-clean sample CV for the SAP Engagement Lead role from
role_configs_12aug.py, applying the three ATS fixes documented in CLAUDE.md
under 'ATS-clean template baseline, effective 11 August 2026':

  1. No CURRICULUM VITAE strip at the top
  2. Single column entry layout with dates and location inline in the title
  3. Standalone Skills section right after Profile, one comma separated line

Output: ats_sample_preview/CV_SAP_Engagement_Lead_ATS.pdf and .html

Does NOT touch the 8 currently drafted CVs. Once Rah approves the look, the
same helpers get merged into build_html.py's html_cv and docx_cv and the 8
drafts get rebuilt.
"""

import os
from html import escape
from pathlib import Path

import weasyprint

from build_html import (
    NAVY_HEX,
    NAVY_GREY_HEX,
    RUST_HEX,
    BODY_HEX,
    RULE_HEX,
    wrap_bold_html,
)
from role_configs_12aug import CONFIGS_12AUG


# Pick the SAP Engagement Lead config as the sample
CFG = next(c for c in CONFIGS_12AUG if "Engagement Lead" in c["folder"])

OUT_DIR = Path("ats_sample_preview")
OUT_DIR.mkdir(exist_ok=True)


# --- Skills derivation ----------------------------------------------------
# Union of every stack list across projects + eRay + SS Engineers, top 25.
SKILLS_EN = [
    "Python", "SQL", "PySpark", "BigQuery", "Databricks", "Delta Lake",
    "Power BI", "Tableau", "Looker Studio", "LangChain", "LangGraph",
    "Ollama", "CatBoost", "LightGBM", "XGBoost", "Prophet", "MICE",
    "scikit-learn", "PyTorch", "dbt", "Apache Airflow", "GCP", "AWS",
    "Docker", "Git", "React", "Playwright",
]
SKILLS_DE = SKILLS_EN  # Same skill names, just the section heading changes


# --- ATS-clean CSS --------------------------------------------------------
CSS_ATS = f"""
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
        background: #ffffff; color: {BODY_HEX}; }}
.page {{ background: #ffffff; }}

h1.name {{ font-size: 22pt; font-weight: 700; color: {NAVY_HEX};
           margin-bottom: 1.5mm; }}
.role-tag {{ font-size: 11pt; color: {NAVY_GREY_HEX}; margin-bottom: 3mm;
             font-weight: 500; }}
.header-rule {{ border-top: 1px solid {NAVY_HEX}; margin-bottom: 4mm; }}

.section {{ margin-bottom: 3mm; page-break-inside: avoid; break-inside: avoid; }}
.section.section-long {{ page-break-inside: auto; break-inside: auto; }}
.section h2 {{ font-size: 11.5pt; color: {NAVY_HEX}; font-weight: 700;
               margin-bottom: 1.5mm; text-transform: uppercase;
               padding-bottom: 0.5mm; border-bottom: 1px solid {RULE_HEX};
               page-break-after: avoid; break-after: avoid; }}

.pd-line {{ font-size: 10.5pt; margin-bottom: 0.4mm; color: {BODY_HEX}; }}
.pd-line .label {{ color: {NAVY_HEX}; font-weight: 700; }}

.profile-text {{ font-size: 10.5pt; line-height: 1.35; text-align: justify;
                 color: {BODY_HEX}; }}

.skills-line {{ font-size: 10.5pt; line-height: 1.4; color: {BODY_HEX}; }}

.entry {{ margin-bottom: 3mm; page-break-inside: avoid; break-inside: avoid; }}
.entry:last-child {{ margin-bottom: 0; }}
.entry .title-line {{ font-size: 11pt; font-weight: 700; color: {NAVY_HEX};
                      margin-bottom: 0.3mm; }}
.entry .sub-line {{ font-size: 10pt; color: {NAVY_GREY_HEX};
                    margin-bottom: 1mm; font-style: italic; }}
.entry ul {{ list-style: none; padding: 0; margin-top: 0.5mm; }}
.entry ul li {{ font-size: 10.5pt; line-height: 1.3; text-align: justify;
                color: {BODY_HEX}; padding-left: 4mm; position: relative;
                margin-bottom: 0.5mm; }}
.entry ul li::before {{ content: "•"; position: absolute; left: 0; top: 0;
                        color: {RUST_HEX}; font-weight: 700; }}
.entry .tech {{ font-size: 9.5pt; color: {NAVY_GREY_HEX}; font-style: italic;
                margin-top: 1mm; }}
.entry .tech .tech-label {{ font-weight: 700; font-style: normal;
                            color: {RUST_HEX}; margin-right: 1mm; }}
.entry strong {{ color: {NAVY_HEX}; font-weight: 700; }}

.lang-line {{ font-size: 10.5pt; margin-bottom: 0.4mm; color: {BODY_HEX}; }}
.lang-line .label {{ color: {NAVY_HEX}; font-weight: 700; }}

.simple-list {{ list-style: none; padding: 0; }}
.simple-list li {{ font-size: 10.5pt; line-height: 1.3; text-align: justify;
                   color: {BODY_HEX}; padding-left: 4mm; position: relative;
                   margin-bottom: 0.4mm; }}
.simple-list li::before {{ content: "•"; position: absolute; left: 0; top: 0;
                           color: {RUST_HEX}; font-weight: 700; }}

@page {{ size: A4; margin: 20mm 18mm 15mm 18mm; }}
"""


def entry_single_column(title_line, sub_line, bullets, tech_stack):
    """Single column entry: title line with dates+location inline, then bullets."""
    bullet_html = "".join(f"<li>{wrap_bold_html(escape(b))}</li>" for b in bullets)
    tech_html = ""
    if tech_stack:
        tech_html = (
            f'<div class="tech"><span class="tech-label">Technologies:</span>'
            f'{escape(", ".join(tech_stack))}</div>'
        )
    sub_html = f'<div class="sub-line">{escape(sub_line)}</div>' if sub_line else ""
    return (
        f'<div class="entry">'
        f'<div class="title-line">{escape(title_line)}</div>'
        f'{sub_html}'
        f'<ul>{bullet_html}</ul>{tech_html}'
        f'</div>'
    )


def render_ats_html(cfg):
    is_de = cfg.get("lang") == "de"

    # Persönliche Daten as one line per field, plain prose
    if is_de:
        pd_fields = [
            ("Adresse", "C2 16, 68159 Mannheim, Deutschland"),
            ("Telefon", "015563603340"),
            ("E-Mail", "rahulrawat2r@gmail.com"),
            ("LinkedIn", "linkedin.com/in/rahulrawat2r"),
            ("GitHub", "github.com/rahulrawat20022002"),
            ("Portfolio", "rah-portfolio.pages.dev"),
            ("Geburtsdatum", "20 February 2002"),
            ("Nationalität", "Indisch, Studentenvisum mit gültiger Arbeitserlaubnis"),
            ("Verfügbarkeit", "Werkstudent 20 Stunden pro Woche sofort, Vollzeit ab April 2027"),
        ]
        heading = {
            "pd": "Persönliche Daten",
            "profile": "Profil",
            "skills": "Fähigkeiten",
            "exp": "Berufserfahrung",
            "edu": "Ausbildung",
            "proj": "Persönliche Projekte",
            "research": "Forschung und Abschlussarbeit",
            "cert": "Zertifikate",
            "ach": "Auszeichnungen",
            "lang": "Sprachen",
        }
        skills = SKILLS_DE
    else:
        pd_fields = [
            ("Address", "C2 16, 68159 Mannheim, Germany"),
            ("Phone", "015563603340"),
            ("Email", "rahulrawat2r@gmail.com"),
            ("LinkedIn", "linkedin.com/in/rahulrawat2r"),
            ("GitHub", "github.com/rahulrawat20022002"),
            ("Portfolio", "rah-portfolio.pages.dev"),
            ("Date of birth", "20 February 2002"),
            ("Nationality", "Indian, student visa with valid work permit"),
            ("Availability", "Werkstudent 20 hours per week immediately, full time from April 2027"),
        ]
        heading = {
            "pd": "Personal Details",
            "profile": "Profile",
            "skills": "Skills",
            "exp": "Professional Experience",
            "edu": "Education",
            "proj": "Personal Projects",
            "research": "Research and Thesis",
            "cert": "Certifications",
            "ach": "Achievements",
            "lang": "Languages",
        }
        skills = SKILLS_EN

    pd_html = "".join(
        f'<div class="pd-line"><span class="label">{escape(lbl)}:</span> {escape(val)}</div>'
        for lbl, val in pd_fields
    )

    # eRay experience entry, single column, dates + location inline
    if is_de:
        eray_title = "Data Scientist at eRay GmbH, Heidelberg, Okt 2025 bis Mrz 2026"
    else:
        eray_title = "Data Scientist at eRay GmbH, Heidelberg, Oct 2025 to Mar 2026"

    experience_html = entry_single_column(
        eray_title,
        None,
        cfg["experience_bullets"],
        ["Python", "CatBoost", "Prophet", "scikit-learn", "MICE"],
    )

    # SS Engineers FT and intern (short, 2 + 1 bullets per calibrated defaults)
    from role_configs import (
        SATENDRA_FT_BULLETS_EN, SATENDRA_FT_BULLETS_DE,
        SATENDRA_INTERN_BULLETS_EN, SATENDRA_INTERN_BULLETS_DE,
    )
    ss_ft_bullets = (SATENDRA_FT_BULLETS_DE if is_de else SATENDRA_FT_BULLETS_EN)[:2]
    ss_intern_bullets = (SATENDRA_INTERN_BULLETS_DE if is_de else SATENDRA_INTERN_BULLETS_EN)[:1]

    if is_de:
        experience_html += entry_single_column(
            "Junior Associate Software Developer at SS Engineers and Contractors, India, Aug 2023 bis Aug 2024",
            None, ss_ft_bullets,
            ["React", "module federation", "Playwright", "AngularJS", "HTML5", "CSS3"],
        )
        experience_html += entry_single_column(
            "Front End Developer Intern at SS Engineers and Contractors, India, Feb 2023 bis Juli 2023",
            None, ss_intern_bullets,
            ["React", "HTML5", "CSS3", "Git"],
        )
    else:
        experience_html += entry_single_column(
            "Junior Associate Software Developer at SS Engineers and Contractors, India, Aug 2023 to Aug 2024",
            None, ss_ft_bullets,
            ["React", "module federation", "Playwright", "AngularJS", "HTML5", "CSS3"],
        )
        experience_html += entry_single_column(
            "Front End Developer Intern at SS Engineers and Contractors, India, Feb 2023 to July 2023",
            None, ss_intern_bullets,
            ["React", "HTML5", "CSS3", "Git"],
        )

    # Education, single column
    if is_de:
        edu_html = (
            entry_single_column(
                "M.Sc. Data Science and Analytics, SRH University of Applied Sciences Heidelberg, GPA 1.9, Apr 2025 bis heute",
                None, [], [],
            )
            + entry_single_column(
                "Bachelor of Technology, GL Bajaj Institute of Technology and Management, CGPA 7.3 of 10, 2019 bis 2023",
                None, [], [],
            )
        )
    else:
        edu_html = (
            entry_single_column(
                "M.Sc. Data Science and Analytics, SRH University of Applied Sciences Heidelberg, GPA 1.9, Apr 2025 to Present",
                None, [], [],
            )
            + entry_single_column(
                "Bachelor of Technology, GL Bajaj Institute of Technology and Management, CGPA 7.3 of 10, 2019 to 2023",
                None, [], [],
            )
        )

    # Personal Projects, capped at 2 entries with up to 3 bullets each
    projects_html = ""
    for proj in cfg["projects"][:2]:
        title_line = f"{proj['title']}, built with {', '.join(proj['stack'])}"
        projects_html += entry_single_column(
            title_line, None, proj["bullets"][:3], [],
        )

    # Research and Thesis
    if is_de:
        research_title = "Bachelor Thesis, Diabetes Prediction Using Machine Learning, GL Bajaj Institute of Technology and Management, 2022 bis 2023"
    else:
        research_title = "Bachelor Thesis, Diabetes Prediction Using Machine Learning, GL Bajaj Institute of Technology and Management, 2022 to 2023"
    research_html = entry_single_column(
        research_title, None, cfg["research_bullets"],
        ["Python", "scikit-learn", "Pandas", "Seaborn", "Google Colab"],
    )

    # Certifications
    cert_items = "".join(f"<li>{wrap_bold_html(escape(c))}</li>" for c in cfg["certifications"])
    cert_html = f'<ul class="simple-list">{cert_items}</ul>'

    # Achievements
    ach_items = "".join(f"<li>{wrap_bold_html(escape(a))}</li>" for a in cfg["achievements"])
    ach_html = f'<ul class="simple-list">{ach_items}</ul>'

    # Languages, one line per language (plain prose)
    if is_de:
        lang_lines = [
            ("Englisch", "Fließend, schriftlich und mündlich"),
            ("Deutsch", "B1 laufend Richtung B2"),
            ("Hindi", "Muttersprache"),
        ]
    else:
        lang_lines = [
            ("English", "Fluent, written and spoken"),
            ("German", "B1 in progress toward B2"),
            ("Hindi", "Native"),
        ]
    lang_html = "".join(
        f'<div class="lang-line"><span class="label">{escape(lbl)}:</span> {escape(val)}</div>'
        for lbl, val in lang_lines
    )

    # Assemble
    body = f"""
<div class="page">
  <h1 class="name">Rahul Rawat</h1>
  <div class="role-tag">{escape(cfg.get("role_strip", ""))}</div>
  <div class="header-rule"></div>

  <div class="section">
    <h2>{escape(heading["pd"])}</h2>
    {pd_html}
  </div>

  <div class="section">
    <h2>{escape(heading["profile"])}</h2>
    <p class="profile-text">{escape(cfg["profile"])}</p>
  </div>

  <div class="section">
    <h2>{escape(heading["skills"])}</h2>
    <p class="skills-line">{escape(", ".join(skills))}</p>
  </div>

  <div class="section section-long">
    <h2>{escape(heading["exp"])}</h2>
    {experience_html}
  </div>

  <div class="section">
    <h2>{escape(heading["edu"])}</h2>
    {edu_html}
  </div>

  <div class="section section-long">
    <h2>{escape(heading["proj"])}</h2>
    {projects_html}
  </div>

  <div class="section">
    <h2>{escape(heading["research"])}</h2>
    {research_html}
  </div>

  <div class="section">
    <h2>{escape(heading["cert"])}</h2>
    {cert_html}
  </div>

  <div class="section">
    <h2>{escape(heading["ach"])}</h2>
    {ach_html}
  </div>

  <div class="section">
    <h2>{escape(heading["lang"])}</h2>
    {lang_html}
  </div>
</div>
"""
    html_doc = f"""<!doctype html>
<html><head><meta charset="utf-8"><style>{CSS_ATS}</style></head>
<body>{body}</body></html>"""
    return html_doc


def main():
    html = render_ats_html(CFG)
    html_path = OUT_DIR / "CV_SAP_Engagement_Lead_ATS.html"
    pdf_path = OUT_DIR / "CV_SAP_Engagement_Lead_ATS.pdf"

    html_path.write_text(html, encoding="utf-8")
    weasyprint.HTML(string=html).write_pdf(str(pdf_path))

    # Count pages
    import subprocess
    r = subprocess.run(
        ["pdfinfo", str(pdf_path)], capture_output=True, text=True,
    )
    pages = "?"
    for line in r.stdout.splitlines():
        if line.startswith("Pages:"):
            pages = line.split(":", 1)[1].strip()
    print(f"Built {pdf_path} at {pages} pages")

    # Print naive ATS extraction preview
    r2 = subprocess.run(
        ["pdftotext", str(pdf_path), "-"], capture_output=True, text=True,
    )
    print("--- naive ATS text extraction, first 60 lines ---")
    for i, line in enumerate(r2.stdout.splitlines()[:60], 1):
        print(f"{i:3d}| {line}")


if __name__ == "__main__":
    main()
