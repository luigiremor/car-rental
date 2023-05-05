class AplicacaoView():
    """
    View responsável por exibir as informações para o usuário.
    """

    def menu_login(self):
        print("1 - Login")
        print("2 - Cadastrar")
        print("3 - Sair")
        print("")

    def menu_principal(self):
        print("1 - Clientes")
        print("2 - Funcionarios")
        print("3 - Veiculos")
        print("4 - Reservas")
        print("5 - Locações")
        print("6 - Sair")
        print("")

    def menu_clientes(self):
        print("1 - Cadastrar Cliente")
        print("2 - Alterar Cliente")
        print("3 - Excluir Cliente")
        print("4 - Listar Clientes")
        print("5 - Buscar Cliente")
        print("6 - Voltar ao Menu Principal")
        print("")

    def menu_funcionarios(self):
        print("1 - Cadastrar Funcionário")
        print("2 - Alterar Funcionário")
        print("3 - Excluir Funcionário")
        print("4 - Listar Funcionários")
        print("5 - Buscar Funcionário")
        print("6 - Voltar ao Menu Principal")
        print("")

    def menu_veiculos(self):
        print("1 - Cadastrar Veiculo")
        print("2 - Alterar Veiculo")
        print("3 - Excluir Veiculo")
        print("4 - Listar Veiculos")
        print("5 - Buscar Veiculo")
        print("6 - Voltar ao Menu Principal")
        print("")

    def menu_reservas(self):
        print("1 - Cadastrar Reserva")
        print("2 - Alterar Reserva")
        print("3 - Excluir Reserva")
        print("4 - Listar Reservas")
        print("5 - Buscar Reserva")
        print("6 - Voltar ao Menu Principal")
        print("")

    def menu_locacoes(self):
        print("1 - Cadastrar Locação")
        print("2 - Alterar Locação")
        print("3 - Excluir Locação")
        print("4 - Listar Locações")
        print("5 - Buscar Locação")
        print("6 - Voltar ao Menu Principal")
        print("")

    def get_input(self, mensagem):
        return input(mensagem)

    def display_mensagem(self, mensagem):
        print(mensagem)
