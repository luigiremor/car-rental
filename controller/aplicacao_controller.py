from controller.auth_controller import AuthController
from controller.clientes_controller import ClientesController
from controller.funcionarios_controller import FuncionariosController
from controller.locacoes_controller import LocacoesController
from controller.reservas_controller import ReservasController
from controller.veiculos_controller import Veiculos_Controller
from view.aplicacao_view import AplicacaoView
from view.cliente_view import ClienteView
from view.funcionario_view import FuncionarioView
from view.locacao_view import LocacaoView
from view.login_view import LoginView
from view.reserva_view import ReservaView
from view.veiculo_view import VeiculoView


class AplicacaoController:
    """
    Controller responsável por gerenciar as operações relacionadas à aplicação.
    """

    def __init__(self):
        self.view = AplicacaoView()
        self.cliente_view = ClienteView()
        self.funcionario_view = FuncionarioView()
        self.veiculo_view = VeiculoView()
        self.reserva_view = ReservaView()
        self.locacao_view = LocacaoView()
        self.login_view = LoginView()

        self.clientes_controller = ClientesController(self.cliente_view)
        self.funcionarios_controller = FuncionariosController(self.funcionario_view)
        self.veiculos_controller = Veiculos_Controller(self.veiculo_view)
        self.reservas_controller = ReservasController(
            self.reserva_view,self.veiculos_controller, self.clientes_controller)
        self.locacoes_controller = LocacoesController(
            self.locacao_view ,self.clientes_controller, self.veiculos_controller, self.funcionarios_controller)
        self.auth_controller = AuthController(
            self.funcionarios_controller, self.login_view)

    def run(self):
        """
        Executa a aplicação.
        """
        while True:
            is_logged = self.handle_menu_login()
            if is_logged:
                self.handle_menu_principal()
            elif is_logged is None:
                break

    def handle_menu_login(self):
        """
        Exibe um menu de opções para o usuário e executa a operação selecionada.
        """
        return self.auth_controller.handle_menu_login()

    def handle_menu_principal(self):
        """
        Exibe um menu de opções para o usuário e executa a operação selecionada.
        """
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
