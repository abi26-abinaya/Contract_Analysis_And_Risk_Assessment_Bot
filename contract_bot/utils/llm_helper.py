def explain_clause(clause):

    text = clause.lower()

    risk_note = ""

    if "indemnify" in text:
        risk_note = "This clause transfers legal liability to you. This is risky."

    elif "terminate without notice" in text:
        risk_note = "Other party can end contract anytime. High business risk."

    elif "non-compete" in text:
        risk_note = "You may not work with competitors. Limits your freedom."

    elif "penalty" in text:
        risk_note = "Financial penalties may apply. Check carefully."

    else:
        risk_note = "This clause defines responsibilities and terms."

    simple = clause[:300]

    return f"""
Explanation:
{simple}

Risk Note:
{risk_note}

Suggested Action:
Negotiate or clarify wording if risky.
"""
