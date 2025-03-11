import requests
import json

url = 'http://localhost:11434/api/generate'


data = {
    "model": "deepseek-r1:1.5b",
    "prompt": "Pull up a list of books that are similar to the new ultimate X men comics 6160 that was written in 2024. Give the recommendations along with the title, author, release date and publisher"
}

response = requests.post(url, json=data, stream=True)


#check response status
if response.status_code == 200:
    print("Generated Text:", end=" ", flush=True)
    #iterate over the streaming process 
    for line in response.iter_lines():
        if line:
            #decode the line and parse the JSON
            decoded_line = line.decode('utf-8')
            result = json.loads(decoded_line)
            #Get the text from the response
            generated_text = result.get("response", "")
            print(generated_text, end=" ", flush=True)
else:
    print("Error:", response.status_code, response.text)