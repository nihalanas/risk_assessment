import streamlit as st
from cvdmodel import *
from llama2 import gen_response
from helper_file import *
from explanations import *


def main():
    st.title("Personal Health Assistant")

    name = st.text_input("What is your name?")

    diabetes_prediction_section()
    bmi_calculator_section()

    st.title("Cardiovascular Disease (CVD) Risk Calculator")

    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=30)
    gender = st.radio("Select your gender:", ("Male", "Female"), key="cvd_gender")

    b_af = st.radio("Are you affected by atrial fibrillation?", ("No", "Yes"), key="cvd_af")
    b_atypicalantipsy = st.radio("Are you on atypical antipsychotic medications?", ("No", "Yes"), key="cvd_atypicalantipsy")
    b_corticosteroids = st.radio("Are you on corticosteroids?", ("No", "Yes"), key="cvd_corticosteroids")
    b_impotence2 = st.radio("Do you have impotence?", ("No", "Yes"), key="cvd_impotence2")
    b_migraine = st.radio("Do you have a history of migraine?", ("No", "Yes"), key="cvd_migraine")
    b_ra = st.radio("Do you have rheumatoid arthritis?", ("No", "Yes"), key="cvd_ra")
    b_renal = st.radio("Do you have renal disease?", ("No", "Yes"), key="cvd_renal")
    b_semi = st.radio("Have you experienced a myocardial infarction?", ("No", "Yes"), key="cvd_semi")
    b_sle = st.radio("Do you have systemic lupus erythematosus?", ("No", "Yes"), key="cvd_sle")
    b_treatedhyp = st.radio("Are you being treated for hypertension?", ("No", "Yes"), key="cvd_treatedhyp")
    b_type1 = st.radio("Do you have type 1 diabetes?", ("No", "Yes"), key="cvd_type1")
    b_type2 = st.radio("Do you have type 2 diabetes?", ("No", "Yes"), key="cvd_type2")
    fh_cvd = st.radio("Do you have a family history of cardiovascular disease?", ("No", "Yes"), key="cvd_fh_cvd")
    smoke_cat = int(st.radio("Enter your smoking category: [0 for Non-Smoker, 1 for Ex-Smoker, 2 for Light Smoker, 3 for Moderate Smoker, 4 for Heavy Smoker]", ("0", "1", "2", "3", "4"), key="cvd_smoke_cat"))
    alc = st.radio("Do you consume alcohol?", ("No", "Yes"), key="cvd_alc")
    active = st.radio("Do you workout?", ("No", "Yes"), key="cvd_active")
    bmi = st.number_input("Enter your BMI score (Body Mass Index Score):", min_value=0.0, value=25.0)
    ratio = st.number_input("Enter ratio of total cholesterol to HDL cholesterol:", min_value=0.0, value=4.0)
    sbp = st.number_input("Enter your systolic blood pressure(SBP):", min_value=0, value=120)
    sbps5 = st.number_input("Enter your standard deviation of at least two most recent systolic blood pressure readings:", min_value=0, value=5)

    if st.button("Calculate RISK Scores"):         
        
        risk_score = calculate_cvd_score(
            age=age,
            gender="male" if gender == "Male" else "female",
            b_AF=1 if b_af == "Yes" else 0,
            b_atypicalantipsy=1 if b_atypicalantipsy == "Yes" else 0,
            b_corticosteroids=1 if b_corticosteroids == "Yes" else 0,
            b_impotence2=1 if b_impotence2 == "Yes" else 0,
            b_migraine=1 if b_migraine == "Yes" else 0,
            b_ra=1 if b_ra == "Yes" else 0,
            b_renal=1 if b_renal == "Yes" else 0,
            b_semi=1 if b_semi == "Yes" else 0,
            b_sle=1 if b_sle == "Yes" else 0,
            b_treatedhyp=1 if b_treatedhyp == "Yes" else 0,
            b_type1=1 if b_type1 == "Yes" else 0,
            b_type2=1 if b_type2 == "Yes" else 0,
            bmi=bmi,
            fh_cvd=1 if fh_cvd == "Yes" else 0,
            alc=1 if alc == "Yes" else 0,
            active=1 if active == "Yes" else 0,
            rati=ratio,
            sbp=sbp,
            sbps5=sbps5,
            smoke_cat=smoke_cat
        )
        
        healthy_score = calculate_healthy_cvd_score(
            age=age,
            gender="male" if gender == "Male" else "female",
            ethrisk=2
        )
        
        relative_risk = calculate_relative_risk(
            risk_score, healthy_score
        )

        st.write(f"Your CVD RISK score is: {risk_score}")
        st.markdown("""
        **CVD Risk Score:** This score estimates your risk of developing cardiovascular diseases (CVDs)
        such as heart attack and stroke over the next 10 years. A higher score indicates a higher risk
        of developing CVD over this period.
        """)

        st.write(f"Your ideal health score is: {healthy_score}")
        st.markdown("""
        **Healthy Risk Score:** This score represents the risk of developing cardiovascular diseases (CVDs)
        if you maintain ideal health behaviors and conditions. That is, this is the ideal score that
        someone of your age and gender is subject to. It serves as a reference point for comparison with
        your actual risk score.
        """)

        st.write(f"Your relative risk score is: {relative_risk}")
        st.markdown("""
        **Relative Risk Score:** This score compares your actual CVD risk with the risk you would have if
        you maintained ideal health behaviors and conditions. A score greater than 1 indicates a higher risk compared to the ideal scenario, while a score less than 1 indicates a lower risk.
        """)

    if st.button("Generate Mitigation Measures"):
        user_data = {
            "name": name,
            "age": age,
            "gender": gender,
            "b_AF": 1 if b_af == "Yes" else 0,
            "b_atypicalantipsy": 1 if b_atypicalantipsy == "Yes" else 0,
            "b_corticosteroids": 1 if b_corticosteroids == "Yes" else 0,
            "b_impotence2": 1 if b_impotence2 == "Yes" else 0,
            "b_migraine": 1 if b_migraine == "Yes" else 0,
            "b_ra": 1 if b_ra == "Yes" else 0,
            "b_renal": 1 if b_renal == "Yes" else 0,
            "b_semi": 1 if b_semi == "Yes" else 0,
            "b_sle": 1 if b_sle == "Yes" else 0,
            "b_treatedhyp": 1 if b_treatedhyp == "Yes" else 0,
            "b_type1": 1 if b_type1 == "Yes" else 0,
            "b_type2": 1 if b_type2 == "Yes" else 0,
            "bmi": bmi,
            "fh_cvd": 1 if fh_cvd == "Yes" else 0,
            "alc": 1 if alc == "Yes" else 0, 
            "active": 1 if active == "Yes" else 0,
            "rati": ratio,
            "sbp": sbp,
            "sbps5": sbps5,
            "smoke_cat": smoke_cat      
        }
        
        risk_score = calculate_cvd_score(
            age=age,
            gender="male" if gender == "Male" else "female",
            b_AF=1 if b_af == "Yes" else 0,
            b_atypicalantipsy=1 if b_atypicalantipsy == "Yes" else 0,
            b_corticosteroids=1 if b_corticosteroids == "Yes" else 0,
            b_impotence2=1 if b_impotence2 == "Yes" else 0,
            b_migraine=1 if b_migraine == "Yes" else 0,
            b_ra=1 if b_ra == "Yes" else 0,
            b_renal=1 if b_renal == "Yes" else 0,
            b_semi=1 if b_semi == "Yes" else 0,
            b_sle=1 if b_sle == "Yes" else 0,
            b_treatedhyp=1 if b_treatedhyp == "Yes" else 0,
            b_type1=1 if b_type1 == "Yes" else 0,
            b_type2=1 if b_type2 == "Yes" else 0,
            bmi=bmi,
            fh_cvd=1 if fh_cvd == "Yes" else 0,
            alc=1 if alc == "Yes" else 0,
            active=1 if active == "Yes" else 0,
            rati=ratio,
            sbp=sbp,
            sbps5=sbps5,
            smoke_cat=smoke_cat
        )
        
        healthy_score = calculate_healthy_cvd_score(
            age=age,
            gender="male" if gender == "Male" else "female",
            ethrisk=2
        )
        
        relative_risk = calculate_relative_risk(
            risk_score, healthy_score
        )
        
        message = generate_template(user_data, risk_score, healthy_score, relative_risk)
        mitigation_measure = gen_response(message)  # Calls the gen_response function from llama2.py file. 
        
        st.write("Mitigation Measures:")
        st.write(mitigation_measure)    

    # Calls explanations for CVD and Diabetes attributes from explanations.py
    st.header("Explanations for CVD Attributes")
    st.markdown(cvd_explanation())

    st.header("Explanations for Diabetic Attributes")
    st.markdown(diabetes_explanation())

if __name__ == "__main__":
    main()



