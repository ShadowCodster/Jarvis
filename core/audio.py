import pyttsx3
import speech_recognition as sr

def listen():
    """Listens to the microphone and returns recognized text."""
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Recognizing...")
                data = recognizer.recognize_google(audio)
                print(f"You said: {data}")
                return data.lower()
            except sr.UnknownValueError:
                print("Not Understanding")
                return ""
            except sr.RequestError:
                print("API unavailable")
                return ""

def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # 1 for female, 0 for male
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()