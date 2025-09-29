# Medical Codex Data Pipeline

## Keywords

- Python 3.13.7 
- ETL pipeline development 
- Data quality validation
- Data extraction 
- File format optimization 
- Production-ready code practices
- Reproducibility


## Objective
From identified medical codexes (7 different medical codex types; collectively codexes), create a data pipeline using automated processes and tools that move raw data to local machines for ETL tasks, with the reproducible scripts available on a public Github repository for version control. 

The aim is to load the transformed data to be available for data wrangling. Proof of concept would be reproducibility from scripts and accompanying files loaded to Github, from where the repository can be cloned and the tasks reproduced. 

<br />

> ## There are many routes to get to Dublin! Take any!
> ### I took this route.....

<br />

<details open>
  <summary>Features</summary>  
<br />

- Cleans and standardizes 7 codex datasets
- Uses a unified schema - "Code, Description, Last updated"
- Logs data quality issues
- Beginner friendly
</details>
<br />

<details open>
  <summary>How to run</summary>  
<br />

- Clone repository
- Install dependencies
</details>
<br />

## 1. Input

<details open>
  <summary>Tech-Stack</summary>  
<br />

- Python 3.13.7
- Visual Code Studio (recommended editor)
- Github (version control and code hosting)
</details>
<br />

<details>
  <summary>Medical Codexes </summary>  
<br />

| Codex Name         | Purpose                                          |
|--------------------|--------------------------------------------------|
| SNOMED CT (US)     | Clinical terminology for findings and disorders  |
| ICD-10-CM (US)     | US-specific diagnosis codes                      | 
| ICD-10 (WHO)       | International diagnosis codes                    | 
| HCPCS (US)         | Healthcare procedures and supplies               | 
| LOINC (US)         | Laboratory/clinical test codes                   | 
| RxNorm (US)        | Medication vocabularies                          | 
| NPI (US)           | Provider identifiers                             | 

</details>
<br />

<details>
  <summary>Data Sources</summary>  
  <br />

- Download raw data files for ICD-10(WHO) NPI, RxNorm and SNOMED from identified under Data Sources above 
- For ICD-10(US), LOINC and HCPC get validated by signing up at <a href="https://uts.nlm.nih.gov/uts/signup-login"> NIH-UMLS.</a>

    - <a href="https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update"> HCPCS (US) </a>
    - <a href="https://www.cms.gov/medicare/coding-billing/icd-10-codes"> ICD-10-CM (US) </a>
    - <a href="https://icdcdn.who.int/icd10/index.html"> ICD-10 (WHO) </a>
    - <a href="https://loinc.org/downloads/"> LOINC (US) </a>
    - <a href="https://download.cms.gov/nppes/NPI_Files.html"> NPI (US) </a>
    - <a href="https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html"> RxNorm (US) </a>
    - <a href="https://www.nlm.nih.gov/healthit/snomedct/archive.html"> SNOMED (US) </a>
</details>

## 2. Workflow

<details>
  <summary>Setup</summary>  
<br />

- Create Github Repo 
- Clone it to VSCode on local machine  
- Optimize VSCode

</details>

<br />
<details open>
  <summary>VSCode environment</summary>  
    
    - Pandas
    - Polars
    - Tabulate
    - Openpyxl

    - Rich
    - Requests    
    - Pyarrow
    - Fastparaquet
    - Wheel
    - PyPi
</details>

<br />
<details>
  <summary>Raw data files</summary>  
<br />

- Download raw data files for ICD-10(WHO) NPI, RxNorm and SNOMED from identified under Data Sources above 
    - For ICD-10(US), LOINC and HCPC get validated by signing up at <a href="https://uts.nlm.nih.gov/uts/signup-login"> NIH-UMLS.</a>
- Codex data downloads are compressed files that need to be extracted. 
    - The folders will have many files that make the codex package that not only have raw data files, but also schema and other information to help understand, use and decode the medical codex data.
- Identify files with relevant codex data. 
    - With .txt, .cvs or .xlsx and other common file types, this can be done by opening these files in popular relevant applications e.g., Notepad, Spreadsheets, and even optimized browsers.
    - Alternatively, appropriately sized files (codex files are large; smaller files can be ignored from extracted data folders), can be opened with python script within VSCode and explored within VSCode.
- This project does not include reading relevant data from a PDF, xml or similar file type.
- Medical codex files such as those from UMLS Metathesaurus or RxNorm, are in Rich Release Format (RRF). 
    - These files are pipe-delimited text files, typically very large, and intended to be loaded into a relational database system for processing rather than directly opened in simple text editors due to size. For this project the contents of the sole RRF file were visible only as an output file or in terminal as a preview '.head()'.

</details>
<br />

