from model.cliente import Cliente
from view.aplicacao_view import AplicacaoView


class ClientesController:
    def __init__(self):
        self.clientes: list[Cliente] = []
        self.view = AplicacaoView()

    def handle_menu_clientes(self):
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
                break
            else:
                self.view.display_mensagem("Opção inválida. Por favor, tente novamente.")

    def handle_cadastrar_cliente(self):
        self.view.display_mensagem("Cadastrar Cliente")
        nome = self.view.get_input("Digite seu nome: ")
        cpf = self.view.get_input("Digite seu CPF: ")
        telefone = self.view.get_input("Digite seu telefone: ")
        endereco = self.view.get_input("Digite seu endereço: ")

        self.clientes.append(Cliente(self.calculate_id(self.clientes), nome, cpf, telefone, endereco))

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
            self.clientes.remove(cliente)
            self.view.display_mensagem("Cliente excluído com sucesso!")
        else:
            self.view.display_mensagem("Cliente não encontrado.")


    def handle_listar_cliente(self):
        self.view.display_mensagem("Listar Clientes")
        for cliente in self.clientes:
            self.view.display_cliente(cliente)

    def buscar_cliente(self, cpf) -> Cliente | None:
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None
    
    def calculate_id(self, lista):
        return len(lista) + 1