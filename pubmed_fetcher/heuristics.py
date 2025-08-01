def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ['university', 'college', 'school', 'institute', 'hospital', 'center', 'centre', 'dept', 'department']
    return not any(word in affiliation.lower() for word in academic_keywords)
