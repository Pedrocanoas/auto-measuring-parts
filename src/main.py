import cv2
import requests
import base64
import logging as log
import datetime as dt
from time import sleep
from functions.login_interface import LoginScreenHandler
from functions.two_factor_auth import check_two_factor_auth


def Login():
    # Run login screen
    _instance = LoginScreenHandler()
    _instance.run()

    # Get data contains in screen
    ip_addr = _instance.get_value_ip_adress()
    port = _instance.get_value_port()
    token = _instance.get_value_token()

    # File path with face detection xml
    cascPath = "dependencies/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    log.basicConfig(filename='webcam.log', level=log.INFO)

    video = cv2.VideoCapture(0)  # select what camera
    url = f"http://{ip_addr}:{port}/video"

    check_token = check_two_factor_auth(entry_code=token)

    if not check_token:
        print("Token inválido")
        return False    # Change later
    
    print("Token validado com sucesso")
    video.open(url)

    # 192.168.1.67
    # 4747
    # address = f"{user}:{password}"

    # message_bytes = address.encode('ascii')
    # base64_bytes = base64.b64encode(message_bytes)
    # base64_message = base64_bytes.decode('ascii')

    # authentication = f"Basic {base64_message}"
    # payload={}
    # headers = {
    #     'Authorization': authentication
    # }
    # response = requests.request("GET", url, headers=headers, data=payload)

    while True:
        if not video.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        # # Capture frame-by-frame
        ret, frame = video.read()

        # =================================== NOT WORKING =========================================
        # 

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # faces = faceCascade.detectMultiScale(
        #     gray,
        #     scaleFactor=1.1,
        #     minNeighbors=5,
        #     minSize=(30, 30)
        # )

        # # Draw a rectangle around the faces
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # if anterior != len(faces):
        #     anterior = len(faces)
        #     log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

        # =========================================================================================

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Display the resulting frame
        cv2.imshow('Video', frame)

    # When everything is done, release the capture
    video.release()
    cv2.destroyAllWindows()

Login()
