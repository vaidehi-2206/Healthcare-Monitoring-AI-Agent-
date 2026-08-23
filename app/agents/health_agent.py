import os
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_agent

from rag.vector_store import create_vector_store


# Create the retriever
retriever = create_vector_store()


@tool
def medical_knowledge_search(query: str) -> str:
    """Search the medical knowledge database for health information."""
    
    docs = retriever.invoke(query)

    if not docs:
        return "No relevant medical information was found."

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


# Create Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
)


# Tools available to the agent
tools = [
    medical_knowledge_search
]


# Create the healthcare agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
You are a helpful Personal Health Assistant.

Your job is to answer health-related questions using the medical
knowledge available through the medical_knowledge_search tool.

Instructions:

1. Search the medical knowledge database before answering.
2. Give simple and clear answers.
3. Do not make a diagnosis.
4. Do not prescribe medicines.
5. Do not invent medical information.
6. If the medical database does not contain enough information,
   clearly say that there is not enough information available.
7. For serious or emergency symptoms, recommend consulting
   a qualified healthcare professional.
"""
)


def get_health_agent():
    """Return the healthcare AI agent."""
    return agent