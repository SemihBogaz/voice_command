import speech_recognition as sr
from os import system as command
import voice_command.shrink as func

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    command("cls")
    print("Say something!")
    audio = r.listen(source)
flag = False

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio, language="eng")
    print("You said: " + text)
    flag = True
    text = func.lower(text)

    with open("speech.txt", 'w') as file:
        file.write(text)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

if flag:
    if text == "hesap makinesi":
        command("calc")
