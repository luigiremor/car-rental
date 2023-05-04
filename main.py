from controller.aplicacao_controller import AplicacaoController


def main():
    controller = AplicacaoController()
    controller.handle_menu_login()

if __name__ == "__main__":
    main()
