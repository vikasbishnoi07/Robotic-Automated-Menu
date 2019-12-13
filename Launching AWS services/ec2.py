#!C:/anaconda/python.exe


import socket
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import requests
import cgi
import cgitb
import time


# In[ ]:


print("content-type:text/html")
print()

cgitb.enable()

s = socket.socket()

s.connect(("192.168.43.217",4567))


speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)



s.send("ec2".encode())
print("ec2 launched successfully")
speaker.say("ec2 instance launched successfully")
speaker.runAndWait()
