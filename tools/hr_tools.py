from langchain_core.tools import tool


@tool
def calculate_match_score(
    resume_skills: str,
    job_skills: str
) -> str:
    """
    Calculates approximate matching percentage
    between resume skills and job skills.
    """

    resume = {
        skill.strip().lower()
        for skill in resume_skills.split(",")
        if skill.strip()
    }

    job = {
        skill.strip().lower()
        for skill in job_skills.split(",")
        if skill.strip()
    }

    if not job:
        return "Match score cannot be calculated."

    matched = resume.intersection(job)

    score = (len(matched) / len(job)) * 100

    missing = job - resume

    return f"""
Match Score: {score:.2f}%

Matched Skills:
{", ".join(matched) if matched else "None"}

Missing Skills:
{", ".join(missing) if missing else "None"}
"""


@tool
def generate_interview_questions(
    skills: str
) -> str:
    """
    Generates interview question topics based on candidate skills.
    """

    skill_list = [
        x.strip()
        for x in skills.split(",")
        if x.strip()
    ]

    questions = []

    for skill in skill_list[:5]:

        questions.append(
            f"1. Explain your experience with {skill}."
        )

        questions.append(
            f"2. What are the important concepts in {skill}?"
        )

    return "\n".join(questions)


@tool
def create_interview_ticket(candidate_name: str) -> str:
    """
    Creates a mock interview evaluation record.
    """

    return (
        f"Interview evaluation created successfully "
        f"for candidate: {candidate_name}"
    )