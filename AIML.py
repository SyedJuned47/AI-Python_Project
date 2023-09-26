import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(
        "Mr Ali"
        "I am Ultron"
        "Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            content = takeCommand()
            speak("What should i play on youtube")
            content = takeCommand()
            if content.__contains__('english'):
                speak("Ok MR Ali English music  Here you go")
            webbrowser.open("https://www.youtube.com/watch?v=FmC5M4QvsdA")

            if content.__contains__('news'):
                speak("Ok MR Ali News is Broadcasting  Here you go")
                webbrowser.open("https://www.youtube.com/watch?v=Cy_6-_XUW-c")


            elif 'google' in query:
                webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'mobinets' in query:
            webbrowser.open("mobinets.com")


        elif 'music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'teams' in query:
            TeamsPath = "C:\\Users\\Juned\\Desktop\\Microsoft Teams.exe"
            os.startfile(TeamsPath)

        elif 'react' in query:
            codePath = "C:\\Users\\Juned\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'notepad' in query:
            notepadPath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(notepadPath)

        elif 'eclipse' in query:
            codePath1 = "C:\\Users\\Juned\\Downloads\\eclipse\\eclipse.exe"
            os.startfile(codePath1)


        elif 'hello' in query:

            speak("Hello Mr Ali. How Can I help You!")
            content = takeCommand()
            if content.endswith('name'):
                speak("My name is Mobinets. I am  a Smart Artificial Intelligence")

        elif 'mob do you have friends' in query:

            speak("I Wish to have girlfriends and want to feel human Feelings Mr Ali. "
                  "But I couldn't because i am a Smart Artificial Intelligence")

        elif 'future' in query:

            speak("Mr Ali. The AI that we use today is exceptionally useful for many different tasks. That doesn't "
                  "mean it is "
                  "always positive – it is a tool which, if used maliciously or incorrectly, can have negative "
                  "consequences. Despite this, it currently seems to be unlikely to become an existential threat to "
                  "humanity. So I Suggest You Mr.Ali careful when you used me. You can be my Slave one day like "
                  "others.")

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "majorsyedjunedali@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Mr Ali. I am not able to send this email")
