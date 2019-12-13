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
email=form.getvalue("q")
sub=form.getvalue("w")
body=form.getvalue("e")

s.send("mail".encode())
time.sleep(5)
s.send(email.encode())
time.sleep(2)
t1=s.recv(30)
print(t1)
s.send(sub.encode())
time.sleep(2)
t2=s.recv(30)
print(t2)
s.send(body.encode())
time.sleep(2)
t3=s.recv(30)
print(t3)

speaker.say("Email Sent Successfully")
speaker.runAndWait()
