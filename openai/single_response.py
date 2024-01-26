from openai import OpenAI
import os

client = OpenAI( api_key=os.environ["OPEN_AI_API_KEY"] )

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are a Fitness Training Expert"
    },
    {
      "role": "user",
      "content": "How do I get fit"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)