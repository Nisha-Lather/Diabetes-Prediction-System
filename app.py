import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Custom styling
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f9fbff;
        }
        .stButton > button {
            background-color: #007bff;
            color: white;
            padding: 10px 24px;
            font-size: 18px;
            border-radius: 10px;
            border: none;
        }
        .stButton > button:hover {
            background-color: #0056b3;
            transition: 0.3s;
        }
        .result {
            font-size: 22px;
            font-weight: bold;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }
        .diabetic {
            background-color: #ffe6e6;
            color: red;
        }
        .not-diabetic {
            background-color: #e6ffe6;
            color: green;
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown("<h1 style='text-align: center; color: #004080;'>🩺 Diabetes Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey;'>Enter your medical info to check diabetes risk</h4>", unsafe_allow_html=True)
st.write("")

# Input fields in two columns
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, step=1)
    glucose = st.number_input("Glucose Level", 0.0, 300.0)
    blood_pressure = st.number_input("Blood Pressure", 0.0, 200.0)
    skin_thickness = st.number_input("Skin Thickness", 0.0, 100.0)

with col2:
    insulin = st.number_input("Insulin Level", 0.0, 900.0)
    bmi = st.number_input("BMI", 0.0, 70.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
    age = st.number_input("Age", 1, 120, step=1)

st.write("")
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

# Predict button
if st.button("🔍 Predict Diabetes Risk"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.markdown(
            "<div class='result diabetic'> The person is likely <b>Diabetic</b>.</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div class='result not-diabetic'> The person is <b>Not Diabetic</b>.</div>",
            unsafe_allow_html=True
        )
st.markdown("</div>", unsafe_allow_html=True)
