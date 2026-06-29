# Jarvis Personal Assistant

A modular, Python-based voice assistant designed to automate daily tasks and respond to voice commands.

## Features
* **Wake Word Detection:** Continuously listens in the background for the wake word ("Hey Jarvis").
* **Modular Architecture:** Audio handling and skill executions are decoupled, making it easy to build out new script automation and capabilities.
* **Current Skills:**
  * Ask for the time ("time now")
  * Search YouTube ("youtube [search query]")
  * Tell jokes ("joke")
* **Clean Shutdown:** Say "exit" or "exit system" to safely shut down the assistant loop.

## Project Structure
```text
jarvis_project/
├── .venv/                  # Python virtual environment (ignored by Git)
├── .gitignore              # Files and folders to be ignored by Git
├── requirements.txt        # Project dependencies
├── main.py                 # The entry point of the application
└── core/                   # Directory for functional modules
    ├── __init__.py         # Makes 'core' a Python package
    ├── audio.py            # Speech recognition and TTS logic
    └── skills.py           # Command parsing and execution