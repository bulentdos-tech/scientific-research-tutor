# app.py
import streamlit as st
import requests

# ---- CONFIG ----
st.set_page_config(
    page_title="Scientific Research Methods Tutor",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Scientific Research Methods Tutor")
st.write("""
Welcome! This interactive platform will guide you **step by step**, from beginner to advanced levels,
in understanding and applying **scientific research methods**. You will be actively engaged, not just reading.
""")

# ---- HOW TO USE ----
with st.expander("How to use this platform"):
    st.markdown("""
1. Follow the steps sequentially.  
2. Always answer the questions before moving forward.  
3. Your answers will be analyzed using AI and corrected when necessary.  
4. Revisit any step at any time.  
5. Focus on **reasoning and logic**, not memorization.
""")

# ---- SIDEBAR ----
st.sidebar.header("Choose Stage")
stage = st.sidebar.selectbox("Select the teaching stage:", [
    "Step 1: Big Picture",
    "Step 2: Decomposition",
    "Step 3: Step-by-Step Problem Modeling",
    "Step 4: Generate Alternatives",
    "Step 5: Research Construction",
    "Step 6: Literature & Gap",
    "Step 7: Self-Critique",
    "Step 8: Expert Review",
    "Step 9: Self-Consistency",
    "Step 10: Reverse Engineering",
    "Step 11: Meta-Prompting",
    "Step 12: Adaptive Learning",
    "Step 13: Optional Advanced"
])

# ---- AI FEEDBACK FUNCTION (Gemini / OpenAI compatible) ----
gemini_key = st.secrets["GEMINI_API_KEY"]  # Or OpenAI key

def get_ai_feedback(prompt_text):
    url = "https://api.gemini.google/v1/ai/feedback"  # Update if using OpenAI
    headers = {
        "Authorization": f"Bearer {gemini_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": f"Analyze this student input and give constructive feedback:\n{prompt_text}",
        "model": "gemini-1.5"  # adjust if using another model
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json().get("output_text", "No feedback returned.")
    except Exception as e:
        return f"Error contacting AI: {e}"

# ---- STAGE LOGIC ----
user_input = ""
feedback = ""

if stage == "Step 1: Big Picture":
    st.header("Step 1: Big Picture (Why Research Exists)")
    st.write("""
Scientific research seeks to **understand the world systematically**, find solutions, and create reliable knowledge.
Think of it as a structured way of **asking questions and finding evidence-based answers**.
""")
    q1 = st.text_input("Question 1: In your own words, why do you think research is important?")
    q2 = st.text_input("Question 2: What is the core logic behind conducting scientific research?")
    if q1 and q2:
        user_input = q1 + "\n" + q2
        feedback = get_ai_feedback(user_input)
        st.success("✅ Your thoughts have been recorded.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 2: Decomposition":
    st.header("Step 2: Decomposition of the Research Process")
    st.write("""
The scientific research process typically includes:
- Problem identification  
- Literature review  
- Literature writing  
- Finding research gaps  
- Research questions  
- Hypotheses  
- Research design (quantitative/qualitative/mixed)  
- Sampling  
- Data collection tools  
- Data analysis  
- Findings and discussion  
""")
    reason = st.text_area("Why do you think research follows this sequence?")
    if reason:
        user_input = reason
        feedback = get_ai_feedback(user_input)
        st.success("✅ Your reasoning recorded.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 3: Step-by-Step Problem Modeling":
    st.header("Step 3: Step-by-Step Research Problem Modeling")
    st.write("""
To create a research problem:
1. Choose your topic area  
2. Define key variables  
3. Establish relationships  
4. Make it measurable  
""")
    user_input = st.text_area("Write your own research problem based on these steps:")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Problem recorded.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 4: Generate Alternatives":
    st.header("Step 4: Alternative Research Problems")
    st.write("Generate 3 alternative research problems and compare pros/cons.")
    user_input = st.text_area("Paste your original research problem:")
    if user_input:
        alternatives = [
            f"{user_input} (alternative 1: focus on variable X)",
            f"{user_input} (alternative 2: broader context Y)",
            f"{user_input} (alternative 3: different relationship Z)"
        ]
        st.write("Suggested alternatives:")
        for alt in alternatives:
            st.write("-", alt)
        best = st.selectbox("Which alternative seems best?", alternatives)
        if best:
            feedback = get_ai_feedback(best)
            st.success(f"Selected alternative: {best}")
            st.info("AI Feedback:\n" + feedback)

elif stage == "Step 5: Research Construction":
    st.header("Step 5: Research Construction")
    st.write("""
1. Formulate research questions  
2. Write hypotheses  
3. Choose research design & justify  
4. Define sample  
5. Develop data collection tools  
6. Select data analysis methods
""")
    user_input = st.text_area("Start with your research questions:")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Research questions saved.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 6: Literature & Gap":
    st.header("Step 6: Literature Writing & Gap Finding")
    st.write("""
- Synthesize literature logically  
- Connect sources  
- Identify the gap that justifies your research  
""")
    user_input = st.text_area("Write a mini literature paragraph:")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Mini literature review recorded.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 7: Self-Critique":
    st.header("Step 7: Self-Critique")
    st.write("Identify mistakes, methodological gaps, and improvement strategies.")
    user_input = st.text_area("Analyze your previous outputs and list corrections:")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Self-critique recorded.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 8: Expert Review":
    st.header("Step 8: Multiple Expert Review")
    st.write("""
Evaluate your work from 3 perspectives:
- Academic expert  
- Methodologist  
- Statistician
""")
    user_input = st.text_area("Write expert feedback (real or imagined):")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Expert perspectives saved.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 9: Self-Consistency":
    st.header("Step 9: Self-Consistency Check")
    st.write("Check for contradictions, methodological validity, and testable hypotheses.")
    user_input = st.text_area("List inconsistencies or confirm alignment:")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Self-consistency confirmed.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 10: Reverse Engineering":
    st.header("Step 10: Reverse Engineering")
    st.write("Analyze a published research article to understand how it was constructed.")
    user_input = st.text_input("Paste the article link or title:")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Article noted for reverse engineering.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 11: Meta-Prompting":
    st.header("Step 11: Meta-Prompting")
    st.write("Design a prompt that could teach this entire research process to someone else.")
    user_input = st.text_area("Write your teaching prompt:")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Meta-prompt recorded.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 12: Adaptive Learning":
    st.header("Step 12: Adaptive Learning")
    st.write("Adjust difficulty, simplify or extend tasks based on student performance.")
    user_input = st.text_area("How should the tasks be adapted for better learning?")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Adaptation strategy saved.")
        st.info("AI Feedback:\n" + feedback)

elif stage == "Step 13: Optional Advanced":
    st.header("Step 13: Optional Advanced")
    st.write("""
- Automatic prompt generation logic  
- How to automate the research learning system using code
""")
    user_input = st.text_area("Ideas or code snippets for automation:")
    if user_input:
        feedback = get_ai_feedback(user_input)
        st.success("✅ Advanced ideas saved.")
        st.info("AI Feedback:\n" + feedback)

# ---- FOOTER ----
st.markdown("---")
st.write("Developed for university students to learn **scientific research methods actively**. Follow all steps sequentially.")
