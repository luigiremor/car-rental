from view.base_view import BaseView


class ClienteView(BaseView):
    """
    View responsável por exibir informações relacionadas a clientes.
    """

    def menu_clientes(self):
        print("1 - Cadastrar Cliente")
        print("2 - Alterar Cliente")
        print("3 - Excluir Cliente")
        print("4 - Listar Clientes")
        print("5 - Buscar Cliente")
        print("6 - Voltar ao Menu Principal")
        print("")

