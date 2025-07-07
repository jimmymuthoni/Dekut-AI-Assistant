import streamlit as st
import requests

BACKEND_URL =  "http://127.0.0.1:8000"


st.title("🎓 DeKUT Smart FAQ Assistant")
st.write("Ask your questions about DeKUT and the School of Computer Science & IT.")

option = st.radio("Select input method:", ["Text", "Voice"])

# For text input
if option == "Text":
    query = st.text_input("Enter your question:")
    if st.button("Ask"):
        if query:
            with st.spinner("Fetching answer..."):
                response = requests.post(f"{BACKEND_URL}/text_query", params={"q": query})
                if response.status_code == 200:
                    st.success("Answer:")
                    st.write(response.json().get("answer"))
                else:
                    st.error("Something went wrong. Please try again.")

elif option == "Voice":
    audio_file = st.file_uploader("Upload your voice query (WAV format)", type=['wav'])
    if st.button("Ask via Voice"):
        if audio_file:
            with st.spinner("Processing voice input..."):
                files = {"audio_bytes": audio_file.getvalue()}
                response = requests.post(f"{BACKEND_URL}/voice_query", files=files)
                if response.status_code == 200:
                    result = response.json()
                    st.success("Answer:")
                    st.write(result.get("answer"))
                else:
                    st.error("Something went wrong. Please try again.")
