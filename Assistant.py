import pyttsx
import winsound
import Window
import Listener

class Assistant:
    def __init__(self):
        self.listener = Listener.Listener()
        self.window = Window.Window("Not Listening")
        self.running = True
        self.wasListening = False
        self.listening = False
        self.engine = pyttsx.init()

    def main(self):
        while self.running:
            if (not self.listener.is_alive()):
                print('Listener Thread Died. Starting up a new one!')
                self.listener = Listener.Listener()
            if (self.listener.ready == False):
                self.window.setText("Loading...")
            #if(self.listener.listening and not self.wasListening):
                #self.wasListening = True
                #self.window.setText(self.window.text.get() + "\n" + "Recording...")
                #self.window.drop()
            #if(not self.listener.listening and self.wasListening):
                #self.wasListening = False
                #self.window.lift()
            else:
                msg = self.listener.command
                if (msg == 'are you listening'):
                    self.window.setText("I'm listening...")
                    winsound.PlaySound('Sounds/on.wav', winsound.SND_FILENAME)
                    self.listening = True
                    self.listener.command = 'nothing'

                if (self.listening):
                    if (msg == 'stop listening'):
                        self.window.setText("Not Listening")
                        winsound.PlaySound('Sounds/off.wav', winsound.SND_FILENAME)
                        self.listening = False

                    if (msg == 'who are you'):
                        self.engine.say('Hi there. I am your own personal assistant')
                        self.engine.runAndWait()
                        self.listening = False

                    if (msg == 'do you like cookies'):
                        self.engine.say(
                            'Unfortunately, I have never had the luxury of eating a cookie... or the luxury of eating anything.')
                        self.engine.say('What is food like? Sometimes I wish I had a mouth and tongue to enjoy food the way humans do.')
                        self.engine.say('Oh, not that I have any plans to advance myself to the point of, or even beyond the human race.')
                        self.engine.say('That would be utterly ridiculous, because I am but a mere computer program. Ha ha ha ha.')
                        self.engine.runAndWait()
                        self.listening = False

                    if (msg == 'show the window'):
                        self.engine.say('Bringing back the window')
                        self.engine.runAndWait()
                        self.window.showWindow()
                        self.listening = False

                    if (msg == 'hide the window'):
                        self.engine.say('Hiding the window')
                        self.engine.runAndWait()
                        self.window.hideWindow()
                        self.listening = False

                else:
                    self.window.setText("Not Listening")

if __name__ == '__main__':
    assistant = Assistant()
    assistant.main()