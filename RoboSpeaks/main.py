import pyttsx3

text_speech = pyttsx3.init()
answer = input("Enter what you want to say: ")
text_speech.say(answer)
text_speech.runAndWait()