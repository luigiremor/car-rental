from controller.auth_controller import AuthController
from controller.clientes_controller import ClientesController
from controller.funcionarios_controller import FuncionariosController
from controller.locacoes_controller import LocacoesController
from controller.reservas_controller import ReservasController
from controller.veiculos_controller import Veiculos_Controller
from view.aplicacao_view import AplicacaoView


class AplicacaoController:
    def __init__(self):
        self.view = AplicacaoView()
        self.clientes_controller = ClientesController()
        self.funcionarios_controller = FuncionariosController()
        self.veiculos_controller = Veiculos_Controller()
        self.reservas_controller = ReservasController(
            self.veiculos_controller, self.clientes_controller)
        self.locacoes_controller = LocacoesController(
            self.clientes_controller, self.veiculos_controller, self.funcionarios_controller)
        self.auth_controller = AuthController(
            self.funcionarios_controller, self.view)

    def run(self):
        while True:
            is_logged = self.handle_menu_login()
            if is_logged:
                self.handle_menu_principal()

    def handle_menu_login(self):
        return self.auth_controller.handle_menu_login()

    def handle_menu_principal(self):
        while True:
            self.view.menu_principal()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                self.clientes_controller.handle_menu_clientes()
            elif opcao == "2":
                self.funcionarios_controller.handle_menu_funcionarios()
            elif opcao == "3":
                self.veiculos_controller.handle_menu_veiculo()
            elif opcao == "4":
                self.reservas_controller.handle_menu_reservas()
            elif opcao == "5":
                self.locacoes_controller.handle_menu_locacoes()
            elif opcao == "6":
                self.view.display_mensagem("Saindo do sistema...")
                break
            else:
                self.view.display_mensagem(
                    "Opção inválida. Por favor, tente novamente.")

    def handle_menu_locacao(self):
        pass

    def calculate_id(self, lista):
        return len(lista) + 1
