"""
tools.py

Refactored version of the original company-provided tools.
Original design intent:
- Search tool
- PDF document reader
- Investment analysis helper
- Risk assessment helper

We removed async + CrewAI coupling to make it stable, testable, and production-ready.
"""

import os
import re
from pypdf import PdfReader

# =========================
# 🔍 Search Tool (Optional Utility)
# =========================
try:
    from crewai_tools import SerperDevTool
    search_tool = SerperDevTool()
except:
    search_tool = None  # Allows project to run even if Serper is not configured


# =========================
# 📄 Financial Document Reader
# =========================
def read_financial_document(path: str = "data/sample.pdf") -> str:
    """
    Reads and extracts text from a PDF file.

    Args:
        path (str): Path to PDF file

    Returns:
        str: Cleaned full document text
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    reader = PdfReader(path)
    full_report = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            full_report += content + "\n"

    return clean_text(full_report)


# =========================
# 🧹 Text Cleaner (From original logic)
# =========================
def clean_text(text: str) -> str:
    """
    Cleans document text:
    - Removes double spaces
    - Removes excessive newlines
    """
    if not text:
        return ""

    # Normalize newlines
    text = text.replace("\r", "\n")

    # Remove excessive blank lines
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")

    # Remove double spaces
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


# =========================
# 📊 Investment Analysis Helper (From original intent)
# =========================
def analyze_investment(financial_document_data: str) -> dict:
    """
    Basic deterministic preprocessing for investment analysis.
    Actual reasoning is done by the LLM agent.
    """
    if not financial_document_data:
        return {
            "status": "error",
            "message": "No financial data provided"
        }

    text = financial_document_data.lower()

    insights = {
        "mentions_revenue": "revenue" in text,
        "mentions_profit": "profit" in text,
        "mentions_loss": "loss" in text,
        "mentions_debt": "debt" in text or "liability" in text,
        "mentions_cashflow": "cash flow" in text,
        "document_length": len(financial_document_data),
    }

    return {
        "status": "ok",
        "signals": insights
    }


# =========================
# ⚠️ Risk Assessment Helper (From original intent)
# =========================
def assess_risk(financial_document_data: str) -> list:
    """
    Extracts simple risk flags from the document.
    """
    if not financial_document_data:
        return []

    risk_keywords = [
        "loss", "decline", "decrease", "risk", "uncertain",
        "lawsuit", "debt", "liability", "bankruptcy", "volatility"
    ]

    found = []
    text = financial_document_data.lower()

    for word in risk_keywords:
        if word in text:
            found.append(word)

    return found


# =========================
# 📦 Full Processing Pipeline
# =========================
def load_and_process_document(path: str = "data/sample.pdf") -> dict:
    """
    Complete pipeline replacing the old broken tool system.
    """
    text = read_financial_document(path)

    return {
        "text": text,
        "investment_signals": analyze_investment(text),
        "risk_flags": assess_risk(text)
    }
# =========================
# 🔧 CrewAI Tool Alias (Compatibility Layer)
# =========================

# CrewAI expects a callable tool named like this
financial_document_tool = read_financial_document
