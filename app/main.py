import streamlit as st
import os
import sys

from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# Project Path Setup
# -----------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))

if current_dir not in sys.path:
    sys.path.append(current_dir)

if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# -----------------------------
# Import Vector Store

# -----------------------------
try:
    from rag.vector_store import create_vector_store
except ModuleNotFoundError:
    from app.rag.vector_store import create_vector_store

# -----------------------------
# Import Health AI Agent
# -----------------------------
try:
    from agents.health_agent import get_health_agent
except ModuleNotFoundError:
    from app.agents.health_agent import get_health_agent

# -----------------------------
# Streamlit Page Settings
# -----------------------------
st.set_page_config(
    page_title="Health Assistant",
    page_icon="🏥"
)

st.title("🏥 My Personal Health Assistant")

# --- NEW SEARCH ENGINE TESTER ---
with st.expander("🛠️ Developer Debug: Test Vector Search Engine"):
    user_test_query = st.text_input("Type a keyword to search your text file (e.g., Crocin):", key="test_search")
    
    if user_test_query:
        # Build the vector search pipeline
        retriever = create_vector_store()
        # Find the 2 closest matches in our health guide text file
        matched_chunks = retriever.get_relevant_documents(user_test_query)
        
        st.write(f"🔍 **Search engine found {len(matched_chunks)} matching segments:**")
        for idx, doc in enumerate(matched_chunks):
            st.info(f"**Segment {idx + 1}:**\n{doc.page_content}")
# ---------------------------------

st.write("Welcome! Let's track your health and medications.")

# ==========================================
# AI Health Assistant
# ==========================================

st.divider()

st.subheader("💬 Ask Your Personal Health Assistant")

user_question = st.text_input(
    "Ask a health-related question:",
    placeholder="Example: What is fever?"
)

if st.button("Get Answer"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching health guide..."):

            # Load the AI agent
            agent = get_health_agent()

            # Ask the AI
            response = agent.invoke({
                "input": user_question
            })

            # Display the answer
            st.success("Answer")

            st.write(response["answer"])