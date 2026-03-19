import streamlit as st
from matcher import analyse

st.set_page_config(page_title="Resume–Job Matcher | Jiya Chaudhari", page_icon="🌸", layout="wide")

st.markdown("""
<style>
  .score-big { font-size: 72px; font-weight: 700; text-align: center; line-height: 1; }
  .score-label { text-align: center; color: #888; font-size: 13px; margin-top: 4px; }
  .pill { display: inline-block; padding: 3px 10px; border-radius: 100px; font-size: 12px; margin: 3px; }
  .pill-green { background: #d1fae5; color: #065f46; }
  .pill-red   { background: #fee2e2; color: #991b1b; }
  .pill-blue  { background: #dbeafe; color: #1e40af; }
  .tip-box { background: #fdf2f8; border-left: 3px solid #ec4899; padding: 10px 16px; border-radius: 4px; margin: 6px 0; font-size: 13px; }
</style>
""", unsafe_allow_html=True)

st.markdown("## 🌸 Resume–Job Matching AI")
st.markdown("*Paste your resume and a job description — get a similarity score + skills gap analysis.*")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📄 Your Resume")
    resume_text = st.text_area("Resume", placeholder="Paste your full resume here...", height=320, label_visibility="collapsed")

with col2:
    st.markdown("### 💼 Job Description")
    job_text = st.text_area("Job", placeholder="Paste the full job description here...", height=320, label_visibility="collapsed")

st.divider()

if st.button("🔍 Analyse Match", type="primary", use_container_width=True):
    if not resume_text.strip() or not job_text.strip():
        st.error("Please paste both a resume and a job description.")
    else:
        with st.spinner("Computing semantic similarity..."):
            result = analyse(resume_text, job_text)

        score = result["score"]
        color = "#22c55e" if score >= 75 else "#f59e0b" if score >= 50 else "#ef4444"
        label = "Strong Match 🎉" if score >= 75 else "Moderate Match 🔶" if score >= 50 else "Weak Match ⚠️"

        st.markdown(f'<div class="score-big" style="color:{color}">{score}%</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="score-label">{label} — semantic similarity score</div>', unsafe_allow_html=True)
        st.progress(int(score))
        st.divider()

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"#### ✅ Matched Skills ({len(result['matched'])})")
            st.caption("In both your resume and the job")
            if result["matched"]:
                st.markdown(" ".join([f'<span class="pill pill-green">{s}</span>' for s in result["matched"]]), unsafe_allow_html=True)
            else:
                st.info("No exact overlap found.")

        with c2:
            st.markdown(f"#### ❌ Missing Skills ({len(result['missing'])})")
            st.caption("In the job but NOT your resume")
            if result["missing"]:
                st.markdown(" ".join([f'<span class="pill pill-red">{s}</span>' for s in result["missing"]]), unsafe_allow_html=True)
            else:
                st.success("No missing skills!")

        with c3:
            st.markdown(f"#### 💡 Bonus Skills ({len(result['bonus'])})")
            st.caption("You have these — not in the job")
            if result["bonus"]:
                st.markdown(" ".join([f'<span class="pill pill-blue">{s}</span>' for s in result["bonus"]]), unsafe_allow_html=True)
            else:
                st.info("No bonus skills.")

        st.divider()
        st.markdown("#### 📋 Personalised Tips")
        for tip in result["tips"]:
            st.markdown(f'<div class="tip-box">{tip}</div>', unsafe_allow_html=True)

st.divider()
st.markdown("<div style='text-align:center;color:#aaa;font-size:12px;'>Built by Jiya Chaudhari · <a href='https://github.com/Jiya4405' style='color:#ec4899'>GitHub</a></div>", unsafe_allow_html=True)