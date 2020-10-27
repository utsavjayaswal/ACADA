# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:52:12 2020

@author: utsav
"""


#jaishriganesh
#verifyface module

from deepface import DeepFace
import cv2
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import numpy as np
import pathlib
import os
from datetime import datetime


def markattendance1():
    wd=os.getcwd()
    #master=Tk()
    #master.eval('tk::PlaceWindow %s center' % master.winfo_toplevel())
    #master.withdraw()
    
    pathlib.Path(wd+'\empa').mkdir(parents=True, exist_ok=True)
    pathlib.Path(wd+'\suspects').mkdir(parents=True, exist_ok=True)
    
    face_cascade = cv2.CascadeClassifier('C:/Users/utsav/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    ida=simpledialog.askstring('input id','plz re-enter your id')
    count=0
    while True:
        _,img=cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray, 1.3, 5)
        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            face = img[y:y+h, x:x+w]
            crd1,crd2=x,y
        cv2.putText(img,"Press s to start verification",(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2)
        cv2.imshow('attendance',img)
        #result=DeepFace.verify(face,wd+'\emp/'+ id+'.jpg',model_name='Facenet')
        
               
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(wd+'\empa/'+ ida+'.jpg',face)
            result=DeepFace.verify(wd+'\empa/'+ ida+'.jpg',wd+'\emp/'+ ida+'.jpg',model_name='Facenet',enforce_detection=False)
            #print(result)
            if result["verified"]==True:
                
                messagebox.showinfo('welcome','face verified!attendance marked at:'+str(datetime.now()))
                
                os.remove(wd+'\empa/'+ ida+'.jpg')
                cap.release()
                cv2.destroyAllWindows()
                return 1,ida
                #break
            else:
                messagebox.showinfo('sorry','verification failed..retry...attendance not marked')
                cv2.imwrite(wd+'\suspects/'+ ida+'.jpg',face)
                os.remove(wd+'\empa/'+ ida+'.jpg')
                cap.release()
                cv2.destroyAllWindows()
                return 2,ida
                
                #break
                
            
            
        
#master.deiconify()
#master.destroy()
#master.quit()    
#axa,bxa=markattendance1()    
#print(axa,bxa)

