import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import subprocess
import os
import openai


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occured in speech recognition!"


def ai(content):
    text = f"OpenAI response for Prompt: {content}\n\n"
    openai.api_key = '''YOUR API KEY'''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["message"]["content"]
    if not os.path.exists('Responses'):
        os.mkdir("Responses")
    
    with open(f"Responses/{''.join(content).strip()}.txt", "w") as f:
        f.write(text)


def ai_chatBot(content):
    openai.api_key = '''YOUR API KEY'''
        
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    print(f"A.I Responded : {response['choices'][0]['message']['content']}")
    say(response['choices'][0]['message']['content'])


if __name__ == '__main__':
    print('Execution Started')
    say('Welcome!')
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [
            ["youtube", "https://www.youtube.com"],
            ["google", "https://www.google.com"]
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
        
        if "Show time".lower() in query.lower():
            currentTime = datetime.datetime.now().strftime("%H Hours : %M Minutes : %S Seconds")
            say(f"The current time is {currentTime}")

        apps = [
            ["chrome", "C:/Program Files/Google/Chrome/Application/chrome.exe"],
            ["VS Code", "C:/Users/Kushal Gupta/AppData/Local/Programs/Microsoft VS Code/Code.exe"],
            ["Word", "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"] 
        ]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]}")
                subprocess.call({app[1]})
                #os.system(f"open {app[1]}")

        if "exit".lower() in query.lower():
            say("Exitting the program")
            exit()

        if "use GPT".lower() in query.lower():
            say("Shifted to Chat GPT Mode")
            while True:
                query = takeCommand()
                if 'exit GPT'.lower() in query.lower():
                    say("Shifting back to Desktop Assistance Mode")
                    say('Welcome Back!')
                    break
                if '' or 'Some error occured in speech recognition!'.lower() in query.lower():
                    continue
                ai(content = query)
                say("Task completed!")


        if "Start AI Chat".lower() in query.lower():
            say("Connected to AI Chat Bot")
            while True:
                query = takeCommand()
                if "Quit AI Chat".lower() in query.lower():
                    say("Shifting back to Desktop Assistance Mode")
                    say('Welcome Back!')
                    break
                ai_chatBot(content = query)
            
