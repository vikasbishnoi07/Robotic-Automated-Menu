# coding: utf-8

# In[ ]:



def speak(x):
    
    import pyttsx3
    engine=pyttsx3.init()
    engine.say(x)
    engine.runAndWait()


# In[ ]:




# In[ ]:


def send(cmd):
    import subprocess as sp
    import socket
    s=socket.socket()
    s.connect(("192.168.43.112",1235))
    s.send(cmd)


# In[ ]:



    


# In[ ]:





# In[ ]:


# In[ ]:


 
 
def ping(a):
    import subprocess
    b=[]
    j=0
    for i in a:
        ping = subprocess.getstatusoutput('ping {} -c 2 '.format(a[j][0]))
        if ping[0] == 0:
            b.append(i)
        else :
            print("{} ip is not reachable . Do you still want to add this y/n".format(a[j][0]))
            speak("{} ip is not reachable . Do you still want to add this y/n".format(a[j][0]))
            kuch=input('')
            if kuch == 'y':
                b.append(i)
            else:
                pass
        j=j+1
    return(b)


# In[ ]:


import subprocess as sp
import socket
s=socket.socket()
import pickle
import getpass
import time
    print("Here is the list of task system can perform")
    print("""
    1. Start HADOOP HDFS Cluster.
    2. Start HADOOP M-R Cluster.
    3. Setup NameNode (Master).
    4. Setup Data Nodes.
    5. Setup Job Tracker. 
    6. Setup Task Trackers.
    7. RESET HADOOP CLUSTERS.
    8. EXIT.
    """)
    namenodeon=0
    jton=0
 
    
    while True:
        print('choose what you want to do')
        speak('choose what you want to perform out of following')
        what_to_do=input('')
        print(what_to_do)
        ips=[]
        
        if '1' in what_to_do or 'one' in what_to_do:
            if namenodeon==1 :
                send('1'.encode())
            else :
                print("first setup hadoop master")
            
            
        if '2' in what_to_do or 'two' in what_to_do:
            if jton==1 :
                
                send('2'.encode())
            else :
                print("first setup hadoop master")
            
        
        
        if '3' in what_to_do or 'three' in what_to_do or 'third' in what_to_do:
            extra=[]
            print('please provide us with ip and password of system you want to add as master ')
            speak('please provide us with ip and password of system you want to add as master ')
            print('Enter your ip:')
            ip_firsttime=input('')
            ip_password=getpass.getpass("enter your password")
            extra.append(ip_firsttime)
            extra.append(ip_password)
            ips.append(extra)
            final_ips=ping(ips)
            namenodeon=1
            print(final_ips)
            send(b'3')
            
            send(pickle.dumps(final_ips))
        
        
        if '4' in what_to_do or 'four' in what_to_do:
            extra=[]
            print('please provide us with ip and password of system you want to add as slave ')
            speak('please provide us with ip and password of system you want to add as slave ')
            print('Enter your ip:')
            while True:
                print("enter ip and password of slave you want to add")
                ip_firsttime=input('')
                ip_password=getpass.getpass("enter your password")
                extra.append(ip_firsttime)
                extra.append(ip_password)
                ips.append(extra)
                extra=[]
                print("Do you want to add more slave y/n")
                speak("Do you want to add more slave")
                add_more_slave=input('')
                if add_more_slave=='y':
                    pass
                elif add_more_slave=='n':
                    break
                
            final_ips=ping(ips)
            print(final_ips)
            
            send(b'4')
        
            send(pickle.dumps(final_ips))
            
        if '5' in what_to_do or 'five' in what_to_do:
            extra=[]
            print('please provide us with ip and password of system you want to add as job tracker ')
            speak('please provide us with ip and password of system you want to add as job tracker ')
            print('Enter your ip:')
            ip_firsttime=input('')
            ip_password=getpass.getpass("enter your password")
            extra.append(ip_firsttime)
            extra.append(ip_password)
            ips.append(extra)
            jton=1
            final_ips=ping(ips)
            print(final_ips)
            
            send(b'5')
            time.sleep(0.5)
            send(pickle.dumps(final_ips))
        
        if '6' in what_to_do or 'six' in what_to_do:
            extra=[]
            print('please provide us with ip and password of system you want to add as task tracker ')
            speak('please provide us with ip and password of system you want to add as task tracker ')
            print('Enter your ip:')
            while True:
                print("enter ip and password of task tracker you want to add")
                ip_firsttime=input('')
                ip_password=getpass.getpass("enter your password")
                extra.append(ip_firsttime)
                extra.append(ip_password)
                ips.append(extra)
                extra=[]
                print("Do you want to add more task tracker y/n")
                speak("Do you want to add more task tracker")
                add_more_slave=input('')
                if add_more_slave=='y':
                    pass
                elif add_more_slave=='n':
                    break
                
            final_ips=ping(ips)
            print(final_ips)
            send(b'6')
            send(pickle.dumps(final_ips))
            
            
        if '7' in what_to_do or 'seven' in what_to_do:
            send(b'7')    
            
        if '8' in what_to_do or 'eight' in what_to_do:
            break
            
        
      
