from controller.clientes_controller import ClientesController
from controller.funcionarios_controller import FuncionariosController
from controller.veiculos_controller import Veiculos_Controller
from model.locacao import Locacao
from view.aplicacao_view import AplicacaoView


class LocacoesController():
    """
    Controller responsável por gerenciar as operações relacionadas às locações.
    """

    def __init__(self, clientes_controller: ClientesController, veiculos_controller: Veiculos_Controller, funcionarios_controller: FuncionariosController):
        self.locacoes: list[Locacao] = []
        self.view = AplicacaoView()
        self.clientes_controller = clientes_controller
        self.veiculos_controller = veiculos_controller
        self.funcionarios_controller = funcionarios_controller

    def handle_menu_locacoes(self):
        """
        Exibe um menu de opções para o usuário e executa a operação selecionada.
        """
        while True:
            self.view.menu_locacoes()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                self.handle_cadastrar_locacao()
            elif opcao == "2":
                self.handle_editar_locacao()
            elif opcao == "3":
                self.handle_excluir_locacao()
            elif opcao == "4":
                self.handle_listar_locacao()
            elif opcao == "5":
                cpf = self.view.get_input("Digite o CPF do cliente: ")
                self.buscar_locacao(cpf)
            elif opcao == "6":
                break
            else:
                self.view.display_mensagem(
                    "Opção inválida. Por favor, tente novamente.")

    def handle_cadastrar_locacao(self):
        """
        Obtém informações do usuário para criar uma nova locação e adicioná-la à lista de locações.
        """
        self.view.display_mensagem("Cadastrar Locação")
        cliente = None
        while cliente is None:
            cpf_cliente = self.view.get_input("Digite o CPF do cliente: ")
            cliente = self.clientes_controller.buscar_cliente(cpf_cliente)
            if cliente is None:
                self.view.display_mensagem("Cliente não encontrado.")
                self.view.display_mensagem("Deseja continuar? (S/N)")
                opcao = self.view.get_input("Digite sua opção: ")
                if opcao.lower() != "s":
                    return

        funcionario = None
        while funcionario is None:
            login_funcionario = self.view.get_input(
                "Digite o login do funcionário: ")
            funcionario = self.funcionarios_controller.buscar_funcionario(
                login_funcionario)
            if funcionario is None:
                self.view.display_mensagem("Funcionário não encontrado.")
                self.view.display_mensagem("Deseja continuar? (S/N)")
                opcao = self.view.get_input("Digite sua opção: ")
                if opcao.lower() != "s":
                    return

        veiculo = None
        while veiculo is None:
            placa_veiculo = self.view.get_input("Digite a placa do veículo: ")
            veiculo = self.veiculos_controller.buscar_veiculo(placa_veiculo)
            if veiculo is None:
                self.view.display_mensagem("Veículo não encontrado.")
                self.view.display_mensagem("Deseja continuar? (S/N)")
                opcao = self.view.get_input("Digite sua opção: ")
                if opcao.lower() != "s":
                    return

        data_inicio = self.view.get_input(
            "Digite a data de início da locação: ")
        data_fim = self.view.get_input("Digite a data de fim da locação: ")

        locacao = Locacao(self.calculate_id(self.locacoes),
                          data_inicio, data_fim, cliente, veiculo, funcionario)

        self.locacoes.append(locacao)

        self.view.display_mensagem("Locação cadastrada com sucesso!")

    def handle_editar_locacao(self):
        """
        Obtém o ID da locação a ser editada e as novas informações do usuário para atualizar a locação.
        """
        self.view.display_mensagem("Editar Locação")
        id = self.view.get_input("Digite o ID da locação: ")
        locacao = self.buscar_locacao(id)

        if locacao is None:
            self.view.display_mensagem("Locação não encontrada.")
            return

        self.view.display_mensagem("Dados da Locação:")
        self.view.display_mensagem(locacao)

        data_inicio = self.view.get_input(
            "Digite a data de início da locação: ")
        data_fim = self.view.get_input("Digite a data de fim da locação: ")

        locacao.set_data_inicio(data_inicio)
        locacao.set_data_fim(data_fim)

        self.view.display_mensagem("Locação editada com sucesso!")

    def handle_excluir_locacao(self):
        """
        Obtém o ID da locação a ser excluída e a remove da lista de locações.
        """
        self.view.display_mensagem("Excluir Locação")
        id = self.view.get_input("Digite o ID da locação: ")
        locacao = self.buscar_locacao(id)
        if locacao is None:
            self.view.display_mensagem("Locação não encontrada.")
            return
        self.locacoes.remove(locacao)
        self.view.display_mensagem("Locação excluída com sucesso!")

    def handle_listar_locacao(self):
        """
        Exibe todas as locações cadastradas.
        """
        self.view.display_mensagem("Listar Locações")
        if len(self.locacoes) == 0:
            self.view.display_mensagem("Não há locações cadastradas.")
            return
        for locacao in self.locacoes:
            self.view.display_mensagem(locacao)

    def buscar_locacao(self, id):
        """
        Busca uma locação pelo ID.
        """
        for locacao in self.locacoes:
            if locacao.get_id() == id:
                return locacao
        return None

    def calculate_id(self, lista):
        return len(lista) + 1
