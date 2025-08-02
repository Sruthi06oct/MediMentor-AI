import streamlit as st
from utils import (
    needs_skin_input, detect_specialist, get_hospitals,
    get_medicine, get_tips, get_risk_score, skin_diagnose,
    ai_chat_response, get_emergency_signs, suggest_tests,
    track_symptoms_log, mental_health_screener,
    get_diet_lifestyle, predict_disease, classify_severity,
    age_based_tip, check_medicine_conflicts, generate_pdf_report
)

# --- Page Config ---
st.set_page_config(page_title="MediMentor AI", page_icon="🧠")
st.title("🩺 MediMentor AI")
st.markdown("#### _AI-powered personalized health suggestions._")

if "history" not in st.session_state:
    st.session_state.history = []

# --- Form UI ---
with st.form("health_form"):
    st.subheader("👤 Personal Info")
    name = st.text_input("Your Name")
    age = st.number_input("Your Age", 1, 120)
    gender = st.radio("Gender", ["Male", "Female", "Other"])

    st.subheader("📝 Symptoms")
    problem = st.text_area("Describe your symptoms")
    severity = st.slider("Severity Level", 1, 10, 5)
    image = st.file_uploader("Upload a skin image (optional)", type=["jpg", "jpeg", "png"])

    st.subheader("📆 Lifestyle Today")
    water = st.slider("Water (glasses)", 0, 15, 8)
    sleep = st.slider("Sleep (hours)", 0, 12, 7)
    exercise = st.selectbox("Exercised today?", ["Yes", "No"])
    stress = st.slider("Stress Level", 0, 10, 5)
    appetite = st.checkbox("Change in appetite")

    submit = st.form_submit_button("💡 Get AI Suggestions")

# --- Main Response ---
if submit and problem:
    st.success(f"Generating suggestions for {name}...")

    st.session_state.history.append(problem)
    log_status = track_symptoms_log(name, problem)

    if image and needs_skin_input(problem):
        st.markdown(f"🧬 **Skin Diagnosis:** `{skin_diagnose(image)}`")

    specialist = detect_specialist(problem)
    st.markdown(f"👨‍⚕️ **Specialist Suggested:** `{specialist}`")

    hospitals = get_hospitals(specialist)
    st.subheader("🏥 Nearby Hospitals")
    for hosp in hospitals:
        st.markdown(f"- {hosp} [🗺️ Map](https://www.google.com/maps/search/{hosp.replace(' ', '+')})")

    meds = get_medicine(problem)
    tips = get_tips(problem)
    tests = suggest_tests(problem)
    diet, lifestyle = get_diet_lifestyle(problem)
    disease = predict_disease(problem)
    risk = get_risk_score(age, gender, severity)
    severity_label = classify_severity(risk)
    age_tip = age_based_tip(age)
    conflict_warning = check_medicine_conflicts(meds)
    mental_result = mental_health_screener(stress, sleep, appetite)
    emergency_msg = get_emergency_signs(problem)

    st.markdown(f"🧠 **Likely Condition:** `{disease}`")
    st.markdown(f"📊 **Risk Score:** `{risk}/100` → {severity_label}")
    st.markdown(f"🧪 **Suggested Tests:** {', '.join(tests)}")

    st.subheader("💊 Suggested Medicines and Dosage")
    for med in meds:
        st.markdown(f"- **{med['name']}**: _{med['dosage']}_")
    st.markdown(conflict_warning)

    st.subheader("📌 Health Tips")
    for tip in tips:
        st.markdown(f"- {tip}")

    st.subheader("🥗 Diet Advice")
    for d in diet:
        st.markdown(f"- {d}")

    st.subheader("🏃 Lifestyle Tips")
    for l in lifestyle:
        st.markdown(f"- {l}")

    st.markdown(f"🔹 **Age-based Tip:** {age_tip}")
    st.markdown(f"🧠 **Mental Health Check:** {mental_result}")
    st.markdown(f"🚨 **Emergency Check:** {emergency_msg}")

    st.divider()
    # --- PDF Report ---
    summary = f"""
Name: {name}
Age: {age}
Gender: {gender}
Problem: {problem}
Specialist: {specialist}
Severity Score: {severity} / 10
Risk Score: {risk}/100 ({severity_label})
Likely Disease: {disease}
Tests: {', '.join(tests)}

Medicines and Dosage:
{chr(10).join([f"{m['name']} - {m['dosage']}" for m in meds])}

Tips: {', '.join(tips)}
Diet: {', '.join(diet)}
Lifestyle: {', '.join(lifestyle)}
Age Tip: {age_tip}
Mental Health: {mental_result}
Emergency: {emergency_msg}
Water: {water} glasses | Sleep: {sleep} hrs | Exercise: {exercise}
    """

    pdf_path = generate_pdf_report(summary)
    with open(pdf_path, "rb") as f:
        st.download_button("📥 Download PDF Report", f, "AI_Health_Report.pdf", mime="application/pdf")

    st.success(log_status)

# --- History Log ---
if st.session_state.history:
    st.subheader("🕓 Previous Symptom Logs")
    for i, sym in enumerate(st.session_state.history[-5:]):
        st.markdown(f"{i+1}. {sym}")

with st.expander("🤖 Ask AI Doctor (Follow-up)", expanded=False):
    followup = st.text_input("Enter your question about your symptoms, medicine, or diet")
    if followup:
        reply = ai_chat_response(followup, problem)
        st.success(f"🧠 AI Doctor says: {reply}")
