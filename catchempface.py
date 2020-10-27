# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:15:16 2020

@author: utsav
"""
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import cv2
import os
import numpy as np
import pathlib

def catchempfacefn(id):

    
        
    
    
    #mastera=Tk()
    #mastera.eval('tk::PlaceWindow %s center' % mastera.winfo_toplevel())
    #mastera.withdraw()
        
    
        
    
    
    
    wd=os.getcwd()
    face_cascade = cv2.CascadeClassifier('C:/Users/utsav/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    pathlib.Path(wd+'\emp').mkdir(parents=True, exist_ok=True)
    flag=0
    
    
    
    
    while True:
        _,img=cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray, 1.3, 5)
        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            face = img[y:y+h, x:x+w]
            crd1,crd2=x,y
        cv2.putText(img,"Press 's' to save the face int directory",(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2)
        #cv2.putText(img,"Press 'esc' to quit",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2)
        #if flag==1: 0
            #cv2.putText(img,"employee face saved",(int(x),int(y)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2)
        cv2.imshow('attendance', img)  
    
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            #id=str(input('enter employee id'))
            #id=simpledialog.askstring('input id','plz enter your id')
            cv2.imwrite(wd+'\emp/'+ id+'.jpg',face)
            
            break
            #flag=1
            
            #cv2.putText(img,"employee face saved",(int(crd1),int(crd2)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2)
        
        
    
         
    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("glee","face saved")
    #mastera.deiconify()
    #mastera.destroy()  
    #mastera.quit()        
        
        
        
    
