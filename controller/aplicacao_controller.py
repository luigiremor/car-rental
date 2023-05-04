from model.cliente import Cliente
from model.funcionario import Funcionario
from model.locacao import Locacao
from model.reserva import Reserva
from model.veiculo import Veiculo
from view.aplicacao_view import AplicacaoView


class AplicacaoController:
    def __init__(self):
        self.listaClientes: list[Cliente] = []
        self.listaFuncionarios: list[Funcionario] = []
        self.listaVeiculos: list[Veiculo] = []
        self.listaReservas: list[Reserva] = []
        self.listaLocacoes: list[Locacao] = []
        self.view = AplicacaoView()


    def handle_menu_login(self):
        while True:
            self.view.menu_login()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                self.handle_login()
            elif opcao == "2":
                self.handle_cadastrar()
            elif opcao == "3":
                self.view.display_mensagem("Saindo do sistema...")
                break
            else:
                self.view.display_mensagem("Opção inválida. Por favor, tente novamente.")

    def handle_login(self):
        self.view.display_mensagem("Login")
        login = self.view.get_input("Digite seu login: ")
        senha = self.view.get_input("Digite sua senha: ")

        funcionario = self.buscar_funcionario(login)

        if funcionario is not None:
            if funcionario.check_password(senha):
                self.view.display_mensagem("Login efetuado com sucesso!")
                self.handle_menu_principal()
            else:
                self.view.display_mensagem("Senha incorreta. Por favor, tente novamente.")


    def handle_cadastrar(self):
        self.view.display_mensagem("Cadastrar")
        nome = self.view.get_input("Digite seu nome: ")
        cpf = self.view.get_input("Digite seu CPF: ")
        telefone = self.view.get_input("Digite seu telefone: ")
        cargo = self.view.get_input("Digite seu cargo: ")
        login = self.view.get_input("Digite seu login: ")
        senha = self.view.get_input("Digite sua senha: ")
        


        self.listaFuncionarios.append(Funcionario(self.calculate_id(self.listaFuncionarios), nome, cpf, telefone, cargo, login, senha))

        self.view.display_mensagem("Cadastro efetuado com sucesso!")
        self.handle_menu_principal()

    def handle_menu_principal(self):
        while True:
            self.view.menu_principal()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                self.view.menu_clientes()
            elif opcao == "2":
                self.view.menu_funcionarios()
            elif opcao == "3":
                self.view.menu_veiculos()
            elif opcao == "4":
                self.view.menu_locacoes()
            elif opcao == "5":
                self.view.menu_reservas()
            elif opcao == "6":
                self.view.display_mensagem("Saindo do sistema...")
                break
            else:
                self.view.display_mensagem("Opção inválida. Por favor, tente novamente.")

    def handle_menu_cliente(self):
        while True:
            self.view.menu_clientes()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                self.handle_cadastrar_cliente()
            elif opcao == "2":
                self.handle_editar_cliente()
            elif opcao == "3":
                self.handle_excluir_cliente()
            elif opcao == "4":
                self.handle_listar_cliente()
            elif opcao == "5":
                cpf = self.view.get_input("Digite o CPF do cliente: ")
                self.buscar_cliente(cpf)
            elif opcao == "6":
                self.handle_menu_principal()
            else:
                self.view.display_mensagem("Opção inválida. Por favor, tente novamente.")

    def handle_cadastrar_cliente(self):
        self.view.display_mensagem("Cadastrar Cliente")
        nome = self.view.get_input("Digite seu nome: ")
        cpf = self.view.get_input("Digite seu CPF: ")
        telefone = self.view.get_input("Digite seu telefone: ")
        endereco = self.view.get_input("Digite seu endereço: ")

        self.listaClientes.append(Cliente(self.calculate_id(self.listaClientes), nome, cpf, telefone, endereco))

        self.view.display_mensagem("Cadastro efetuado com sucesso!")
    
    def handle_editar_cliente(self):
        self.view.display_mensagem("Editar Cliente")
        cpf = self.view.get_input("Digite o CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if cliente is not None:
            nome = self.view.get_input("Digite seu nome: ")
            telefone = self.view.get_input("Digite seu telefone: ")
            endereco = self.view.get_input("Digite seu endereço: ")

            cliente.set_nome(nome)
            cliente.set_telefone(telefone)
            cliente.set_endereco(endereco)

            self.view.display_mensagem("Cliente editado com sucesso!")
        else:
            self.view.display_mensagem("Cliente não encontrado.")


    def handle_excluir_cliente(self):
        self.view.display_mensagem("Excluir Cliente")
        cpf = self.view.get_input("Digite o CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if cliente is not None:
            self.listaClientes.remove(cliente)
            self.view.display_mensagem("Cliente excluído com sucesso!")
        else:
            self.view.display_mensagem("Cliente não encontrado.")


    def handle_listar_cliente(self):
        self.view.display_mensagem("Listar Clientes")
        for cliente in self.listaClientes:
            self.view.display_cliente(cliente)

    def handle_menu_funcionario(self):
        while True:
            self.view.menu_funcionarios()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                self.handle_cadastrar_funcionario()
            elif opcao == "2":
                self.handle_editar_funcionario()
            elif opcao == "3":
                self.handle_excluir_funcionario()
            elif opcao == "4":
                self.handle_listar_funcionario()
            elif opcao == "5":
                login = self.view.get_input("Digite o login do funcionário: ")
                self.buscar_funcionario(login)
            elif opcao == "6":
                self.handle_menu_principal()
            else:
                self.view.display_mensagem("Opção inválida. Por favor, tente novamente.")
    
    def handle_cadastrar_funcionario(self):
        self.view.display_mensagem("Cadastrar Funcionário")
        nome = self.view.get_input("Digite seu nome: ")
        cpf = self.view.get_input("Digite seu CPF: ")
        telefone = self.view.get_input("Digite seu telefone: ")
        cargo = self.view.get_input("Digite seu cargo: ")
        login = self.view.get_input("Digite seu login: ")
        senha = self.view.get_input("Digite sua senha: ")


        self.listaFuncionarios.append(Funcionario(self.calculate_id(self.listaFuncionarios), nome, cpf, telefone, cargo, login, senha))

        self.view.display_mensagem("Cadastro efetuado com sucesso!")
        self.handle_menu_funcionario()

    def handle_editar_funcionario(self):
        self.view.display_mensagem("Editar Funcionário")
        login = self.view.get_input("Digite o login do funcionário: ")
        funcionario = self.buscar_funcionario(login)

        if funcionario is not None:
            nome = self.view.get_input("Digite seu nome: ")
            telefone = self.view.get_input("Digite seu telefone: ")
            cargo = self.view.get_input("Digite seu cargo: ")
            senha = self.view.get_input("Digite sua senha: ")

            funcionario.set_nome(nome)
            funcionario.set_telefone(telefone)
            funcionario.set_cargo(cargo)
            funcionario.set_senha(senha)

            self.view.display_mensagem("Funcionário editado com sucesso!")
        else:
            self.view.display_mensagem("Funcionário não encontrado.")

        self.handle_menu_funcionario()

    def handle_excluir_funcionario(self):
        self.view.display_mensagem("Excluir Funcionário")
        login = self.view.get_input("Digite o login do funcionário: ")
        funcionario = self.buscar_funcionario(login)

        if funcionario is not None:
            self.listaFuncionarios.remove(funcionario)
            self.view.display_mensagem("Funcionário excluído com sucesso!")
        else:
            self.view.display_mensagem("Funcionário não encontrado.")

        self.handle_menu_funcionario()
    
    def handle_listar_funcionario(self):
        self.view.display_mensagem("Listar Funcionários")
        for funcionario in self.listaFuncionarios:
            self.view.display_funcionario(funcionario)
        self.handle_menu_funcionario()

    def handle_menu_veiculo(self):
        while True:
            self.view.menu_veiculos()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                self.handle_cadastrar_veiculo()
            elif opcao == "2":
                self.handle_editar_veiculo()
            elif opcao == "3":
                # self.handle_excluir_veiculo()
                pass
            elif opcao == "4":
                # self.handle_listar_veiculo()
                pass
            elif opcao == "5":
                placa = self.view.get_input("Digite a placa do veículo: ")
                self.buscar_veiculo(placa)
            elif opcao == "6":
                self.handle_menu_principal()
            else:
                self.view.display_mensagem("Opção inválida. Por favor, tente novamente.")

    def handle_cadastrar_veiculo(self):
        self.view.display_mensagem("Cadastrar Veículo")
        marca = self.view.get_input("Digite a marca do veículo: ")
        modelo = self.view.get_input("Digite o modelo do veículo: ")
        placa = self.view.get_input("Digite a placa do veículo: ")
        cor = self.view.get_input("Digite a cor do veículo: ")
        categoria = self.view.get_input("Digite a categoria do veículo: ")
        ano = self.view.get_input("Digite o ano do veículo: ")
        valor_diaria = self.view.get_input("Digite o valor do veículo: ")
        disponivel = self.view.get_input("Digite se o veículo está disponível: (S/N)")
        is_disponivel = disponivel.lower() == "s"

        self.listaVeiculos.append(Veiculo(self.calculate_id(self.listaVeiculos), marca, modelo, ano, placa, cor, categoria, is_disponivel, valor_diaria))

        self.view.display_mensagem("Cadastro efetuado com sucesso!")
        self.handle_menu_veiculo()

    def handle_editar_veiculo(self):
        self.view.display_mensagem("Editar Veículo")
        placa = self.view.get_input("Digite a placa do veículo: ")
        veiculo = self.buscar_veiculo(placa)

        if veiculo is not None:
            marca = self.view.get_input("Digite a marca do veículo: ")
            modelo = self.view.get_input("Digite o modelo do veículo: ")
            cor = self.view.get_input("Digite a cor do veículo: ")
            categoria = self.view.get_input("Digite a categoria do veículo: ")
            ano = self.view.get_input("Digite o ano do veículo: ")
            valor_diaria = self.view.get_input("Digite o valor do veículo: ")
            disponivel = self.view.get_input("Digite se o veículo está disponível: (S/N)")
            is_disponivel = disponivel.lower() == "s"

            veiculo.set_marca(marca)
            veiculo.set_modelo(modelo)
            veiculo.set_cor(cor)
            veiculo.set_categoria(categoria)
            veiculo.set_ano(ano)
            veiculo.set_valor_diaria(valor_diaria)
            veiculo.set_is_disponivel(is_disponivel)

            self.view.display_mensagem("Veículo editado com sucesso!")


    def handle_menu_reserva(self):
        pass

    def handle_menu_locacao(self):
        pass

    def buscar_funcionario(self, login):
        for funcionario in self.listaFuncionarios:
            if funcionario.get_login() == login:
                return funcionario
        return None
    
    def buscar_cliente(self, cpf):
        for cliente in self.listaClientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None
    
    def buscar_veiculo(self, placa):
        for veiculo in self.listaVeiculos:
            if veiculo.get_placa() == placa:
                return veiculo
        return None
    
    def buscar_reserva(self, id):
        for reserva in self.listaReservas:
            if reserva.get_id() == id:
                return reserva
        return None
    
    def buscar_locacao(self, id):
        for locacao in self.listaLocacoes:
            if locacao.get_id() == id:
                return locacao
        return None

    def calculate_id(self, lista):
        return len(lista) + 1