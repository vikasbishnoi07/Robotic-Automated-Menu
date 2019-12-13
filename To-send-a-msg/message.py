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

form=cgi.FieldStorage()
num=form.getvalue("q")
msg=form.getvalue("w")


s.send("msg".encode())
s.send(num.encode())
t1=s.recv(20)
print(t1)
time.sleep(3)
s.send(msg.encode())
t2=s.recv(20)
print(t2)

speaker.say("Your Message Sent Successfully")
speaker.runAndWait()
