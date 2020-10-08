import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
volume=engine.getProperty("volume")
rate=engine.getProperty("rate")
engine.setProperty("voice",voices[1].id)
engine.setProperty("volume",volume-0.1)
engine.setProperty("rate",rate-20)
def wish():
    hour=int(datetime.datetime.now().hour)
    if (hour>0 and hour<12):
        speak("Good morning sir")
    elif (hour>12 and hour<18):
        speak("Good Afternoon sir")
    elif (hour>18):
        speak("Good evening sir")
    speak("I am phineix. please tell me how may i help you")

def  speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    '''This function use to listen
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
         print("Recognizing")
         query=r.recognize_google(audio,language="en-in")
         print(f"User said: {query}\n")
    except Exception as e:
        print("say that again please..")
        return "None"
    return speak(query)

if __name__ == "__main__":
    wish()
    while True:
        query=takeCommand().lower
        

