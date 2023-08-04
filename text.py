import streamlit as st
import requests
from config import key
from PIL import Image
import io

prompt = st.chat_input("Enter your prompt here")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message["content"])

if prompt:
    with st.spinner("Processing"):
        #st.write("The input is:" , prompt)
        st.chat_message("user").markdown(prompt)
        r = requests.post('https://clipdrop-api.co/text-to-image/v1',
            files = {
          'prompt': (None, prompt, 'text/plain')
        },
            headers = { 'x-api-key': key }
        )

        if (r.ok):
            images = Image.open(io.BytesIO(r.content))
            st.image(image=images)
            st.session_state.messages.append({"role" : "user", "content" : prompt})
            #with st.chat_message("assistant"):
                #st.markdown(images)
                #st.session_state.messages.append({"role" : "user", "content" : prompt})
        else:
            r.raise_for_status()
    
