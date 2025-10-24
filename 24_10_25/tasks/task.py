import os
import json
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

# 3. Define prompt templates
summary_prompt = ChatPromptTemplate.from_template(
    "<s>[INST] Summarize the following topic in simple terms for a beginner: '{topic}'. Keep it short and clear.[/INST]</s>"
)

quiz_prompt = ChatPromptTemplate.from_template(
    "<s>[INST] Generate 3 quiz questions (without answers) to test understanding of the topic: '{topic}'. Keep them simple and relevant.[/INST]</s>"
)

# 4. Define parser
parser = StrOutputParser()


# 5. Create reusable generation functions
def generate_summary(topic: str) -> str:
    chain = summary_prompt | llm | parser
    return chain.invoke({"topic": topic})


def generate_quiz(topic: str) -> str:
    chain = quiz_prompt | llm | parser
    return chain.invoke({"topic": topic})


# 6. Main execution flow
user_topic = input("Enter a topic to summarize and generate quiz: ").strip()

summary = generate_summary(user_topic)
quiz = generate_quiz(user_topic)

print("\n--- SUMMARY ---\n")
print(summary)

print("\n--- QUIZ QUESTIONS ---\n")
print(quiz)

# 7. Log results
os.makedirs("logs", exist_ok=True)

log_entry = {
    "timestamp": datetime.now().isoformat(),
    "topic": user_topic,
    "summary": summary,
    "quiz": quiz,
}

with open("logs/sequential_chain_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(log_entry) + "\n")

print("\nResults logged to logs/sequential_chain_log.jsonl")