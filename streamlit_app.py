pip install google-generativeai
import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="Droid")
st.title("Hi, Droid here :robot_face:")

google_api_key = st.sidebar.text_input('Google API Key', type='password')

os.environ['GOOGLE_API_KEY'] = google_api_key
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')


def run():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if mssg := st.chat_input("Say something..."):
            chat = model.start_chat(history=[])
            st.chat_message("user").markdown(mssg)
            st.session_state.messages.append({"role": "user", "content": mssg})
            response = chat.send_message(mssg)
            res = response.text
            with st.chat_message("Assistant"):
                st.markdown(res)
            st.session_state.messages.append({"role": "Assistant", "content": res})

if __name__ == "__main__":
    try:
        run()
    except:
        st.error("Please provide Google API Key")
