# Cardiovascular Disease & Diabetes Risk Assessment Tool

## Introduction

This project is a comprehensive Risk Assessment tool for Cardiovascular Disease (CVD) and Diabetes. It leverages Large Language Model (LLM) capabilities to provide personalized mitigation measures. The tool predicts an individual's susceptibility to CVD over the next decade and generates tailored mitigation measures based on user-provided attributes and calculated risk scores.

## Features

- Diabetes prediction using trained classifier models (Logistic Regression and Support Vector Machines)
- CVD risk assessment using an adapted risk model for the Indian population (Cox proportional hazard modeling)
- BMI calculator
- Personalized mitigation measure generation using LLAMA2 LLM via OLLAMA

## Technology Stack

- Frontend: Streamlit
- Backend: Python
- Machine Learning: Scikit-learn
- Large Language Model: LLAMA2 (via OLLAMA)

## System Requirements

Minimum System Requirements:
- Processor: Quad-core Intel/AMD processor or higher (i5 equivalent)
- RAM: 8 GB
- Storage: At least 10 GB of free space
- Python Version: 3.8 or later

Recommended System Requirements:
- Processor: 6-Core Intel/AMD processor (i7 equivalent or higher)
- RAM: 16 GB or more
- Storage: 20 GB or more of free space for models and dependencies
- Python Version: 3.10 or later

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nihalanas/risk_assessment.git
   cd risk_assessment
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and install OLLAMA from [here](https://ollama.com/download). Select the model that you want to run in the background. (By default, it is set to `llama2`)

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the provided local URL in your web browser.

3. Use the application in the following order:
   - Complete the diabetes prediction section
   - Use the BMI calculator
   - Fill out the CVD risk assessment form
   - Generate personalized mitigation measures

## Customization

To use different LLM models, select them from the OLLAMA application and update the 'model' field in the [llama2.py](https://github.com/nihalanas/risk_assessment/blob/main/llama2.py) file.

## Note

Running an LLM in the background using OLLAMA is a resource-intensive computation. Ensure you have a system with at least 8GB RAM (16GB recommended). Depending on system capabilities, measure generation might take a few minutes. You can confirm it's working by checking the 'Running' action bar in the top right of the Streamlit application.

## License

Project is under MIT License.
