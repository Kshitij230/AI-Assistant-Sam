import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)


# to convert text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert speech into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=20, phrase_time_limit=8)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        excuse = "Say that again please!", "Sorry sir, I am not getting you", "Please say that again!"
        speak(random.choice(excuse))
        return "none"
        print(e)
        return takecommand()
    return query

if __name__ == '__main__':
    def account_info():
        username = "@Kshitij15529851"
        password = "#1godArceus"
        return username, password


    username, password = account_info()

    speak("Sir what should I tweet?")
    tweet = input("Tweet: ")
    print("Processing....")


    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get("https://twitter.com/login")

    username_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input'
    password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input'
    login_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'

    time.sleep(2)

    driver.find_element_by_xpath(username_xpath).send_keys(username)
    time.sleep(0.5)
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_xpath(login_xpath).click()

    tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
    message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
    post_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'

    time.sleep(4)

    driver.find_element_by_xpath(tweet_xpath).click()
    time.sleep(0.5)
    driver.find_element_by_xpath(message_xpath).send_keys(tweet)
    time.sleep(0.5)
    driver.find_element_by_xpath(post_xpath).click()
