from typing import TypedDict
from langgraph.graph import StateGraph, END
from crewai import Task, Crew

from agents.symptom_agent import SymptomAgent
from agents.diagnosis_agent import DiagnosisAgent
from agents.diet_agent import DietAgent
from agents.report_agent import ReportAgent


# ----------- DEFINE SHARED STATE -----------
class HealthState(TypedDict):
    input: str
    symptoms: str
    diagnosis: str
    diet: str
    report: str


# ----------- NODE FUNCTIONS (USING CREW + TASK) -----------

def symptom_node(state: HealthState) -> HealthState:
    task = Task(
        description=f"Analyze and interpret these symptoms safely: {state['input']}",
        agent=SymptomAgent,
        expected_output="A structured summary of symptoms."
    )
    crew = Crew(agents=[SymptomAgent], tasks=[task])
    result = crew.kickoff()
    state["symptoms"] = result
    return state


def diagnosis_node(state: HealthState) -> HealthState:
    task = Task(
        description=f"Based on symptoms, determine likely non-medical conditions: {state['symptoms']}",
        agent=DiagnosisAgent,
        expected_output="Possible common conditions with explanation (No medical advice)."
    )
    crew = Crew(agents=[DiagnosisAgent], tasks=[task])
    result = crew.kickoff()
    state["diagnosis"] = result
    return state


def diet_node(state: HealthState) -> HealthState:
    task = Task(
        description=f"Suggest safe foods and hydration guidance for: {state['diagnosis']}",
        agent=DietAgent,
        expected_output="Simple meal plan and precaution suggestions."
    )
    crew = Crew(agents=[DietAgent], tasks=[task])
    result = crew.kickoff()
    state["diet"] = result
    return state


def report_node(state: HealthState) -> HealthState:
    task = Task(
        description=f"Create a friendly, easy-to-read health report based on: {state['diet']}",
        agent=ReportAgent,
        expected_output="Final summarized wellness report."
    )
    crew = Crew(agents=[ReportAgent], tasks=[task])
    result = crew.kickoff()
    state["report"] = result
    return state


# ----------- BUILD THE GRAPH -----------
def create_health_graph():
    graph = StateGraph(state_schema=HealthState)

    graph.add_node("symptom_analysis", symptom_node)
    graph.add_node("diagnosis", diagnosis_node)
    graph.add_node("diet_planning", diet_node)
    graph.add_node("report_generation", report_node)

    graph.set_entry_point("symptom_analysis")
    graph.add_edge("symptom_analysis", "diagnosis")
    graph.add_edge("diagnosis", "diet_planning")
    graph.add_edge("diet_planning", "report_generation")
    graph.add_edge("report_generation", END)

    return graph.compile()


# ----------- OUTPUT CLEANUP -----------
def simplify_answer(answer: str) -> str:
    try:
        return answer.replace("\\n", "\n")
    except:
        return answer


# ----------- MAIN WORKFLOW CALL -----------
def run_health_workflow(user_input: str) -> str:
    try:
        graph = create_health_graph()
        response = graph.invoke({"input": user_input})
        return simplify_answer(response["report"])
    except Exception as e:
        print("[ERROR] workflow execution failed:", e)
        return "⚠️ Something went wrong while processing your request."
