import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="BMI Calculator", layout="centered")

st.title("BMI Calculator")

weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Height (m)", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if weight <= 0 or height <= 0:
        st.error("Please enter positive numbers for weight and height.")
    else:
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            result = "Underweight"
            color = "blue"
        elif bmi < 25:
            result = "Normal"
            color = "green"
        elif bmi < 30:
            result = "Overweight"
            color = "orange"
        else:
            result = "Obese"
            color = "red"

        st.markdown(f"**BMI:** <span style='color:{color}'>{bmi}</span>", unsafe_allow_html=True)
        st.markdown(f"**Result:** <span style='color:{color}'>{result}</span>", unsafe_allow_html=True)

        categories = ["Underweight", "Normal", "Overweight", "Obese"]
        ranges = [18.5, 25, 30, 40]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(categories, ranges, color=["blue", "green", "orange", "red"])
        ax.axhline(y=bmi, color="black", linestyle="--", label=f"Your BMI: {bmi}")
        ax.set_ylabel("BMI Value")
        ax.set_title("BMI Category Chart")
        ax.legend()
        st.pyplot(fig)
