#
# Classification Response
# Categorize the following companies:
#

from openai import OpenAI
import os

client = OpenAI( api_key=os.environ["OPEN_AI_API_KEY"] )

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Categorize the following companies:" 
      "Microsoft Corporation, Roche Holding AG, Apple Inc, Amazon.com, Inc,Pfizer Inc, "
      "JPMorgan Chase & Co.,Johnson & Johnson, Bank of America Corporation, "
      "Industrial and Commercial Bank of China ."
    }
  ],
  max_tokens=200
)
print(response.choices[0].message.content)