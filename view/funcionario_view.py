from view.base_view import BaseView


class FuncionarioView(BaseView):
    """
    View responsável por exibir informações relacionadas a funcionários.
    """

    def menu_funcionarios(self):
        print("1 - Cadastrar Funcionário")
        print("2 - Alterar Funcionário")
        print("3 - Excluir Funcionário")
        print("4 - Listar Funcionários")
        print("5 - Buscar Funcionário")
        print("6 - Voltar ao Menu Principal")
        print("")

