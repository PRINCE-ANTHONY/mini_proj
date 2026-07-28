import os
from io import BytesIO
from gtts import gTTS
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

st.set_page_config(
    page_title="AI voice assistant",
    page_icon="microphone",
    layout="centered"
)

load_dotenv()
fetch_api_key = os.getenv("groq_api_key")

if not fetch_api_key:
    st.error("Please set the GROQ_API_KEY environment variable.")
    st.stop()

client = Groq(api_key=fetch_api_key)

def generate_ai_response(question):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", 
            "content": (
            "You are a helpful assistant."
            "Answer the user's questions as best as you can.")
            },
            {"role": "user",
            "content": question
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=300
    )
    return chat_completion.choices[0].message.content

def convert_text_to_speech(text):
    audio_buffer = BytesIO()
    speech = gTTS(text=text, lang='en')
    speech.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer
    
    
st.title("🎙️LEMORA AI")

st.write(
    '''This is an AI voice assistant that can answer your questions.  
You can ask it anything you want and it will answer it.'''
)

audio_val = st.audio_input("Record your question:")

if audio_val is not None:
    st.audio(audio_val, format="audio/wav")

    with st.spinner("Converting speech to text..."):
        try:
            transcription = client.audio.transcriptions.create(
                file=("recording.wav", audio_val.getvalue()),
                model="whisper-large-v3-turbo",
                response_format="json",
                temperature=0.0
            )
            transcribed_text = transcription.text.strip()
        except Exception as e:
            st.error(f"Transcription failed: {e}")
            transcribed_text = ""

    st.subheader("You asked:")

    if transcribed_text:
        st.write(transcribed_text)
        with st.spinner("Generating AI response..."):
            ai_response = generate_ai_response(transcribed_text)

        st.subheader("AI ASSISTANT:")
        st.write(ai_response)
        with st.spinner("Converting text to speech..."):
            audio_response = convert_text_to_speech(
            ai_response   
            )                                    
            st.audio(audio_response, format="audio/mp3")
            
    else:
        st.warning("No speech detected. Please try again.")