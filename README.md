# Genius Voice Assistant

The Genius Voice Assistant is a Python application that uses the OpenAI GPT-3 model to provide voice-based interactions. It listens for a trigger word, "genius," and starts recording the user's query. The recorded audio is then transcribed to text and sent to the GPT-3 model for generating a response. The response is then spoken back to the user.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- OpenAI Python library
- pyttsx3 library
- speech_recognition library

You will also need an API key from OpenAI to use their GPT-3 model. Place the API key in the `openai.api_key` variable in the code.

## Installation

1. Clone this repository to your local machine or download the code files.
2. Install the required dependencies.

## Usage

1. Run the `main.py` file: `python main.py`.
2. Once the application is running, say "genius" to trigger the assistant.
3. Speak your query or question after the assistant starts listening.
4. The assistant will generate a response using the GPT-3 model and speak it back to you.
