import requests
import io
import os
from PIL import Image
from config import key
import streamlit as st

st.title("Image generation")
prompt = st.text_input("Enter your prompt here")
if st.button("Generate Image"):
  with st.spinner("Processing"):
    r = requests.post('https://clipdrop-api.co/text-to-image/v1',
      files = {
          'prompt': (None, prompt, 'text/plain')
      },
      headers = { 'x-api-key': key }
    )

    if (r.ok):
        images = Image.open(io.BytesIO(r.content))
        st.image(image=images)
    else:
      r.raise_for_status()
