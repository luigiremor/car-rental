
from controller.clientes_controller import ClientesController
from controller.veiculos_controller import Veiculos_Controller
from model.reserva import Reserva
from view.reserva_view import ReservaView


class ReservasController():
    """
    Controller responsável por gerenciar as operações relacionadas às reservas.
    """

    def __init__(self, view: ReservaView,veiculos_controller: Veiculos_Controller, clientes_controller: ClientesController):
        self.view = view
        self.reservas: list[Reserva] = []
        self.veiculos_controller = veiculos_controller
        self.clientes_controller = clientes_controller

    def handle_menu_reservas(self):
        """
        Exibe um menu de opções para o usuário e executa a operação selecionada.
        """
        while True:
            self.view.menu_reservas()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                self.handle_cadastrar_reserva()
            elif opcao == "2":
                self.handle_editar_reserva()
            elif opcao == "3":
                self.handle_excluir_reserva()
            elif opcao == "4":
                self.handle_listar_reservas()
            elif opcao == "5":
                id = self.view.get_input("Digite o id da reserva: ")
                reserva = self.buscar_reserva(id)
                if reserva is not None:
                    self.view.display_mensagem(reserva)
                else:
                    self.view.display_mensagem("Reserva não encontrada.")
            elif opcao == "6":
                break
            else:
                self.view.display_mensagem(
                    "Opção inválida. Por favor, tente novamente.")

    def handle_cadastrar_reserva(self):
        """
        Obtém informações do usuário para criar uma nova reserva e adicioná-la à lista de reservas.
        """
        self.view.display_mensagem("Cadastrar Reserva")
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

        data_inicio = self.view.get_input("Digite a data de início: ")
        data_fim = self.view.get_input("Digite a data de fim: ")

        self.reservas.append(Reserva(self.calculate_id(
            self.reservas), data_inicio, data_fim, cliente, veiculo))

        self.view.display_mensagem("Cadastro efetuado com sucesso!")

    def handle_editar_reserva(self):
        """
        Obtém informações do usuário para editar uma reserva existente.
        """
        self.view.display_mensagem("Editar Reserva")
        id = self.view.get_input("Digite o id da reserva: ")
        reserva = self.buscar_reserva(id)

        if reserva is not None:
            data_inicio = self.view.get_input("Digite a data de início: ")
            data_fim = self.view.get_input("Digite a data de fim: ")

            reserva.set_data_inicio(data_inicio)
            reserva.set_data_fim(data_fim)

            self.view.display_mensagem("Reserva editada com sucesso!")
        else:
            self.view.display_mensagem("Reserva não encontrada.")

    def handle_excluir_reserva(self):
        """
        Obtém informações do usuário para excluir uma reserva existente.
        """
        self.view.display_mensagem("Excluir Reserva")
        id = self.view.get_input("Digite o id da reserva: ")
        reserva = self.buscar_reserva(id)

        if reserva is not None:
            self.reservas.remove(reserva)
            self.view.display_mensagem("Reserva excluída com sucesso!")
        else:
            self.view.display_mensagem("Reserva não encontrada.")

    def handle_listar_reservas(self):
        """
        Exibe todas as reservas cadastradas.
        """
        self.view.display_mensagem("Listar Reservas")
        for reserva in self.reservas:
            self.view.display_mensagem(reserva)

    def buscar_reserva(self, id) -> Reserva | None:
        """
        Busca uma reserva na lista de reservas pelo id.
        """
        for reserva in self.reservas:
            if reserva.get_id() == id:
                return reserva
        return None

    def calculate_id(self, lista):
        return len(lista) + 1
