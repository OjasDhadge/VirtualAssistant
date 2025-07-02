import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()  # Creating a listener object from the speech_recognition module4
engine = pyttsx3.init()  # Creating and initializing engine to speak to you
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:  # using microphone using sr as source
            print("Listening...")
            voice = listener.listen(source)  # Creating voice variable to listen through the source
            command = listener.recognize_google(voice)  # Creating a cmd var to hold voice command given by user.
            command = command.lower()
            # if 'jarvis' in command:
                # command = command.replace('jarvis', '')

    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('current time is' + time)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry')
    elif 'joke' in command:
        jox = pyjokes.get_joke()
        print(jox)
        talk(jox)
    elif 'hey' in command:
        print('hello Client!, How can i help you today? ')
        talk('hello Client!, How can i help you today?')
    elif 'how are you' in command:
        print('I am great, Thankyou for asking,  how can i help you? ')
        talk('I am great, Thankyou for asking,  how can i help you?')
    elif 'your' in command:
        intro = ('My name is Vocal Eyes, and i am your virtual assistant.')
        print(intro)
        talk(intro)
    elif 'help' in command:
        help = ('sure, i can help you in lot of ways')
        print(help)
        talk(help)
        # talk('I am your virtual assistant, and my name is Jarvis')
    else:
        talk('sorry, can you come again?.')


while True:
    run_jarvis()

