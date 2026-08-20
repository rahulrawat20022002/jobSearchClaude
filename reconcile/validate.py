#!/usr/bin/env python3
"""Validate every drafted role per the 19 August 2026 rules."""
import pypdf
from pathlib import Path

FOLDERS = [
    "Amprion Dortmund Werkstudent KI",
    "Ed Zueblin Stuttgart Werkstudent BI Data Analytics",
    "PwC Deutschland Werkstudent AI Adoption Enablement",
]

# Banned per 19 Aug 2026: no toward B2, Databricks, Delta Lake, LangChain, PyTorch
# PERSONAL DETAILS block is retired; PD strings are informational not banned but
# per CLAUDE.md gate override those are considered satisfied by new header.
HARD_BANNED = ["toward B2", "Databricks", "Delta Lake", "LangChain", "PyTorch",
               "Richtung B2"]  # also DE-track embellishment

REQUIRED_FILES = [
    "CV_Rahul_Rawat.md",
    "CV_Rahul_Rawat.html",
    "CV_Rahul_Rawat.pdf",
    "CV_Rahul_Rawat.docx",
    "CoverLetter_Rahul_Rawat.md",
    "CoverLetter_Rahul_Rawat.html",
    "CoverLetter_Rahul_Rawat.pdf",
    "CoverLetter_Rahul_Rawat.docx",
]

root = Path("/tmp/JobSearch/drafts")
failed = []
for f in FOLDERS:
    folder = root / f
    problems = []
    for req in REQUIRED_FILES:
        p = folder / req
        if not p.exists() or p.stat().st_size == 0:
            problems.append(f"missing/empty: {req}")
    cv_pdf = folder / "CV_Rahul_Rawat.pdf"
    if cv_pdf.exists():
        reader = pypdf.PdfReader(str(cv_pdf))
        pages = len(reader.pages)
        if pages not in (2, 3):
            problems.append(f"page count {pages}, need 2 or 3")
        full = "".join(p.extract_text() or "" for p in reader.pages)
        for banned in HARD_BANNED:
            if banned in full:
                problems.append(f"banned string present: {banned}")
    if problems:
        failed.append((f, problems))
        print(f"FAIL {f}")
        for p in problems:
            print(f"   - {p}")
    else:
        print(f"OK   {f} (all 8 files, CV PDF {pages} pages, banned strings absent)")

if failed:
    print(f"\n{len(failed)} role(s) FAILED validation")
    exit(1)
print("\nAll roles PASSED validation")
