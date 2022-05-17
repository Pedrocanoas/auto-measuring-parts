import tkinter as tk



class LoginScreenHandler:
    def __init__(self): 
        self.tk_instance = tk.Tk()
        self.screen_width = 400
        self.screen_height = 300
        self.label_ip = "IP:"
        self.label_port = "Porta: "
        self.label_token = "Token:"
    
    def initialize_login_screen(self):
        self.canvas_instance = tk.Canvas(self.tk_instance, width=400, height=300)
        self.canvas_instance.pack()

        self.ip = tk.Entry(self.tk_instance)
        self.canvas_instance.create_window(225, 120, window=self.ip)
        label_ip = tk.Label(self.tk_instance, text=self.label_ip)
        self.canvas_instance.create_window(125, 120, window=label_ip)

        self.port = tk.Entry(self.tk_instance)
        self.canvas_instance.create_window(225, 140, window=self.port)
        label_port = tk.Label(self.tk_instance, text=self.label_port)
        self.canvas_instance.create_window(125, 140, window=label_port)

        self.token = tk.Entry(self.tk_instance)
        self.canvas_instance.create_window(225, 100, window=self.token)
        label_token = tk.Label(self.tk_instance, text=self.label_token)
        self.canvas_instance.create_window(125, 100, window=label_token)

    def screen_action(self):
        self.value_ip_adress = self.ip.get()
        self.value_port = self.port.get()
        self.value_token = self.token.get()
        self.tk_instance.destroy()

    def run(self):
        self.initialize_login_screen()
        submit_button = tk.Button(text='Login', command=self.screen_action)
        self.canvas_instance.create_window(200, 170, window=submit_button)
        self.tk_instance.mainloop()

    def get_value_ip_adress(self):
        return self.value_ip_adress

    def get_value_port(self):
        return self.value_port
    
    def get_value_token(self):
        return self.value_token
