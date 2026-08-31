
import streamlit as st
import os
import sys
from dotenv import load_dotenv

# Load environment variables
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
# Import Health AI Agent
# -----------------------------
try:
    from agents.health_agent import get_health_agent
except ModuleNotFoundError:
    from app.agents.health_agent import get_health_agent

# -----------------------------
# Create AI Agent
# -----------------------------
agent = get_health_agent()

# -----------------------------
# Streamlit Page Settings
# -----------------------------
st.set_page_config(
    page_title="Healthcare Monitoring AI Agent",
    page_icon="🏥",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.title("🏥 Healthcare Monitoring AI Agent")

st.write(
    "Ask healthcare-related questions and get AI-powered "
    "information using a medical knowledge base."
)

st.divider()

# -----------------------------
# Health Assistant
# -----------------------------
st.subheader("💬 Ask Your Health Assistant")

user_question = st.text_area(
    "Enter your question:",
    placeholder="Example: What are the symptoms of fever?",
    height=100
)

if st.button("🔍 Get Answer", use_container_width=True):

    if user_question.strip():

        with st.spinner("🤖 Finding the best answer..."):

            try:
                result = agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": user_question
                            }
                        ]
                    }
                )

                response = result["messages"][-1].content

                # Convert Gemini/LangChain response to normal text
                if isinstance(response, list):
                    text_parts = []

                    for item in response:
                        if isinstance(item, dict):
                            if "text" in item:
                                text_parts.append(item["text"])
                        else:
                            text_parts.append(str(item))

                    response = "\n".join(text_parts)

                st.subheader("🤖 AI Response")
                st.write(response)

            except Exception as e:
                st.error("❌ Error while processing your question:")
                st.exception(e)

    else:
        st.warning("⚠️ Please enter a health-related question.")

# -----------------------------
# Health Disclaimer
# -----------------------------
st.divider()

st.warning(
    "⚠️ Health Disclaimer: This AI assistant provides general "
    "health information for educational purposes only. It is not "
    "a substitute for professional medical advice, diagnosis, or treatment."
)

st.caption("Healthcare Monitoring AI Agent • Powered by AI + RAG")


