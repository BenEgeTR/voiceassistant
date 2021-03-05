import jarvis_ai as jr

if __name__ == "__main__":
    jr.wishMe()
    while True:
        query = jr.takeCommand().lower()

        if 'wikipedia search' in query:
            jr.wikipedia()
            
        elif "write this down" in query:
            jr.notee()

        elif "go to sleep" in query:
            jr.sleepJarvis

        elif 'play' in query:
            jr.play()

        elif 'the time' in query:
            jr.timee()

        elif 'shut down the system' in query:
            jr.shutDown()

        elif 'restart the system' in query:
            jr.restart()
        
        elif "what is " in query:
            jr.whatIs()
        
        elif "who is" in query:
            jr.whoIs()

        elif 'could you hear me' in query:
            jr.speak("Yes sir")

        elif "stop" in query:
            jr.sleepJarvis()

        elif "i guess its time" in query: # Math
            jr.openMath()
        
        elif "science" in query: # Fen
            jr.openScience()

        elif "Turkish" in query: # Türkçe
            jr.openTurkish()

        elif "English" in query: # İngilizce
            jr.openEnglish()

        elif "Visual arts" in query: # Görsel Sanatlar
            jr.openVSArts()

        elif "coding" in query: # Bilişim
            jr.openCoding()

        elif "german" in query: # Almanca
            jr.openGerman()
        
        elif "guide" in query: # Rehberlik
            jr.openGuide()
        
        elif "religion" in query: # Din
            jr.openReligion()

        elif 'thanks' in query:
            jr.speak("no problem sir")
        
        elif 'joke' in query:
            jr.joke()

        #Open Stuff
        elif 'open youtube' in query:
            jr.openYoutube()

        elif "play chill music" in query:
            jr.openChillMusic()

        elif 'open reddit' in query:
            jr.openReddit()

        elif 'open google' in query:
            jr.openGoogle()
            
        elif 'open whatsapp' in query:
            jr.openWhatsapp()

        elif "stack overflow" in query:
            jr.stackOverFlow()

        elif 'open code' in query:
            jr.openCode()
        
        elif 'open minecraft' in query:
            jr.openMinecraft()

        elif 'open command prompt' in query:
            jr.openCMD()