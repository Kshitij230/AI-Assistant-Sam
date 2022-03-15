import os
import speech_recognition as sr

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 2
        audio = r.listen(source, phrase_time_limit=3)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        return takecommand()
    return query



if __name__ == "__main__":

    while True:
        query = takecommand().__str__().lower()
        if "hey sam" in query or "wake up" in query or "utho sam" in query or "sam utho" in query:
            os.startfile("E:\\Sam 2.0\\Sam 2.0 .exe file\\Sam.py")

        elif "quit sam" in query or "stop sam" in query or "stop it" in query:
            os.system("taskkill /f /im py.exe")
            

        else:
            print()
