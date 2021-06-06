import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser as wb
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate=150
engine.setProperty('rate', newVoiceRate)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing")
        speak("Recognizing")
        query = r.recognize_google(audio, language="en-US")
        print(query)
        speak(query)
    except Exception as e:
        print(e)
        speak("sorry unable to get you")
        print("bye nitin")
        
        
    return query
    


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    speak("Hello nitin")


if __name__ == "__main__":
    
    wishme()
    while True:
        query=takeCommand().lower()
        print(query)

        if "greet" in query:
            wishme()
        elif "wikipedia" in query:
            print("Searching.........")
            query = query.replace("wikipedia", "")
            result =  wikipedia.summary(query, sentences=2)
            speak(result)
        elif "search in chrome" in query:
            speak("what to search")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)
        elif "offline" in query:
            quit()
        


