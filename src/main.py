import traceback
from functions.app_handler import AppHandler
from exceptions.custom_exceptions import InvalidToken


def main_function():
    run_instance = AppHandler()
    run_instance.call_init_screen()
    run_instance.build_url_video()
    run_instance.set_object_measure_area()
    run_instance.open_webcam()
    run_instance.object_measure_handler()


if "__main__" == __name__:
    print("\n\t\t\t\t\t\t==================================")
    print("\t\t\t\t\t\tSistema de Auto Medição de Objetos")
    print("\t\t\t\t\t\t==================================\n")

    try:
        print("[INFO] -> Executando sistema...")
        main_function()
        print("[INFO] -> Sistema executado com sucesso!!!")

    except InvalidToken:
        print("[INFO] -> Timeout ao verificar Token de acesso a camera!")

    except Exception as e:
        print(f"[INFO] -> Erro ao executar sistema: {e}")
        print(f"[LOG ERROR] -> {traceback.format_exc}")