import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_openai import ChatOpenAI

# ================================
# 🔐 Load LLM
# ================================
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

# ================================
# 📊 Financial Analyst Agent
# ================================
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal=(
        "Analyze the provided financial document text and answer the user's query "
        "with a professional, structured financial analysis."
    ),
    backstory=(
        "You are a senior financial analyst working in an investment firm. "
        "You rely strictly on the provided document content and do not hallucinate data."
    ),
    verbose=True,
    memory=False,
    tools=[],   # ✅ NO TOOLS (IMPORTANT)
    llm=llm,
    max_iter=3,
    allow_delegation=False
)

# ================================
# 🧾 Document Verifier Agent
# ================================
document_verifier = Agent(
    role="Financial Document Verification Specialist",
    goal="Verify whether the provided text looks like a valid financial document.",
    backstory="You are a financial audit specialist.",
    verbose=True,
    memory=False,
    tools=[],   # ✅ NO TOOLS
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# ================================
# 💰 Investment Advisor Agent
# ================================
investment_advisor = Agent(
    role="Investment Strategy Advisor",
    goal="Propose sensible investment strategies based on the provided analysis.",
    backstory="You are a certified investment advisor.",
    verbose=True,
    memory=False,
    tools=[],   # ✅ NO TOOLS
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# ================================
# ⚠️ Risk Assessor Agent
# ================================
risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Identify financial and business risks from the provided document.",
    backstory="You are a corporate risk management expert.",
    verbose=True,
    memory=False,
    tools=[],   # ✅ NO TOOLS
    llm=llm,
    max_iter=2,
    allow_delegation=False
)
