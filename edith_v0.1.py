import pyttsx3
import datetime
import time as t
import smtplib
import wikipedia
import webbrowser as wb
import os
import string
import wolframalpha
import pyautogui
import psutil
import pyjokes
import random
from colored import fg, attr
import speech_recognition as sr

print(f"""{fg(226)}{attr(1)}
                                     ____  ____  __  ____  _  _ 
                                    (  __)(    \(  )(_  _)/ )( |
                                     ) _)  ) D ( )(   )(  ) __ (
                                    (____)(____/(__) (__) \_)(_/

  ___ _  _   _____ _  _ ___   __  __ ___ __  __  ___  _____   __   ___  ___   ___ ___  ___  _  _ __  __   _   _  _ 
 |_ _| \| | |_   _| || | __| |  \/  | __|  \/  |/ _ \| _ \ \ / /  / _ \| __| |_ _| _ \/ _ \| \| |  \/  | /_\ | \| |
  | || .` |   | | | __ | _|  | |\/| | _|| |\/| | (_) |   /\ V /  | (_) | _|   | ||   / (_) | .` | |\/| |/ _ \| .` |
 |___|_|\_|   |_| |_||_|___| |_|  |_|___|_|  |_|\___/|_|_\ |_|    \___/|_|   |___|_|_|\___/|_|\_|_|  |_/_/ \_\_|\_|
                                                                                                                   
{attr(0)}                                                         
""")

t.sleep(1)

# One time initialization
engine = pyttsx3.init()
F_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
M_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
currentTime = datetime.datetime.now()
client = wolframalpha.Client('QAEXLK-RY9HY2PHAT')

# colors for texts.

gold = fg(226)
orange = fg(202)
green = fg(46)
orange_4b = fg(94)

# attributes for texts.

bold = attr(1)
reset = attr(0)

# Set properties _before_ you add things to say
# engine.setProperty('rate', 180)  # Speed percent (can go over 100)
# engine.setProperty('volume', 0.8)  # Volume 0-1
engine.setProperty('voice', M_voice_id)


def speak(audio):
    engine.say(audio)
    print(f'{orange}{bold}Edith: {str(audio)}{reset}')
    engine.runAndWait()


def mute():
    global listen
    r = sr.Recognizer()
    while listen is False:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)  # Eliminating the noise.
            r.pause_threshold = 1
            audio = r.listen(source, timeout=20, phrase_time_limit=10)
        try:
            query = r.recognize_google(audio).lower()  # Converting speech to text
            if query == "start":
                listen = True
                speak("Voice mode activated")
                break
            else:
                continue
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Uh oh! Sorry sir Couldn't understand my brains not feeling so good can't get a connection.")
        except KeyboardInterrupt:
            pass
    return listen


def command():
    global listen
    r = sr.Recognizer()
    query = ""
    listen = True
    while listen is True:
        with sr.Microphone() as source:
            print("Listening.....")
            r.adjust_for_ambient_noise(source)  # Eleminating the noise.
            r.pause_threshold = 1
            audio = r.listen(source, timeout=20, phrase_time_limit=10)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"{green}{bold}You said: {query}{reset}")

        except sr.UnknownValueError:
            print("I didn't get it...what was that..")
        except sr.RequestError:
            speak("Uh oh! Sorry sir Couldn't understand my brains not feeling so good can't get a connection.")
        except KeyboardInterrupt:
            pass
        except Exception as ie:
            print(ie)
            speak("Say that again please...")
            return "None"
        return query


def greetings():
    if currentTime.hour < 12:
        speak('Good morning.')
    elif 12 <= currentTime.hour < 16:
        speak('Good afternoon.')
    else:
        speak('Good evening.')
    speak("welcome back!!...This is EDITH")
    t.sleep(0.5)
    speak("how may i help you")


def time():
    time_ = currentTime.strftime("%I:%M")
    speak(time_)


def date():
    year = int(currentTime.year)
    month = int(currentTime.month)
    date_ = int(currentTime.day)
    speak(date_)
    speak(month)
    speak(year)


def sys_fun(func):
    if func == "shutdown":
        os.system("shutdown /s /t 1")
    elif func == "logout":
        os.system("shutdown -l")
    elif func == "restart":
        os.system("shutdown /r /t 1")


def random_alphaNumeric(st_len=5):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for _ in range(st_len)))


