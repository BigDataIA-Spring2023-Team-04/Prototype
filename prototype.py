import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key =  st.secrets["Open_AI_key"]

def translate_text(text, target_language):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate this text into {target_language}: {text}",
        temperature=0.5,
        max_tokens=1024,
        n = 1,
        stop=None
    )
    return response.choices[0].text.strip()

def analyze_sentiment(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Analyze the sentiment of this text: {text}",
        temperature=0.5,
        max_tokens=1024,
        n = 1,
        stop=None
    )
    return response.choices[0].text.strip()

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n = 1,
        stop=None
    )
    return response.choices[0].text.strip()

st.title("Welcome to the Multi-Purpose Chatbot!")

text = st.text_input("Enter your text message:")

action = st.selectbox("What do you want to do with your text?", ("", "Translate", "Analyze Sentiment", "Generate Text"))

if action == "Translate":
    target_language = st.text_input("Enter target language:")
    if st.button("Translate Text"):
        translated_text = translate_text(text, target_language)
        st.write("Translated Text:", translated_text)

elif action == "Analyze Sentiment":
    if st.button("Analyze Sentiment"):
        sentiment = analyze_sentiment(text)
        st.write("Sentiment Analysis:", sentiment)

elif action == "Generate Text":
    prompt = st.text_input("Enter prompt:")
    if st.button("Generate Text"):
        generated_text = generate_text(prompt)
        st.write("Generated Text:", generated_text)
