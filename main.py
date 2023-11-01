"""import wikipedia
infoTopic = input("Enter your topic(please be specific):")

print (wikipedia.summary(infoTopic))

tryit = input("Do you want to perform a manual search? (y/n)")
a = 'y'

if tryit == a:
    print("Program Initiated")
    time.sleep(2)
    pyautogui.click(1149, 1051)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(3)
    pyautogui.write(infoTopic)
    pyautogui.keyDown("enter")
else:
    print("Thanks for your query!!
import wikipedia

def summarize_wikipedia_page():
    topic = input("Enter your topic(please be specific): ")
    summary = wikipedia.summary(topic)
    sentences = summary.split('. ')
    summary_4_sentences = '. '.join(sentences[:4]) + '.'
    return summary_4_sentences

print(summarize_wikipedia_page())
import wikipedia

def summarize_wikipedia_page():
    topic = input("Enter your topic(please be specific): ")
    try:
        summary = wikipedia.summary(topic)
        sentences = summary.split('. ')
        summary_4_sentences = '. '.join(sentences[:4]) + '.'
        return summary_4_sentences
    except wikipedia.exceptions.PageError:
        return "Invalid topic. Please try another topic."

print(summarize_wikipedia_page())
import pyttsx3
pyttsx3. init()
text = ("Hello World")
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()"""

import pyttsx3
pyttsx3.speak("Oh wow! It's amazing I got this to work in just one line of code")