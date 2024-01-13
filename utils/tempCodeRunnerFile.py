chat_bot = OpenAI_cl()
messages = [{'role': 'user','content': 'hôm nay là ngày bao nhiêu'},]
chat_bot.create_chat_completion(messages=messages)