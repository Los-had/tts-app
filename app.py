from tts import speak
from tkinter import *

win = Tk()
win.geometry("350x350")
win.title("TTS-app")

about = Label(win, text="Aplicativo que fala os seus textos").pack()
user_text = Entry(win)
user_text.pack()

def speakUserText():
    txt = user_text.get()
    speak(txt)

speak_button = Button(win, text="Falar", command=speakUserText).pack()

win.mainloop()