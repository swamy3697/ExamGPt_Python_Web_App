import streamlit as st
import openai

def get_openai_response(prompt,api_key):
    try:
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
       
        st.error(f"An error occurred: {e}")
        return "API key is not working."


 

def handle_submit():
    st.session_state.submit = True

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'submit' not in st.session_state:
    st.session_state['submit'] = False

st.title("ExamGPT")

api_key = "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"


user_input = st.text_input("Your message:", key="user_input", on_change=handle_submit)

if st.session_state.submit and user_input and api_key:
  bot_response = get_openai_response(user_input, api_key)
  st.session_state.messages.append((user_input, bot_response))
  st.session_state['submit'] = False
  st.experimental_rerun()


st.write("---")
for user_msg, bot_msg in reversed(st.session_state.messages): 
    st.write(f"**You:** {user_msg}")
    st.write(f"**ExamGPT:** {bot_msg}")
    st.write("---")
