import streamlit as st
from health_workflow import create_health_graph
from database import init_db, save_report, get_reports
from pdf_generator import generate_pdf

# Initialize DB
init_db()

# Page Style
st.set_page_config(page_title="MedMate", layout="wide")

# ----- Custom CSS Styling -----
st.markdown("""
    <style>
    .title {font-size: 36px; font-weight: bold; text-align: center; color: #2B7A78;}
    .subtitle {font-size: 18px; text-align: center; color: #3A3A3A; margin-bottom: 30px;}
    .card {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
        margin-top: 20px;
    }
    .sidebar-report {
        background: #DEF7E8;
        padding: 8px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# ----- Title -----
st.markdown("<div class='title'>🩺 MedMate</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>" " Your AI Health Companion for Wellness Guidance, Symptom Insights & Personalized Diet Plans</div>", unsafe_allow_html=True)

# ----- Input Form -----
with st.container():
    symptoms = st.text_area("📝 Describe your symptoms:", placeholder="e.g., fever, headache, tiredness...")
    col1, col2 = st.columns(2)
    with col1:
        duration = st.text_input("⏳ Duration:", placeholder="e.g., 3 days")
    with col2:
        severity = st.selectbox("⚠️ Severity Level:", ["Mild", "Moderate", "Severe"])
    generate_btn = st.button("✨ Generate Health Report", use_container_width=True)

# ----- Processing -----
if generate_btn and symptoms.strip():

    with st.spinner(" Analyzing your symptoms... Please wait..."):
        graph = create_health_graph()
        result = graph.invoke({
            "input": symptoms,
            "duration": duration,
            "severity": severity
        })

    diagnosis = str(result.get("diagnosis", "No result"))
    diet = str(result.get("diet", "No result"))
    report = str(result.get("report", "No summary"))

    # Save to DB
    save_report(symptoms, duration, severity, diagnosis, diet, report)

    st.success("✅ Report Generated Successfully!")




    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🧠 Possible Health Conditions")
    st.write(diagnosis)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🥗 Personalized Diet Recommendations")
    st.write(diet)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📄 Final Well-Being Summary")
    st.write(report)
    st.markdown("</div>", unsafe_allow_html=True)

    # PDF Download
    pdf_data = {
        "Symptoms": symptoms,
        "Duration": duration,
        "Severity": severity,
        "Diagnosis": diagnosis,
        "Diet": diet,
        "Report": report
    }
    pdf_file = generate_pdf(pdf_data)
    with open(pdf_file, "rb") as f:
        st.download_button("⬇️ Download Report as PDF", f, file_name=pdf_file, use_container_width=True)


# ---- Sidebar: Saved Reports History -----
st.sidebar.header("📜 Previous Reports")
history = get_reports()

if history:
    for row in history:
        st.sidebar.markdown(f"""
        <div class='sidebar-report'>
        🩺 <b>Symptoms:</b> {row[1]} <br>
        ⏳ <b>Duration:</b> {row[2]} <br>
        ⚠️ <b>Severity:</b> {row[3]}
        </div>
        """, unsafe_allow_html=True)
else:
    st.sidebar.write("No saved reports yet.")




