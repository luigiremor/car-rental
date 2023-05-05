from view.base_view import BaseView


class LocacaoView(BaseView):
    """
    View responsável por exibir informações relacionadas a locações.
    """

    def menu_locacoes(self):
        print("1 - Cadastrar Locação")
        print("2 - Alterar Locação")
        print("3 - Excluir Locação")
        print("4 - Listar Locações")
        print("5 - Buscar Locação")
        print("6 - Voltar ao Menu Principal")
        print("")
