import eel
import json
import _thread
import subprocess
from utils.environment import MODELS_PATH
from utils.environment import JSON_FILE_FULL_PATH
from functions.two_factor_auth import check_two_factor_auth


class InitialScreenHandler:
    @eel.expose
    def camera_params(front_ip, front_port, front_token):
        body_response_js = {
            'ip': front_ip,
            'port': front_port
        }

        check_token = check_two_factor_auth(entry_code=front_token)
        if check_token:
            with open(JSON_FILE_FULL_PATH, 'w') as f:
                json.dump(body_response_js, f)
            print("Matando Thread...")
            subprocess.call("taskkill /F /IM chrome.exe")
            _thread.interrupt_main()
    
    def call_initial_screen(self):
        eel.init(MODELS_PATH)
        eel.start("index.html")
        # eel.start("index.html", mode='chrome', cmdline_args=['--kiosk']) # Full Screen
    
    def run(self):
        self.call_initial_screen()
