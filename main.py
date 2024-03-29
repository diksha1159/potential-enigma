import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from bs4 import BeautifulSoup


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

def get_weather(city):
    try:
        # Construct the URL to search for weather in the specified city
        url = f'https://www.google.com/search?q=weather+in+{city}'
        
        # Make an HTTP request to fetch the weather information
        response = requests.get(url)
        
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the temperature information from the parsed HTML
        temperature = soup.find('div', class_='BNeawe').text
        
        # Return the weather information
        return f"The weather in {city} is {temperature}."
    except Exception as e:
        return f"Sorry, I couldn't fetch the weather information for {city}, is there anything else you would like me to do for you?."

def NewsFromBBC():
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "1f20debee1e043e1bd935f8eac09d02c"
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
    return results


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'weather' in command:
        talk("Which city's weather do you want to know?")
        city = take_command()
        weather_info = get_weather(city)
        talk(weather_info)
    elif 'news' in command:
        talk("Here are the latest news headlines.")
        news_headlines = NewsFromBBC()
        for headline in news_headlines:
            talk(headline)
    else:
        talk('Please say the command again.')


talk("Hi, I am Jarvis. How can I assist you today?")
while True:
    run_jarvis()

 