# MediMentor-AI
# 🩺 MediMentor AI
Hackathon_24/
├── main.py                 # 💻 Streamlit frontend app (UI & user logic)
├── utils.py                # 🧠 Backend AI logic and helper functions
├── requirements.txt        # 📦 Python dependencies
├── README.md               # 📄 Project documentation (this file)
├── assets/                 # 🖼️ Optional: Images, icons, or screenshots
│   └── screenshot1.png     #     Sample app screenshot
├── data/                   # 🗂️ Optional: PDF reports or user logs
│   └── health_report.pdf   #     Example generated PDF report
└── .streamlit/             # ⚙️ Streamlit config (optional)
    └── config.toml         #     Custom page settings (title, favicon)

An AI-powered Health Advisor built with Streamlit to assist users with:
- Disease prediction
- Specialist suggestion
- Medicine & dosage recommendation
- Diet & lifestyle tips
- Mental health screening
- PDF health report generation

## 📦 Features
- AI skin diagnosis (optional image)
- Emergency signal detection
- Chat with AI doctor
- LangChain chat memory support (optional)
- Export reports in PDF

## 🛠️ Tech Stack
- Streamlit
- Python (utils)
- fpdf (PDF)
- LangChain (optional)

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run main.py
