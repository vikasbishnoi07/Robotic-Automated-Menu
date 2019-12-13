#!C:/anaconda/python.exe


print("content-type:text/html")
print()

import socket
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import requests
import cgi
import cgitb
import subprocess as sp
import os






form=cgi.FieldStorage()
Account = form.getvalue("q")
Register = form.getvalue("w")
if "NO" in Account:
    if "YES" in Register:
        os.system("python Recognize_Face.py")
        redirectURL = "http://localhost/pythoncode/auth.py"
        print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')

if "YES" in Account:
    if "NO" in Register:
        os.system("python Face_Detection.py")
        print()
