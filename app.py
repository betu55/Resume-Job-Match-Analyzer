import streamlit as st

st.set_page_config(
    page_title="Resume-to-Job Match Analyzer",
    layout="wide"
)

st.title("Resume-to-Job Match Analyzer")
st.write(
    "Upload resumes and job descriptions to compare skill overlap, NLP similarity, and role fit."
)

st.info("Project setup complete. Next step: add text cleaning and skill extraction.")
