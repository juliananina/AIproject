# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:40:10 2024

@author: Harjot
"""

import requests

for number in range(1, 71):
    
    file_path = 'outputfiles/'+str(number)+'.txt'  # Replace with your file's path
    
    # Open the file, read its content, and store it in a string
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Your OpenAI API key
    api_key = "I REMOVED THIS KEY TO PROTECT MY CHAT GPT ACCESS"
    
    # Define the endpoint and the API key
    url = "https://api.openai.com/v1/chat/completions"
    
    # Define the headers, including your API key for authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Define the data payload (message history in this case)
    data = {
        "model": "gpt-3.5-turbo",  # You can change to "gpt-4" or other models available
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "analyse the case study and answer the discusion questions" + content}
        ]
    }
    
    # Make the POST request to the OpenAI API
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        output_file_path = "outputfilesResponses/response"+str(number)+".txt"
        with open(output_file_path, 'w',encoding='utf-8') as file:
            response_data = response.json()
            chat_reply = response_data['choices'][0]['message']['content']
            print(f"ChatGPT: {chat_reply}")
            file.write(chat_reply)
    else:
        print(f"Error: {response.status_code}, {response.text}")
