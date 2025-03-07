import cowsay
import pyttsx3

engine = pyttsx3.init()
something = input("Say something  ")
cowsay.trex(something)
engine.say(something)
engine.runAndWait()