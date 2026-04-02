import streamlit as st

# ---- CONFIG ----
st.set_page_config(
    page_title="Scientific Research Methods Tutor",
    page_icon="📚",
    layout="wide"
)

# ---- AI FEEDBACK FUNCTION ----
def get_ai_feedback(prompt_text):
    if not prompt_text:
        return "Please provide an answer to get feedback."
    # Bu kısım ileride bir API'ye bağlanabilir
    return "Analysis: Your reasoning is logically sound. In a scientific context, ensure your variables are measurable."

st.title("📚 Scientific Research Methods Tutor")
st.write("""
Welcome! This interactive platform will guide you **step by step** through scientific research methods.
""")

# ---- SIDEBAR ----
st.sidebar.header("Choose Stage")
stage = st.sidebar.selectbox("Select the teaching stage:", [
    "Step 1: Big Picture",
    "Step 2: Decomposition",
    "Step 3: Problem Modeling",
    "Step 4: Generate Alternatives",
    "Step 5: Research Construction",
    "Step 6: Literature & Gap",
    "Step 7: Self-Critique"
])

# ---- STAGE LOGIC ----

if stage == "Step 1: Big Picture":
    st.header("Step 1: Big Picture (Why Research Exists)")
    st.write("Scientific research seeks to understand the world systematically.")
    
    q1 = st.text_input("Question 1: Why do you think research is important?", key="s1_q1")
    q2 = st.text_input("Question 2: What is the core logic behind scientific research?", key="s1_q2")
    
    if st.button("Submit Answers", key="btn_s1"):
        if q1 and q2:
            st.success("✅ Recorded!")
            st.info(get_ai_feedback(q1 + " " + q2))
        else:
            st.warning("Please fill in both fields.")

elif stage == "Step 2: Decomposition":
    st.header("Step 2: Decomposition of the Research Process")
    st.write("- Problem identification\n- Literature review\n- Research questions\n- Methodology")
    
    reason = st.text_area("Why do you think research follows this sequence?", key="s2_area")
    if st.button("Analyze My Reason", key="btn_s2"):
        if reason:
            st.info(get_ai_feedback(reason))
        else:
            st.warning("Please write your thoughts first.")

elif stage == "Step 3: Problem Modeling":
    st.header("Step 3: Step-by-Step Problem Modeling")
    st.markdown("1. Choose topic\n2. Define variables\n3. Establish relationships")
    
    p_model = st.text_area("Write your research problem here:", key="s3_area")
    if st.button("Submit Problem", key="btn_s3"):
        st.info(get_ai_feedback(p_model))

elif stage == "Step 4: Generate Alternatives":
    st.header("Step 4: Alternative Research Problems")
    orig_prob = st.text_input("Paste your original research problem:", key="s4_in")
    if orig_prob:
        st.write("Suggested alternatives:")
        st.write(f"- Focus on socio-economic factors of: {orig_prob}")
        st.write(f"- Comparative analysis of: {orig_prob}")
        
        alt_choice = st.selectbox("Which approach is better?", ["Original", "Socio-economic", "Comparative"], key="s4_sel")
        if st.button("Evaluate Choice", key="btn_s4"):
            st.success(f"You chose: {alt_choice}")

elif stage == "Step 5: Research Construction":
    st.header("Step 5: Research Construction")
    r_ques = st.text_area("Formulate your research questions:", key="s5_area")
    if st.button("Save Questions", key="btn_s5"):
        st.info(get_ai_feedback(r_ques))

elif stage == "Step 6: Literature & Gap":
    st.header("Step 6: Literature Writing & Gap Finding")
    lit_review = st.text_area("Write a mini literature paragraph:", key="s6_area")
    if st.button("Analyze Literature", key="btn_s6"):
        st.info(get_ai_feedback(lit_review))

elif stage == "Step 7: Self-Critique":
    st.header("Step 7: Self-Critique")
    critique = st.text_area("Identify potential weaknesses in your design:", key="s7_area")
    if st.button("Submit Critique", key="btn_s7"):
        st.success("Self-reflection recorded.")

# ---- FOOTER ----
st.markdown("---")
st.caption("Scientific Research Methods Tutor - V1.0")
