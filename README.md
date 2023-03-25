# Prototype

# Link to Live application

The chatbot is deployed on Streamlit and can be accessed using the following link: https://bigdataia-spring2023-team-04-prototype-prototype-2i2ebh.streamlit.app/

Codelabs Documentation of use cases and testing: https://codelabs-preview.appspot.com/?file_id=1BIJSANR2hE2q1OD_HA10DkJXvv5zMzkRXoOoVH6ZIQI#3
# Multi-Purpose Chatbot
The Multi-Purpose Chatbot is an application that allows you to perform different types of text analysis and generation tasks using the OpenAI API. You can use it to translate text, analyze sentiment, and generate new text based on a given prompt.

# Installation

To use this chatbot locally, follow these steps:

1. Clone this repository: git clone https://github.com/BigDataIA-Spring2023-Team-04/Prototype.git

2. Install the required packages: pip install -r requirements.txt

3. Set your OpenAI API key as an environment variable: export OPENAI_API_KEY=YOUR_API_KEY

4. Run the application: streamlit run prototype.py

# Usage
To use the Multi-Purpose Chatbot, simply run the prototype.py file. You will be prompted to enter a text message, and then you can choose what you want to do with that text. Here are the available options:

# Translate: 
Enter the target language you want to translate the text to.

# Analyze Sentiment: 
This will analyze the sentiment of the text and give you a score from -1 to 1.

# Generate Text: 
Enter a prompt for the model to generate text based on.

You can type exit at any time to quit the application.

# Example
Here's an example of how you can use the Multi-Purpose Chatbot:

```
Welcome to the Multi-Purpose Chatbot!
Enter your text message or type 'exit' to quit: Hello, how are you doing?

What do you want to do with your text?
1. Translate
2. Analyze Sentiment
3. Generate Text
4. Type a new text message
Enter your choice (1/2/3/4): 1
Enter target language: Spanish
Translated Text: Hola, ¿cómo estás?

What do you want to do with your text?
1. Translate
2. Analyze Sentiment
3. Generate Text
4. Type a new text message
Enter your choice (1/2/3/4): 2
Sentiment Analysis: Positive (score: 0.898)

What do you want to do with your text?
1. Translate
2. Analyze Sentiment
3. Generate Text
4. Type a new text message
Enter your choice (1/2/3/4): 3
Enter prompt: Once upon a time
Generated Text: in a land far, far away, there lived a princess who was cursed to sleep for a hundred years...

What do you want to do with your text?
1. Translate
2. Analyze Sentiment
3. Generate Text
4. Type a new text message
Enter your choice (1/2/3/4): exit
```

# Credits
The Multi-Purpose Chatbot was created by Sivaranjani, Rishab Singh, Karan Raman Agrawal, Lokeshwaran using the OpenAI API.


