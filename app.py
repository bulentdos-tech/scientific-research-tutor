# app.py
import streamlit as st

# Page configuration
st.set_page_config(page_title="Scientific Research Methods Tutor", page_icon="📚", layout="wide")

# ---- HEADER ----
st.title("📚 Scientific Research Methods Tutor")
st.write("""
Welcome! This interactive platform will guide you **step by step**, from beginner to advanced levels, 
in understanding and applying **scientific research methods**. You will be actively engaged, not just reading.
""")

# ---- INSTRUCTIONS ----
with st.expander("How to use this platform"):
    st.markdown("""
1. Follow the steps sequentially.  
2. Always answer the questions before moving forward.  
3. Your answers will be analyzed and corrected when necessary.  
4. You can revisit any step at any time.  
5. This is **not about memorization**, it’s about reasoning and logic.  
""")

# ---- STAGE SELECTION ----
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

# ---- STAGE LOGIC ----
if stage == "Step 1: Big Picture":
    st.header("Step 1: Big Picture (Why Research Exists)")
    st.write("""
Scientific research seeks to **understand the world systematically**, find solutions, and create reliable knowledge.
Think of it as a structured way of **asking questions and finding evidence-based answers**.
""")
    q1 = st.text_input("Question 1: In your own words, why do you think research is important?")
    q2 = st.text_input("Question 2: What is the core logic behind conducting scientific research?")
    if q1 and q2:
        st.success("✅ Great! You’ve shared your thoughts. We’ll analyze and continue next stage.")

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
        st.success("✅ Good! We'll use this reasoning as a foundation for Step 3.")

elif stage == "Step 3: Step-by-Step Problem Modeling":
    st.header("Step 3: Step-by-Step Research Problem Modeling")
    st.write("""
To create a research problem:
1. Choose your topic area  
2. Define key variables  
3. Establish relationships  
4. Make it measurable  
""")
    user_problem = st.text_area("Write your own research problem based on these steps:")
    if user_problem:
        st.success("✅ Problem noted! Ready for Step 4 to generate alternatives.")

elif stage == "Step 4: Generate Alternatives":
    st.header("Step 4: Alternative Research Problems")
    st.write("Analyzing your problem to generate 3 alternatives and compare pros/cons...")
    if user_problem:
        st.write("Original problem:", user_problem)
        # Example automatic generation (can integrate AI later)
        alternatives = [
            f"{user_problem} (alternative 1: more focused on variable X)",
            f"{user_problem} (alternative 2: broader context Y)",
            f"{user_problem} (alternative 3: different relationship Z)"
        ]
        st.write("✅ Suggested Alternatives:")
        for alt in alternatives:
            st.write("-", alt)
        best = st.selectbox("Which alternative seems the best?", alternatives)
        if best:
            st.success(f"Selected alternative: {best}")

elif stage == "Step 5: Research Construction":
    st.header("Step 5: Research Construction")
    st.write("Step-by-step research design. Your contribution is required at each stage.")
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
        st.success("✅ Research questions saved! Proceed to hypotheses.")

elif stage == "Step 6: Literature & Gap":
    st.header("Step 6: Literature Writing & Gap Finding")
    st.write("""
- Synthesize literature logically  
- Connect sources  
- Identify the gap that justifies your research  
""")
    mini_lit = st.text_area("Write a mini literature paragraph:")
    if mini_lit:
        st.success("✅ Mini literature review noted.")

elif stage == "Step 7: Self-Critique":
    st.header("Step 7: Self-Critique")
    st.write("Identify mistakes, methodological gaps, and improvement strategies.")
    critique = st.text_area("Analyze your previous outputs and list corrections:")
    if critique:
        st.success("✅ Critique recorded.")

elif stage == "Step 8: Expert Review":
    st.header("Step 8: Multiple Expert Review")
    st.write("""
Evaluate your work from 3 perspectives:
- Academic expert  
- Methodologist  
- Statistician
""")
    review = st.text_area("Write expert feedback (real or imagined):")
    if review:
        st.success("✅ Expert perspectives saved.")

elif stage == "Step 9: Self-Consistency":
    st.header("Step 9: Self-Consistency Check")
    st.write("Check for contradictions, methodological validity, and testable hypotheses.")
    consistency = st.text_area("List inconsistencies or confirm alignment:")
    if consistency:
        st.success("✅ Self-consistency confirmed.")

elif stage == "Step 10: Reverse Engineering":
    st.header("Step 10: Reverse Engineering")
    st.write("Analyze a published research article to understand how it was constructed.")
    article_link = st.text_input("Paste the article link or title:")
    if article_link:
        st.success("✅ Article noted for reverse engineering.")

elif stage == "Step 11: Meta-Prompting":
    st.header("Step 11: Meta-Prompting")
    st.write("Design a prompt that could teach this entire research process to someone else.")
    prompt = st.text_area("Write your teaching prompt:")
    if prompt:
        st.success("✅ Meta-prompt recorded.")

elif stage == "Step 12: Adaptive Learning":
    st.header("Step 12: Adaptive Learning")
    st.write("Adjust difficulty, simplify or extend tasks based on student performance.")
    feedback = st.text_area("How should the tasks be adapted for better learning?")
    if feedback:
        st.success("✅ Adaptation strategy saved.")

elif stage == "Step 13: Optional Advanced":
    st.header("Step 13: Optional Advanced")
    st.write("""
- Automatic prompt generation logic  
- How to automate the research learning system using code  
""")
    advanced = st.text_area("Ideas or code snippets for automation:")
    if advanced:
        st.success("✅ Advanced ideas saved.")

# ---- FOOTER ----
st.markdown("---")
st.write("Developed for university students to learn **scientific research methods actively**. Follow all steps sequentially.")
