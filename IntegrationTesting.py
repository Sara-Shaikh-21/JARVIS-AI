from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QMovie
import speech_recognition as sr
import os

from nltk import word_tokenize


def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        return "None"
    return query


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, path="C:/Users/Sara/PycharmProjects/Python/PBL/test.py"):
        super(MyWindow, self).__init__()
        uic.loadUi('gui.ui', self)
        # self.movie = QMovie('pic.jpg')
        # self.label.scaleContent()
        self.path = path


if __name__ == '__main__':
    import sys

    while True:
        query1 = takeCommandMIC().lower()
        query1 = word_tokenize(query1)
        if 'jarvis' in query1:
            print("Hello")
            sys.exit(os.system('test.py'))
