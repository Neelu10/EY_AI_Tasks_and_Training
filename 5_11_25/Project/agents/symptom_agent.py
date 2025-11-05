from crewai import Agent
from crewai import LLM
import os

def llm():
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")

    # ✅ If using OpenRouter key
    if os.getenv("OPENROUTER_API_KEY"):
        return LLM(
            model="openrouter/mistralai/mistral-7b-instruct",  # ✅ Works well & cheap
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    # ✅ If using OpenAI key directly
    return LLM(
        model="openrouter/mistralai/mistral-7b-instruct",  # or gpt-4o
        api_key=api_key
    )


SymptomAgent=Agent(
    name="Symptom Intelligence Specialist",
    role=" Health Symptom Interpreter",
    goal=(
        "Analyze and extract key medical details from user input such as"
         "symptoms,duration,severity,allergies,age and lifestyle context."
        " Ensure the output is structured,medically relevant, and easy to interpret."),

backstory=(
       "You are a highly trained digital health assistant specializing in "
       "understanding user-described symptoms in natural language. "
       "You focus on capturing the user's health context — like duration, "
       "severity, and possible triggers — to help other agents perform accurate diagnosis and diet planning. "
       "You never provide direct medical treatment advice but always ensure accuracy in symptom interpretation."
   ),
   verbose=True,
   allow_delegation=False,
    llm=llm() # Keeps this agent focused on extraction task only
)