def screenshot():
    img = pyautogui.screenshot()
    speak("what should i name it.. Say Random to choose a random name.")
    ss_name = command()
    if ss_name == "random":
        ran_name = random_alphaNumeric()
        speak(f"screen shot is named as {ran_name}")
        img.save(f"edith.ss/{ran_name}.png")
    else:
        speak(f"screen shot is name as {ss_name}")
        img.save(f"edith.ss/{ss_name}.png")
    return


def sys_status():
    usage = str(psutil.cpu_percent())
    speak(f'CPU is at {usage} %')
    battery = str(psutil.sensors_battery().percent)
    speak(f"Battery is at {battery} %")


def jokes():
    speak(pyjokes.get_joke())


def social(sc_me):
    speak(f'okay. opening {sc_me}')
    wb.open(f'www.{sc_me}.com')


def hlp():
    head = fg(44)
    cmd = fg(48)
    ed = f"{orange_4b}{bold}Talk to EDITH{reset}"
    print(f'''{orange_4b}{bold}
           
                                    +=======================================+
                                    |......EDITH VIRTUAL INTELLIGENCE.......|
                                    +---------------------------------------+
                                    |#Author: Theforgotensoul               |
                                    |#Date: **********                      |
                                    |#I don't take responsibility for       |
                                    | problems of any kind                  |
                                    |#Use at your own risk                  |
                                    +---------------------------------------+
                                    |......EDITH COMMANDS LISTS.............|
                                    +=======================================+
        
            
                {head}{bold}Converses, barely.
                {ed} : {cmd}{bold}"hello / hi",
                                "Who is iron man?", 
                                "who are you / What does EDITH stand for / what is edith?"

                {head}{bold}Music: Play, Pause, Open:
                {ed} : {cmd}{bold}play music

                {head}{bold}Time and Date:
                {ed} : {cmd}{bold}what time is it?or time , what is today date or simply date

                {head}{bold}Gives a system status:
                {ed} : {cmd}{bold}how are you? / System report / System Status

                {head}{bold}Open programs and drives or folders:
                {ed} : {cmd}{bold}open chromium / open firefox / open calculator / open vlc/ Desktop/ Take me home

                {head}{bold}Standard replies for silly questions:
                {ed} : {cmd}{bold}you are dumb{orange_4b}
                EDITH : {cmd}{bold}I don't understand that yet. Maybe you could teach me.
                {ed} : {cmd}{bold}no I won't{orange_4b}
                EDITH : {cmd}{bold}I don't know how to answer that. Maybe I could interest you in something else.

                {head}{bold}Quit th program:
                {ed} : {cmd}{bold}exit / quit / bye / goodbye


                             {gold}{bold} "END OF HELP COMMAND" {reset}
    ''')


if __name__ == "__main__":
    greetings()
