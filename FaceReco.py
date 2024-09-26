import streamlit as st
import cv2
import numpy as np 


st.title("Face Recognition App")
def detect_face(img):
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
    return img


upload=st.file_uploader("Choose an image",type=["jpg","png","jpeg"])

if upload is not None:
    raw_byte=np.asarray(bytearray(upload.read()),dtype=np.uint8)
    img=cv2.imdecode(raw_byte,cv2.IMREAD_COLOR)
    
    resultimg=detect_face(img)
    
    st.image(resultimg,channels="BGR")
