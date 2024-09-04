<!-- <img align="center" alt="Coding" width="100%" height='300px' src=""> -->

___
## Introduction

A Risk Assessment tool for Cardiovascular Disease (CVD) and Diabetes, which leverages LLM capabilities and provides personalized mitigation measures. 

The tool predicts an individual's susceptibility to CVD over the next decade and generates tailored mitigation measures based on user-provided attributes and the risk scores generated. 

Utilizing Streamlit for the user interface. Has trained classifiers models including Logistic Regression and Support Vector Machines for diabetes prediction, and adapted an existing risk model for the Indian population using Cox proportional hazard modeling. Leverages LLAMA2 LLM capabilitees using OLLAMA functionality for personalized mitigation generation, considering individual risk scores. 

___

> [!NOTE]  
> You must have Ollama downloaded if you want the model to be run using Ollama.
> If you don't already have it installed, you can get it downloaded from [here](https://ollama.com/download)

___

## Installation

1. Download the ZIP file, unzip it, and open the resulting folder in your preferred IDE, such as Visual Studio Code or you can also clone the repository by copying the web url and pasting it in your directory's
git bash terminal using the command:-
   ```bash
   git clone https://github.com/nihalanas/cvd_last.git
   ```

2. Install the libraries mentioned in [requirements.txt](https://github.com/nihalanas/cvd_last/blob/main/requirements.txt)

   In VS Code Terminal run the following command:
   
   ```python
   pip install -r requirements.txt
   ```
___

<!-- [!IMPORTANT] -->

___

3. Download the Ollama application so that the LLM can be run. By default the model will run the Llama2 7B parameters model. Others models can also be run, the available models can be selected from the Ollama application and the name can be updated in the 'model' field in this [file](https://github.com/nihalanas/cvd_last/blob/main/llama2.py)
 
4. Run the [app.py](https://github.com/nihalanas/cvd_last/blob/main/app.py) python file.

   ```python
   Streamlit run app.py
   ```
____
