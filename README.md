🩺 Project Description: MediMentor AI

MediMentor AI is a smart, AI-powered health assistant built using Python and Streamlit. It provides personalized medical guidance based on user symptoms, lifestyle inputs, and basic health data. The system suggests the right specialist, nearby hospitals, potential conditions, medicines (with dosage), tests, risk severity, diet and lifestyle changes, and even mental health checks — all summarized in a downloadable PDF health report.

It also includes an AI-powered Q&A chatbot ("Ask AI Doctor") for users to ask follow-up questions, creating an interactive and helpful virtual consultation experience.

🌟 Key Highlights

✅ Symptom analysis & disease prediction

✅ Personalized specialist & test suggestions

✅ AI-based medicine dosage recommendations

✅ Mental health screener

✅ Emergency warning detector

✅ Skin diagnosis from image input

✅ PDF health summary generator

✅ AI Doctor Q&A (chat-style)

✅ Elegant UI built with Streamlit

💼 MediMentor AI – Project Summary

🔎 General Description

MediMentor AI is a virtual health advisor designed to bridge the gap between early symptom detection and professional medical consultation. It leverages rule-based AI logic and machine learning with Streamlit to offer personalized health suggestions. Users input symptoms, lifestyle habits, and optional skin images to receive a tailored summary of possible conditions, risk levels, specialist suggestions, and medication with dosage. A downloadable PDF report wraps up the insights.

Plan of Action:

Collect user inputs: symptoms, lifestyle, demographics

Apply domain logic to identify specialist, medicine, condition

Score severity and risk based on age, gender, symptom level

Offer tips, emergency alerts, and follow-up chatbot

Generate a downloadable PDF health summary

This helps reduce hospital overloads and promotes digital-first preventive healthcare.

✨ Novelty / Uniqueness

Unlike typical symptom checkers, MediMentor AI introduces:

Personalized medicine with dosage

Skin image diagnosis (AI-simulated)

Mental health screening based on lifestyle

Emergency sign detection and conflict-aware medicine suggestions

Follow-up AI chat with optional LangChain memory

The system is modular, transparent, and easily adaptable for clinics, health kiosks, or research use.

🌍 Business / Social Impact

This solution improves accessibility in rural and urban areas by enabling self-assessment at home. It reduces unnecessary visits, supports early detection, and empowers users with preventive care insights.

Business Benefits:

🕒 Low-cost rollout (<2 weeks for MVP)

☁️ Rapid deployment on cloud (Streamlit Cloud, Heroku)

🔄 Easily scalable across demographics

It unlocks B2B partnerships in telehealth, pharmacies, and diagnostic APIs.

💼 Scope of Work

The system is divided into the following core modules:

User Input Module – Collects demographics, symptoms, lifestyle, and image.

Analysis Engine – Predicts disease, detects emergency and severity.

Recommendation Engine – Suggests medicine, dosage, tests, and specialist.

Wellness Module – Mental screening, lifestyle and diet tips.

Skin Analysis Module – Analyzes skin condition (placeholder logic).

AI Chat Module – Follow-up health Q&A with optional chat memory.

Report Generator – Creates structured PDF summary for download.

Session Tracker – Shows recent symptoms and maintains context.

📦 Deliverables:

✅ Functional Streamlit Web App

✅ Modular backend logic (utils.py)

✅ Downloadable PDF report

✅ AI chatbot with symptom context

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run main.py
