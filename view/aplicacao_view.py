class AplicacaoView():

    def menu_login(self):
        print("1 - Login")
        print("2 - Cadastrar")
        print("3 - Sair")
        print("")

    def menu_principal(self):
        print("1 - Clientes")
        print("2 - Funcionarios")
        print("3 - Veiculos")
        print("4 - Locações")
        print("5 - Reservas")
        print("6 - Sair")
        print("")

    def menu_clientes(self):
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Buscar Cliente")
        print("4 - Alterar Cliente")
        print("5 - Excluir Cliente")
        print("6 - Sair")
        print("")

    def display_cliente(self, cliente):
        print(cliente)

    def menu_funcionarios(self):
        print("1 - Cadastrar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Buscar Funcionário")
        print("4 - Alterar Funcionário")
        print("5 - Excluir Funcionário")
        print("6 - Sair")
        print("")

    def display_funcionario(self, funcionario):
        print(funcionario)

    def menu_veiculos(self):
        print("1 - Cadastrar Veículo")
        print("2 - Listar Veículos")
        print("3 - Buscar Veículo")
        print("4 - Alterar Veículo")
        print("5 - Excluir Veículo")
        print("6 - Sair")
        print("")
    
    def menu_reservas(self):
        print("1 - Cadastrar Reserva")
        print("2 - Listar Reservas")
        print("3 - Buscar Reserva")
        print("4 - Alterar Reserva")
        print("5 - Excluir Reserva")
        print("6 - Sair")
        print("")

    def menu_locacoes(self):
        print("1 - Cadastrar Locação")
        print("2 - Listar Locações")
        print("3 - Buscar Locação")
        print("4 - Alterar Locação")
        print("5 - Excluir Locação")
        print("6 - Sair")
        print("")
    
    def get_input(self, mensagem):
        return input(mensagem)
    
    def display_mensagem(self, mensagem):
        print(mensagem)

    