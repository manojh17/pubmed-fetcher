from Bio import Entrez
from pubmed_fetcher.heuristics import is_non_academic
from pubmed_fetcher.types import PaperData
import pandas as pd
import xml.etree.ElementTree as ET

Entrez.email = "hjonam1702@gmail.com"

def fetch_and_process_results(query: str, output_file: str | None, debug: bool = False):
    # Step 1: Search
    search = Entrez.esearch(db="pubmed", term=query, retmax=50)
    ids = Entrez.read(search)['IdList']
    if not ids:
        print("No results found.")
        return

    # Step 2: Fetch full XML records
    fetch = Entrez.efetch(db="pubmed", id=",".join(ids), retmode="xml")
    root = ET.parse(fetch).getroot()

    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"

        non_academic_authors = []
        company_affiliations = []
        email = ""

        authors = article.findall(".//Author")
        for author in authors:
            name_parts = [
                author.findtext("ForeName") or "",
                author.findtext("LastName") or ""
            ]
            fullname = " ".join(name_parts).strip()

            affiliation = author.findtext(".//Affiliation") or ""
            if "@" in affiliation and not email:
                email = affiliation.split()[-1].strip(".;()")

            if affiliation and is_non_academic(affiliation):
                non_academic_authors.append(fullname)
                company_affiliations.append(affiliation)

        if non_academic_authors:
            results.append(PaperData(
                pubmed_id=pmid,
                title=title,
                publication_date=pub_date,
                non_academic_authors=", ".join(non_academic_authors),
                company_affiliations=", ".join(set(company_affiliations)),
                corresponding_author_email=email
            ))

    df = pd.DataFrame([r.__dict__ for r in results])
    if df.empty:
        print("No non-academic authors found.")
    elif output_file:
        df.to_csv(output_file, index=False)
        print(f"✅ Saved {len(df)} results to {output_file}")
    else:
        print(df.to_string(index=False))
