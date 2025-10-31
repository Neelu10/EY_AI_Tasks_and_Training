# summarizer_tool.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.2,
    max_tokens=300,
    api_key=api_key,
    base_url=base_url,
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def summarize_text(text: str) -> str:
    prompt = (
        "You are a clear, concise summarizer. Summarize the following text in 3-6 short sentences:\n\n"
        f"{text}\n\nSummary:"
    )
    response = llm.invoke(prompt)
    return response.content.strip()

def summarize_history() -> str:
    messages = memory.load_memory_variables({}).get("chat_history", [])
    if not messages:
        return "No conversation history to summarize."
    # join last N messages
    concat = "\n".join([m.content for m in messages[-10:]])
    return summarize_text(concat)

if __name__ == "__main__":
    print("=== Summarizer Tool ===\nCommands:\n - summarize <text>\n - summarize_history\n - exit\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break
        if user_input.lower().startswith("summarize_history"):
            out = summarize_history()
            print("Agent:", out)
            memory.save_context({"input": user_input}, {"output": out})
            continue
        if user_input.lower().startswith("summarize"):
            text = user_input[len("summarize"):].strip()
            if not text:
                print("Agent: Please provide text after 'summarize'.")
                continue
            out = summarize_text(text)
            print("Agent:", out)
            memory.save_context({"input": user_input}, {"output": out})
            continue
        # fallback: ask LLM for a short summary of the user input
        try:
            out = summarize_text(user_input)
            print("Agent:", out)
            memory.save_context({"input": user_input}, {"output": out})
        except Exception as e:
            print("Error:", e)
