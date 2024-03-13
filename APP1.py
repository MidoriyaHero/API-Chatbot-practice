import google.generativeai as genai
import streamlit as st


# App title
st.set_page_config(page_title="🤗💬 CHATBOT ÁcK QKỈ")

# Hugging Face Credentials
with st.sidebar:
    st.title('🤗💬 CHATBOT ÁcK QKỈ')
    reset_button_key = "reset_button"
    reset_button = st.button("Reset Chat",key=reset_button_key)
    if reset_button:
        st.session_state.messages = []
        
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input):
    # Hugging Face Login
    genai.configure(api_key='YOUR-API-KEY')
    model = genai.GenerativeModel('gemini-pro')
    # Create ChatBot                        
    chatbot = model.generate_content(prompt_input)
    return chatbot.text

# User-provided prompt
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)