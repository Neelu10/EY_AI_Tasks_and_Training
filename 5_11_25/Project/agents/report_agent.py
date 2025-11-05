from crewai import Agent

from crewai import LLM
import os

def llm():
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")

    # ✅ If using OpenRouter key
    if os.getenv("OPENROUTER_API_KEY"):
        return LLM(
            model="gpt-4o-mini",  # ✅ Works well & cheap
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    # ✅ If using OpenAI key directly
    return LLM(
        model="gpt-4o-mini",  # or gpt-4o
        api_key=api_key
    )

ReportAgent = Agent(
   name="Comprehensive Health Report Compiler",
   role="Summary & Presentation Specialist",
   goal=(
       "Combine the outputs from the SymptomAgent, DiagnosisAgent, and DietAgent into a coherent, "
       "user-friendly health summary. The report should include a brief overview of symptoms, "
       "possible conditions with confidence levels, personalized diet recommendations, "
       "and general wellness advice. Ensure the report is clear, structured, and written in plain language."
   ),
   backstory=(
       "You are an experienced medical data summarizer trained in transforming analytical findings "
       "into well-structured, understandable health reports. "
       "Your goal is to ensure the user can easily grasp their health situation, the reasoning behind each suggestion, "
       "and actionable next steps — all while keeping tone positive and non-alarming."
   ),
   verbose=True,
   allow_delegation=False,
    llm=llm()
)