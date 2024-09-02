import streamlit as st
from cvdmodel import calculate_cvd_score, calculate_healthy_cvd_score, calculate_relative_risk
from llama2 import gen_response
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
    message += "\nTaking my attributes and risk scores into account, give me personalized mitigation measures and areas in which I can improve and to what extend I must follow these measures according to the risk scores and my age."
    return message

def calculate_bmi(height, weight):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

def main():

    st.title("Personal Health Assistant")

    name = st.text_input("What is your name?")

    st.title("Diabetes Predictor")
    age = st.number_input("Enter your age:", min_value=0, max_value=90, value=30)
    gender = st.radio("Select your gender:", ("Male", "Female"))
    polyuria = st.radio("Do you experience Polyuria (Excessive urination)?", ("No", "yes"))
    polydipsia = st.radio("Do you experience Polydipsia (Excessive thirst)?", ("No", "yes"))
    sudden_weight_loss = st.radio("Do you experience Sudden Weight Loss?", ("No", "yes"))
    weakness = st.radio("Do you experience Weakness?", ("No", "yes"))
    polyphagia = st.radio("Do you experience Polyphagia (excessive hunger)?", ("No", "yes"))
    genital_thrush = st.radio("Do you experience Genital Thrush?", ("No", "yes"))
    visual_blurring = st.radio("Do you experience Visual Blurring?", ("No", "yes"))
    itchy_skin = st.radio("Do you experience Itchy Skin?", ("No", "yes"))
    irritability = st.radio("Do you experience Irritability?", ("No", "yes"))
    delayed_healing = st.radio("Do you experience Delayed Healing?", ("No", "yes"))
    partial_paresis = st.radio("Do you experience Partial Paresis?", ("No", "yes"))
    muscle_stiffness = st.radio("Do you experience Muscle Stiffness?", ("No", "yes"))
    alopecia = st.radio("Do you experience Alopecia?", ("No", "yes"))
    obesity = st.radio("Do you have Obesity?", ("No", "yes"))

    if st.button("Predict Diabetes"):
        input_data = {
            "age": age,
            "gender": gender,
            "polyuria": polyuria,
            "polydipsia": polydipsia,
            "sudden_weight_loss": sudden_weight_loss,
            "weakness": weakness,
            "polyphagia": polyphagia,
            "genital_thrush": genital_thrush,
            "visual_blurring": visual_blurring,
            "itchy_skin": itchy_skin,
            "irritability": irritability,
            "delayed_healing": delayed_healing,
            "partial_paresis": partial_paresis,
            "muscle_stiffness": muscle_stiffness,
            "alopecia": alopecia,
            "obesity": obesity
        }
        diabetes_results = models_demo(input_data)
        st.write("Diabetes Prediction Results:")
        for model, prediction in diabetes_results.items():
            if prediction == 'Positive':
                st.write(f"{model} model predicts that you might be **Non-Diabetic**")
            else:
                st.write(f"{model} model predicts that you might be **Diabetic**")

    st.title("BMI Calculator")

    height = st.number_input("Enter your height (in cm):", min_value=0, value=200)
    weight = st.number_input("Enter your weight (in kg):", min_value=0, value=100)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(height, weight)
        st.write(f"Your BMI is: {bmi:.2f}")

    st.title("Cardiovascular Disease (CVD) Risk Calculator")

    b_af = st.radio("Are you affected by atrial fibrillation?", ("No", "Yes"))
    b_atypicalantipsy = st.radio("Are you on atypical antipsychotic medications?", ("No", "Yes"))
    b_corticosteroids = st.radio("Are you on corticosteroids?", ("No", "Yes"))
    b_impotence2 = st.radio("Do you have impotence?", ("No", "Yes"))
    b_migraine = st.radio("Do you have a history of migraine?", ("No", "Yes"))
    b_ra = st.radio("Do you have rheumatoid arthritis?", ("No", "Yes"))
    b_renal = st.radio("Do you have renal disease?", ("No", "Yes"))
    b_semi = st.radio("Have you experienced a myocardial infarction?", ("No", "Yes"))
    b_sle = st.radio("Do you have systemic lupus erythematosus?", ("No", "Yes"))
    b_treatedhyp = st.radio("Are you being treated for hypertension?", ("No", "Yes"))
    b_type1 = st.radio("Do you have type 1 diabetes?", ("No", "Yes"))
    b_type2 = st.radio("Do you have type 2 diabetes?", ("No", "Yes"))
    fh_cvd = st.radio("Do you have a family history of cardiovascular disease?", ("No", "Yes"))
    smoke_cat = int(st.radio("Enter your smoking category:          [0 for Non-Smoker, 1 for Ex-Smoker, 2 for Light Smoker, 3 for Moderate Smoker, 4 for Heavy Smoker]", ("0", "1", "2", "3", "4")))
    alc = st.radio("Do you consume alcohol?", ("No", "Yes"))
    active = st.radio("Do you workout?", ("No", "Yes"))
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
        **CVD Risk Score:** This score estimates your risk of developing cardiovascular diseases (CVDs) such as heart attack and stroke over the next 10 years. A higher score indicates a higher risk of developing CVD over this period.

        """)

        st.write(f"Your ideal health score is: {healthy_score}")
        st.markdown("""
        **Healthy Risk Score:** This score represents the risk of developing cardiovascular diseases (CVDs) if you maintain ideal health behaviors and conditions. That is, this is the ideal score that someone of your age and gender is subject to. It serves as a reference point for comparison with your actual risk score.

        """)

        st.write(f"Your relative risk score is: {relative_risk}")
        st.markdown("""
        **Relative Risk Score:** This score compares your actual CVD risk with the risk you would have if you maintained ideal health behaviors and conditions. A score greater than 1 indicates a higher risk compared to the ideal scenario, while a score less than 1 indicates a lower risk.
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
        mitigation_measure = gen_response(message)
        st.write("Mitigation Measures:")
        st.write(mitigation_measure)



    st.header("Explanations for CVD Attributes")
    st.markdown("""
    - **Atrial Fibrillation (AF):** Irregular heart rhythm that can lead to blood clots, stroke, and heart failure.
    - **Atypical Antipsychotic Use:** Taking medications for certain mental health conditions that may increase the risk of diabetes and heart problems.
    - **Corticosteroid Use:** Using medications like prednisone, which can raise blood pressure, blood sugar, and cholesterol levels.
    - **Impotence:** Difficulty achieving or maintaining an erection, which can be a sign of heart disease.
    - **Migraine:** Severe headaches that may increase the risk of stroke and heart attack, especially in women.
    - **Rheumatoid Arthritis (RA):** Inflammatory joint disease that can affect the heart and increase cardiovascular risk.
    - **Renal Disease:** Kidney damage that can lead to high blood pressure and heart problems.
    - **Myocardial Infarction (MI):** Heart attack, a serious condition caused by blocked blood flow to the heart muscle.
    - **Systemic Lupus Erythematosus (SLE):** Autoimmune disease that can affect the heart, joints, and other organs.
    - **Treated Hypertension:** High blood pressure that requires medication to control and reduce the risk of heart disease.
    - **Type 1 Diabetes:** Autoimmune condition where the body attacks insulin-producing cells, leading to high blood sugar levels.
    - **Type 2 Diabetes:** Metabolic disorder characterized by insulin resistance or reduced insulin production, increasing the risk of heart disease.
    - **Body Mass Index (BMI):** Measure of body fat based on height and weight. A BMI over 25 indicates overweight, increasing the risk of heart problems.
    - **Family History of Cardiovascular Disease (CVD):** Increased risk of heart disease if close relatives have had heart attacks, strokes, or other heart-related conditions.
    - **Waist-to-Hip Ratio:** Measure of fat distribution in the body. Higher ratios indicate more abdominal fat, increasing the risk of heart disease.
    - **Systolic Blood Pressure (SBP):** Top number in blood pressure readings, indicating the pressure in arteries when the heart beats. High SBP increases the risk of heart disease and stroke.
    - **Standard Deviation of SBP:** Variation in blood pressure readings over time. High variability may indicate an increased risk of heart problems.
    - **Smoking Category:** Level of tobacco use, with higher categories indicating greater risk of heart disease and other health issues.
    - **Alcohol Consumption:** Amount of alcohol consumed, which can affect heart health depending on the quantity and frequency of consumption.
    - **Physical Activity Level:** Level of exercise, with higher activity levels associated with lower risk of heart disease and better overall health.
    """)

    st.header("Explanations for Diabetic Attributes")
    st.markdown("""
    - **Polyuria:** Frequent urination, often accompanied by increased thirst. It can be a sign of high blood sugar levels in diabetes.
    - **Polydipsia:** Excessive thirst, often accompanied by dry mouth. It occurs when the body tries to compensate for fluid loss from frequent urination.
    - **Sudden Weight Loss:** Rapid and unintentional weight loss, which may occur due to uncontrolled diabetes or insulin deficiency.
    - **Weakness:** Lack of strength or energy, which can result from fluctuating blood sugar levels and inadequate glucose utilization in diabetes.
    - **Polyphagia:** Excessive hunger or increased appetite, often seen in uncontrolled diabetes due to the body's inability to use glucose for energy.
    - **Genital Thrush:** Yeast infection in the genital area, common in individuals with uncontrolled diabetes due to high blood sugar levels providing a favorable environment for yeast growth.
    - **Visual Blurring:** Blurred or impaired vision, which can occur due to high blood sugar levels affecting the shape of the eye lens in individuals with uncontrolled diabetes.
    - **Itchy Skin:** Persistent itching or dry skin, often experienced by individuals with uncontrolled diabetes due to poor circulation and nerve damage.
    - **Irritability:** Mood swings or irritability, which can result from fluctuating blood sugar levels affecting brain function and emotional regulation.
    - **Delayed Healing:** Slow wound healing or frequent infections, which can occur in individuals with uncontrolled diabetes due to impaired immune function and poor circulation.
    - **Partial Paresis:** Weakness or paralysis affecting part of the body, commonly seen in individuals with uncontrolled diabetes due to nerve damage (neuropathy).
    - **Muscle Stiffness:** Stiffness or rigidity in the muscles, which can result from nerve damage (neuropathy) or reduced blood flow in individuals with uncontrolled diabetes.
    - **Alopecia:** Hair loss or thinning, which can occur in individuals with uncontrolled diabetes due to poor circulation and nutrient deficiencies affecting hair follicles.
    - **Obesity:** Excess body weight or adiposity, which is a risk factor for developing type 2 diabetes and can exacerbate symptoms in individuals with existing diabetes.
    """)

if __name__ == "__main__":
    main()




