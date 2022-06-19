import cv2
from time import sleep
from utils.environment import SCALE
from utils.environment import W_MEASURE_AREA
from utils.environment import H_MEASURE_AREA
from dependencies.treat_image import reorder
from dependencies.treat_image import warpImg
from dependencies.treat_image import findDis
from dependencies.treat_image import getContours
from exceptions.custom_exceptions import InvalidToken
from functions.login_interface import InitialScreenHandler
from functions.two_factor_auth import check_two_factor_auth


class AppHandler:
    def call_init_screen(self):
        init_screen_instance = InitialScreenHandler()
        init_screen_instance.run()

    def call_check_token(self):
        check_token = check_two_factor_auth(entry_code=self.token)
        if not check_token:
            print("[INFO] -> Token inválido")
            # raise InvalidToken

    def build_url_video(self):
        # self.url = f"http://{self.ip_addr}:{self.port}/video"
        self.url = "http://192.168.1.66:4747/video"
        print("[INFO] -> Token validado com sucesso")

    def set_object_measure_area(self):
        self.wP = W_MEASURE_AREA * SCALE
        self.hP = H_MEASURE_AREA * SCALE

    def open_webcam(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.open(self.url)
        self.cap.set(10,160)
        self.cap.set(3,1920)
        self.cap.set(4,1080)

    def object_measure_handler(self):
        while True:
            _, img = self.cap.read()

            imgContours , conts = getContours(img,minArea=50000,filter=4)
            if len(conts) != 0:
                biggest = conts[0][2]
                imgWarp = warpImg(img, biggest, self.wP,self.hP)
                imgContours2, conts2 = getContours(
                    imgWarp,
                    minArea=2000, 
                    filter=4,
                    cThr=[50,50],
                    draw = False
                )

                if len(conts) != 0:
                    for obj in conts2:
                        cv2.polylines(imgContours2,[obj[2]],True,(0,255,0),2)
                        nPoints = reorder(obj[2])
                        nW = round((findDis(nPoints[0][0]//SCALE,nPoints[1][0]//SCALE)/10),1)
                        nH = round((findDis(nPoints[0][0]//SCALE,nPoints[2][0]//SCALE)/10),1)
                        cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                                        (255, 0, 255), 3, 8, 0, 0.05)
                        cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                                        (255, 0, 255), 3, 8, 0, 0.05)
                        x, y, w, h = obj[3]
                        cv2.putText(imgContours2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                                    (255, 0, 255), 2)
                        cv2.putText(imgContours2, '{}cm'.format(nH), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                                    (255, 0, 255), 2)
                cv2.imshow('A4', imgContours2)

            img = cv2.resize(img,(0,0),None,0.5,0.5)
            cv2.imshow('Original',img)
            
            key = cv2.waitKey(1)
            if key == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()
