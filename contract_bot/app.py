import streamlit as st

from utils.extractor import extract_text
from utils.clause_splitter import split_clauses
from utils.ner import extract_entities
from utils.risk_engine import risk_score, clause_type
from utils.llm_helper import explain_clause
from utils.report_generator import generate_pdf
from utils.audit_logger import save_audit


st.title("📄 Contract Risk Assessment Bot (GenAI Legal Assistant)")

file = st.file_uploader("Upload Contract", type=["pdf", "docx", "txt"])

if file:

    text = extract_text(file, file.name)

    entities = extract_entities(text)

    st.subheader("🔎 Extracted Entities")
    st.write(entities)

    clauses = split_clauses(text)

    results = []

    st.subheader("📑 Clause Analysis")

    for clause in clauses:

        risk = risk_score(clause)
        ctype = clause_type(clause)

        explanation = explain_clause(clause)

        st.markdown("---")
        st.write(f"### Risk: {risk}")
        st.write(f"Type: {ctype}")
        st.write(explanation)

        results.append({
            "clause": clause,
            "risk": risk,
            "type": ctype,
            "explanation": explanation
        })


    if st.button("Generate PDF Report"):
        filename = generate_pdf(results)
        st.success("Report Generated!")
        st.download_button("Download Report", open(filename, "rb"), filename)


    save_audit(results)
