from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

from tools import read_financial_document
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid



app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str, file_path: str):
    # 1. Read PDF
    document_text = read_financial_document(file_path)

    # 2. Hard limit to avoid crashes
    MAX_CHARS = 8000
    if len(document_text) > MAX_CHARS:
        document_text = document_text[:MAX_CHARS]

    # 3. Create LLM directly (bypass CrewAI crash)
    llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0.2
)


    # 4. Build prompt manually
    prompt = f"""
You are a senior financial analyst.

Here is the financial document:

{document_text}

User question:
{query}

Using ONLY the document content, create a professional financial analysis including:
- Summary of the company / report
- Key financial performance points
- Risks and red flags
- Opportunities
- Final conclusion

IMPORTANT:
- Do NOT invent numbers or facts
- Do NOT use external knowledge
- Base everything strictly on the document
"""

    # 5. Call model
    response = llm.invoke(prompt)

    return response.content


@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze_financial_document_api(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        if not query or query.strip() == "":
            query = "Analyze this financial document for investment insights"

        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
