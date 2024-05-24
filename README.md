# Alexa Personal Assistant

Alexa Personal Assistant is a Python-based virtual assistant that can perform various tasks such as answering questions, playing music, providing information from Wikipedia, telling jokes, opening websites, sending emails, and more.

## Features

- **Voice Recognition**: Utilizes the SpeechRecognition library to recognize voice commands.
- **Text-to-Speech**: Employs the pyttsx3 library to convert text responses into audible speech.
- **QA System**: Answers questions based on predefined Q&A pairs stored in a JSON file.
- **Task Execution**: Executes various tasks based on user commands, including playing music on YouTube, fetching information from Wikipedia, telling jokes, and more.
- **Web Interaction**: Can open specific websites such as YouTube, Google, and Stack Overflow using the webbrowser module.
- **Email Sending**: Allows sending emails through a configured SMTP server.
- **Time Reporting**: Reports the current time when asked.
- **Personalized Greetings**: Greets the user based on the time of day.

## Getting Started

To get started with Alexa Personal Assistant, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/DhruvilPatel603/Alexa_Assistant.git
    ```

2. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

4. Create a JSON file named `QA.json` in the project directory. This file should contain custom Q&A pairs in the following format:

    ```json
    {
        "What is the capital of France?": "The capital of France is Paris.",
        "Who is the president of the United States?": "The president of the United States is Joe Biden."
        // Add more Q&A pairs as needed
    }
    ```

5. Run the `Alexa.py` script:

    ```bash
    python Alexa.py
    ```

6. Start giving voice commands to Alexa and enjoy its functionalities!

## Usage

- Upon running the `Alexa.py` script, Alexa will greet you and await your voice commands.
- Simply say "Alexa" followed by your command or question.
- Alexa will respond accordingly, performing tasks or providing information as requested.

**Note**: Alexa will only respond if you precede your command with the word "Alexa".
