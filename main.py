import speech_recognition as sr
from selenium import webdriver
class voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()
    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(f"Command received: {command}")
            except sr.UnknownValueError:
                pass
listener=voice()