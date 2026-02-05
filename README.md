# 📄 Contract Analysis & Risk Assessment Bot (GenAI Legal Assistant)

## 🚀 Overview

The Contract Analysis & Risk Assessment Bot is a GenAI-powered legal assistant designed to help Small and Medium Businesses (SMEs) understand complex legal contracts in simple business language.

Legal documents are often difficult to interpret for non-lawyers, leading to hidden risks, unfair clauses, and financial losses.  
This system automatically analyzes contracts, detects risky clauses, explains them clearly, and suggests safer alternatives.

---

## 🎯 Problem Statement

Small businesses frequently sign:

- Employment Agreements
- Vendor Contracts
- Lease Agreements
- Service Contracts
- Partnership Deeds

Without legal expertise, they may miss:

❌ Indemnity risks  
❌ Hidden penalties  
❌ Unilateral termination  
❌ Non-compete restrictions  
❌ IP ownership transfer  

This creates legal and financial risks.

---

## ✅ Solution

This project uses **NLP + Generative AI** to:

1. Read contracts (PDF/DOCX/TXT)
2. Extract clauses
3. Detect legal entities
4. Identify obligations & liabilities
5. Calculate risk scores
6. Explain clauses in simple English
7. Suggest safer alternatives
8. Generate downloadable reports

---

## ✨ Key Features

### 📂 File Support
- PDF
- DOCX
- TXT

### 🧠 NLP Capabilities
- Clause extraction
- Named Entity Recognition (Parties, Dates, Money)
- Obligation vs Right vs Prohibition detection

### ⚠ Risk Assessment
- Clause-level risk scoring (Low / Medium / High)
- Detects:
  - Indemnity
  - Penalty clauses
  - Non-compete
  - Auto-renewal
  - Lock-in periods
  - Arbitration & jurisdiction
  - IP transfer

### 🤖 AI Assistance
- Plain English explanations
- Risk highlights
- Suggested improvements

### 📑 Outputs
- Clause-by-clause insights
- Risk dashboard
- PDF export report
- JSON audit logs

---

## 🛠 Tech Stack

| Component | Technology |
|----------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| NLP | spaCy, NLTK |
| AI Reasoning | GPT (optional) / Rule-based |
| File Parsing | pdfplumber, python-docx |
| Reports | ReportLab |
| Storage | JSON logs |

---

## 📁 Project Structure

