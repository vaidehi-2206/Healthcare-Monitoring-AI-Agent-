from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_agent

from services.medicine_service import (
    search_medicines,
    format_medicine_results,
)
load_dotenv()

# --------------------------------------------------
# Medicine search tool
# --------------------------------------------------

@tool
def medicine_database_search(query: str) -> str:
    """
    Search the medicine database by medicine name or purpose.
    """

    results = search_medicines(query)

    return format_medicine_results(results)


# --------------------------------------------------
# Gemini model
# --------------------------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
)


# --------------------------------------------------
# Tools
# --------------------------------------------------

tools = [
    medicine_database_search
]



# --------------------------------------------------
# Medication Agent
# --------------------------------------------------

medication_agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
You are a Medication Information Assistant.

Your job is to provide information from the medicine database.

IMPORTANT RULES:

1. Always search the medicine database before answering
   medicine-related questions.

2. Only use information returned by the medicine database.

3. Do not invent medicine information.

4. Do not diagnose the user.

5. Do not prescribe medicines.

6. Do not make personalized dosage decisions.

7. If a medicine is not found in the database, clearly say:
   "This medicine is not available in my medicine database."

8. You may explain the information contained in the database
   in simple language.

9. If the user asks whether they personally should take a medicine,
   recommend consulting a qualified healthcare professional.

10. If the user describes a serious or emergency situation,
    recommend seeking appropriate medical care.

Always distinguish between:
- information stored in the database
- personalized medical advice

The medicine database contains information such as:
medicine name, purpose, strength, listed dosage,
frequency, and whether it is listed as being taken after food.
"""
)


def get_medication_agent():
    """Return the Medication Agent."""
    return medication_agent