from view.base_view import BaseView


class VeiculoView(BaseView):
    """
    View responsável por exibir informações relacionadas a veiculos.
    """

    def menu_veiculos(self):
        print("1 - Cadastrar Veiculo")
        print("2 - Alterar Veiculo")
        print("3 - Excluir Veiculo")
        print("4 - Listar Veiculos")
        print("5 - Buscar Veiculo")
        print("6 - Voltar ao Menu Principal")
        print("")
