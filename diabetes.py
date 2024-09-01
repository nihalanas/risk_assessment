import pickle  
import numpy as np  


# Function to normalize age and append it to the input list
def Age_to_onehot(inLst, input):
    try:
        normalized_age = (int(input) - 16) / (90 - 16) 
        inLst.extend([normalized_age]) 
    except ValueError as e:
        print(f"Note: {e}; using default value")  
        inLst.extend([0.5]) 


# Function to convert Boolean input to one-hot encoding and append to the list
def Bool_to_onehot(inLst, input):
    if input.lower() in ['yes', 'y', '1']:
        inLst.extend([1, 0])  
    elif input.lower() in ['no', 'n', '0']:
        inLst.extend([0, 1])  
    else:
        print("Note: Input pattern not recognized; using default value") 
        inLst.extend([0, 1])  


# Function to convert gender input to one-hot encoding and append to the list.
def Gender_to_onehot(inLst, input):
    if input.lower() in ['male', 'm', '1']:
        inLst.extend([1, 0])  
    elif input.lower() in ['female', 'f', '0']:
        inLst.extend([0, 1])  
    else:
        print("Note: Input pattern not recognized; using default value") 
        inLst.extend([1, 0])  


# Function to process input data and make predictions using pre-trained models.
def models_demo(input_data):
    inputLst = []  # Initialize an empty list to store the processed input
    questions = {
        "age": Age_to_onehot,  # Map the age input to its processing function
        "gender": Gender_to_onehot,  # Map the gender input to its processing function
        "polyuria": Bool_to_onehot,  # Map Boolean inputs to their processing function
        "polydipsia": Bool_to_onehot,
        "sudden_weight_loss": Bool_to_onehot,
        "weakness": Bool_to_onehot,
        "polyphagia": Bool_to_onehot,
        "genital_thrush": Bool_to_onehot,
        "visual_blurring": Bool_to_onehot,
        "itchy_skin": Bool_to_onehot,
        "irritability": Bool_to_onehot,
        "delayed_healing": Bool_to_onehot,
        "partial_paresis": Bool_to_onehot,
        "muscle_stiffness": Bool_to_onehot,
        "alopecia": Bool_to_onehot,
        "obesity": Bool_to_onehot
    }


    for key, func in questions.items():
        answer = input_data[key]  # Gets the user input for each question.
        func(inputLst, answer)  # Processes the input and appends it to the list.

    inputLst = np.array(inputLst, dtype=float).reshape(1, -1)  # Converts list to NumPy array and reshape for model input.

    # Load pre-trained models from pickle files
    with open("model_lr.pkl", 'rb') as f:
        model_lr = pickle.load(f)

    with open("model_lin_svc.pkl", 'rb') as f:
        model_lin_svc = pickle.load(f)

    with open("model_polyn_svc.pkl", 'rb') as f:
        model_polyn_svc = pickle.load(f)


    models = {
        "Logistic Regression": model_lr, 
        "Linear SVC": model_lin_svc,
        "Polynomial SVC": model_polyn_svc
    }


    results = {}
    for name, model in models.items():
        prediction = model.predict(inputLst)  # Uses each model to make a prediction.
        results[name] = prediction  

    return results  
