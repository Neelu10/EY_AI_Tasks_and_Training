from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

# Define tools or chains for each agent
def extract_data_tool(input_text):
    return f"Extracted data from: {input_text}"

def summarize_tool(data):
    return f"Summary: {data[:50]}..."

def email_tool(summary):
    return f"Email sent with content: {summary}"

# Wrap tools as LangChain Tools
tools = [
    Tool(name="DataExtractor", func=extract_data_tool, description="Extracts data from text"),
    Tool(name="Summarizer", func=summarize_tool, description="Summarizes extracted data"),
    Tool(name="EmailSender", func=email_tool, description="Sends summary via email")
]

# Initialize agent
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.2,
    max_tokens=300,
    api_key=api_key,
    base_url=base_url,
)
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

# Run agent chaining
input_text = "Customer feedback document"
response = agent.run(input_text)
print(response)