<details>
  <summary>VSCode folder structure</summary>  
<br />

>Create local storage and VSCode folder structure

```
medical-codex-pipeline/
├── input/
├── scripts/
│   ├── snomed_processor.py
│   ├── icd10cm_processor.py
│   ├── icd10who_processor.py
│   ├── hcpcs_processor.py
│   ├── loinc_processor.py
│   ├── rxnorm_processor.py
│   └── npi_processor.py
├── output/
│   ├── csv/
├── utils/
│   └── common_functions.py
├── requirements.txt
├── README.md
└── .gitignore
```
</details>
<br />
<details>
  <summary>Data pipeline</summary>  
  <br />

- From the downloaded data packages, upload identified suitable raw datafiles to the cloned project repository in VSCode.

> PANDAS
- Explore data in the 1st raw .csv file extracts
- Generate relevant data in the terminal 
- Extract 2nd .csv files with relevant columns, rename, add a 3rd column
- Used Rich (a Python library) to better present the raw and extracted files in the terminal
- Truncate the final output into 3rd .csv files with fixed-width-columns

> POLARS  
- Code, data exploration and extraction steps are mostly the same as for Pandas but the code methods and syntax are different in some cases.
</details>
<br />
<details open>
  <summary>Output extraction</summary>
<br />

- Raw data .csv file to explore
- Extracted .csv file with 3 targeted columns
- Fixed-width column-aligned .csv
</details>
<br />
<details open>
  <summary>Push to Github</summary>

```
medical-codex-pipeline/
├── scripts/
│   ├── snomed_processor.py
│   ├── icd10cm_processor.py
│   ├── icd10who_processor.py
│   ├── hcpcs_processor.py
│   ├── loinc_processor.py
│   ├── rxnorm_processor.py
│   └── npi_processor.py
├── utils/
│   └── common_functions.py
├── requirements.txt
├── README.md
└── .gitignore
```
</details>

## 3. Output
<details>
  <summary>Project data outputs</summary>
<br />

- Raw data downloads used compliant methods and protocols.
- Dependencies and configuration setting for Github repository via VSCode configurations reflected in Requirements.txt
- Raw data file ingested via VSCode with output in .CSV file type.
    - 2 columns extracted from each processed codex data file columns relevant to a unique identifier and description extracted 
        -  These 2 columns renamed as 'Code', and 'Description'.  
    - 1 column needs to be added to the output file with the date of last update (e.g.,'Last_updated')
- Explored files using Pandas and Polars.
- Code validated in the terminal and previewing output files. 
- Generated a 3 .csv files
    - Raw
    - Short: with 3 extracted columns
    - Aligned: with fixed width columns
- Reproducibility ensured via Github repository and unit testing each module and script.
- README.md created to aide reproducibility.
</details>
<br />
<details open>
  <summary>Limitations</summary>
<br />
- Documentation of steps not robust
- Logging module embedded in the code was hashed out and needs to be redone
</details>
<br />
<details>
  <summary>Validate reproducibility</summary>
<br />
- After the final push to Github repository, clone the code in a new local VSCode folder, and reproduce the results for validation and to test reproducibility, and identify bugs and issues in reproducibility noted in an issue log. 
- In case of issues try and identify if the issues are because of environment/dependencies or script, and resolve. 
**<h3>Remember, there are many ways to get to Dublin!</h3>**
</details>
<br />
<details>
  <summary>Clean up local machine</summary>
<br />
  Finally, after validating the cloned files and testing reproducibility (identifying issues in an issue log for further improvement), archive the project folder on your machine, noting the raw data file download process so it can be repeated. The raw data files can be deleted from the local machine. 
  
  - Record key learning in whichever way you deem fit. The important thing is to learn and understand the concepts and process. 
  
  - Move on to the next project, but after understanding the concepts not just hacking out output files through vibe coding. 
</details>
<br />
<details open>
  <summary>Learnings and insights</summary>
<br />

- The complexity level of the sample starter codes was incremental in difficulty, exploring different types of data processing techniques with each sample code. 
- Sample codes exposed different techniques, and as a result, tools and dependencies, to process data and create data pipelines using basic Python code, VSCode dependencies, environment creation, and Github integration.
- The use of LLM supported coding also exposed many other ways to process the data to create data pipelines than shared in the sample code blocks. 
- LLM use gave exposure to the sheer expanse of coding in data analytics.
- Various dependencies: Inbuilt Python modules, Python libraries and 3rd party modules. (Tabular, Datetime, Path, Wheel, Openpyxl, Fastparquet, Pyarrow.)
- Python code workflow using VSCode integrating to Github.
</details>


---
## ✨ To many more data pipelines, smooth data flows and insightful analytics ahead! 📊 
