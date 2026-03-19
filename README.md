# 🌸 Resume–Job Matching AI

An NLP-powered tool that scores how well your resume matches a job description — and shows exactly which skills you're missing.

**🔗 Live Demo: [jiya-resume-matcher.streamlit.app](https://jiya-resume-matcher.streamlit.app)**

---

## What it does

1. Paste your resume and a job description
2. Gets encoded into 384-dimensional vectors using `sentence-transformers`
3. Computes **cosine similarity** — a semantic match score 0–100%
4. Shows ✅ matched skills, ❌ missing skills, 💡 bonus skills
5. Gives personalised tips to improve your match

---

## Results

| Metric | Value |
|---|---|
| Similarity method | Cosine similarity on 384-dim embeddings |
| Model | `all-MiniLM-L6-v2` |
| Skills library | 80+ technical and PM skills |

---

## Tech stack

- **Python** — core logic
- **sentence-transformers** — semantic NLP embeddings  
- **scikit-learn** — cosine similarity
- **Streamlit** — UI and deployment

---

## How to run locally
```bash
git clone https://github.com/Jiya4405/resume-matcher.git
cd resume-matcher
pip install -r requirements.txt
streamlit run app.py
```

---

*Built by [Jiya Chaudhari](https://www.linkedin.com/in/jiyachaudhari/)*