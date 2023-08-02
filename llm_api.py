import requests
import json

import logging 


logging.basicConfig(filename='logs.log',
                    level=logging.INFO,
					format='%(levelname)s:%(asctime)s:%(message)s',
					datefmt="%Y-%m-%d %H:%M:%S")


# Add a StreamHandler to print logs to the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) 
console_formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s', datefmt="%d/%m/%Y- %H:%M:%S")
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

def get_apiKey():
    try:
        with open('config.json') as f:  # Try to open the file
            config = json.load(f)
        api_key = config['API_KEY']
        logging.info("Loading Api key.")
        return api_key
    except FileNotFoundError as e:
        logging.error("Error: 'config.json' file not found.")
        raise e
        

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
        try:
            response = requests.post(self.URL, json=payload, headers=self.headers)
            text = response.json()
            return text["LLAMA"]
        except Exception as e :
            logging.error("Error with status code" + str(response.status_code))
            raise e
        
        
if __name__ == "__main__":
    with open('config.json') as f:
        config = json.load(f)

    api_key = config['API_KEY']
    
    chatLLAMA = LLM(api_key)
    print(chatLLAMA.get_reply("can you integrate mod x from -1 to 1 with respect to x?"))
