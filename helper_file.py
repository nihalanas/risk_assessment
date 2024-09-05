# Helper file with functions to be used in the main file

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
