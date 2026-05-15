import streamlit as st
import pandas as pd

from src.file_reader import read_uploaded_file
from src.skill_matcher import compare_skills

st.set_page_config(
  page_title="Resume-to-Job Analyzer",
  page_icon="📄",
  layout="wide"
)


st.header("📄 Resume-to-Job Analyzer")
st.write(
  "Upload a resume and job description to compare skill overlap."
)
st.empty()

with st.expander("Show Instructions"):
  st.markdown(
      """
    - Upload your resume in PDF, DOCX, or TXT format.
    - Upload the job description in PDF, DOCX, or TXT format.
    - The tool will extract skills from both documents and compare them.
    """
  )

# Load skill keywords from CSV and prepare for matching
with st.container(border=True):
  st.subheader("Step 1: Add Resume and Job Description")

  with st.spinner("Loading skill keywords..."):
    skill_df = pd.read_csv("data/skill_keywords.csv")
    skill_list = skill_df["skill"].dropna().tolist()

    resume_col, job_col = st.columns(2)

    with resume_col:
        st.markdown("### Resume")

        resume_file = st.file_uploader(
          "Upload resume file",
          type=["pdf", "docx", "txt"],
          key="resume_file"
        )

        resume_pasted_text = st.text_area(
          "Or paste resume text",
          height=250,
          placeholder="Paste your resume text here...",
          key="resume_text"
        )

    with job_col:
        st.markdown("### Job Description")

        job_file = st.file_uploader(
          "Upload job description file",
          type=["pdf", "docx", "txt"],
          key="job_file"
        )

        job_pasted_text = st.text_area(
          "Or paste job description text",
          height=250,
          placeholder="Paste the job description here...",
          key="job_text"
        )

# Analyze skills and display results
with st.container(border=True):
  st.subheader("Step 2: Analyze Skills")

  if not (resume_file or resume_pasted_text.strip()) or not (job_file or job_pasted_text.strip()):
    st.warning("Please upload both a resume and a job description to analyze.")
  else:
    if st.button("Compare Skills"):
      try:
        with st.spinner("Reading and Anlyzing files..."):
          resume_text = read_uploaded_file(resume_file) if resume_file else resume_pasted_text
          job_text = read_uploaded_file(job_file) if job_file else job_pasted_text
          results = compare_skills(resume_text, job_text, skill_list)

        st.subheader("Skill Match Score")
        st.metric(
            "Skill Match",
            f'{results["skill_score"]}%'
        )

        col1, col2 = st.columns(2)

        with col1:
          st.subheader("Resume Skills Found")
          st.write(results["resume_skills"])

          st.subheader("Matched Skills")
          if results["matched_skills"]:
            st.success(", ".join(results["matched_skills"]))
          else:
            st.warning("No matched skills found.")

          with col2:
            st.subheader("Job Skills Found")
            st.write(results["job_skills"])

            st.subheader("Missing Skills")
            if results["missing_skills"]:
              st.error(", ".join(results["missing_skills"]))
            else:
              st.success("No missing skills found.")

          with st.expander("Preview Extracted Resume Text"):
            st.write(resume_text[:3000])

          with st.expander("Preview Extracted Job Description Text"):
            st.write(job_text[:3000])

      except Exception as e:
        st.error(f"An error occurred while processing the files: {e}")
