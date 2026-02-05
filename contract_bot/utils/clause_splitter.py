import re

def split_clauses(text):
    clauses = re.split(r'\n\d+\.|\n[A-Z][A-Z ]+:|\n•', text)

    cleaned = []
    for c in clauses:
        c = c.strip()
        if len(c) > 40:
            cleaned.append(c)

    return cleaned
