from model.cliente import Cliente
from view.aplicacao_view import AplicacaoView
from view.cliente_view import ClienteView


class ClientesController:
    """
    Controller responsável por gerenciar as operações relacionadas aos clientes.
    """

    def __init__(self, view: ClienteView):
        self.clientes: list[Cliente] = []
        self.view = view

    def handle_menu_clientes(self):
        """
        Exibe um menu de opções para o usuário e executa a operação selecionada.
        """
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
                self.view.display_mensagem(
                    "Opção inválida. Por favor, tente novamente.")

    def handle_cadastrar_cliente(self):
        """
        Obtém informações do usuário para criar um novo cliente e adicioná-lo à lista de clientes.
        """
        self.view.display_mensagem("Cadastrar Cliente")
        nome = self.view.get_input("Digite seu nome: ")
        cpf = self.view.get_input("Digite seu CPF: ")
        telefone = self.view.get_input("Digite seu telefone: ")
        endereco = self.view.get_input("Digite seu endereço: ")

        self.clientes.append(Cliente(self.calculate_id(
            self.clientes), nome, cpf, telefone, endereco))

        self.view.display_mensagem("Cadastro efetuado com sucesso!")

    def handle_editar_cliente(self):
        """
        Obtém o CPF do cliente a ser editado e as novas informações do usuário para atualizar o cliente correspondente.
        """
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
        """
        Obtém o CPF do cliente a ser excluído e remove-o da lista de clientes.
        """
        self.view.display_mensagem("Excluir Cliente")
        cpf = self.view.get_input("Digite o CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if cliente is not None:
            self.clientes.remove(cliente)
            self.view.display_mensagem("Cliente excluído com sucesso!")
        else:
            self.view.display_mensagem("Cliente não encontrado.")

    def handle_listar_cliente(self):
        """
        Exibe todos os clientes cadastrados.
        """
        self.view.display_mensagem("Listar Clientes")
        for cliente in self.clientes:
            self.view.display_mensagem(cliente)

    def buscar_cliente(self, cpf) -> Cliente | None:
        """
        Busca um cliente pelo CPF.
        """
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None

    def calculate_id(self, lista):
        """
        Calcula o ID do novo cliente a ser cadastrado.
        """
        return len(lista) + 1
