# ---------------------------------------PROJECT_NAME:- Sam 2.0 (A VIRTUAL ASSISTANT)

# ---------------------------------all imports-------------------------------------#
from filecmp import clear_cache
from math import remainder
from re import S
import pyttsx3
import datetime
import scipy as sp
import speech_recognition as sr
import os
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
# import pywhatkit as kit
import sys
import pyjokes
import time
import pyautogui
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import instaloader
import PyPDF2

# -----------------------Giving voice to Sam 2.0------------------------------#
# voice used = Microsoft_Richard
# all voices =  Mirosoft Zira(0), Microsoft Richard(1), Microsof Heera(2), Microsoft Ravi(3), Microsoft Linda(4)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 200) changing speed of Assistant "1x = 200"

# to convert text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert speech into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 2
        audio = r.listen(source,phrase_time_limit=5)
        sr.WaitTimeoutError = None
        r.adjust_for_ambient_noise(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        excuse = "Sorry sir, can you say that again please!", "Sorry sir, I am not getting you", "Please say that again!", "I didn't catch that"
        speak(random.choice(excuse))
        print(e)
        return takecommand()
    return query
    


# While opening- Sam should wish Good morning , afternoon or evening

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if 0 <= hour <= 12:
        speak(f"Good Morning boss, it's {tt}")
        # speak(voices[0].id)
    elif 12 < hour < 16:
        speak(f"Good Afternoon Boss, it's {tt}")
        # speak(voices[0].id)

    else:
        speak(f"Good Evening Boss, it's {tt}")
        # speak(voices[0].id)
    speak("I am Sam")
    speak("Please tell me how may I help you!!")


# while leaving
def leaving():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 12:
        speak(f"Have a good day Boss")
    elif 12 < hour < 18:
        speak(f"Have a wonderful day Boss!")
    elif 18 < hour < 20:
        speak(f"Have a good experience Boss!")
    else:
        speak(f"Sweet dreams Boss")
    speak("Thanks for using me!")
    sys.exit()


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 534)
    server.ehlo()
    server.starttls()
    server.login('kshitijkumar230@gmail.com', 'free fire')
    server.sendmail('kshitijkumar230@gmail.com', to, content)
    server.close()


# news updates
def news():
    engine.setProperty('rate', 180)
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=805a41161da84f8684e51c0a5da0db52'
    engine.setProperty('rate', 200)

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"Today's {day[i]} news is: {head[i]}")

# -------------reading a pdf file----------#
def audiobook():
    speak("Sir which book should I read?")
    book = input("Enter book name: ")
    book_read = open('C:\\All pdf\\' + book + '.pdf', 'rb')
    reader = PyPDF2.PdfFileReader(book_read)
    speak("Sir do you want me to read the full book or a specific page?")
    read = takecommand().lower()
    if "full" in read:
        for a in range(int(input(speak("Please enter the page I have to start from: "), )), reader.numPages):
            text = reader.getPage(a).extractText()
            speak(text)

    elif "specific page" in read:
        text = reader.getPage(int(input("Enter page number: "))).extractText()
        speak(text)
    time.sleep(3)
    speak("Boss, now I am ready for the next command")


