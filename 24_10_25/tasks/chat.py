import os
import json
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 1. Load environment variables
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY missing in .env")

# 2. Initialize model (Mistral via OpenRouter)
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    max_tokens=512,
    api_key=api_key,
    base_url=base_url,
)

# 3. Conversation memory (local to this session)
conversation_history = [
    SystemMessage(content="You are a friendly and concise AI assistant.")
]

# 4. Chat loop
print("=== Start Chatting with Memory ===")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    # Add user message to history
    conversation_history.append(HumanMessage(content=user_input))

    # Get model response
    response = llm.invoke(conversation_history)
    assistant_reply = response.content

    print(f"\nAssistant: {assistant_reply}\n")

    # Add assistant message to history
    conversation_history.append(AIMessage(content=assistant_reply))

# 5. Log conversation at end of chat
os.makedirs("logs", exist_ok=True)

log_entry = {
    "timestamp": datetime.now().isoformat(),
    "conversation": [
        {"role": msg.type, "content": msg.content} for msg in conversation_history
    ],
}

with open("logs/memory_chat_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(log_entry) + "\n")

print("\nConversation logged to logs/memory_chat_log.jsonl")