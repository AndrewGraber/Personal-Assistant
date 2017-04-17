from Tkinter import *
import threading

class Window(threading.Thread):
    def __init__(self, text):
        self.window = Tk() #Instantiate the window
        self.window.geometry('200x50+0+0') #Sets size and position
        self.window.overrideredirect(1) #Removes Window Border
        self.window.attributes('-topmost', True) #Makes sure window is always on top
        self.window.configure(background="purple")
#        self.window.setBackground("gray")
        self.text = StringVar() #Creates a StringVar
        self.text.set(text) #Set text value to passed argument
        #self.text.setTextColor("purple")
        self.label = Label(self.window, textvariable=self.text, height=16) #Creates the label in which to hold the text
        self.label.configure(background="purple")
        self.label.configure(foreground="grey")
        self.label.configure(font=("Coolvetica RG", 16))
        self.label.pack()
        threading.Thread.__init__(self) #Initialize this as a thread (so it can run independently from the other parts of the program)
        self.start() #Start this object up!

    def run(self):
        self.window.mainloop() #Makes the window actually appear

    def setText(self, text):
        self.text.set(text)

    def hideWindow(self):
        self.window.geometry('0x0')

    def showWindow(self):
        self.window.geometry('200x50+0+0')

    def drop(self, amount = 50):
        self.window.geometry('%dx%d+0+0' % (self.window.winfo_width(), self.window.winfo_height() + 50))

    def lift(self, amount = 50):
        self.window.geometry('%dx%d+0+0' % (self.window.winfo_width(), self.window.winfo_height() - 50 if self.window.winfo_height() >= 100 else self.window.winfo_height()))