from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

SKILL_LIBRARY = [
    "python", "sql", "r", "javascript", "java", "c++", "scala", "bash",
    "pandas", "numpy", "scikit-learn", "sklearn", "tensorflow", "pytorch",
    "keras", "xgboost", "matplotlib", "seaborn", "plotly", "streamlit",
    "huggingface", "nlp", "machine learning", "deep learning", "regression",
    "classification", "clustering", "k-means", "random forest", "neural network",
    "tableau", "looker", "power bi", "excel", "google analytics", "mixpanel",
    "amplitude", "dbt", "airflow", "spark", "hadoop",
    "postgresql", "mysql", "mongodb", "bigquery", "snowflake", "redshift",
    "product management", "roadmap", "a/b testing", "user research",
    "okrs", "kpis", "agile", "scrum", "jira", "confluence", "figma",
    "wireframing", "user stories", "go-to-market",
    "aws", "gcp", "azure", "docker", "kubernetes", "git", "github",
    "ci/cd", "api", "rest api", "fastapi", "flask", "django",
    "statistics", "hypothesis testing", "p-value", "confidence interval",
    "linear regression", "logistic regression", "time series", "forecasting",
]

def extract_skills(text):
    text_lower = text.lower()
    found = set()
    for skill in SKILL_LIBRARY:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found.add(skill)
    return found

print("Loading NLP model... (first run downloads ~90MB, takes ~30s)")
MODEL = SentenceTransformer('all-MiniLM-L6-v2')
print("Model ready!")

def compute_similarity(text_a, text_b):
    embeddings = MODEL.encode([text_a, text_b])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(float(score) * 100, 1)

def analyse(resume_text, job_text):
    score = compute_similarity(resume_text, job_text)
    resume_skills = extract_skills(resume_text)
    job_skills    = extract_skills(job_text)
    matched = resume_skills & job_skills
    missing = job_skills - resume_skills
    bonus   = resume_skills - job_skills

    tips = []
    if score < 50:
        tips.append("⚠️ Low match. Mirror the job description language in your resume.")
    elif score < 70:
        tips.append("🔶 Moderate match. Add keywords from the job description naturally.")
    else:
        tips.append("✅ Strong match! Focus on quantifying your impact.")
    if len(missing) > 5:
        tips.append(f"📚 You're missing {len(missing)} skills. Prioritise the top 2–3.")
    if "a/b testing" in missing:
        tips.append("💡 A/B testing appears in the job — add any relevant experience.")
    if "sql" in missing:
        tips.append("💡 SQL appears in the job but not your resume — add it if you know it.")

    return {
        "score":   score,
        "matched": sorted(matched),
        "missing": sorted(missing),
        "bonus":   sorted(bonus),
        "tips":    tips,
    }