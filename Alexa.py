from functions import *

def run_alexa():
    command = take_command()
    if command:
        for question, answer in qa_data.items():
            if question.lower() in command:
                talk(answer)
                return True
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'what is time right now' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            try:
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except wikipedia.exceptions.PageError:
                talk("Sorry, I couldn't find any information on " + person)
            except wikipedia.exceptions.DisambiguationError as e:
                talk("There are multiple results for " + person + ". Please be more specific.")
        elif 'kem chho' in command:
            talk('majama')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'open youtube website' in command:
            webbrowser.open("youtube.com")
        elif 'open google website'  in command:
            webbrowser.open("google.com")
        elif 'open stackoverflow website' in command:
            webbrowser.open("stackoverflow.com")
        elif 'open code' in command:
            talk('Opening Visual Studio Code')
            codePath = "Use Your App.exe Path"
            os.startfile(codePath)
        elif 'open chrome' in command:
            talk('Opening Chrome')
            codePath = "Use Your App.exe Path"
            os.startfile(codePath)
        elif 'email' in command:
            try:
                talk("What should I say?")
                content = take_command()
                to = "emailofuser@gmail.com"    
                sendEmail(to, content)
                talk("Email has been sent!")
            except Exception as e:
                print(e)
                talk("Sorry. I am not able to send this email")
        elif 'exit' in command or 'no' in command:
            talk('Goodbye! Have a nice day.')
            return False
        else:
            talk('Please say the command again.')
    return True

def main_loop():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")
    talk("Hello, I am Alexa, your personal assistant.")
    talk("How can I help you?")
    
    while True:
        if not run_alexa():
            break
        talk("How else can I help you?")


if __name__ == "__main__":
    main_loop()
