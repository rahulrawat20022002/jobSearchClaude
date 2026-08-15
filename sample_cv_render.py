"""
Sample CV render, 2 August 2026.

Generates CV_Sample_ThreeExperience.html so Rah can see how the new three entry
Experience section (eRay GmbH, Satendra Singh full time, Satendra Singh intern)
renders inside the full 19 July 2026 Lebenslauf template.

Reuses build_html.py CSS and helper functions so the sample matches the real
pipeline pixel for pixel. This script does NOT touch the pipeline itself, it
just renders a preview file.
"""

from html import escape
from datetime import date
from pathlib import Path

from build_html import (
    CSS, HDR_EN, PD_FIELDS_EN,
    _entry_html, _entry_head_only_html, wrap_bold_html,
)
from role_configs import (
    ERAY_BULLETS_EN, DIABETES_BULLETS_EN,
    SATENDRA_FT_BULLETS_EN, SATENDRA_INTERN_BULLETS_EN,
    P_RAG_EN, P_CREDITIQ_EN,
)


ROOT = Path(__file__).resolve().parent

# --- Sample tailored content for the preview ------------------------------
SAMPLE_PROFILE = (
    "Data scientist with hands on delivery in time series forecasting, "
    "recursive machine learning pipelines, and multi year front end development "
    "for a family owned engineering firm. Currently a Master of Science student "
    "in Data Science and Analytics at SRH University of Applied Sciences "
    "Heidelberg with 20 hours per week Werkstudent availability immediately and "
    "full time from April 2027."
)

# SS Engineers and Contractors, bullets pulled from role_configs.py so the
# sample stays in lock step with what the real pipeline will ship.
SATENDRA_FT_BULLETS = SATENDRA_FT_BULLETS_EN
SATENDRA_INTERN_BULLETS = SATENDRA_INTERN_BULLETS_EN

# A pared down set of Personal Projects for the preview so the sample stays
# readable at two to three pages. The real pipeline picks per role. Both
# projects are pulled directly from role_configs.py so bullets match the
# pipeline source of truth.
SAMPLE_PROJECTS = [
    {
        "date_label": "2026",
        "kind_label": "Personal",
        "title": f"{P_RAG_EN['title']}: {', '.join(P_RAG_EN['stack'][:4])}",
        "bullets": P_RAG_EN["bullets"],
        "stack": P_RAG_EN["stack"],
    },
    {
        "date_label": "2025 to 2026",
        "kind_label": "Academic, SRH Heidelberg",
        "title": f"{P_CREDITIQ_EN['title']}: {', '.join(P_CREDITIQ_EN['stack'][:4])}",
        "bullets": P_CREDITIQ_EN["bullets"],
        "stack": P_CREDITIQ_EN["stack"],
    },
]


