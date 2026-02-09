import streamlit as st
import pandas as pd

st.set_page_config(page_title="BMI Calculator", layout="centered")

st.title("BMI Calculator")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")

with col2:
    height = st.number_input("Height (m)", min_value=0.0, format="%.2f")

if st.button("Calculate BMI", use_container_width=True):
    if weight <= 0 or height <= 0:
        st.error("Please enter positive numbers for weight and height.")
    else:
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            result = "Underweight"
            color = "🔵"
        elif bmi < 25:
            result = "Normal"
            color = "🟢"
        elif bmi < 30:
            result = "Overweight"
            color = "🟠"
        else:
            result = "Obese"
            color = "🔴"

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Your BMI", bmi)
        with col2:
            st.metric("Category", result)

        # BMI Chart Data
        bmi_data = {
            "Category": ["Underweight", "Normal", "Overweight", "Obese"],
            "Max BMI": [18.5, 25, 30, 40],
            "Color": ["blue", "green", "orange", "red"]
        }
        df = pd.DataFrame(bmi_data)
        
        st.bar_chart(df.set_index("Category")["Max BMI"], use_container_width=True)
        st.success(f"✅ Your BMI is {bmi} - You are {result}!")
