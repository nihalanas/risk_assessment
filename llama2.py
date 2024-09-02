import ollama

def gen_response(message1):
    stream = ollama.chat(
        model='llama2',    # Specify the model from Ollama here.
        messages=[{'role': 'user', 'content': message1}],   # Sends the user's message to the model.     
        stream=True,
    )
    response= ""     # This empty string accumulates response.
    for chunk in stream:
        response += chunk['message']['content']    # Appends each chunk to response string.
    print("this is the output from llama2 file", response)
    return response