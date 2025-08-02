from typing import List, Tuple
import random
from fpdf import FPDF

def needs_skin_input(problem: str) -> bool:
    keywords = ["rash", "itching", "acne", "eczema", "psoriasis", "redness"]
    return any(word in problem.lower() for word in keywords)

def detect_specialist(problem: str) -> str:
    problem = problem.lower()
    if "heart" in problem or "chest" in problem:
        return "Cardiologist"
    elif "skin" in problem or "rash" in problem:
        return "Dermatologist"
    elif "mental" in problem or "stress" in problem:
        return "Psychiatrist"
    elif "eye" in problem:
        return "Ophthalmologist"
    else:
        return "General Physician"

def get_hospitals(specialist: str) -> List[str]:
    return [f"{specialist} Care Center {i}" for i in range(1, 4)]

def get_medicine(problem: str) -> List[dict]:
    problem = problem.lower()
    if "fever" in problem or "cold" in problem:
        return [
            {"name": "Paracetamol", "dosage": "500mg, twice a day after meals"},
            {"name": "Cetirizine", "dosage": "10mg, once at night"},
        ]
    elif "pain" in problem or "inflammation" in problem:
        return [
            {"name": "Ibuprofen", "dosage": "400mg, every 6-8 hours after food"},
            {"name": "Diclofenac", "dosage": "50mg, twice a day"},
        ]
    elif "acne" in problem or "pimples" in problem:
        return [
            {"name": "Clindamycin Gel", "dosage": "Apply once daily on affected area"},
            {"name": "Doxycycline", "dosage": "100mg, once a day for 7 days"},
        ]
    else:
        return [
            {"name": "Multivitamin", "dosage": "1 tablet daily after breakfast"},
            {"name": "Antacid", "dosage": "10ml, before meals if needed"},
        ]

def check_medicine_conflicts(meds: List[dict]) -> str:
    names = [m["name"] for m in meds]
    if "Ibuprofen" in names and "Diclofenac" in names:
        return "⚠️ Avoid combining Ibuprofen and Diclofenac without doctor advice."
    return "✅ No known conflicts among suggested medicines."

def get_tips(problem: str) -> List[str]:
    return ["Stay hydrated", "Rest well", "Avoid junk food"]

def suggest_tests(problem: str) -> List[str]:
    return ["Blood Test", "X-ray", "Urine Test"] if "fever" in problem else ["General Checkup"]

def get_diet_lifestyle(problem: str) -> Tuple[List[str], List[str]]:
    return (["More vegetables", "Limit sugar"], ["Exercise 30 mins", "Avoid stress"])

def predict_disease(problem: str) -> str:
    return random.choice(["Flu", "Diabetes", "Hypertension", "Dermatitis"])

def get_risk_score(age: int, gender: str, severity: int) -> int:
    risk = severity * 10
    if age > 60:
        risk += 10
    if gender.lower() == "male":
        risk += 5
    return min(risk, 100)

def classify_severity(score: int) -> str:
    if score >= 80:
        return "🔴 High Risk"
    elif score >= 50:
        return "🟠 Moderate Risk"
    else:
        return "🟢 Low Risk"

def age_based_tip(age: int) -> str:
    if age < 18:
        return "Ensure vaccination schedule is followed"
    elif age < 40:
        return "Focus on building healthy habits"
    else:
        return "Regular health screenings are important"

def mental_health_screener(stress: int, sleep: int, appetite: bool) -> str:
    if stress > 7 and sleep < 5:
        return "🧠 At risk of mental burnout"
    elif appetite:
        return "🧠 Monitor appetite-related mood changes"
    return "🧠 Mental state appears stable"

def get_emergency_signs(problem: str) -> str:
    return "🚨 Emergency signs detected. Seek help!" if "unconscious" in problem else "No emergency signs."

def track_symptoms_log(name: str, problem: str) -> str:
    return "Symptoms logged successfully."

def skin_diagnose(image) -> str:
    return "Possible eczema (AI suggestion)"

def ai_chat_response(question: str, problem: str) -> str:
    return f"Based on your problem '{problem}', I suggest: {question}"

def generate_pdf_report(summary: str) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in summary.strip().split('\n'):
        pdf.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True)
    output_path = "health_report.pdf"
    pdf.output(output_path)
    return output_path

def ai_chat_response(question: str, problem: str) -> str:
    # Basic mock logic for AI response
    if "take" in question.lower() and "medicine" in question.lower():
        return "You should take medicines as prescribed. Avoid overdose and consult a doctor if symptoms worsen."
    elif "diet" in question.lower():
        return "Include fruits, green vegetables, and hydrate well. Avoid processed foods."
    elif "exercise" in question.lower():
        return "Light exercise is good, but avoid heavy workouts during illness. Focus on rest."
    elif "test" in question.lower():
        return "Diagnostic tests help identify the root issue. Follow your doctor's advice on which to take."
    else:
        return "That’s a great question. For best results, please consult a real doctor for personalized answers."
