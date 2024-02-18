# Voice-Controlled Desktop Assistant with AI Chat Integration

This Python script creates a voice-controlled desktop assistant with additional features for interacting with OpenAI's GPT-3.5 model for AI-driven chat conversations. The assistant utilizes various libraries and modules for speech recognition, text-to-speech conversion, web browsing, application launching, and interaction with external APIs.

## Features

- Voice recognition and speech synthesis for user interaction.
- Opening websites (e.g., YouTube, Google) based on user commands.
- Displaying the current time upon request.
- Launching applications (e.g., Chrome, VS Code, Word) based on user commands.
- Integration with OpenAI's GPT-3.5 model for AI-driven chat conversations.
- Seamless switching between desktop assistant mode and AI chat mode.

## Requirements

- Python 3.x
- Libraries: `speech_recognition`, `win32com`, `webbrowser`, `datetime`, `subprocess`, `os`, `openai`

## Usage

1. Clone the repository or download the Python script.
2. Install the required libraries using pip: `pip install -r requirements.txt`.
3. Obtain OpenAI API key and replace the placeholder in the script with your actual key.
4. Run the Python script: `python desktop_assistant.py`.
5. Follow the voice prompts and give commands to interact with the assistant or engage in AI chat conversations.

## Configuration

- Replace the placeholder OpenAI API key with your actual key.
- Customize the list of supported websites and applications according to your preferences.
- Adjust voice recognition parameters or error handling mechanisms as needed.

## Contributing

Contributions to enhance the functionality, improve code quality, or fix bugs are welcome. Please fork the repository, make your changes, and submit a pull request.

## Disclaimer

This script is provided for educational and demonstration purposes only. Use it responsibly and be mindful of privacy and security considerations while interacting with external services and APIs.