def _sample_html():
    hdr = HDR_EN

    # Personal Details
    pd_rows = "".join(
        f'<tr><td class="label">{escape(lbl)}</td><td class="value">{escape(val)}</td></tr>'
        for lbl, val in PD_FIELDS_EN
    )
    pd_html = f'<table class="pd-table">{pd_rows}</table>'

    # Experience, three entries in reverse chronological order. Bullets are
    # trimmed per entry so the sample fits inside the two to three page A4
    # target with the STAR format expansion.
    exp_html = (
        _entry_html(
            "Oct 2025 to Mar 2026", "Heidelberg",
            "eRay GmbH", "Data Scientist",
            ERAY_BULLETS_EN[:3],
            ["Python", "CatBoost", "Prophet", "scikit learn", "MICE"],
        )
        + _entry_html(
            "Aug 2023 to Aug 2024", "India",
            "SS Engineers and Contractors",
            "Junior Associate Software Developer",
            SATENDRA_FT_BULLETS,
            ["React", "module federation", "Playwright", "AngularJS", "HTML5", "CSS3"],
        )
        + _entry_html(
            "Feb 2023 to July 2023", "India",
            "SS Engineers and Contractors",
            "Front End Developer Intern",
            SATENDRA_INTERN_BULLETS,
            ["React", "HTML5", "CSS3", "Git", "code review workflow"],
        )
    )

    # Personal Projects, sample. Kept to one entry so the sample fits the two
    # to three page A4 window with the expanded three entry Experience section
    # and STAR bullets.
    proj_html = ""
    for p in SAMPLE_PROJECTS[:1]:
        proj_html += _entry_html(
            p["date_label"], p["kind_label"],
            p["title"], "",
            p["bullets"][:2], p["stack"],
        )

    # Education
    edu_html = (
        _entry_head_only_html(
            "Apr 2025 to Present", "Heidelberg",
            "M.Sc. Data Science and Analytics",
            "SRH University of Applied Sciences Heidelberg, GPA 1.9",
        )
        + _entry_head_only_html(
            "2019 to 2023", "Greater Noida, India",
            "Bachelor of Technology in Computer Science",
            "GL Bajaj Institute of Technology and Management, CGPA 7.3 of 10",
        )
    )

    # Research
    research_html = _entry_html(
        "2022 to 2023", "Greater Noida, India",
        "Bachelor Thesis, Diabetes Prediction Using Machine Learning",
        "GL Bajaj Institute of Technology and Management, IEEE style paper",
        DIABETES_BULLETS_EN[:2],
        ["Python", "scikit learn", "Pandas", "Seaborn"],
    )

    # Certifications, achievements, languages, sample values. Signature block
    # retired 4 August 2026.
    certs = [
        "NVIDIA, Building LLM Applications With Prompt Engineering, issued 12 November 2025.",
        "AWS Academy Graduate, AWS Academy Cloud Foundations, issued 15 July 2025.",
        "SAS Certified Specialist, Visual Business Analytics Using SAS Viya, issued 7 May 2025.",
    ]
    certs_html = (
        '<ul class="simple-list">'
        + "".join(f"<li>{escape(c)}</li>" for c in certs)
        + "</ul>"
    )
    achievements = [
        "USAII Global AI Hackathon 2026, Finalist at Graduate Level, awarded by the United States Artificial Intelligence Institute for innovation and applied AI on real world challenges."
    ]
    ach_html = (
        '<ul class="simple-list">'
        + "".join(f"<li>{wrap_bold_html(escape(a))}</li>" for a in achievements)
        + "</ul>"
    )
    lang_fields = [
        ("English", "Fluent, written and spoken"),
        ("German", "B1 in progress toward B2"),
        ("Hindi", "Native"),
    ]
    lang_rows = "".join(
        f'<tr><td class="label">{escape(lbl)}</td><td class="value">{escape(val)}</td></tr>'
        for lbl, val in lang_fields
    )
    lang_html = f'<table class="pd-table">{lang_rows}</table>'

    role_strip = "Data Scientist, sample preview"

    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Rahul Rawat, sample CV preview</title><style>{CSS}</style></head><body><div class="page">
<div class="cv-tag">C U R R I C U L U M &nbsp; V I T A E</div>
<h1 class="name">Rahul Rawat</h1>
<div class="role-tag">{escape(role_strip)}</div>
<div class="header-rule"></div>
<section class="section"><h2>{escape(hdr['pd'])}</h2>{pd_html}</section>
<section class="section"><h2>{escape(hdr['profile'])}</h2><p class="profile-text">{wrap_bold_html(escape(SAMPLE_PROFILE))}</p></section>
<section class="section section-long"><h2>{escape(hdr['experience'])}</h2>{exp_html}</section>
<section class="section section-long"><h2>{escape(hdr['projects'])}</h2>{proj_html}</section>
<section class="section"><h2>{escape(hdr['education'])}</h2>{edu_html}</section>
<section class="section"><h2>{escape(hdr['research'])}</h2>{research_html}</section>
<section class="section"><h2>{escape(hdr['certifications'])}</h2>{certs_html}</section>
<section class="section"><h2>{escape(hdr['achievements'])}</h2>{ach_html}</section>
<section class="section"><h2>{escape(hdr['languages'])}</h2>{lang_html}</section>
</div></body></html>"""


def main():
    out_html = ROOT / "CV_Sample_ThreeExperience.html"
    out_html.write_text(_sample_html(), encoding="utf-8")
    print(f"Wrote {out_html}")

    # Try to render PDF too if weasyprint is available
    try:
        import weasyprint
        out_pdf = ROOT / "CV_Sample_ThreeExperience.pdf"
        weasyprint.HTML(string=out_html.read_text(encoding="utf-8")).write_pdf(str(out_pdf))
        print(f"Wrote {out_pdf}")
    except Exception as e:
        print(f"PDF render skipped: {e}")


if __name__ == "__main__":
    main()
