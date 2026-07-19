from langchain_google_genai import ChatGoogleGenerativeAI
from app.rag.vector_store import create_vector_store


def get_health_agent():
    """
    Creates a Healthcare AI Agent using Google Gemini.
    """

    retriever = create_vector_store()

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )

    return retriever, llm