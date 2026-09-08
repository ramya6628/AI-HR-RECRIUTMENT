import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

from agent.graph import create_graph

load_dotenv()

st.set_page_config(
    page_title="AI HR Recruitment Assistant",
    page_icon="🤖"
)

st.title("🤖 AI HR Recruitment Assistant")

st.write(
    "Upload a resume and enter the job description "
    "to analyze candidate suitability."
)


# -----------------------------
# Resume Upload
# -----------------------------

resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


candidate_name = st.text_input(
    "Candidate Name"
)


# -----------------------------
# Job Description
# -----------------------------

job_description = st.text_area(
    "Job Description",
    height=200,
    placeholder="Enter the job description here..."
)


# -----------------------------
# Analyze
# -----------------------------

if st.button("🔍 Analyze Resume"):

    if resume_file is None:

        st.warning(
            "Please upload a resume."
        )

    elif job_description.strip() == "":

        st.warning(
            "Please enter the job description."
        )

    else:

        with st.spinner(
            "AI is analyzing the resume..."
        ):

            reader = PdfReader(
                resume_file
            )

            resume_text = ""

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    resume_text += text


            graph = create_graph()


            result = graph.invoke({

                "resume": resume_text,

                "job_description":
                    job_description,

                "candidate_name":
                    candidate_name,

                "knowledge": "",

                "result": ""
            })


        st.success(
            "Resume analysis completed!"
        )


        st.subheader(
            "📊 AI Analysis"
        )

        st.write(
            result["result"]
        )
        