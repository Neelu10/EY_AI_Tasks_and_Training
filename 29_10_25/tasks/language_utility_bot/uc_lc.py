# ============================================================
# Memory-Tools.py — Conversational Mistral Agent (fully working)
# ============================================================

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory


# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")


# ------------------------------------------------------------
# 2. Initialize the Mistral model via OpenRouter
# ------------------------------------------------------------
llm = ChatOpenAI(
    model="google/gemma-3n-e4b-it:free",
    temperature=0.4,
    max_tokens=512,
    api_key=api_key,
    base_url=base_url,
)


# ------------------------------------------------------------
# 3. Define helper tools
# ------------------------------------------------------------
def change_case(text: str,mode:str) -> str:
    """Convert text to uppercase or lowercase"""
    if mode == "upper":
        return text.upper()
    elif mode == "lower":
        return text.lower()
    else:
        return "Invalid mode.Use upper or lower case"


# ------------------------------------------------------------
# 4. Initialize memory
# ------------------------------------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# ------------------------------------------------------------
# 5. Conversational loop
# ------------------------------------------------------------
print("\n=== Start chatting with your Agent ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    try:
        #Case Change
        if user_input.lower().startswith("upper"):
            text = user_input[len("upper"):].strip()
            result = change_case(text, "upper")
            print("Agent:", result)
            memory.save_context({"input": user_input}, {"output": result})
            continue

        if user_input.lower().startswith("lower"):
            text = user_input[len("lower"):].strip()
            result = change_case(text, "lower")
            print("Agent:", result)
            memory.save_context({"input": user_input}, {"output": result})
            continue

        # Default: use LLM
        response = llm.invoke(user_input)
        print("Agent:", response.content)
        memory.save_context({"input": user_input}, {"output": response.content})

    except Exception as e:
        print("Error:", e)