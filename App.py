import google.generativeai as genai
import streamlit as st

st.title("CHATBOT ÁcK QKỈ")
genai.configure(api_key='YOUR-API-KEY')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
with st.sidebar:

    reset_button_key = "reset_button"
    reset_button = st.button("Reset Chat",key=reset_button_key)
    if reset_button:
        st.session_state.messages = []
        temp = 1

if prompt := st.chat_input("What is up?"):
    if temp == 1:

        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response = chat.send_message(prompt)
            for chunk in response:
                full_response = ''
                full_response += (chunk.text)
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    else:
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response = chat.send_message(prompt, stream=True)
            for chunk in response:
                full_response = ''
                full_response += (chunk.text)
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})