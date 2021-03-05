import subprocess
import datetime
import pyttsx3
import speech_recognition as sr
import os
import pywhatkit
import webbrowser
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

youtube = "https://www.youtube.com"
reddit = "https://www.reddit.com"
chillmusic = "https://www.youtube.com/watch?v=RLWcYADoV84"
google = "https://www.google.com"
whatsapp = "https://web.whatsapp.com"
mathurl = "[YOUR URL]"
scienceurl = "[YOUR URL]"
turkishurl = "[YOUR URL]"
englishurl = "[YOUR URL]"
vsurl = "[YOUR URL]"
codeurl = "[YOUR URL]"
germanurl = "[YOUR URL]"
guideurl = "[YOUR URL]"
religionurl = "[YOUR URL]"
lunarpath = "[YOUR PATH]"
cmdpath = "C:\\WINDOWS\\system32\\cmd.exe"
codepath = "[YOUR PATH]"


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

    vscode = "[YOUR PATH]"
    subprocess.Popen([vscode, file_name])

def play():
    song = query.replace('could you play', '')
    speak('playing ' + song)
    pywhatkit.playonyt(song)

def timee():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f" the time is {strTime}")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello. Please tell me how may I help you")   
def shutDown():
    os.system("shutdown /s /t 5")

def restart():
    os.system("shutdown /r /t 5")

def sleepJarvis():
    speak("ok")
    exit()

def whoIs():
    wolf_res = query.replace("search", "")
    wolf_res = query.replace(" ", "+")
    webbrowser.open("https://www.wolframalpha.com/input/?i=" + wolf_res)

def whatIs():
    wolf_res = query.replace("what is ", "")
    wolf_res = wolf_res.replace(" ","")
    wolf_res = wolf_res.replace("+", "%2B")
    webbrowser.open("https://www.wolframalpha.com/input/?i=" + wolf_res)

def notee():
    speak("What would you like me to write down?")
    note_text = takeCommand()
    note(note_text)
    speak("I've made a note of that")

query = takeCommand().lower()

def openCMD():
    speak("opening command prompt")
    os.startfile(cmdpath)

def joke():
    speak(pyjokes.get_joke())

def wikipedia():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia search", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def stackOverFlow():
    question = query.replace("stack overflow", "")
    webbrowser.open("https://stackoverflow.com/search?q=" + (question))

def openCode():
    os.startfile(codepath)

def openMinecraft():
    speak('opening minecraft')
    os.startfile(lunarpath)

def openYoutube():
    speak("Opening youtube")
    webbrowser.open(youtube)

def openChillMusic():
    speak("Opening chill music")
    webbrowser.open(chillmusic)

def openReddit():
    speak("Opening reddit")
    webbrowser.open(reddit)

def openGoogle():
    speak("Opening google")
    webbrowser.open(google)

def openWhatsapp():
    speak("Opening whatsapp")
    webbrowser.open(whatsapp)

def openMath():
    webbrowser.open(mathurl)

def openScience():
    webbrowser.open(scienceurl)

def openTurkish():
    webbrowser.open(turkishurl)

def openEnglish():
    webbrowser.open(englishurl)

def openVSArts():
    webbrowser.open(vsurl)

def openCoding():
    webbrowser.open(codeurl)

def openGerman():
    webbrowser.open(germanurl)

def openGuide():
    webbrowser.open(guideurl)

def openReligion():
    webbrowser.open(religionurl)
