from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict

from langgraph.graph import StateGraph, END

from langchain_google_genai import ChatGoogleGenerativeAI

from rag.rag import search_hr_knowledge

from tools.hr_tools import (
    calculate_match_score,
    generate_interview_questions,
    create_interview_ticket
)


class HRState(TypedDict):

    resume: str
    job_description: str
    candidate_name: str

    knowledge: str
    result: str


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)


def analyze_resume(state: HRState):

    resume = state["resume"]
    job = state["job_description"]

    knowledge = search_hr_knowledge(
        "HR recruitment requirements and interview guidelines"
    )

    prompt = f"""
You are an AI HR Recruitment Assistant.

Analyze the candidate resume against the job description.

RESUME:
{resume}

JOB DESCRIPTION:
{job}

HR KNOWLEDGE:
{knowledge}

Provide:

1. Candidate skills
2. Required job skills
3. Matching skills
4. Missing skills
5. Match percentage
6. Candidate strengths
7. Candidate weaknesses
8. Recommendation
9. Interview questions

Do not invent information that is not present
in the resume.
"""

    response = llm.invoke(prompt)

    return {
        "knowledge": knowledge,
        "result": response.content
    }


def create_graph():

    graph = StateGraph(HRState)

    graph.add_node(
        "analyze_resume",
        analyze_resume
    )

    graph.set_entry_point(
        "analyze_resume"
    )

    graph.add_edge(
        "analyze_resume",
        END
    )

    return graph.compile()