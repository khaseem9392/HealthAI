import streamlit as st
from modules.chat_interface import answer_patient_query
from modules.disease_predictor import predict_disease
from modules.treatment_plan import generate_treatment_plan
from modules.health_analytics import generate_demo_chart

st.set_page_config(page_title="HealthAI", page_icon="🩺", layout="wide")
st.sidebar.title("HealthAI Navigation")
choice = st.sidebar.radio("Go to", ["Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics"])

if choice == "Patient Chat":
    st.header("🗨 Patient Chat")
    query = st.text_input("Ask a health question")
    if st.button("Send"):
        response = answer_patient_query(query)
        st.markdown(response)

elif choice == "Disease Prediction":
    st.header("🧪 Disease Prediction")
    with st.form("prediction_form"):
        symptoms = st.text_input("Symptoms")
        age = st.number_input("Age", 0, 120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        history = st.text_input("Medical History")
        hr = st.number_input("Heart Rate (bpm)", 40, 180)
        sys = st.number_input("BP - Systolic", 80, 200)
        dia = st.number_input("BP - Diastolic", 50, 130)
        glucose = st.number_input("Glucose Level (mg/dL)", 50, 300)
        recent = st.text_input("Recent Events (travel, exposure, etc.)")
        submit = st.form_submit_button("Predict")
    if submit:
        result = predict_disease(symptoms, age, gender, history, hr, sys, dia, glucose, recent)
        st.text(result)

elif choice == "Treatment Plans":
    st.header("💊 Treatment Plan")
    condition = st.text_input("Enter condition (e.g. Diabetes, Cold)")
    if st.button("Generate Plan"):
        plan = generate_treatment_plan(condition)
        st.text(plan)

elif choice == "Health Analytics":
    st.header("📊 Health Analytics")
    fig = generate_demo_chart()
    st.plotly_chart(fig)