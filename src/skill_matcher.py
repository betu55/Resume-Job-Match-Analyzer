import re
from src.preprocess import clean_text


def build_skill_pattern(skill):
    """
    Builds a stricter regex pattern so skills match as full terms,
    not as pieces inside other skills.

    Examples:
    - C does not match C#
    - Java does not match JavaScript
    - API does not match REST APIs unless API appears separately
    """

    cleaned_skill = clean_text(skill)
    escaped_skill = re.escape(cleaned_skill)
    return rf"(?<![a-z0-9+#.]){escaped_skill}(?![a-z0-9+#.])"

def extract_skills(text, skills):
  """
  Finds skills in the cleaned text based on a predefined list of skills.
  """
  cleaned_text = clean_text(text)
  found_skills = []

  sorted_skills = sorted(skills, key=len, reverse=True)

  for skill in sorted_skills:
    cleaned_skill = clean_text(skill)

    if not cleaned_skill:
      continue

    pattern = build_skill_pattern(cleaned_skill)

    if re.search(pattern, cleaned_text):
      found_skills.append(skill.lower())
  
  return sorted(set(found_skills))

def calculate_skill_overlap(resume_skills, job_skills):
  """
  Calculates the percentage of job skills that are present in the resume.
  """
  if not job_skills:
    return 0.0
  
  matched_skills = set(resume_skills) & set(job_skills)
  skill_score = (len(matched_skills) / len(job_skills)) * 100
  
  return round(skill_score, 2)

def compare_skills(resume_text, job_text, skill_list):
  """
  Extracts skills from both resume and job description, then calculates overlap.
  """
  resume_skills = extract_skills(resume_text, skill_list)
  job_skills = extract_skills(job_text, skill_list)

  matched_skills = sorted(set(resume_skills) & set(job_skills))
  missing_skills = sorted(set(job_skills) - set(resume_skills))
  
  skill_score = calculate_skill_overlap(resume_skills, job_skills)
  
  return {
    "resume_skills": resume_skills,
    "job_skills": job_skills,
    "matched_skills": matched_skills,
    "missing_skills": missing_skills,
    "skill_score": skill_score
  }