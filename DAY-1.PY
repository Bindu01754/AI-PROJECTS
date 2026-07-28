# user={
#     "name": "Ravi",
#     "city":"coorg",
#     "order":"Pork"
# }

# print(f"Hello {user['name']}!")
# print(f"Delivering {user['order']} to {user['city']}")


# user1={
#     "name": "Anu",
#     "followers": 1000,
#     "likes": 500
# }

# print(f"Hello {user1['name']}!")
# print(f"You have {user1['followers']} followers and {user1['likes']} likes!") 

# sentiment Analysis
# from transformers import pipeline
# classifier = pipeline("sentiment-analysis")
# result = classifier("I love eating idly in coorg")
# print(result)

# from transformers import pipeline
# classifier = pipeline("sentiment-analysis")
# result = classifier("I hate eating idly in coorg")
# print(result)

# from transformers import pipeline
# classifier = pipeline("sentiment-analysis")
# result = classifier("I eat idly in coorg")
# print(result)

# from transformers import pipeline
# generator = pipeline("text-generation", model="gpt2")
# output = generator("Artificial Intelligence will",max_length=40)
# print(output[0]['generated_text'])


# from transformers import pipeline
# generator = pipeline("text-generation", model="gpt2")
# output = generator("Once upon a time there was a girl in coorg",max_length=40)
# print(output[0]['generated_text'])

# from transformers import pipeline
# generator = pipeline("text-generation", model="gpt2")
# output = generator("Once upon a time in coorg",max_length=40)
# print(output[0]['generated_text'])

# from transformers import pipeline
# generator = pipeline("text-generation", model="gpt2")
# output = generator("give me a joke",max_length=40)
# print(output[0]['generated_text']) 

import requests
import os 
API_KEY = os.getenv("HF_API_KEY")
response = requests.post("https://api-inference.huggingface.co/models/gpt2", headers={"Authorization": f"Bearer {API_KEY}"}, json={"inputs": "python is great because"})
print(response.json())