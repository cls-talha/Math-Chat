import requests
import json



class LLM:
    def __init__(self, api_key : str) -> None:
        
        self.api_key = api_key #rapid api key can be found here -> https://rapidapi.com/rphrp1985/api/open-ai21
        self.URL = "https://open-ai21.p.rapidapi.com/conversationllama"
        
        self.headers =  {
                "content-type": "application/json",
                "X-RapidAPI-Key": self.api_key,
                "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
            }
    
    def get_reply(self, question : str) -> str:
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "web_access": False
        }
        
        response = requests.post(self.URL, json=payload, headers=self.headers)
        text = response.json()
        return text["LLAMA"]
    
    
if __name__ == "__main__":
    with open('config.json') as f:
        config = json.load(f)

    api_key = config['API_KEY']
    
    chatLLAMA = LLM(api_key)
    print(chatLLAMA.get_reply("can you integrate mod x from -1 to 1 with respect to x?"))
