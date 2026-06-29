from core.audio import listen, speak
from core.skills import execute_command

def main():
    print("System starting...")
    speak("System starting. Waiting for wake word.")
    
    # Master switch for the entire program
    system_running = True 
    
    while system_running:
        wake_word_check = listen()
        
        if wake_word_check and "hey jarvis" in wake_word_check:
            speak("How can I help you?")
            
            # Active command loop
            while True:
                command = listen()
                
                # execute_command returns False when 'exit' or 'stop' is said
                keep_going = execute_command(command) 
                
                if not keep_going:
                    # Shut down the master switch and break the inner loop
                    system_running = False 
                    break
                    
        # Optional: A direct way to kill it without saying the wake word first
        elif wake_word_check and 'exit system' in wake_word_check:
            speak("Shutting down the system.")
            system_running = False

if __name__ == '__main__':
    main()