import streamlit as st

# ---- CONFIG ----
st.set_page_config(
    page_title="Scientific Research Methods Tutor",
    page_icon="📚",
    layout="wide"
)

# ---- SESSION STATE INITIALIZATION ----
# Kullanıcının verdiği cevapları hafızada tutmak için
if 'answers' not in st.session_state:
    st.session_state['answers'] = {}

# ---- FAKE AI FEEDBACK FUNCTION ----
def get_ai_feedback(prompt_text):
    # İleride buraya requests ile bir API bağlayabilirsin.
    if not prompt_text:
        return "Lütfen önce bir cevap yazın."
    return f"AI Analysis: Your input shows a good understanding of research logic. Focus more on empirical evidence in the next steps."

# ---- SIDEBAR ----
st.sidebar.header("Navigation")
stage = st.sidebar.selectbox("Choose Stage:", [
    "Step 1: Big Picture",
    "Step 2: Decomposition",
    "Step 3: Problem Modeling",
    "Step 4: Generate Alternatives",
    # ... Diğer stepleri buraya ekleyebilirsin
])

st.title("📚 Scientific Research Methods Tutor")

# ---- STAGE LOGIC ----

if stage == "Step 1: Big Picture":
    st.header("Step 1: Big Picture (Why Research Exists)")
    st.write("Scientific research seeks to understand the world systematically.")
    
    # Form kullanarak her butona basıldığında sayfanın gereksiz yenilenmesini önleyebiliriz
    with st.form("step1_form"):
        q1 = st.text_input("Why is research important?")
        submit = st.form_submit_button("Submit Answer")
        
        if submit:
            if q1:
                feedback = get_ai_feedback(q1)
                st.success("✅ Recorded!")
                st.info(feedback)
                st.session_state['answers']['step1'] = q1
            else:
                st.warning("Please write something before submitting.")

elif stage == "Step 2: Decomposition":
    st.header("Step 2: Decomposition")
    st.write("The scientific research process follows a logical sequence.")
    
    with st.form("step2_form"):
        reason = st.text_area("Why do you think research follows this sequence?")
        submit = st.form_submit_button("Analyze My Reasoning")
        
        if submit:
            feedback = get_ai_feedback(reason)
            st.info(feedback)

# ---- FOOTER ----
st.sidebar.markdown("---")
st.sidebar.write("💡 **Tip:** Complete steps in order for the best experience.")
