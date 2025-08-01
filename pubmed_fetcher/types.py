from dataclasses import dataclass

@dataclass
class PaperData:
    pubmed_id: str
    title: str
    publication_date: str
    non_academic_authors: str
    company_affiliations: str
    corresponding_author_email: str
