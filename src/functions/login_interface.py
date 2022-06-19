import eel
from utils.environment import MODELS_PATH


class InitialScreenHandler:
    @eel.expose
    def camera_params(front_ip, front_port, front_token):
        print(f"front_ip: {front_ip}")
        print(f"front_port: {front_port}")
        print(f"front_token: {front_token}")
        
        global body_camera_params
        body_camera_params = {
            "ip": front_ip,
            "port": front_port,
            "token": front_token
        }
        return body_camera_params
    
    def call_initial_screen(self):
        eel.init(MODELS_PATH)
        eel.start("index.html")
        # eel.start("index.html", mode='chrome', cmdline_args=['--kiosk']) # Full Screen
    
    def run(self):
        self.call_initial_screen()
        
