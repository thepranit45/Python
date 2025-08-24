# install any external python module of your intrest
# pyttsx3 module is used to convert text to speak 
import pyttsx3
sentence='''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night'''
texttospeak=pyttsx3.speak(sentence)
# OR
sentence2=pyttsx3.init()
sentence2.say("hello")
sentence2.runAndWait()