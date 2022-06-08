import cv2
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

    video = cv2.VideoCapture(0)
    url = f"http://{ip_addr}:{port}/video"
    check_token = check_two_factor_auth(entry_code=token)

    if not check_token:
        print("Token inválido")
        return False    # Change later
    
    print("Token validado com sucesso")
    video.open(url)

    while True:
        if not video.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        # # Capture frame-by-frame
        ret, frame = video.read()

        # Display the resulting frame
        cv2.imshow('Video', frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

        # Display the resulting frame
        cv2.imshow('Video', frame)

    # # When everything is done, release the capture
    # video.release()
    # cv2.destroyAllWindows()

Login()