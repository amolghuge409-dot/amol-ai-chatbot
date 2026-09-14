import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("gemini_api_key")
client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="Amol's AI Chatbot",
    page_icon="🤖",
)

st.title("Amol's AI Chatbot")
st.caption("Powered by Amol ")

if"previous_interaction_id" not in st.session_state:
    st.session_state.previous_interaction_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask anything..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                if st.session_state.previous_interaction_id is None:

                    interaction = client.interactions.create(
                        model="gemini-3.6-flash",
                        input=prompt
                    )

                else:

                    interaction = client.interactions.create(
                        model="gemini-3.6-flash",
                        input=prompt,
                        previous_interaction_id=
                        st.session_state.previous_interaction_id
                    )

                answer = interaction.output_text

                st.session_state.previous_interaction_id = interaction.id

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })
        
            except Exception as e:
                st.error(f"Error: {e}")