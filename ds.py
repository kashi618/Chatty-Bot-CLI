from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.environ['DEEPSEEK_API_KEY'], base_url="https://api.deepseek.com")

# Gather user prompt
userInput = input("Enter prompt: ")

# Define Deepseek behaviour
systemInput = "You are an expert AI assistant designed to provide accurate, detailed, and well-structured responses."

# Create Deepseek chat completion request
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": systemInput},
        {"role": "user", "content": userInput},
    ],
    stream=False
)

# Return results
print(response.choices[0].message.content)
