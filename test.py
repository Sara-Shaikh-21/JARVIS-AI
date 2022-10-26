import datetime
import os
import sys

import pyautogui
import pyttsx3
import speech_recognition as sr
import smtplib
import pywhatkit
import psutil
from PyQt5 import QtWidgets
from wikipedia import wikipedia
from nltk.tokenize import word_tokenize
import secrets
from secrets import senderemail, epwd, to
import time as tt
import requests
import webbrowser as wb
import subprocess as sp
from IntegrationTesting import MyWindow

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour <= 12):
        pyttsx3.speak("Good Morning Ma'am.")
    elif hour >= 12 and hour <= 18:
        pyttsx3.speak("Good Afternoon Ma'am")
    else:
        pyttsx3.speak("Good Evening Ma'am")


engine = pyttsx3.init()
engine.say("Hello,Jarvis here,how can I help you?")
engine.runAndWait()
wishMe()


def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        pyttsx3.speak("Say that again Please...")
        return "None"
    return query


def screenshot():
    uname = os.getenv('username')
    name_img = tt.time()
    name_img = f'C:\\Users\\{uname}\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  # H=hr,M=mins,S=sec
    pyttsx3.speak("The current time is:")
    pyttsx3.speak(Time)


def mail():  # wrapper for sendMail function
    try:
        pyttsx3.speak("What should I say ?")
        content = takeCommandMIC()
        sendEmail(content)

    except Exception as e:
        print(e)
        pyttsx3.speak("Unable to send the email")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    dat = int(datetime.datetime.now().day)
    pyttsx3.speak("Today's date is:")
    pyttsx3.speak(dat)
    pyttsx3.speak(month)
    pyttsx3.speak(year)


def youtube():
    pyttsx3.speak("what should i search for on youtube")
    topic = takeCommandMIC()
    pywhatkit.playonyt(topic)


def cpu():
    usage = str(psutil.cpu_percent())
    pyttsx3.speak('CPU is at' + usage)


def battery_per():
    battery = psutil.sensors_battery()
    pyttsx3.speak('Battery is at ')
    pyttsx3.speak(battery.percent)


def remember_that():
    pyttsx3.speak("what should i remember")
    data = takeCommandMIC()
    pyttsx3.speak("ok")
    remember = open('data.txt', 'w')
    remember.write(data)
    remember.close()


def remembered_data():
    remember = open('data.txt', 'r')
    pyttsx3.speak("you told me to remember that " + remember.read())


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        pyttsx3.speak("Good Morning!")
    elif hour >= 12 and hour < 15:
        pyttsx3.speak("Good Afternoon!")
    elif hour >= 15 and hour < 20:
        pyttsx3.speak("Good Evening!")
    else:
        pyttsx3.speak("Good Night!")
    greeting()


def searchGoogle():
    # print("Google")
    pyttsx3.speak('What do I search for?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q=' + search)


def sendEmail(content):
    pyttsx3.speak("Whom should I send the mail to ?")
    try:
        person = takeCommandMIC()
        mailId = secrets.people.get(person)
        server = smtplib.SMTP('smtp.gmail.com', 587)  # 587-port no. of gmail
        server.starttls()
        server.login(senderemail, epwd)
        server.sendmail(senderemail, mailId, content)
        server.close()
        pyttsx3.speak("Email sent successfully")
    except Exception as e:
        print(e)
        pyttsx3.speak("Person doesn't exist")


# enable allow less secure apps option on mail


def weatherUpdate():
    pyttsx3.speak("please tell me the city name")
    city = takeCommandMIC()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=8f63cb0348a4736da138da4b395fdde4'
    res = requests.get(url)
    data = res.json()
    weather = data['weather'][0]['main']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    temperature = round((temperature - 32) * 5 / 9)
    pyttsx3.speak(f'weather in {city}' + 'is consisting of {}'.format(description))
    pyttsx3.speak('and temperature is : {} degree celcius'.format(temperature))


def searchWiki():
    pyttsx3.speak('What do I search for?')
    search = takeCommandMIC()
    result = wikipedia.summary(search, sentences=2)
    pyttsx3.speak(result)


def whatsApp(phone, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone=' + phone + '&text=' + Message)
    tt.sleep(50)
    # x = 926, y = 953
    pyautogui.click(926, 953)
    pyautogui.press('enter')


def OpenApps(query):
    uname = os.getenv('username')
    sysroot = os.getenv('SystemRoot')
    print(sysroot)
    if "notepad" in query:
        Program = "Notepad.exe"
        filename = "Demo.txt"
        sp.Popen([Program, filename])
    elif "paint" in query:
        Program = "mspaint.exe"
        filename = "Demo.txt"
        sp.Popen([Program, filename])
    elif "v" or "s" or "code" in query:
        Program = f'C:\\Users\\{uname}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        filename = "Demo.txt"
        sp.Popen([Program, filename])
    elif "documents" in query:
        docs = f'C:\\Users\\{uname}\\Documents'
        os.startfile(docs)
    elif "pictures" in query:
        pics = f'C:\\Users\\{uname}\\Pictures'
        os.startfile(pics)


def alarm():
    pyttsx3.speak("Tell me the  time to put an alarm")
    time = input()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.showMaximized()
    # app.exec()
    while True:
        flag=0
        query = takeCommandMIC().lower()
        query = word_tokenize(query)
        if 'time' in query:
            time()
        # 2
        elif 'date' in query:
            date()
        # 3
        elif 'open' in query:
            OpenApps(query)
        # 4
        elif 'mail' in query:
            mail()
        # 5
        elif 'youtube' in query:
            youtube()
        # 6
        elif 'remember' in query:
            remember_that()
        # 7
        elif 'know' in query:
            remembered_data()
        # 8
        elif 'cpu' in query:
            cpu()
        # 9
        elif 'google' in query:  # capital case is considered
            searchGoogle()
        # 10
        elif 'battery' in query:
            battery_per()

        # 11
        elif 'screenshot' in query:
            screenshot()
        # 12
        elif 'weather' in query:
            weatherUpdate()
        # 13
        elif 'notepad' in query:
            OpenApps(query)
        # 14
        elif 'paint' in query:
            OpenApps(query)
        # 15

        # 17
        elif 'offline' in query:
            flag = 1
            pyttsx3.speak("Bye Have a good day ahead...")
            window.close()
            sys.exit(os.system('IntegrationTesting.py'))
        # 18
        elif 'wikipedia' in query:
            searchWiki()

        # 19

        # 20
        elif 'message' in query:
            username = {
                'Saurabh': '+91 9850365380',
                'Sheetal': '+91 8421732301',
                'Gauri': '+91 7499193610',
                'Karishma': '+91 9284788401'

            }
            try:
                pyttsx3.speak("Who do you wish to message ?")
                name = takeCommandMIC()
                phone = username[name]
                pyttsx3.speak("What is the message to be sent")
                message = takeCommandMIC()
                whatsApp(phone, message)
                # sendEmail(content)
                pyttsx3.speak("Whatsapp message sent successfully")

            except Exception as e:
                print(e)
                pyttsx3.speak("Unable to send the whatsapp message")
        # 24
        elif 'alarm' in query:
            alarm()

        else:
            pyttsx3.speak("Not among the above commands")

        if flag == 0:
            pyttsx3.speak("Do you want me to do something else ? ")
            choice = takeCommandMIC().lower()
            tt.sleep(10)
            if choice == "yes":
                pyttsx3.speak("Kindly tell what to do")
                pass
            else:
                pyttsx3.speak("Thankyou")
                window.close()
                sys.exit(os.system('IntegrationTesting.py'))

