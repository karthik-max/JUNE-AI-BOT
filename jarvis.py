import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import time
import requests
from covid import Covid
from textblob import TextBlob

from GoogleNews import GoogleNews




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)







def convert(c):
    f=(c*9/5)+32
    return float(f)
    
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")
    speak("I am June How May I Help You")
    
    
def input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...............")
        r.energy_threshold=200
        r.pause_threshold = 0.6
        audio=r.listen(source)
        
        try:
            print("Recognizing............")
            query=r.recognize_google(audio,language='en-in')
            print(f"Boss Said:{query}\n")
            
        except Exception as e:
            print(e)
            print("Could you repeat boss")
            return "none"
    return query

                    
        
if __name__ == "__main__":   
    wish()
    while True:
        query = input().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia Boss")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)   
            
        elif 'introduce yourself' in query:
            demo = "Hello My name is June"
            speak(demo)
            demo = demo.replace("Hello My name is June","")
            time.sleep(0.25)
            
            demo="I am an AI Assistant Bot"
            speak(demo)
            demo = demo.replace("I am an AI Assistant Bot", "")
            time.sleep(0.25)
            
            demo="How may I Help you"
            speak(demo)
            demo = demo.replace("How may I Help you", "")
            time.sleep(0.25)
            
        elif 'introduce your dad' in query:
            
            demo="My dads name is karthik" 
            speak(demo)
            time.sleep(0.5)
            
            demo = "he built me"
            speak(demo)
            time.sleep(0.5)
            
            demo="He is studying in A J Institute of Engineering an Technology Mangalore"
            speak(demo)
            time.sleep(0.5)
            
            demo = "With Computer Science as his Stream"
            speak(demo)
            time.sleep(0.5)
            
            demo = "He is also a Member of Students Association Called ENIGMA"
            speak(demo)
            time.sleep(0.5)
            
            demo = "He has Done a diploma Course in animation and VFX"
            speak(demo)
            time.sleep(0.5)
                 
            demo = "Some of his hobbies are"
            speak(demo)
            time.sleep(0.5)
            
            demo = "Playing Guitar"
            speak(demo)
            time.sleep(0.5)
            
            demo = "Editing"
            speak(demo)
            time.sleep(0.5)
            
            demo = "Stock Market Trading"
            speak(demo)
            time.sleep(0.5)
            
        elif 'who is your dad' in query:
            demo="I don't know Who is my dad"
            speak(demo)
            time.sleep(0.25)
            
            demo="But Karthik is my Creator"
            speak(demo)
            time.sleep(0.25)
            
            demo = "So He is My Dad"
            speak(demo)
            time.sleep(0.25)
        
        elif 'video search' in query: 
            vdemo=query.split(" ",2)[2]
            print(vdemo)
            webbrowser.open('https://www.youtube.com/results?search_query='+vdemo)
            
        elif 'open youtube' in query:
            speak("opening")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("opening")
            webbrowser.open("Google.com")
        
        elif 'open department' in query:
            speak("opening")
            webbrowser.open("https://www.ajiet.edu.in/pages/dept.php")
        
        elif 'open github' in query:
            speak("opening")
            webbrowser.open("github.com")
            
        elif "search" in query:
            find=query.split(' ',1)[1]
            try:
                url = "https://www.google.co.in/search?q="
                webbrowser.open(url+find)
            except:
                speak("cannot Recognize")
                
        elif "make me laugh" in query:
            url = "https://www.memedroid.com/"
            webbrowser.open(url)
        
        elif  'play music' in query:
            dir='D:\\my music\\new folder'
            song=os.listdir(dir)
            rand = random.randint(0,len(song)-1)
            os.startfile(os.path.join(dir,song[rand]))
            if 'stop' in query:
                os.close()
        
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strtime}")
        
        elif 'thank' in query:
            demo="Your Welcome Boss"
            speak(demo)
        
        elif 'resume' in query:
            speak("opening Resume")
            dir='E:\\karthik files\\resume'
            resume=os.listdir(dir)
            os.startfile(os.path.join(dir,resume[0]))
            
        elif 'open android studio' in query:
            speak("opening android studio")
            loc = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(loc)
            
        elif 'open code' in query:
            speak("opening Visual Studio Code ")
            loc = "C:\\Users\\Karthik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(loc)  
            
        elif 'quit' in query:
            speak("OK Boss")
            break
        
        elif 'open facebook' in query:
            speak("opening")
            webbrowser.open("facebook.com")
            
        elif 'open whatsapp' in query:
            speak("opening")
            webbrowser.open("https://web.whatsapp.com/")
        
        elif 'open Stackoverflow' in query:
            speak("opening")
            webbrowser.open("stackoverflow.com")
            
        elif 'weather in' in query:
            city=query.split(" ",2)[2]
            url = "https://openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02".format(city)
            res=requests.get(url)
            output=res.json()
            
            weather_stat=str(output['weather'][0]['description'])
            temp=convert(int(output['main']['temp']))
            feels=convert(int(output['main']['feels_like']))

            
            press=str(output['main']['pressure'])
            wind_speed=str(output['wind']['speed'])
            speak(f"Sir in {city}")
            time.sleep(.025)
            speak(f"the weather status is {weather_stat}")
            time.sleep(0.5)
            speak(f"with temperature of, {temp} fahrenheit")
            time.sleep(0.5)
            speak(f"but it feels like the temperature is, {feels} fahrenheit ")
            speak(f"pressure of, {press} pascals")
            time.sleep(0.5)
            speak(f"wind speed of, {wind_speed} knots")
            
            
        elif 'get' in query:
            url=query.split(" ",1)[1]
            googlenews=GoogleNews
            googlenews=GoogleNews('en')
            googlenews=GoogleNews(period='d')
            googlenews.search(url)
            googlenews.getpage(1)
            googlenews.result()
            news=googlenews.gettext()
            speak(news)
            
        elif 'say hello to' in query:
            hello=query.split(" ",3)[3]
            speak(f"hello {hello}, have a great day")
            
        elif 'covid in' in query:
            country=query.split(" ",2)[2]
            covid=Covid()
            str=covid.get_status_by_country_name(country)
            speak("Live Updates on Corona Virus")
            time.sleep(0.25)
            speak(str)
            time.sleep(0.25)
            speak("Stay Home and break the corona link") 
            
        elif 'analyse my mood' in query:
            a_sentiment=0
            a_subjectivity=0
            speak("sir, could you Describe how was your day in one statement")  
            statement=str(input())
            blob=TextBlob(statement)
            a_sentiment+=blob.sentiment.polarity/len(statement)
            a_subjectivity+=blob.sentiment.subjectivity/len(statement)
            speak("sir")
            a_subjectivity=round(a_sentiment,4)
            a_sentiment=round(a_subjectivity,4)
            print(a_sentiment)
            print(a_subjectivity)
            speak(f"The Sentiment Value of the statement seems to be {a_sentiment}, and")
            speak(f"The Subjectivity value of your statement seems to be {a_subjectivity}")
            if a_sentiment < 0.00:
                speak("so you might have had a bad day, sorry to hear that")
            elif a_sentiment > 0.00:
                speak("You are having a good day, happy to hear")
            else:
                speak("the day seems to be normal")
        
        else:
            speak("I dont know how to do that")
    
    
    