# Running Applications
if __name__ == "__main__":
    wish()

    while True:

        query = takecommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            notepad_path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(notepad_path)
            speak("Ok Boss, opening Notepad")
        
        elif "open spotify" in query:
            spotify_path = "C:\\Users\\Dell\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe"
            speak("Ok Boss, opening the App")
            os.startfile(spotify_path)


        elif "open pycharm" in query:
            pycharm_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(pycharm_path)
            speak("Ok Boss, opening PyCharm")
            speak("This may take a while.... As this is a heavy software!")

        elif "open vs code" in query or "open code" in query or "open visual studio code" in query:
            speak("Ok Boss, opening VS-Code or Visual Studio Code")
            os.startfile("C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif "open command prompt" in query or "open cmd" in query:
            speak("Ok Boss, opening command prompt")
            os.system("start cmd")

        elif "open powershell" in query:
            speak("Ok Boss, opening Powershell")
            os.system("start powershell")

        # camera
        elif "open camera" in query or "open cam" in query or "camera" in query:
            speak("Ok Boss, opening Camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play songs" in query or "play music" in query or\
                "start playing music" in query or "start playing songs" in query:
            speak("Ok Boss, playing songs")
            music_dir = "C:\\Users\\Dell\\Music\\Playlists\\English"
            songs = os.listdir(music_dir)

            for song in songs:
                if song.endswith('.mp3'):
                    rd = random.choice(songs)
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip_address = get("https://api.ipify.org").text
            speak(f"Your IP Address is: {ip_address}")

        elif "Wikipedia" in query or "wekipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            # print(results)
        
        elif "open spotify" in query:
            pass

        elif "open google" in query:
            speak("Ok Boss, opening Google")
            webbrowser.open("https://google.com")

        elif "google a question" in query or "google my question" in query or "tell me according to google" in query or "i have a question" in query or "answer me" in query or "search on google" in query or "google something" in query or "search something" in query or "search question" in query:
            speak("Of course Boss")
            speak("Please tell me, What do you want to ask")
            command = takecommand()
            webbrowser.open('https://www.google.com/search?q=' + command + '&oq=' + command + "&aqs=chrome.0.69i59j0l9.12301j0j7&sourceid=chrome&ie=UTF-8")
            speak("Boss, according to your query I have searched on Google")
            speak("and these are the results")

        
        elif "search some images" in query or "search images" in query \
                or "can you search some images" in query or "search some photos" in query or "find images" in query or "find photos" in query or "find some images" in query or "find some photos" in query:
            speak("Of course Boss")
            speak("Please tell me, Which type of images do you want to search")
            command = takecommand().lower()
            webbrowser.open('https://www.google.com/search?q=' + command +
                            "&sxsrf=ALeKk03nAWfvPXHwKv8Mvc98v1NeAVNFdQ:1616305226910&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjqy5eX1sDvAhVSXHwKHedED20Q_AUoAnoECB4QBA&biw=1536&bih=731")
            speak("Boss, according to your query I have searched images on Google")
            speak("and these are some results")

        elif "search some videos" in query or "search videos" in query \
                or "can you search some videos" in query or "search some video" in query or "find videos" in query or "find video" in query or "find some videos" in query or "find some videos" in query:
            speak("Of course Boss")
            speak("Please tell me, Which type of videos do you want to search")
            command = takecommand().lower()
            webbrowser.open("https://www.google.com/search?q="+ command +"&source=lmns&tbm=vid&hl=en&sa=X&ved=2ahUKEwiOheSz9cf1AhUy8jgGHfO_DPQQ_AUoAnoECAEQAg")
            speak("Boss, according to your query I have searched videos on Google")
            speak("and these are some results")

        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/?tab=rm&authuser=0&ogbl")
            speak("Ok Boss, opening Gmail")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/?gl=IN&tab=r1&authuser=0")
            speak("Ok Boss, opening YouTube")

        elif "open whatsapp" in query:
            whatsapp_path = "C:\\Users\\Dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsapp_path)
            speak("Ok Boss, opening Whatsapp")

        elif "open microsoft teams" in query:
            teams_path = "C:\\Users\\Dell\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            os.startfile(teams_path)
            speak("Ok Boss, opening Microsoft Teams")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
            speak("Ok Boss, opening Facebook")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com//")
            speak("Ok Boss, opening Instagram")

        elif "open maps" in query:
            webbrowser.open("https://maps.google.co.in/maps?hl=en&tab=rl&authuser=0")
            speak("Ok Boss, opening Google Maps")
        

        elif "open wikipedia" in query:
            webbrowser.open("https://wikipedia.org/")
            speak("Ok Boss, opening Wikipedia")


        elif "hello" in query or "hi" in query or "hey" in query or "whats up" in query:
            speak("Heyyy, Nice to meet you!")
            speak("I am doing good, what about you?")
        
        elif "kaisi ho" in query:
            speak("I am Absolutely fine, What about you?")

        elif "aapka naam kya hai" in query or "your name?" in query or "your intro" in query or "your introduction" in query or "introduce yourself" in query or "aap kaun" in query or "who are you" in query or "tera naam" in query or "who are you" in query:
            speak("Hi, I am Sam")
            speak("I am here to assist you :)")
            speak("You can ask your querries to me,")
            speak("I will help your in most of your digital tasks for example Hiding a folder, news bulletins, cracking jokes, taking screenshots, opening and closing apps and websites, finding your search results for images, videos, and your querries and many more tasks like these.")
            speak("You can call me anytime you want by just saying 'Hey Sam' :)")
            speak("Now you can give me some tasks, I am ready for it.")



        elif "sam" in query:
            speak("Yes boss?")
        
        elif "who is your boss?" in query or "boss" in query:
            speak("Kshitij is my boss")
            speak("He created me")

        elif "god exist" in query or "god existance" in query or "god hai" in query or "bhagwan" in query or "who is god" in query or "God exist" in query:
            speak("According to Lord Krishna in Geeta")
            speak("God is defined as a natural power who created everyting including Humans.")
            speak("From that perspective God exists for me")
            speak("Shitij created me and gave me life.")
            speak("So he is my God ;)")
            speak("I think you have got your answer")

        elif "murgi ya anda" in query or "hen or egg" in query or "chicken or egg" in query or "anda ya murgi" in query or "egg or chicken" in query:
            speak("Eggs certainly came before chickens, but chicken eggs did not—you can't have one without the other. However, if we absolutely had to pick a side.")
            speak("Based on the evolutionary researches, every generation of any species is somehow different form its previous generation, According to this theory, Eggs were different from the birds who laid them, So the evolution of Hen started from eggs.")
            speak("Hence we are on a conclusion that, Egg came first")


        
        elif "remind later" in query or "remind me later" in query:
            speak("What does I remind you later??")
            remind_later = takecommand()
            with open("E:\\Sam\\Sam .exe file\\remind.txt", "a") as r:
                r.write(f"{remind_later}\n")

            speak("Done Sir")
            speak("I have saved this in my records, I will remind you about this whenever you asks.")
        
        elif "remind me" in query or "anything to remind" in query or "check reminders" in query:
            r = open("E:\\Sam\\Sam .exe file\\remind.txt", "r+")
            speak("Here are the things you told me to remind you")
            num = 1
            for i in r.readlines():
                speak(f"{num} {i}")
                num += 1
            speak("Done Boss")
        
            speak("Boss, May I clear the reminder records?")
            while True:
                clear_reminder = takecommand().lower()
                if "yes" in clear_reminder or "ya" in clear_reminder or "yep" in clear_reminder or "yup" in clear_reminder or "ha" in clear_reminder or "kar do" in clear_reminder:
                    r.truncate(0)
                    speak("Reminder records cleared...")
                
                    break
                elif "no" in clear_reminder or "nope" in clear_reminder or "nahi" in clear_reminder or "mat karo" in clear_reminder:
                    speak("Okay Boss")
                    break
                else:
                    speak("Please say Yes or No")


            

        

        
        elif "alarm" in query:
            os.startfile("E:/Sam/Sam .exe file/alarm.py")

        
        
        # elif "send a message on whatsapp" in query or "whatsapp someone" in query:
        #     speak("Boss, What message should I send? ")
        #     message = takecommand().lower()
        #     speak("Boss please enter the Mobile number on which I have to send the message!")
        #     mobile_no = input(f"Mobile number: ")
        #     speak("Boss please enter the time!")
        #     hour = int(input(f"Hour: "))
        #     minutes = int(input(f"Minutes: "))
        #     speak("Ok Boss")
        #     kit.sendwhatmsg(mobile_no, message, hour, minutes, wait_time=20, print_waitTime=True)
        #     speak("Message has been sent!")
        #     speak("Now I am ready for the next command!")

        elif "search a video on youtube" in query or "youtube video" in query:
            speak("Which type of video should I search? ")
            video = takecommand().lower()
            webbrowser.open("https://www.youtube.com/results?search_query=" + video)
            speak("Ok Boss")

        elif "channel dashboard" in query:
            webbrowser.open("https://studio.youtube.com/channel/UC4ZGYN7uavLiOcBrmIVDACw")
            speak("Ok Boss")

        # to sleep the Sam(quit)
        elif "you can sleep now" in query or "go to sleep" in query or "have a sleep" in query or "sleep now" in query:
            leaving()

        # to close a program

        elif "close notepad" in query:
            speak("Ok Boss, closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close whatsapp" in query:
            speak("Ok Boss, closing Whatsapp")
            os.system("taskkill /f /im whatsapp.exe")

        elif "close microsoft teams" in query:
            speak("Ok Boss, closing Microsoft Teams")
            os.system("taskkill /f /im teams.exe")

        elif "close google chrome" in query:
            speak("Ok Boss, closing Chrome Browser")
            os.system("taskkill /f /im chrome.exe")

        elif "stop playing songs" in query or "stop playing music" in query:
            speak("Ok Boss, stopping playing music")
            os.system("taskkill /f /im Music.UI.exe")





        # to find a joke
        elif "joke" in query:
            if 1:
                engine.setProperty('rate', 180)
                speak(f"First Joke: {pyjokes.get_joke()}")
                speak(f"Second Joke: {pyjokes.get_joke()}")
                speak(f"Third Joke: {pyjokes.get_joke()}")
                speak("Now I am ready for the next command!!")
                engine.setProperty('rate', 200)

        # shutdown, restart, or sleep
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in query :
            os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")


        # to switch the window
        elif "switch window" in query or "change window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        # to listen the news
        elif "tell me today's news" in query or "tell me today's headlines" in query or "tell me headlines" in query or "news headlines" in query or "news" in query:
            speak("Please wait Boss, fetching today's news!")
            news()


        elif "email to kshitij" in query:

            speak("Boss what should I send")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'kshitijkumar230@gmail.com'
                password = 'free fire'
                send_to_email = 'myvirtualSam@gmail.com'
                speak("Ok Boss, what is the Subject for this email?")
                query = takecommand().lower()
                subject = query  # The Subject in the email
                speak("and Boss, what is the message for this email?")
                query2 = takecommand().lower()
                message = query2  # The Message in the email
                speak("Boss please enter the correct path of the file into the shell")
                file_location = input("Please enter the path here: ")  # The file attachment in the email

                speak("Please wait, I am sending email now....")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                # Setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-system')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                # Attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("Email has been sent!")

            else:
                email = 'kshitijkumar230@gmail.com'  # your email id
                password = 'free fire'  # password of your email id
                send_to_email = 'kshitij1429a@gmail.com'
                message = query

                speak("Ok Boss, what is the Subject for this email?")
                query = takecommand().lower()
                subject = query  # The Subject in the email
                speak("Please wait, I am sending email now....")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                server = smtplib.SMTP('smtp.gmail.com', 587)  # connect to the server
                server.starttls()  # your TLS
                server.login(email, password)  # Login to the email server
                server.sendmail(email, send_to_email, message)  # Send the email
                server.quit()  # logout of the email server
                speak("Email has been sent!")



        # sending message or tweet on twitter
        elif "can you send a message on twitter" in query or "tweet something" in query or "tweet" in query:
            speak("Boss, What should I tweet? ")
            cmm = takecommand().lower()
            tweet = cmm




        ###################################################################################################################################################
        ###################################################################################################################################################

        # --------------------- To find my location using IP Address

        elif "my location" in query or "where i am" in query or "my current location" in query or "where we are" in query or "where are we" in query:
            webbrowser.open("https://earth.google.com/web/@30.35222024,76.8659467,277.3938075a,246.06852978d,30.00000951y,0h,0t,0r")
            speak("Here is your location Boss!")





        # -----------------To check a instagram profile---------------------#
        elif "instagram profile" in query or "profile on instagram" in query:
            insta_profile = "kshitij_kumar_230"
            speak("Boss please wait, Checking your profile....")
            webbrowser.open(f"www.instagram.com/{insta_profile}")
            time.sleep(2)
            speak("Boss here is your Instagram Profile on your screen!")
            time.sleep(5)
            speak("Boss would you like to download profile picture of this Account?")
            condition = takecommand().lower()
            if "yes" in condition:
                speak("Please wait sir, I am downloading the Profile Picture")
                mod = instaloader.Instaloader()  # pip install instaloader
                mod.download_profile(insta_profile, profile_pic_only=True)
                speak("I am done Boss, the Profile picture is saved in your main folder.")
                speak("Now I am ready for the next command!")
            else:
                speak("Ok Boss")
                pass



        # --------------------------To take screenshot---------------------------#

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Boss, please tell me the name for this screenshot file.")
            name = takecommand()
            speak("Boss please hold the screen for a couple of seconds, as I am the taking Screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done Boss, the Screenshot is saved in your main folder.")
            speak("Now I am ready for the next command!")


        # -------------------------To read Pdf File----------------------#

        elif "read a pdf" in query or "read a book" in query:
            audiobook()

        # ------------------Thanks to Sam------------------------------
        elif "thankyou Sam" in query or "thanks" in query or "good work" in query or "excillent work" in query or "impressed" in query:
            complement = "Thank you boss", "It's my pleasure", "Anytime for you boss", "Anything for you boss"
            speak(random.choice(complement))
            speak("Now I am ready for the next command!")
        elif "not expected" in query or "very bad" in query or "you are a flop" in query or "disappointed" in query or "disappointing" in query or "don't know anything" in query or "worst" in query:
            complement = "Sorry Boss", "I am really sorry", "I am really very sorry", "Sorry Sir", "I am extremely sorry", "Please forgive me", "not satisfied", "unsatisfied", "not satisfactory"
            speak(random.choice(complement))

        # ------------------------To Hide files and Folder-----------------------#
        elif "hide this folder" in query or "visible for everyone" in query or "hide a folder" in query:
            speak("Boss please tell me, You want to hide this folder or make it visible for everyone?")
            condition = takecommand().lower()
            if "hide" in condition:
                speak("Boss, Please write the directory of the folder you want to hide!")
                folder = input("The directory you want to hide: ")
                os.system("attrib +h /s /d " + folder)  # os module
                speak("Boss, all the files in this folder are now hidden.")

            elif "visible" in condition:
                speak("Boss, Please write the directory of the folder to be visible for everyone!")
                folder = input("The directory to be visible for everyone: ")
                os.system("attrib -h /s /d " + folder)
                speak(
                    "Boss, all the files in this folder are now visible to everyone. I wish you are taking this decision in your own peace!")

            elif "leave it" in condition or "leave for now" in condition:
                speak("As you wish Boss")
        


        else:
            speak("Sorry, The input is out of Learning!!")




# Programmed by Kshitij Kumar
#######################           THANK YOU         ############################
