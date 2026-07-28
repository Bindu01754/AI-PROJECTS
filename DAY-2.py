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