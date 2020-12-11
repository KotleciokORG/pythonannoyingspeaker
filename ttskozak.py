import pyttsx3,os
engine = pyttsx3.init()
engine.setProperty("rate", 250)

txt = "Jebac skrinta Jebac skrinta Jebac skrinta Jebac skrinta Jebac skrinta Jebac skrinta "

for i in range(10):
    engine.say(txt)
    engine.runAndWait()
    