from datetime import datetime
import re


def process_query(query: str) -> str:
    query = query.lower().strip()

    # --- Math operation ---
    math_match = re.findall(r"(\d+)\s*(?:\+|add|and)\s*(\d+)", query)
    if math_match:
        a, b = map(int, math_match[0])
        return f"The sum of {a} and {b} is {a + b}."

    # --- Reverse word ---
    if "reverse" in query:
        word_match = re.findall(r"reverse (?:this word:|word:)?\s*([a-zA-Z]+)", query)
        if word_match:
            word = word_match[0]
            return f"The reverse of '{word}' is '{word[::-1]}'."

    # --- Date / Time query ---
    if "date" in query or "today" in query:
        today = datetime.now().strftime("%A, %d %B %Y")
        return f"Today's date is {today}."

    # --- CrewAI / LLM fallback (optional integration) ---
    try:
        from langchain.chat_models import ChatOpenAI
        llm = ChatOpenAI(model_name="mistralai/mistral-7b-instruct", temperature=0)
        response = llm.predict(f"Answer this concisely: {query}")
        return response
    except Exception:
        pass

    return "Sorry, I couldn’t understand that. Try asking something like 'Add 10 and 20' or 'Reverse this word: Hello'."
