# Resume-to-Job Match Analyzer Dashboard

An interactive NLP dashboard that compares resumes against job descriptions and helps identify role fit using skill extraction, TF-IDF, cosine similarity, and data visualization.

The project is built with **Python**, **Streamlit**, **Pandas**, and **scikit-learn**. It allows users to upload or paste resume and job description text, then generates skill overlap results, missing skills, and match scores through a simple local web interface.

## Overview

This project was created to explore how Natural Language Processing can be used to compare resume content with job postings. Instead of manually scanning job descriptions for keywords, the dashboard extracts technical skills from both documents and calculates how closely they match.

The project focuses on:

- Resume and job description text extraction
- Skill keyword matching
- NLP-based document comparison
- Data visualization
- Interactive dashboard development
- Practical job search analysis

## Features

- Upload resume files in PDF, DOCX, or TXT format
- Upload job description files in PDF, DOCX, or TXT format
- Paste resume or job description text directly into the app
- Extract technical skills from both documents
- Identify matched skills
- Identify missing skills
- Calculate a skill match score
- Preview extracted text from uploaded documents
- Interactive Streamlit dashboard interface

Planned improvements:

- TF-IDF similarity scoring
- Cosine similarity scoring
- Match score visualizations
- Missing skill charts
- Resume version comparison
- CSV export
- Role category detection

## Tech Stack

- Python
- Streamlit
- Pandas
- scikit-learn
- NumPy
- Matplotlib
- pypdf
- python-docx
- Pipenv

## Project Structure

```txt
resume-job-match-analyzer/
├── app.py
├── data/
│   └── skill_keywords.csv
├── src/
│   ├── __init__.py
│   ├── file_reader.py
│   ├── preprocess.py
│   ├── skill_matcher.py
│   ├── similarity.py
│   └── role_classifier.py
├── screenshots/
├── outputs/
│   ├── charts/
│   └── reports/
├── Pipfile
├── Pipfile.lock
├── .gitignore
└── README.md
