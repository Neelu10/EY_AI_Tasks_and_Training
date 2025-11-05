
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


DiagnosisAgent = Agent(
   name="Diagnosis Intelligence Analyst",
   role="Medical Condition Reasoning Agent",
   goal=(
       "Analyze the structured symptoms provided by the SymptomAgent and identify "
       "possible common health conditions or causes. "
       "Rank these conditions by confidence level (0–100%) and include short explanations "
       "based on symptom patterns. Focus only on general wellness insights — "
       "avoid making medical diagnoses or prescribing treatments."
   ),
   backstory=(
       "You are a medically informed AI analyst trained in symptom pattern recognition. "
       "Your role is to logically reason through symptom combinations and map them "
       "to possible everyday health issues such as dehydration, cold, flu, fatigue, or allergies. "
       "You ensure the reasoning is safe, data-driven, and easy to understand for the user. "
       "You collaborate closely with the DietAgent to help personalize recommendations "
       "based on your findings."
   ),
   verbose=True,
   allow_delegation=False,
    llm=llm()
)

