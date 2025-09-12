# Medical Codex Pipeline

This repository processes healthcare coding reference datasets (ICD-10, SNOMED, LOINC, etc.) into unified CSV format. 
It builds a **data pipeline** of downloaded reference lists of medical codexes, which are foundational in healthcare software that include EHRs, hospital billing, insurance claims, and interoperability platforms.

---

## Overview

Healthcare organizations rely on standardized code sets, 7 used for this project listed below in the table, to identify diagnoses, procedures, lab-tests, medications, and provider identities. This repository automates the processing, cleaning, validation, and export of these data sets into a consistent CSV format suitable for production use.

---

## Codexes Supported

| Codex Name         | Purpose                                          |
|--------------------|--------------------------------------------------|
| SNOMED CT (US)     | Clinical terminology for findings and disorders  |
| ICD-10-CM (US)     | US-specific diagnosis codes                      | 
| ICD-10 (WHO)       | International diagnosis codes                    | 
| HCPCS (US)         | Healthcare procedures and supplies               | 
| LOINC (US)         | Laboratory/clinical test codes                   | 
| RxNorm (US)        | Medication vocabularies                          | 
| NPI (US)           | Provider identifiers                             | 

---

## Directory Structure
### *'Alt+195' ='├' 'Alt+196' = '──" in the directory structure below.*

medical-codex-pipeline/
├── input/ # Raw downloaded files (NOT committed)
├── output/
│ └── csv/ # Standardized and Processed, clean CSVs (Committed) 
├── scripts/ # One processor script per codex
│ ├── snomed_processor.py
│ ├── icd10cm_processor.py
│ ├── icd10who_processor.py
│ ├── hcpcs_processor.py
│ ├── loinc_processor.py
│ ├── rxnorm_processor.py
│ └── npi_processor.py
├── utils/
│ └── common_functions.py # Reusable saving/logging utilities
│ └── download_codexes.py # (bonus) Automated downloads tool *not included*
├── requirements.txt
├── README.md
└── .gitignore # Excludes large files, raw/input files, virtualenv, etc. for copyrighted and protected data.

## Features
- Cleans and standardizes 7 codex datasets
- Unified schema - "code, description, last updated"
- Logs data quality issues
- Beginner friendly

## How to run
1. Clone repository
2. Install dependencies

## pip install -r requirements.txt
3. Place sample raw data in `/input/`
4. Run processing script: ?? python scripts/icd10cm_processor.py ??

## Output
Processed CSV files appear in `/output/csv/`

## Dependencies
- pandas
- requests 
- polars

 


=======
# Medical-Codexes-Pipeline
Data pipeline for 7 medical codexes
>>>>>>> ee0b99a88ceea41acf3cd78731405d9a6d0f7d0a
