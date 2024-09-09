# Helper file with functions to be used in the main file

import streamlit as st
from diabetes import models_demo    


def generate_template(user_data, risk_score, healthy_score, relative_risk):
    message = f"Hi, I'm {user_data['name']}, a {user_data['gender']} aged {user_data['age']} with the following health information:\n"
    message += f"- Atypical Antipsychotic Use: {user_data.get('b_atypicalantipsy', 'Unknown')}\n"
    message += f"- Corticosteroid Use: {user_data.get('b_corticosteroids', 'Unknown')}\n"
    message += f"- Impotence: {user_data.get('b_impotence', 'Unknown')}\n"
    message += f"- Migraine: {user_data.get('b_migraine', 'Unknown')}\n"
    message += f"- Rheumatoid Arthritis: {user_data.get('b_ra', 'Unknown')}\n"
    message += f"- Renal Disease: {user_data.get('b_renal', 'Unknown')}\n"
    message += f"- Sleep Apnea: {user_data.get('b_semi', 'Unknown')}\n"
    message += f"- Systemic Lupus Erythematosus: {user_data.get('b_sle', 'Unknown')}\n"
    message += f"- Treated Hypertension: {user_data.get('b_treatedhyp', 'Unknown')}\n"
    message += f"- Type 1 Diabetes: {user_data.get('b_type1', 'Unknown')}\n"
    message += f"- Type 2 Diabetes: {user_data.get('b_type2', 'Unknown')}\n"
    message += f"- BMI: {user_data.get('bmi', 'Unknown')}\n"
    message += f"- Family History of Cardiovascular Disease: {user_data.get('fh_cvd', 'Unknown')}\n"
    message += f"- Waist-to-Hip Ratio: {user_data.get('ratio', 'Unknown')}\n"
    message += f"- Systolic Blood Pressure (SBP): {user_data.get('sbp', 'Unknown')}\n"
    message += f"- High SBP (>130): {user_data.get('sbps5', 'Unknown')}\n"
    message += f"- Smoking Category: {user_data.get('smoke_cat', 'Unknown')}\n"
    message += f"- Alcohol Consumption: {user_data.get('alc', 'Unknown')}\n"
    message += f"- Physical Activity Level: {user_data.get('active', 'Unknown')}\n"
    message += f"- CVD Risk Score: {risk_score}\n"
    message += f"- Healthy Risk Score: {healthy_score}\n"
    message += f"- Relative Risk Score: {relative_risk}\n"
    message += '''\nAnalyze my attributes and risk scores closely, then give me personalized mitigation
    measures and areas in which I should make changes to my lifestyle depending on myattribute and to
    what extend I must follow these measures according to the risk scores and my age.'''
    return message


def calculate_bmi(height, weight):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi


def diabetes_prediction_section():
    st.title("Diabetes Predictor")
    
    
    input_data = {
        "age": st.number_input("Enter your age:", min_value=0, max_value=90, value=30),
        "gender": st.radio("Select your gender:", ("Male", "Female"), key="diabetes_gender"),
        "polyuria": st.radio("Do you experience Polyuria (Excessive urination)?", ("No", "yes"), key="diabetes_polyuria"),
        "polydipsia": st.radio("Do you experience Polydipsia (Excessive thirst)?", ("No", "yes"), key="diabetes_polydipsia"),
        "sudden_weight_loss": st.radio("Do you experience Sudden Weight Loss?", ("No", "yes"), key="diabetes_sudden_weight_loss"),
        "weakness": st.radio("Do you experience Weakness?", ("No", "yes"), key="diabetes_weakness"),
        "polyphagia": st.radio("Do you experience Polyphagia (excessive hunger)?", ("No", "yes"), key="diabetes_polyphagia"),
        "genital_thrush": st.radio("Do you experience Genital Thrush?", ("No", "yes"), key="diabetes_genital_thrush"),
        "visual_blurring": st.radio("Do you experience Visual Blurring?", ("No", "yes"), key="diabetes_visual_blurring"),
        "itchy_skin": st.radio("Do you experience Itchy Skin?", ("No", "yes"), key="diabetes_itchy_skin"),
        "irritability": st.radio("Do you experience Irritability?", ("No", "yes"), key="diabetes_irritability"),
        "delayed_healing": st.radio("Do you experience Delayed Healing?", ("No", "yes"), key="diabetes_delayed_healing"),
        "partial_paresis": st.radio("Do you experience Partial Paresis?", ("No", "yes"), key="diabetes_partial_paresis"),
        "muscle_stiffness": st.radio("Do you experience Muscle Stiffness?", ("No", "yes"), key="diabetes_muscle_stiffness"),
        "alopecia": st.radio("Do you experience Alopecia?", ("No", "yes"), key="diabetes_alopecia"),
        "obesity": st.radio("Do you have Obesity?", ("No", "yes"), key="diabetes_obesity")
    }


    if st.button("Predict Diabetes"):
        diabetes_results = models_demo(input_data)
        st.write("Diabetes Prediction Results:")
        for model, prediction in diabetes_results.items():
            if prediction == 'Positive':
                st.write(f"{model} model predicts that you might be **Diabetic**")
            else:
                st.write(f"{model} model predicts that you might be **Non-Diabetic**")


def bmi_calculator_section():
    st.title("BMI Calculator")

    height = st.number_input("Enter your height (in cm):", min_value=0, value=200)
    weight = st.number_input("Enter your weight (in kg):", min_value=0, value=100)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(height, weight)
        st.write(f"Your BMI is: {bmi:.2f}")