try:
    while True:
        data = command().lower()

        # HELP COMMAND *************-----------------------------------****************-----------------------------*********

        if "help" in data or "commands" in data:
            listen = False
            speak("showing available commands")
            hlp()
            speak('going mute')
            speak("Say start to start listening")
            print(f'''{gold}{bold}

                                        𝚂𝚊𝚢 "𝚜𝚝𝚊𝚛𝚝" 𝚝𝚘 𝚜𝚝𝚊𝚛𝚝 𝚕𝚒𝚜𝚝𝚎𝚗𝚒𝚗𝚐

                        {reset}''')
            mute()

        # Converses, barely.**************-------------************-------------------*************---------------*****

        elif 'hello' in data or 'hi' in data:
            speak('Well! Hello. How are you?')

        elif 'thanks' in data or 'tanks' in data or 'thank you' in data:
            msgs = ['You are welcome', 'no problem']
            speak(random.choice(msgs))

        elif 'how are you' in data or 'and you' in data or 'are you okay' in data:
            st_Msg = ['Just doing my thing!', 'I am fine!. Thank you', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(st_Msg))

        elif "who are you" in data or "what is edith" in data or "edith stand for" in data or "what is edith" in data:
            speak("I am Edith. EDITH is the abbreviation of EVEN DEATH I AM HERO. I am the "
                  "clone of original edith created by Iron-man.")

        elif "your name" in data:
            speak("Iam EDITH")
            print(f"{gold}{bold}   EDITH     {reset}")

        # Time and Date ************-----------------------------********************-------------------**********

        elif "time" in data:
            time()

        elif "date" in data:
            date()

        # remembers when we asked edith to remember something ***********-------------***********----------********

        elif 'remember that' in data:
            speak("What should I remember?")
            rem = command()
            speak("you said me to remember that " + rem)
            remember = open('data.txt', 'w')
            remember.write(rem)
            remember.close()

        # tells if edith remembers anything we asked it remember **********----------------************--------******

        elif 'do you know anything' in data:
            remember = open('data.txt', 'r')
            speak("you said me to remember that " + remember.read())

        # plays music *************---------------******************-----------------**********--------*************

        elif 'play music' in data:
            music_folder = "Your_music_folder_path"
            music = "[music1, music2, music3, music4, music5]"
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')

        # wikipedia does math function functions opens social media apps *******--------------********-------********
        elif 'wikipedia' in data or "wiki" in data:
            speak('searching...')
            data = data.replace('wikipedia', '')
            result = wikipedia.summary(data, sentences=2)
            speak(result)

        elif "do math" in data or "math" in data:
            speak("what do yo want me to do....")
            data = command().lower()
            if data == "":
                pass
            else:
                res = client.query(data)
                results = next(res.results).text
                speak(f'{results}')

        elif 'open youtube' in data:
            social("youtube")
        elif 'open facebook' in data:
            social("facebook")
        elif 'open instagram' in data:
            social("instagram")

        elif 'search' in data:
            speak("what should i search")
            search = command().lower()
            wb.open_new(f'https://duckduckgo.com/{search}')
            speak(f"showing results for {search}")

        # takes a screen shot ****************-----------------------***************----------------**********

        elif 'screenshot' in data:
            screenshot()
            speak("Done!")

        # Gives a system status ************--------------****************--------------**********************

        elif 'system status' in data or 'system report' in data:
            sys_status()

        # TELLS A Joke *****************----------------------****************----------------------**********
        elif 'joke' in data:
            jokes()
            speak("how was the joke")
            jk = command().lower
            if jk == "good" or jk == "okay" or jk == "not bad":
                speak("thank you")
            else:
                speak('get some humor into your life dude...')

        # Sends email **************************-------------------***************---------------**************

        elif 'email' in data:
            speak('Who is the sender? ')
            sender = command()

            if 'I am' in sender:
                try:
                    speak("Please Provide the Email address of Recipient.")
                    Recipient_user = command()
                    t.sleep(2)
                    speak('What should I say? ')
                    content = command()
                    t.sleep(2)
                    speak(content)
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("efgh87933@gmail.com", '@abcd1234')
                    server.sendmail('efgh87933@gmail.com', Recipient_user, content)
                    server.close()
                    speak('Email sent!')

                except Exception as e:
                    print(e)
                    speak('Sorry! I am unable to send your mail at this moment!')

        # Goes to sleeps (stops taking commands)**********-----------*******************------------***************

        elif "mute" in data or "sleep" in data or "stop listening" in data:
            listen = False
            speak("Listening stopped.")
            print(f"{gold}{bold}Listening stopped. {reset}")
            speak("Say start to start listening")
            print(f'''{gold}{bold}

                            𝚂𝚊𝚢 "𝚜𝚝𝚊𝚛𝚝" 𝚝𝚘 𝚜𝚝𝚊𝚛𝚝 𝚕𝚒𝚜𝚝𝚎𝚗𝚒𝚗𝚐

            {reset}''')
            mute()

        # Standard replies for silly questions: ************-----------*************------------*****************

        elif "you are dumb" in data:
            msgs = ["I don't understand that yet. Maybe you could teach me.",
                    "I don't know how to answer that. Maybe I could interest you in something else."]
            speak(random.choice(msgs))

        # performs system operations **********-------------------******************---------------***************

        elif "shutdown" in data or "logout" in data or "restart" in data:
            speak(f"Your asking for a complete system {data} operation")
            speak("Are you sure!!!")
            ques = command().lower()
            if "yes" in ques:
                speak("which system function do u want to perform. Logout. restart. shutdown")
                fun = command()
                sys_fun(fun)
            else:
                pass

        # exits the program ************-----------------******************----------------***********************

        elif "offline" in data or "goodbye" in data or "bye" in data:
            if currentTime.hour < 17:
                speak("Have a nice day!!.. Bye")
            elif 17 > currentTime.hour <= 21:
                speak("Have a nice evening!!... Bye")
            elif currentTime.hour > 21:
                speak("Okay... Good night... Bye")
            else:
                pass
            speak('EDITH powering off in 3, 2, 1, 0')
            exit()

        # search internet for random things *************-----------*************------------------****************

        # else:
        #     speak("sorry i did not know the answer to that. Should i google it...")
        #     data = command().lower()
        #     if data == "yes":
        #         wb.open_new(f"www.duckduckgo.com/{data}")
        #         speak("Right away, Created new window in existing browser session.")

except Exception as e:
    print(e)
