HIGH_RISK = [
    "indemnify",
    "unlimited liability",
    "terminate without notice",
    "penalty",
    "non-compete",
    "exclusive rights",
    "auto renew",
    "ip transfer"
]

MEDIUM_RISK = [
    "arbitration",
    "lock-in",
    "jurisdiction",
    "confidentiality breach",
    "late fee"
]


def clause_type(clause):

    c = clause.lower()

    if "shall" in c or "must" in c:
        return "Obligation"
    if "may" in c:
        return "Right"
    if "shall not" in c or "prohibited" in c:
        return "Prohibition"

    return "General"


def risk_score(clause):

    score = 0
    text = clause.lower()

    for word in HIGH_RISK:
        if word in text:
            score += 3

    for word in MEDIUM_RISK:
        if word in text:
            score += 1

    if score >= 3:
        return "High"
    elif score >= 1:
        return "Medium"
    else:
        return "Low"
