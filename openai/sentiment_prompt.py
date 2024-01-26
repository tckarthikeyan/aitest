#
# Sentiment Response
#

from openai import OpenAI
import os

client = OpenAI( api_key=os.environ["OPEN_AI_API_KEY"] )

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Classify the sentiment in the two statements:" 
      "Good, I like the way the course designed. It is a quick recap of all the java concepts.thanks"
      "The quizzes can be better"
    }
  ],
  max_tokens=200
)
print(response.choices[0].message.content)