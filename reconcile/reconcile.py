#!/usr/bin/env python3
"""
Reconcile applied-log.csv against Notion. Notion is source of truth for Status.
Only updates the CSV; never writes to Notion Status.
"""
import csv
import shutil
from datetime import date

CSV_PATH = "/tmp/JobSearch/applied-log.csv"
BAK_PATH = f"/tmp/JobSearch/applied-log.csv.bak_{date.today().strftime('%Y%m%d')}"

# Ground truth mapping from Notion queries for rows currently 'drafted' in CSV
# (company, role) -> Notion Status
NOTION_STATUS = {
    ("retorio", "working student, ai engineer agentic systems"): "Not listed Anymore",
    ("assetmetrix gmbh", "working student, ai engineering"): "applied",
    ("phoenix contact", "werkstudent, data science und ki"): "applied",
    ("bsh home appliances group", "working student, engineering data analytics and classification"): "rejected",
    ("viadee unternehmensberatung ag", "werkstudent, data science und process mining"): "rejected",
    ("bmw group", "werkstudent, data science und ki tool entwicklung fuer qualitaetsanalyse"): "applied",
    ("kfw bankengruppe", "werkstudent, it data science und ki"): "applied",
    ("allianz insurance", "working student, data science"): "applied",
    ("siemens energy", "werkstudent, ki-basierte optimierungsinitiativen"): "applied",
    ("siemens ag", "werkstudent, data science im operativen service"): "rejected",
    ("deloitte", "werkstudent oder praktikant, digital und ai analytics"): "rejected",
}

def key(company, role):
    return (company.strip().lower(), role.strip().lower())

# Read CSV
with open(CSV_PATH, newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

updated = 0
changes = []
for i, row in enumerate(data):
    if len(row) < 6:
        continue
    d, company, role, loc, source, status = row[0], row[1], row[2], row[3], row[4], row[5]
    k = key(company, role)
    if status == "drafted" and k in NOTION_STATUS:
        new_status = NOTION_STATUS[k]
        if new_status != status:
            row[5] = new_status
            data[i] = row
            updated += 1
            changes.append((company, role, "drafted", new_status))

print(f"Updated {updated} rows")
for c in changes:
    print("  ", c)

# Backup and write
shutil.copy2(CSV_PATH, BAK_PATH)
with open(CSV_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
print(f"Backup: {BAK_PATH}")
