# 🧪 PubMed Fetcher: Research Paper Extractor with Non-Academic Author Filter

## 🚀 Project Overview

This tool is a Python CLI utility that searches **PubMed** for biomedical research papers using a user-specified query and filters papers where **at least one author is affiliated with a pharmaceutical or biotech company** (i.e., **non-academic**).

The extracted data includes:
- PubMed ID
- Title
- Publication Date
- Non-academic Author(s)
- Company Affiliation(s)
- Corresponding Author Email (if available)

Results can be saved in a **CSV file** or printed directly to the terminal.

---

## ✅ Why This Approach?

PubMed contains a massive number of biomedical research papers, but the goal is to **identify industry involvement** in research. Most academic affiliations contain strings like “University”, “Hospital”, or “Institute”. This tool uses **heuristics** to detect and extract **non-academic authors**, especially from **pharma/biotech sectors**.

This approach ensures:
- Flexibility (full PubMed query syntax support),
- Precision (filters by affiliations),
- Automation (easy to integrate into pipelines),
- CLI simplicity (can be scripted, containerized, etc.)

---

## 🧠 How It Works (Architecture)

### 🔄 Workflow
1. Accepts a **PubMed query** as input via CLI.
2. Uses **Entrez API (Biopython)** to:
   - Search article IDs (`esearch`)
   - Fetch article metadata (`efetch` with XML)
3. Parses full article metadata to:
   - Extract author names, affiliations, publication year, and emails.
4. Applies heuristics to:
   - Identify **non-academic affiliations**.
5. Outputs filtered records to:
   - **CSV file** if `-f` specified,
   - **Terminal** if no file is given.

---

## 🧱 Project Structure

pubmed_fetcher/
├── pubmed_fetcher/
│ ├── init.py
│ ├── cli.py # CLI interface
│ ├── core.py # Main fetch & parse logic
│ ├── heuristics.py # Logic to detect non-academic affiliations
│ └── types.py # Typed dataclass for paper structure
├── tests/
│ └── test_core.py # (Optional test file)
├── pyproject.toml # Poetry config
└── README.md


### Step 1: Clone the repository

git clone https://github.com/manojh17/pubmed-fetcher.git
cd pubmed-fetcher

### Step 2: Install using Poetry

poetry install

### How to Run

poetry run get-papers-list "your pubmed search query" [options]

### Options:
-f, --file → Output CSV file name. If omitted, prints to console.

-d, --debug → Show debug output.

-h, --help → Show help message.

