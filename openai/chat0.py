#
# Single Response
#

from openai import OpenAI
import os

client = OpenAI( api_key=os.environ["OPEN_AI_API_KEY"] )

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are an expert rap song composer." 
    },
    {
      "role": "user",
      "content": "Write a rap song with a village background"
    }
  ],
  max_tokens=200
)
print(response.choices[0].message.content)