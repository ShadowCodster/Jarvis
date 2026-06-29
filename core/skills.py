import webbrowser
import datetime
import pyjokes
from core.audio import speak, listen

def execute_command(command):
    """Parses the command and executes the corresponding skill."""
    if not command:
        return True # Continue listening if nothing was heard

    if "your name" in command:
        speak("My name is Peter")
        return True

    elif "time now" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        return True

    elif 'youtube' in command:
        search_query = command.replace("youtube", "").strip()
        speak(f"Opening YouTube for {search_query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
        return True

    elif 'joke' in command:
        speak(pyjokes.get_joke())
        return True

    elif 'exit' in command or 'stop' in command:
        speak("Ok, Thank you. Have a nice day.")
        return False # This will break the main loop

    else:
        speak("I have very limited features, but I can tell you a joke. Would you like to hear one?")
        response = listen()
        if response and "yes" in response:
            speak(pyjokes.get_joke())
        else:
            speak("Ok, no problem.")
        return True