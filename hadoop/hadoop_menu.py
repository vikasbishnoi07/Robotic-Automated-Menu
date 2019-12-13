#!/usr/bin/python36
print("content-type: text/html")
print()
def speak(x):
#       import speech_recognition as sr 
        import pyttsx3
#       import pyaudio
        engine=pyttsx3.init()                                                                                          
        engine.say(x)                                                                                                  
        engine.runAndWait()                                                                                            
import getpass
import subprocess as sp
import hadoop
import ansiblehost
import pickle
import host
def ping(a):
    import subprocess as sp
    b=[]                                                                                                               
    j=0
    for i in a:
         x = sp.getstatusoutput('ping -c 2 {} '.format(a[j][0]))
                                                                                                                       
         if x[0] == 0:
            b.append(i)                                                                                                
            print("succesfully added!\n")                  
         else :                                                                     
            pass
         j=j+1
    return(b)                                                                                       
print("Here is the list of task system can perform")
print("""           1. Start HADOOP HDFS Cluster.
           2. Start HADOOP M-R Cluster.
           3. Setup NameNode (Master).
           4. Setup Data Nodes.
           5. Setup Job Tracker. 
           6. Setup Task Trackers.
           7. EXIT.
 """)                                                                                                             
namenodeon=0
jton=0
while True:
        print('choose what you want to do ',end= ' ')
        speak('choose what you want to perform out of following')
        what_to_do=input('')
        ips=[]
        if '1' in what_to_do or 'one' in what_to_do:
            if namenodeon==1 :
                hadoop.hadooprunmaster()                                                                               
                hadoop.hadooprunslave()                                                                                
            else :
                print("first setup hadoop master")
        if '2' in what_to_do or 'two' in what_to_do:
            if jton==1 :
                hadoop.hadooprunjt()                                                                                   
                hadoop.hadoopruntt()                                                                                   
            else :
                print("first setup hadoop master")
        if '3' in what_to_do or 'three' in what_to_do or 'third' in what_to_do:
            extra=[]
            print('please provide us with ip and password of system you want to add as master ')
            speak('please provide us with ip and password of system you want to add as master ')
            print('Enter your ip:',end=' ')
            ip_firsttime=input('')
            ip_password=getpass.getpass("enter your password" )
            extra.append(ip_firsttime)                                                                                 
            extra.append(ip_password)                                                                                  
            ips.append(extra)                                                                                          
            final_ips=ping(ips)                                                                                        
            namenodeon=1
            host.master(ips)                                                                                           
            ansiblehost.master(ips)                                                                                    
            hadoop.hadoopsetmaster()
        if '4' in what_to_do or 'four' in what_to_do:
            extra=[]                                                                                                   
            print('please provide us with ip and password of system you want to add as slave ')
            speak('please provide us with ip and password of system you want to add as slave ')
            print('Enter your ip:',end=' ')
            while True:
                print("enter ip and password of slave you want to add",end=' ')
                ip_firsttime=input('')
                ip_password=getpass.getpass("enter your password")
                extra.append(ip_firsttime)                                                                             
                extra.append(ip_password)                                                                              
                ips.append(extra)                                                                                      
                extra=[]                                                                                               
                print("Do you want to add more slave y/n",end=' ')
                speak("Do you want to add more slave")
                add_more_slave=input('')
                if add_more_slave=='y':
                    pass
                elif add_more_slave=='n':
                    break
            final_ips=ping(ips)                                                                                        
            print(final_ips[0][0])
            a=host.slave(ips)                                                                                          
            ansiblehost.slave(ips)                                                                                     
            hadoop.hadoopsetslave()                                                                                    
        if '5' in what_to_do or 'five' in what_to_do:
            extra=[]                                                                          
            prin('please provide us with ip and password of system you want to add as job tracker ',end=' ')
            speak('please provide us with ip and password of system you want to add as job tracker ')
            print('Enter your ip:',end= ' ')
            ip_firsttime=input('')
            ip_password=getpass.getpass("enter your password")
            extra.append(ip_firsttime)                                                                                 
            extra.append(ip_password)                                                                                  
            ips.append(extra)                                                                                          
            jton=1
            final_ips=ping(ips)                                                                                        
            print(final_ips[0][0])
            a=host.jt(ips)                                                                                             
            ansiblehost.jt(ips)                                                                                        
            hadoop.hadoopsetjt()                                                                                       
        if '6' in what_to_do or 'six' in what_to_do:
            extra=[]                                                                                                   
            print('please provide us with ip and password of system you want to add as task tracker ',end= ' ')
            speak('please provide us with ip and password of system you want to add as task tracker ')
            print('Enter your ip:',end=' ')
            while True:
                print("enter ip and password of task tracker you want to add",end=' ')
                ip_firsttime=input('')
                ip_password=getpass.getpass("enter your password")
                extra.append(ip_firsttime)                                                                             
                extra.append(ip_password)                                                                              
                ips.append(extra)                                                                                      
                extra=[]                                                                                               
                print("Do you want to add more task tracker y/n",end=' ')
                speak("Do you want to add more task tracker")
                add_more_slave=input('')
                if add_more_slave=='y':
                    pass
                elif add_more_slave=='n':
                    break
            final_ips=ping(ips)                                                                                        
            a=host.tt(ips)                                                                                             
            ansiblehost.tt(ips)                                                                                        
            hadoop.hadoopsettt()                                                                                       
        if '7' in what_to_do or 'seven' in what_to_do:
            break
