import eel
import requests
from utils.environment import MODELS_PATH

@eel.expose
class InitialScreenHandler:
    def camera_params(front_ip, front_port, front_user, front_password):
        url = f"http://{front_ip}:{front_port}/video"
        response = requests.get(url, auth=(front_user, front_password))

        print(response.status_code)
        print(response.json())
        return True
    
    def call_initial_screen(self):
        eel.init(MODELS_PATH)
        eel.start("index.html")
        # eel.start("index.html", mode='chrome', cmdline_args=['--kiosk']) # Full Screen
    
    def run(self):
        self.call_initial_screen()
        
