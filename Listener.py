import threading
import speech_recognition as sr

import Miscellaneous
import ConnectionChecker

WIT_AI_KEY = "VR76YG3PY55TB6TWK7O3LBKS3QL3KKUH"


class Listener(threading.Thread):
    def __init__(self):
        self.running = True
        self.command = "nothing"
        self.ready = False
        self.listening = False
        self.inet = ConnectionChecker.ConnectionChecker()
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        self.rec = sr.Recognizer()
        with sr.Microphone() as self.source:
            self.rec.adjust_for_ambient_noise(self.source, duration=2)
        self.ready = True

        while(self.running):
            print('Listening')
            with sr.Microphone() as self.source:
                self.listening = True
                self.audio = self.rec.listen(self.source)
                self.listening = False

            if(not self.inet.isConnected):
                try:
                    self.command = self.rec.recognize_sphinx(self.audio)
                    print("Sphinx: " + self.command)
                except sr.UnknownValueError:
                    print("Sphinx: Could not understand what you said")
                except sr.RequestError as e:
                    print("Sphinx error: {0}".format(e))

            else:
                try:
                    self.command = self.rec.recognize_wit(self.audio, WIT_AI_KEY)
                    print("Wit: " + self.command)
                except sr.UnknownValueError:
                    print("Wit: Could not understand what you said")
                except sr.RequestError as e:
                    print("ERR: {0}".format(e))
                    print("Lost internet connection. Using Sphinx to interpret voice commands. Results may be less accurate")
                    self.inet.isConnected = False
                except:
                    self.running = False
                    print("THREAD DIED IDK WHY")