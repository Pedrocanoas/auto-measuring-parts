import cv2
import sys
import requests
import base64
from requests.auth import HTTPBasicAuth
import tkinter as tk
import logging as log
import datetime as dt
from time import sleep

login = tk.Tk()

canvas1 = tk.Canvas(login, width=400, height=300)
canvas1.pack()

username = tk.Entry(login)
canvas1.create_window(225, 80, window=username)
label_user = tk.Label(login, text='Usuário:')
canvas1.create_window(125, 80, window=label_user)

password = tk.Entry(login)
canvas1.create_window(225, 100, window=password)
label_pass = tk.Label(login, text='Senha:')
canvas1.create_window(125, 100, window=label_pass)

ip = tk.Entry(login)
canvas1.create_window(225, 120, window=ip)
label_ip = tk.Label(login, text='IP:')
canvas1.create_window(125, 120, window=label_ip)

port = tk.Entry(login)
canvas1.create_window(225, 140, window=port)
label_port = tk.Label(login, text='Porta:')
canvas1.create_window(125, 140, window=label_port)

def Login():
    user = username.get()
    senha = password.get()
    ip_adress = ip.get()
    porta = port.get()
    login.destroy()
    # File path with face detection xml
    cascPath = "XMLs/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    log.basicConfig(filename='webcam.log', level=log.INFO)

    video = cv2.VideoCapture(0)  # select what camera
    url = "http://"+ip_adress+":"+porta+"/video"
    adress = user+':'+senha
    message_bytes = adress.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    authentication = 'Basic '+base64_message
    payload={}
    headers = {
    'Authorization': authentication
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    video.open(response)
    anterior = 0

    while True:
        if not video.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        # Capture frame-by-frame
        ret, frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if anterior != len(faces):
            anterior = len(faces)
            log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Display the resulting frame
        cv2.imshow('Video', frame)

    # When everything is done, release the capture
    video.release()
    cv2.destroyAllWindows()


button1 = tk.Button(text='Login', command=Login)
canvas1.create_window(200, 170, window=button1)

login.mainloop()
