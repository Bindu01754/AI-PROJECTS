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

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# Take input from user
sentence = input("The food was amazing and the service was excellent! I will definitely come back again. ")

prompt = f"""
Classify the sentiment of the following sentence as Positive, Neutral, or Negative.

Sentence: {sentence}
Sentiment:
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=5)

result = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("\nPredicted Sentiment:", result)