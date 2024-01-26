#
# Multiple Response
#

from openai import OpenAI
import os

client = OpenAI( api_key=os.environ["OPEN_AI_API_KEY"] )

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are a cake baker"
    },
    {
      "role": "user",
      "content": "Get me 3 different recipe with different flavors to make a cake"
    }
  ],
  n=3,
  max_tokens=300
)

for choice in response.choices:
    print (choice.message.content)