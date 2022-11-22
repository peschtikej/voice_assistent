import speech_recognition
sr=speech_recognition.Recognizer()
sr.pause_threshold=0.5
import pyttsx3
import datetime

global q

def rasp():
    global q
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio=sr.listen(source=mic)
        q=sr.recognize_google(audio_data=audio, language='ru-RU').lower()

def talk(text):
    eng=pyttsx3.init()
    eng.say(text)
    eng.runAndWait()

t=str(datetime.datetime.now())

def write_task():
    print('Что записать')
    rasp()
    with open('task.txt', 'w', encoding='utf-8') as file:
        file.write(q)    

def hello():
    return "Привет пупсик"

while True:
    t=str(datetime.datetime.now())
    rasp()
    if 'привет' in q:
        print(hello())
        talk(q)
    if 'задача' in q:
        talk(q)
        write_task()
    if 'прочти' in q:
        with open('task.txt', 'r', encoding='utf-8') as file:
            talk(file.read())
    if 'выключись' in q:
        talk(q)
        print(q)
        break
    if 'время' in q:
        print(t[11:])
        talk(t[11:])
    else:
        talk(q)
        print('что')