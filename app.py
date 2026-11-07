import os
import streamlit as st
from google import genai
from PIL import Image

# Initialize Gemini Client
client = genai.Client(api_key="AQ.Ab8RN6LVWCR-eGWLoehM0diJldFz4IsTkEID1UEs2nAO1WXxEjw")
st.set_page_config(page_title="Orbital Vision - Autonomous Satellite Inspector", page_icon="🛰️", layout="centered")

st.title("🛰️ Orbital Vision")
st.caption("AI-Powered Spacecraft Hull & Solar Array Anomaly Inspector")
st.write(
    "Upload visual telemetry, satellite imagery, or orbital component photos to run automated "
    "structural anomaly detection, evaluate micrometeorite/thermal damage severity, and generate EVA repair protocols."
)

# Sidebar configurations
with st.sidebar:
    st.header("⚙️ Telemetry Settings")
    orbit_type = st.selectbox("Orbit Designation", ["Low Earth Orbit (LEO)", "Geostationary (GEO)", "Deep Space Gateway", "Lunar Orbit"])
    urgency_filter = st.radio("Diagnostic Depth", ["Standard Scan", "Critical Structural Safety Check"])

# File uploader
uploaded_file = st.file_uploader("Upload visual telemetry photo:", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Orbital Telemetry Scan", use_container_width=True)
    
    if st.button("🔍 Run Anomaly Detection Scan", type="primary"):
        with st.spinner("Analyzing visual telemetry with gemini-3.8-flash..."):
            try:
                prompt = f"""
                You are NASA/ESA's head Autonomous Spacecraft Inspection & Repair AI.
                Analyze the provided image of spacecraft/satellite hardware and format your analysis strictly in Markdown:

                ### 📡 1. Component Identification & Anomaly Scan
                - **Target Component:** Identify the machine, solar panel, hull, or machinery shown.
                - **Detected Structural Anomalies:** List cracks, burns, surface wear, debris impact points, or component failures found.
                - **Overall Structural Integrity Score:** (Assign a percentage e.g., 78% Operational Integrity).

                ### ⚠️ 2. Threat & Severity Assessment
                Classify the primary issue using one of these risk ratings:
                - 🔴 **CRITICAL HAZARD** (Immediate risk of mission failure or atmospheric decompression)
                - 🟡 **MODERATE DEGRADATION** (Requires scheduled maintenance within 48 hours)
                - 🟢 **NOMINAL / MINOR WEAR** (Non-critical surface anomaly)

                ### 🛠️ 3. Spacewalk (EVA) Repair Protocol
                Provide step-by-step engineering instructions for astronauts or robotic arms to repair the anomaly:
                1. *Isolation Step:* How to safely power down or depressurize the component.
                2. *Repair Step:* Exact materials/tools needed (e.g., thermal tape, patch kit, solar panel cell swap).
                3. *Verification Step:* Diagnostic test to confirm fix.
                """

                response = client.models.generate_content(
                    model='gemini-3.8-flash',
                    contents=[img, prompt]
                )

                st.success("Telemetry Scan & Diagnostic Complete!")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Error executing Gemini API: {e}")