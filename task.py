from crewai import Task
from agents import financial_analyst

analyze_financial_document = Task(
    description=(
        "You are given the following financial document content:\n\n"
        "{document_text}\n\n"
        "User question:\n"
        "{query}\n\n"
        "Using ONLY the document content, create a professional financial analysis including:\n"
        "- Summary of the company / report\n"
        "- Key financial performance points\n"
        "- Risks and red flags\n"
        "- Opportunities\n"
        "- Final conclusion\n\n"
        "IMPORTANT RULES:\n"
        "- Do NOT invent numbers or facts\n"
        "- Do NOT use external knowledge\n"
        "- Base everything strictly on the document\n"
        "- If something is missing, clearly state it is not available in the document\n"
    ),
    expected_output=(
        "A structured, professional financial analysis with clear sections, insights, risks, "
        "opportunities, and conclusions strictly based on the provided document."
    ),
    agent=financial_analyst,
    tools=[],   # ✅ NO TOOLS
    async_execution=False
)
