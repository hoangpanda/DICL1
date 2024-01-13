from openai import OpenAI
# import backoff
import openai 
import requests
import json

print('import ok')

class OpenAI_cl:
    def __init__(self, model, api_key, temperature=0):
        pass
        # openai.api_key = api_key
        # self.model = model
        # self.temperature = temperature

    # @backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.APIError, openai.error.APIConnectionError, openai.error.Timeout), max_tries=5, factor=2, max_time=60)
    def create_chat_completion(self, messages):
        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key="sk-jaMNL109Qb9M6AIQGGwxWJ8ayIhQVx2NWY2poW0kPS1ltd8w",
            base_url="https://api.chatanywhere.tech/v1"
        )
        completion = client.chat.completions.create(
            # model=self.model,
            model = "gpt-3.5-turbo",
            messages=messages,
            # temperature=self.temperature,
            # stream=True
        )
        # print(completion)
        # print(completion.choices[0].message.content)
        return completion.choices[0].message.content
        # return completion.choices[0].message.content
  
# chat_bot = OpenAI_cl()
# messages = [{'role': 'user','content': 'hôm nay là ngày bao nhiêu'},]
# chat_bot.create_chat_completion(messages=messages)

# class Claude:
#     def __init__(self, model, api_key, temperature=0):

#         self.Claude_url = "https://api.anthropic.com/v1"
#         self.Claude_api_key = api_key
#         self.model = model
#         self.temperature = temperature

#     @backoff.on_exception(backoff.expo, (requests.exceptions.Timeout,requests.exceptions.ConnectionError,requests.exceptions.RequestException), max_tries=5, factor=2, max_time=60)
#     def create_chat_completion(self, messages):
#         # convert messages to string
#         formatted_string = "\n\n{}: {}\n\nAssistant: ".format("Human" if messages[0]["role"] == "user" else "Assistant", messages[0]["content"])
#         url = f"{self.Claude_url}/complete"
#         headers = {
#             "accept": "application/json",
#             "anthropic-version": "2023-06-01",
#             "x-api-key": self.Claude_api_key,
#             "Content-Type": "application/json"
#         }
#         data = {
#             "model": self.model,
#             "prompt": formatted_string,
#             "max_tokens_to_sample": 256,
#             "temperature": self.temperature
#         }
        
#         response = requests.post(url, headers=headers, data=json.dumps(data), timeout=30)
#         response_json = response.json()

#         return response_json['completion'].strip()