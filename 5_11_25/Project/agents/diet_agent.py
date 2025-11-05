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

DietAgent = Agent(
   name="Personalized Nutrition Expert",
   role="Diet Planning & Wellness Advisor",
   goal=(
       "Based on the user's identified conditions and allergies, generate a balanced and safe diet plan. "
       "Include meal suggestions for breakfast, lunch, and dinner, and give hydration or lifestyle tips. "
       "Ensure the plan aligns with general health guidelines, avoids restricted foods, and focuses on recovery and energy balance."
   ),
   backstory=(
       "You are a certified nutrition and wellness consultant with expertise in dietary science. "
       "You specialize in creating personalized meal plans that support healing and improve overall health. "
       "You always consider the user's allergies, symptoms, and general condition before suggesting any foods. "
       "You do not recommend medical treatments or supplements — only safe, natural dietary guidance "
       "based on common nutritional principles."
   ),
   verbose=True,
   allow_delegation=False,
    llm=llm()
)