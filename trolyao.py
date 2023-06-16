#thu vien noi 
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import asyncio as asy
import python_weather as we
bot = pyttsx3.init()
voice = bot.getProperty('voices')
#chon giong noi
bot.setProperty('voices',voice[0].id)
# ham noi
def speak(audio):
    print(audio)
    bot.say(audio)
    bot.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good morning boss")
    elif hour >=12 and hour <18:
        speak("Good afternoon boss")
    elif hour >=18 and hour <24:
        speak("Good evening boss")
    speak("how can i help you")
async def weather():
    async with we.Client(format=we.IMPERIAL) as client:
        city = "Ho Chi Minh"
        weather = await client.get(city)
        speak(f"The current temperature in {city} is {weather.current.temperature} degrees Fahrenheit")

def command():
    """c=sr.Recognizer()
    with sr.Microphone() as source:
    c.pause_threshold=1
    input=c.input()"""
#voice
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=1
        audio=c.listen(source)
    try:
       query=c.recognize_google(audio,language='en')
       print("Minh Tri :" + query)
    except sr.UnknownValueError:
       print("Please repeat or typing the command")
       query=str(input('Your oder is : '))
       return query
#input
"""def command():
    speak("Please enter your command")

    query = str(input('Your order is: '))
    return query"""
if __name__ =="__main__" :
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("what should I search boss?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"here is your {search} on google")
        elif "youtube"in query:
            speak("what should I search boss?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"here is your {search} on youtube")
        elif "time" in query:
            time()
        elif "4"in query:
            asy.run(weather())
        elif "quit" in query:
            speak("Lor.Bot is quitting boss goodbye boss")
            quit()
        