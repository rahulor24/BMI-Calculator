import streamlit as st

st.title("BMI Calculator")

st.header("Enter your details")
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
height = st.number_input("Height (cm)", min_value=0.0, step=0.1)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / ((height / 100) ** 2)
        st.subheader(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.error("Please enter a valid height greater than 0.")