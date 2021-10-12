import speech_recognition as sr
import pyttsx3, pywhatkit

name = "juanita"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
for i in voices:
    print(i)

def talk(text):
    engine.say(text) #Voz Sintetica
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc) #Reconocer Voz
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')

    except:
        pass
    return rec

def run_juanita():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproce', '')
        print("Reproduciendo " + music)
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)

if __name__ == '__main__':
    run_juanita()