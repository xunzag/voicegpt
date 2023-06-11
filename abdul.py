import openai
import pyttsx3
import speech_recognition as sr
import time

openai.api_key = "Your Api Key goes here"

engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Abdul doesn't understand")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    trigger_word = "genius"
    while True:
        print("Say 'genius' to start recording your query..")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == trigger_word:
                    filename = "input.wav"
                    print("Speak, I am all ears..")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")

                        
                        response = generate_response(text)
                        print(f"Genius says: {response}")

                        speak_text(response)
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
