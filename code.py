import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from googlesearch import search

global command

listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
        engine.say(text)
        engine.runAndWait()
        

def take_command():
        try:
                with sr.Microphone() as source:
                        print("listening...")
                        voice = listener.listen(source)
                        command = listener.recognize_google(voice)
                        command=command.lower()
                        if 'alpha' in command:
                                command = command.replace('alpha','')
                                print(command)
                        
        except:
                pass
        return command


def run_alpha():
        command = take_command()
        file_out=open("flie_out.txt","w")
        file_in=open("data_input.txt","w")
        file_in.write(command+'\n')
        print(command)
        if 'play' in command:
                song =command.replace('play','')
                talk('playing'+ song)
                pywhatkit.playonyt(song)
        elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is '+ time)
        elif 'who the heck is' in command:
                person = command.replace('who the heck is','')
                info = wikipedia.summary(person,1)
                print(info)
                talk(info)
                file_out.write(info+'\n')
        elif 'date' in command:
                talk('sorry, I have a headache')

        elif 'are you single' in command:
                talk('I am in a relationship with wifi')
        elif 'joke' in command:
                talk(pyjokes.get_joke())
        elif 'exit'in command:
                engine.say("Thank you for using me, This is ALPHA signing off")
                print("Thank you for using me, This is ALPHA signing off......")
                file_out.write("exit\n")
        elif 'search'in command:
                serh = command.replace('search','')
                data= search(command)
                print(data)
                talk(data)
                file_out.write(data+'\n')
        else:
                talk('Please say the command again.')
        


while True:
        
        run_alpha()
        
