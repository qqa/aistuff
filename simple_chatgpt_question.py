import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def ask_chatgpt(question):
  """
  Sends a question to ChatGPT and returns the response.
  """
  response = OpenAI(api_key=client.api_key).chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": question,
          }
      ],
      model="gpt-3.5-turbo",
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
  )
  return response.choices[0].message.content.strip()

# Get user input
question = input("Ask ChatGPT a question: ")

# Call the function and print the response
answer = ask_chatgpt(question)
print(f"ChatGPT:\n {answer}")
