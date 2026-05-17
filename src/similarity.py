from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.preprocess import clean_text

def calculate_tf_idf_similarity(resume_text, job_text):
  """
  Calcualtes NLP similarity between resume and job description using TF-IDF vectorization and cosine similarity.
  """

  cleaned_resume = clean_text(resume_text)
  cleaned_job = clean_text(job_text)

  documents = [cleaned_resume, cleaned_job]

  vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 3),
    max_features=1500
  )

  tfidf_matrix = vectorizer.fit_transform(documents)

  similarity = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:2]
  )[0][0]

  return round(similarity * 100, 2)


def calculate_overall_score(skill_score, nlp_score, skill_weight=0.7, nlp_weight=0.3):
  """
  Combines skill match score and NLP similarity score into an overall score.
  - 70% skill match
  - 30% NLP similarity
  """
  overall_score = (skill_score * skill_weight) + (nlp_score * nlp_weight)
  return round(overall_score, 2)