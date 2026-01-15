# 📊 Financial Document Analyzer  
## 🛠️ CrewAI Debug Assignment → Production-Ready AI System

**Author:** Nancy Dua  
**Program:** BTech CSE (Generative AI / Data )  
**Context:** VWO Internship Debug Challenge + System Stabilization Project

---

## 🧠 Project Overview

This project is a **complete rescue, refactor, and production-hardening** of a severely broken AI-based financial document analysis system originally built using CrewAI.

The original system:

- ❌ Crashed on startup  
- ❌ Used CrewAI tools incorrectly  
- ❌ Failed Pydantic validation  
- ❌ Did not actually read PDFs  
- ❌ Hallucinated financial data  
- ❌ Had dependency and environment conflicts  
- ❌ Was completely unusable in real environments  

---

## ✅ What This Project Is Now

This repository contains a **fully fixed, stable, production-like backend** that:

- 📄 Accepts financial PDF documents  
- 🔍 Extracts text deterministically  
- 🧠 Uses LLM only for reasoning (not hallucination)  
- 📊 Produces structured financial analysis:
  - Summary
  - Performance
  - Risks
  - Opportunities
  - Conclusion
- ⚡ Runs on FastAPI  
- 🆓 Uses **Groq LLaMA 3.1 Free API** (no paid OpenAI needed)  
- 🛡️ Safely handles large documents  
- 🧱 Has a clean, debuggable architecture  

---

## 🧨 Phase 1 — Bugs in the Original CrewAI System

### 1. Broken CrewAI Tool System
- Tools were passed as functions instead of `BaseTool` objects
- Caused **Pydantic validation crashes**
- API could not start

### 2. PDF Reader Was Not Working
- File path never reached the agent
- No real document content was ever analyzed

### 3. Task Input Mismatch
- Task expected `{file_path}` but received nothing
- Result: **hallucinated output**

### 4. Hallucination-Promoting Prompts
Prompts encouraged:
- Making up URLs  
- Making up numbers  
- Fake financial analysis  

### 5. Dependency & Environment Conflicts
- CrewAI, LangChain, OpenTelemetry, etc. conflicted
- Project could not be installed cleanly
- Conda + venv mixed → total chaos

---

## 🔧 Phase 2 — Fixes Implemented (CrewAI Stabilization)

- ❌ Removed broken CrewAI tool system
- ✅ Implemented deterministic PDF reading using PyPDF
- ✅ Extract document text **before** calling any AI
- ✅ CrewAI used **only for reasoning**
- ✅ Prompts rewritten to:
  - Forbid hallucinations
  - Enforce document-only analysis
  - Produce professional structured output
- ✅ Simplified architecture
- ✅ API now starts and runs reliably

---

## 🚀 Phase 3 — Production Hardening & Modernization

### 6. CrewAI Pipeline Instability
**Fix:**  
Bypassed unstable CrewAI orchestration and implemented a **direct controlled LLM pipeline**.

---

### 7. Prompt Template Variable Crash (500 Error)
**Fix:**  
Rebuilt prompt injection pipeline and safely inserted extracted text.

---

### 8. PDF Size / Token Overflow Crashes
**Fix:**  
Hard limit: **8000 characters** before sending to LLM.

---

### 9. OpenAI API Failures (401 / 429 / Quota)
**Fix:**  
Replaced OpenAI with **Groq LLaMA 3.1 Free API**

Model used:
llama-3.1-8b-instant

---

### 10. Environment & Dependency Hell
**Fix:**
- Fully isolated project into `venv`
- Clean reinstall of all packages
- Single stable dependency stack

---

### 11. LangChain Version Conflicts
**Fix:**
- Removed unnecessary LangChain stack
- Simplified direct LLM integration

---

### 12. FastAPI File Upload Crashes
**Fix:**
- Proper file validation
- Temporary file handling
- Exception-safe PDF parsing

---

### 13. Import & Startup Failures
**Fix:**
- Refactored folder structure
- Fixed circular imports
- Simplified boot process

---

## 🏗️ Final Architecture

project/
│── main.py # FastAPI server
│── analyzer.py # LLM logic
│── pdf_utils.py # PDF extraction
│── requirements.txt
│── .env
│── venv/

