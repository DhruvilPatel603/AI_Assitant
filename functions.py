import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import json
import time
import webbrowser
import smtplib
import os
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def load_qa(file_path):
    with open(file_path, 'r') as file:
        qa_data = json.load(file)
    return qa_data


qa_data = load_qa('QA.json')


def talk(text):
    engine.say(text)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pateldhruvil662@gmail.com', 'lbeo bpqm fzwh fodb')
    server.sendmail('pateldhruvil662@gmail.com', to, content)
    server.close()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Sleeping..')
            time.sleep(1)
            print('listening...')
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
                
             
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open('user_questions.txt', 'a') as log_file:
                    log_file.write(f"{timestamp}: {command}\n")
                
                return command
    except Exception as e:
        print(f"Error: {str(e)}")
        return ""
    return ""
