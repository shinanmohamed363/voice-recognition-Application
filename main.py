import speech_recognition as sr
import pyttsx3 
import logging
import os
import datetime

import webbrowser
#this is logger for the application
Log_DIR ="LOGS"
LOG_FILE_NAME="application.log"

os.makedirs(Log_DIR, exist_ok=True)
log_path=os.path.join(Log_DIR,LOG_FILE_NAME)


logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)


#Taking the male voice from my system
engine=pyttsx3. init('sapi5')
voices=engine.getProperty("voices")

engine.setProperty("voice",voices[1].id)

#engine.say(" hello boss how can i help you  ");
#engine.runAndWait();

def speak(text):
    """this function covert text to voice"""
    "args:"
    "returns:"
    engine.say(text)
    engine.runAndWait() 

#speak("hello boss wellcome to ai ")   

def takecommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
   
   try:
      print("recognizing...")
      query=r.recognize_google(audio,language="en-in")
      print(f"user said:{query}\n")
   
   except Exception as e:
      logging.info(e)

      print("say that again please")
      speak("say that again please")
      return "None"
   
   return query

  #wish you function
def wish_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning, boss!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon, boss!")
    else:
        speak("Good evening, boss!")
    
    # Speak the introduction after the greeting
    speak("I am Jarvis. Tell me, boss, how can I help you?")





while True:
# wish_me()

 query = takecommand().lower()
 print(query)

 if "time" in query:
  strTime = datetime.datetime.now().strftime("%H:%M")
  speak(f" boss time is {strTime}")
 elif " what is your name" in query:
    speak("my name is jarvious")

 elif "exit" in query:
    speak ("bye sir ")
    exit()
#text = takecommand()
#print(text)
#speak(text)

