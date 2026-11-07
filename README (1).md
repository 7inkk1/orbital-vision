# 🛰️ Orbital Vision – Autonomous Spacecraft Anomaly Inspector

An AI-powered space safety dashboard leveraging Google Gemini 3.8-Flash to diagnose spacecraft visual telemetry, calculate structural integrity scores, and auto-generate 3-step EVA repair protocols in real time.

## 🚀 Key Features
- **Multi-Orbit Telemetry Baseline Selection:** Supports LEO, Geostationary, Deep Space Gateway, and Lunar orbits.
- **Diagnostic Depth Modes:** Toggle between Standard Scan and Critical Structural Safety Check.
- **Automated 3-Part Reports:** Instant anomaly detection, threat/severity assessment, and actionable EVA repair steps (Isolation, Repair, Verification).

## 🛠️ Tech Stack
- **Frontend:** Python, Streamlit
- **AI Engine:** Google Gemini SDK (`google-genai`) running on `gemini-3.8-flash`

## 🏃 Local Setup & Run
1. Clone this repository:
   ```bash
   git clone [https://github.com/7inkk1/orbital-vision.git](https://github.com/7inkk1/orbital-vision.git)
   cd orbital-vision
   Install dependencies:

Bash
pip install -r requirements.txt
Set your Gemini API key:

Bash
export GEMINI_API_KEY="your_api_key_here"
Run the application:

Bash
streamlit run app.py
📹 Demo Video
Watch the full 3-minute project demonstration on YouTube.
