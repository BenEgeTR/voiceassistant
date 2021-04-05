import subprocess
import datetime
import pyttsx3
import speech_recognition as sr
import os
import pywhatkit
import webbrowser
import pyjokes
import wikipedia

youtube = "https://www.youtube.com"
reddit = "https://www.reddit.com"
chillmusic = "https://www.youtube.com/watch?v=RLWcYADoV84"
google = "https://www.google.com"
whatsapp = "https://web.whatsapp.com"
mathurl = "https://zoom.us/j/8336213784?pwd=VFVGbXZaekhMTEp6Z3dnZHo5RXhyUT09"
scienceurl = "https://us02web.zoom.us/j/5434954272?pwd=ZFZZUTRicDQ2TW1uYVB0SWN4ZlROdz09"
turkishurl = "https://us02web.zoom.us/j/8998357323?pwd=ZFVqeGpxR2hOdkJ4SjA1K1Q1RU5Cdz09"
englishurl = "https://us02web.zoom.us/j/4820057951?pwd=bXZOMUhoOTNjN1V3MXVTMnJzRU4wQT09"
vsurl = "https://us02web.zoom.us/j/5461783245?pwd=azl6c0pWUnk1Vjl2WDhmbWZaVFlpQT09"
codeurl = "https://us02web.zoom.us/j/5135085726?pwd=RllaMUFzYUVDVEs5NStUblROcDlxdz09"
germanurl = "https://zoom.us/j/3171772449?pwd=VEMzSk9EZUZFcXdiRlhnV2NTWExhUT09"
guideurl = "https://zoom.us/j/3257859687?pwd=YkRFZm9XNy9jcXpJVThMZ1RvdzBNQT09"
religionurl = "https://zoom.us/j/3287418527?pwd=UGhlZWxOMk51"
lunarpath = "C:\\Users\\Egehan\\AppData\\Local\\Programs\\lunarclient\\Lunar Client.exe"
cmdpath = "C:\\WINDOWS\\system32\\cmd.exe"
codepath = "C:\\Users\\Egehan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-tr')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("I couldnt understand you")
        return "None"
    return query
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    vscode = "C:\\Users\\Egehan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    subprocess.Popen([vscode, file_name])
if __name__ == "__main__":
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello. Please tell me how may I help you")   
    while True:
        query = takeCommand().lower()

        if 'wikipedia search' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif "write this down" in query:
            speak("What would you like me to write down?")
            note_text = takeCommand()
            note(note_text)
            speak("I've made a note of that")

        elif "go to sleep" in query:
            speak("OK")
            exit()

        elif "alexa" in query:
            speak("I,  hate, alexa, and, fuck, you")
 
        elif 'play' in query:
            song = query.replace('could you play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the time is {strTime}")

        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
        
        elif "what is " in query:
            wolf_res = query.replace("what is ", "")
            wolf_res = wolf_res.replace(" ","")
            wolf_res = wolf_res.replace("+", "%2B")
            webbrowser.open("https://www.wolframalpha.com/input/?i=" + wolf_res)
        
        elif "who is" in query:
            wolf_res = query.replace("search", "")
            wolf_res = query.replace(" ", "+")
            webbrowser.open("https://www.wolframalpha.com/input/?i=" + wolf_res)

        elif 'could you hear me' in query:
            speak("Yes sir")

        elif "stop" in query:
            speak("ok")
            exit()

        elif "i guess its time" in query: # Math
            webbrowser.open(mathurl)
        
        elif "science" in query: # Fen
            webbrowser.open(scienceurl)

        elif "Turkish" in query: # Türkçe
            webbrowser.open(turkishurl)

        elif "English" in query: # İngilizce
            webbrowser.open(englishurl)

        elif "Visual arts" in query: # Görsel Sanatlar
            webbrowser.open(vsurl)

        elif "coding" in query: # Bilişim
            webbrowser.open(codeurl)

        elif "german" in query: # Almanca
            webbrowser.open(germanurl)
        
        elif "guide" in query: # Rehberlik
            webbrowser.open(guideurl)
        
        elif "religion" in query: # Din
            webbrowser.open(religionurl)

        elif 'thanks' in query:
            speak("no problem sir")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        #Open Stuff
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open(youtube)

        elif "play chill music" in query:
            webbrowser.open(chillmusic)

        elif 'open reddit' in query:
            webbrowser.open(reddit)

        elif 'open google' in query:
            webbrowser.open(google)
            
        elif 'open whatsapp' in query:
            webbrowser.open(whatsapp)

        elif "stack overflow" in query:
            question = query.replace("stack overflow", "")
            webbrowser.open("https://stackoverflow.com/search?q=" + (question))

        elif 'open code' in query:
            os.startfile(codepath)
        
        elif 'open minecraft' in query:
            speak('opening minecraft')
            os.startfile(lunarpath)

        elif 'open command prompt' in query:
            speak("opening command prompt")
            os.startfile(cmdpath)