import streamlit as st
import openai

openai.api_key = st.secrets["Open_AI_key"]

def process_text(text, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        max_tokens=1024,
        n=1,
        stop=None
    )
    return response.choices[0].message['content'].strip()

st.title("Welcome to the Multi-Purpose Chatbot!")

text = st.text_input("Enter your text message (max 50 characters):", max_chars=50)

action = st.selectbox("What do you want to do with your text?", ("", "Translate", "Analyze Sentiment", "Generate Text"))

if action == "Translate":
    target_language = st.text_input("Enter target language:")
    if st.button("Translate Text"):
        translated_text = process_text(text, f"Translate this text into {target_language}:")
        st.write("Translated Text:", translated_text)

elif action == "Analyze Sentiment":
    if st.button("Analyze Sentiment"):
        sentiment = process_text(text, "Analyze the sentiment of this text:")
        st.write("Sentiment Analysis:", sentiment)

elif action == "Generate Text":
    prompt = st.text_input("Enter prompt (max 50 characters):", max_chars=50)
    if st.button("Generate Text"):
        generated_text = process_text(prompt, "")
        st.write("Generated Text:", generated_text)
