import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wishing
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour == 0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good after noon sir")
    else:
        speak ("good evening sir ")
    speak("i Am jarvish Tell me how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... :")
        audio = r.listen(source)
        try:
            print("Reconizing........")
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said:\n Please say that again:")
        return text
    
if __name__ == "__main__":
    wishme()
    
    
    #logic to exicute task
    while True:
        a=takecommand()
        text=a.lower()
        try:
            if 'wikipedia' in text:
                speak('Searching wikipidea')
                text=text.replace("wikipedia","")
                result=wikipedia.summary(text,sentences=2)
                speak("According to wikipedia")
                speak(result)
            elif 'pratik' in text:
                speak("According to Our sources  Prateek is mahinee katuaa")
            elif 'awasthi' in text:
                speak("i never think that you will ask me about your bro, he is your bro you shoud know about him")
            elif 'open youtube' in text:
                webbrowser.open("youtube.com")
            elif 'open google' in text:
                webbrowser.open("google.com")
            elif 'open email' in text:
                webbrowser.open("gmail.com")
            elif 'zoom' in text:
                webbrowser.open("zoom.com")
            elif 'Moive' in text:
                webbrowser.open("zoom.com")
            elif 'the time' in text:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            elif text=='':
                speak("Speak again")

        except:
            speak("Say somthing Valid")
            text=takecommand().lower()

            