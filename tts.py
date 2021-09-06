import pyttsx3

def speak(text):
    tts = pyttsx3.init()
    tts.say(text)
    tts.runAndWait()

if __name__ == '__main__':
    speak('Funcionou!')