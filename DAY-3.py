while True:
    user = input("You: ")
    if user.lower() == "bye":
       print("Bot: Goodbye! Have a nice day")
       break
    print("Bot: You said:",user)

response = {
    "hello":"Hi! how can I help you?",
    "good morning":"Good morning ! how are you today!",
    "hi":"Hello!",
    "how are you":"I'm doing great!",
    "what id ai":"AI stands for artificial intelligence",
    "python":"python is one of the most popular programming languages",
    "bye": "Goodbye!"
}
while True:
    user = input ("You: ").lower()
    if user == "bye":
        print("Bot:",response["bye"])
        break
    print("Bot:",response.get(user,"sorry,I don't understand that."))


import google.generativeai as genai
genai.configure()
model = genai.GenerativeModel("gemini-flash-latest")
print("AI  chatbot")
print("Type 'exit' to quit.\n")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = model.generate_content(user)
    print("Bot:",response.text)

import google.generativeai as genai
genai.configure()
model = genai.GenerativeModel("gemini-flash-latest")
chat = model.start_chat(history=[])
print("AI  chatbot")
print("Type 'exit' to quit.\n")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = chat.send_message(user)
    print("Bot:",response.text)

import requests
response = requests.get()
print(response.json())

import requests
response = requests.get()
print(response.json())

import requests
username = input("enter your github username: ")
response = requests.get()
print(response.json())

import json

student = {
    "name":"John Doe ",
    "age":20,
    "major":"Computer Science ",
    "courses":["Data Structure","Algorithms","Databases"]
}
print(json.dumps(student,indent=4))

import json
text = '{"name": "John", "age": 30, "city": "New York"}'
obj=json.loads(text)
print(obj["name"])
print(obj["age"])
print(obj["city"])

import requests
response = requests.get()
print(response.json())
print("Name:", response.json()["name"])
print("predicted Age:", response.json()["age"])

import requests
data = {
    "title":"Learning AI",
    "body":"Today I learned about AI and its application :",
    "userId":1
}
response = requests.post(json=data)
print(response.status_code)
print(response.json())

import requests
data = {
    "college":"cit",
    "student":"bindu :",
    "userId":14
}
response = requests.post(json=data)
print(response.status_code)
print(response.json())