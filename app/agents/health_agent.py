from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.rag.vector_store import create_vector_store


def get_health_agent():
    """
    Creates a Healthcare AI RAG Agent using Google Gemini.
    """

    # Create vector store retriever
    retriever = create_vector_store()

    # Create Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )

    # Prompt for healthcare assistant
    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful Personal Health Assistant.

        Use the following healthcare information to answer the user's question.

        Context:
        {context}

        User Question:
        {question}

        Instructions:
        - Give a clear and simple answer.
        - Do not make a diagnosis.
        - Do not prescribe medicines.
        - If the information is not available in the context, say that you
          do not have enough information.
        - Encourage the user to consult a qualified healthcare professional
          for serious or emergency concerns.

        Answer:
        """
    )

    # Create the RAG chain
    def health_agent(inputs):
        question = inputs["question"]

        # Search relevant healthcare information
        documents = retriever.invoke(question)

        # Combine retrieved documents
        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        # Generate answer
        response = llm.invoke(
            prompt.format_messages(
                context=context,
                question=question,
            )
        )

        return response.content

    return health_agent