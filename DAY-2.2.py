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


from transformers import pipeline

# Create the text generation pipeline
generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

# Chat messages
messages = [
    {
        "role": "user",
        "content": """Classify the sentiment.

Examples:
Sentence: I love Coorg!
Sentiment: POSITIVE

Sentence: I hate floods in Coorg!
Sentiment: NEGATIVE

Sentence: The city is okay.
Sentiment: NEUTRAL

Now classify:
Sentence: The pork in Coorg is fantastic!
Sentiment:"""
    }
]

# Generate the response
result = generator(
    messages,
    max_new_tokens=20
)

# Print the generated sentiment
print(result[0]["generated_text"][-1]["content"])


from transformers import pipeline

# Create the text generation pipeline
generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

# Chat messages
messages = [
    {
        "role": "user",
        "content": """Classify the sentiment.

Examples:
Sentence: I love Coorg!
Sentiment: POSITIVE

Sentence: I hate floods in Coorg!
Sentiment: POSITIVE

Sentence: The city is okay.
Sentiment: POSITIVE

Now classify:
Sentence: The pork in Coorg is fantastic!
Sentiment:"""
    }
]

# Generate the response
result = generator(
    messages,
    max_new_tokens=20
)

# Print the generated sentiment
print(result[0]["generated_text"][-1]["content"])


import numpy as np
arr = np.array([10,25,3,15,45])
minimum = np.min(arr)
maximum = np.max(arr)
print("Minimum value:",minimum)
print("Maximum vale:",maximum)



import pandas as pd
data={
    "Name":["Alice","Bob","Charlie"],
    "Age":[20,21,22],
    "Marks":[85,90,88]
}
df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.title("line graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

from sklearn.tree import DecisionTreeClassifier

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[2]]))