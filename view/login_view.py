from view.base_view import BaseView


class LoginView(BaseView):
    """
    View responsável por exibir informações relacionadas a login.
    """

    def menu_login(self):
        print("1 - Login")
        print("2 - Cadastrar")
        print("3 - Sair")
        print("")

