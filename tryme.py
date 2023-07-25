import os
import openai
from config import key

openai.api_key = key

response = openai.Image.create(
  prompt = "white cat",
  n = 1,
  size = "256x256"
)
image_url = response['data'][0]['url']
print("tryme")
