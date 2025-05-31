import speech_recognition as sr
import pyttsx3
import webbrowser as web
import os
import musiclinks

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# function to speak
def speak(text) :
    print(f"Nexo : {text}") 
    engine.say(text)
    engine.runAndWait()

# function to process commands
def processCommand(command) : 

    # open from browsers

    if "open google" in command.lower() :
        web.open("https://google.com")

    elif "open gmail" in command.lower() :
        web.open("https://gmail.com")

    elif "open facebook" in command.lower() :
        web.open("https://facebook.com")

    elif "open insta" in command.lower() :
        web.open("https://instagram.com")

    elif "open linkedin" in command.lower() :
        web.open("https://linkedin.com")

    elif "open youtube" in command.lower() :
        web.open("https://youtube.com")

    elif "open spotify" in command.lower() :
        web.open("https://spotify.com")

    elif "open twitter" in command.lower() :
        web.open("https://twitter.com")

    elif "open github" in command.lower() : 
        web.open("https://github.com")

    # Opening system Apps

    elif "open chrome" in command.lower() :
        os.system("start chrome")

    elif "open notepad" in command.lower() : 
        os.system("notepad.exe")

    elif "open wordpad" in command.lower() :
        os.system("start write")

    elif "open paint" in command.lower() : 
        os.system("calculator.exe")

    elif "open paint" in command.lower() or "open mspaint" in command.lower():
        os.system("start mspaint")

    elif "open excel" in command.lower():
        os.system("start excel")

    elif "open word" in command.lower():
        os.system("start winword")

    elif "open powerpoint" in command.lower():
        os.system("start powerpnt")

    elif "open vs code" in command.lower() : 
        os.system("code")

    # playing songs from Youtube

    elif command.lower().startswith("play") : 
        songname = command.lower().split(" ")[1]
        song = musiclinks.links[songname]
        web.open(song)

    else :
        speak(f"Sorry can't process your command")



# Main code - for any type of command first call "Nexo" then provide the command

speak("Initializing Assistant...")
while True : 
    print("Recognizing...")
    try : 
        with sr.Microphone() as source : 
            print("Listening...")
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

        command = recognizer.recognize_google(audio)
        print(f"Heard: {command}")

        if(command.lower() == "nexo") : 
            speak("Yeah")
            with sr.Microphone() as source : 
                print("Nexo Active...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)

                processCommand(command)
    
    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase.")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e : 
        print("Error : {0}".format(e))
