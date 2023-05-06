from view.base_view import BaseView


class AplicacaoView(BaseView):
    """
    View responsável por exibir as informações do menu principal.
    """

    def menu_principal(self):
        print("1 - Clientes")
        print("2 - Funcionarios")
        print("3 - Veiculos")
        print("4 - Reservas")
        print("5 - Locações")
        print("6 - Sair")
        print("")
        