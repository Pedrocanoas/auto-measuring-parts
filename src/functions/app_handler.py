import cv2
from time import sleep
from functions.login_interface import LoginScreenHandler
from functions.two_factor_auth import check_two_factor_auth
from exceptions.custom_exceptions import InvalidToken


class AppHandler:
    def __init__(self):
        pass

    def call_login_screen(self):
        _instance = LoginScreenHandler()
        _instance.run()

        self.ip_addr = _instance.get_value_ip_adress()
        self.port = _instance.get_value_port()
        self.token = _instance.get_value_token()

    def call_check_token(self):
        check_token = check_two_factor_auth(entry_code=self.token)
        if not check_token:
            print("Token inválido")
            # raise InvalidToken

    def build_url_video(self):
        self.url = f"http://{self.ip_addr}:{self.port}/video"
        print("Token validado com sucesso")

    def call_video(self):
        video = cv2.VideoCapture(0)
        video.open(self.url)
        
        while True:
            if not video.isOpened():
                print('Unable to load camera.')
                sleep(5)

            # # Capture frame-by-frame
            ret, frame = video.read()

            # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Display the resulting frame
            cv2.imshow('Video', frame)

    def run(self):
        pass