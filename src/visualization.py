import matplotlib.pyplot as plt
import pandas as pd

def plot_score_breakdown(skill_score, nlp_score, overall_score):
    """
    Plots a bar chart showing the breakdown of skill match score, NLP similarity score, and overall score.
    """
    scores = [skill_score, nlp_score, overall_score]
    labels = ['Skill Match', 'NLP Similarity', 'Overall Score']

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.bar(labels, scores, color=['#4CAF50', '#2196F3', '#FFC107'])
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score (%)")
    ax.set_title("Score Breakdown")
    
    for index, score in enumerate(scores):
        ax.text(index, score+2, f"{score}%", ha="center")
    
    plt.tight_layout()
    return fig

def plot_matched_vs_missing(matched_skills, missing_skills):
    """
    Creates a bar chart comparing matched skills and missing skills.
    """

    labels = ['Matched Skills', 'Missing Skills']
    counts = [len(matched_skills), len(missing_skills)]

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.bar(labels, counts, color=['#4CAF50', '#F44336'])
    ax.set_ylabel("Number of Skills")
    ax.set_title("Matched vs Missing Skills")
    
    for index, count in enumerate(counts):
        ax.text(index, count+0.1, str(count), ha="center")
    
    plt.tight_layout()
    return fig

def get_skill_category_counts(skills, skill_df):
    """
    Groups a list of skills by category using the skill_keywords.csv file.
    Returns a DataFrame with category and count columns.
    """

    if not skills:
        return pd.DataFrame(columns=['category', 'count'])
    
    normalized_skills = [skill.lower() for skill in skills]

    cleaned_skill_df = skill_df.copy()
    cleaned_skill_df['skill'] = cleaned_skill_df['skill'].str.lower()

    matched_rows = cleaned_skill_df[
        cleaned_skill_df["skill"].isin(normalized_skills)
    ]

    category_counts = (
      matched_rows.groupby("category")
      .size()
      .reset_index(name="count")
      .sort_values("count", ascending=False)
    )

    return category_counts

def plot_skills_by_category(skills, skill_df, title):
    """
    Creates a bar chart showing how many skills fall into each category.
    """

    category_counts = get_skill_category_counts(skills, skill_df)

    fig, ax = plt.subplots(figsize=(7, 4))

    if category_counts.empty:
        ax.text(0.5, 0.5, "No skills found", ha="center", va="center")
        ax.set_axis_off()
        return fig
    
    ax.bar(category_counts['category'], category_counts['count'], color='#2196F3')
    ax.set_ylabel("Number of Skills")
    ax.set_title(title)
    ax.tick_params(axis="x", rotation=30)
    
    for index, count in enumerate(category_counts['count']):
        ax.text(index, count+0.1, str(count), ha="center")
    
    plt.tight_layout()
    return fig