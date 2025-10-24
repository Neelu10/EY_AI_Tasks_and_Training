import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import streamlit as st

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    st.error("OPENROUTER_API_KEY not found in .env file")
    st.stop()

llm = ChatOpenAI(
    model="moonshotai/kimi-dev-72b:free",
    temperature=0.7,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)

#UI
st.title("LangChain OpenRouter AI Chat")
user_input = st.text_area("Enter your prompt:")

if st.button("Get Response"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt!")
    else:
        messages = [
            SystemMessage(content="You are a helpful and concise AI assistant."),
            HumanMessage(content=f"<s>[INST] Explain in simple terms how convolutional neural networks work. [/INST]</s>")
        ]
        try:
            response = llm.invoke(messages)
            st.subheader("Assistant Response:")
            st.write(response.content.strip() or "(no content returned)")
        except Exception as e:
            st.error(f"Error: {e}")