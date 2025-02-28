import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import google.generativeai as genai
import os

# Configure Google GenAI API (Use environment variables for security)
genai.configure(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

# Initialize LangChain LLM (Using OpenAI model as an example)
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# Function to generate travel recommendations
def generate_travel_plan(source, destination):
    # Prepare the prompt for LangChain
    prompt = f"""
    I am planning a trip from {source} to {destination}.
    Provide travel options including:
    - Flight
    - Train
    - Bus
    - Cab
    Include estimated costs and time durations.
    """

    # LangChain interaction (Correct usage of invoke())
    messages = [
        SystemMessage(content="You are a helpful travel assistant."),
        HumanMessage(content=prompt)
    ]
    response = llm.invoke(messages)

    # Google GenAI (Ensure correct model usage)
    model = genai.GenerativeModel('gemini-pro')
    google_response = model.generate_content(prompt)

    # Combine responses
    return response.content, google_response.text

# Streamlit UI
st.title("🛫 AI-Powered Travel Planner")

# Input: Source and Destination
source = st.text_input("📍 Enter Source Location")
destination = st.text_input("📍 Enter Destination Location")

if st.button("🚀 Find Travel Options"):
    if source and destination:
        langchain_response, google_response = generate_travel_plan(source, destination)

        st.subheader("✈️ Travel Options (LangChain)")
        st.write(langchain_response)

        st.subheader("🤖 Travel Options (Google GenAI)")
        st.write(google_response)
    else:
        st.warning("⚠️ Please enter both source and destination.")
