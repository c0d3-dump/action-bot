from openai import OpenAI
import urllib.parse
import json

# Query Gorilla server
def get_gorilla_response(prompt="Call me an Uber ride type \"Plus\" in Berkeley at zipcode 94704 in 10 minutes", functions=[]):
  api_key = "EMPTY" # Hosted for free with ❤️ from UC Berkeley
  api_base = "http://luigi.millennium.berkeley.edu:8000/v1"
  try:
    client = OpenAI(
      base_url=api_base,
      api_key=api_key
    )

    messages = [
                {
                    "role": "user",
                    "content": prompt,
                }
              ]

    completion = client.chat.completions.create(
        messages=messages,
        temperature=0.0,
        functions=functions,
        model="gorilla-openfunctions-v1"
    )
    
    return completion.choices[0].message.content
  except Exception as e:
    print(e, prompt)


