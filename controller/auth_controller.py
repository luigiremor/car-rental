from controller.funcionarios_controller import FuncionariosController
from model.funcionario import Funcionario


class AuthController:
    def __init__(self, funcionarios_controller: FuncionariosController, view):
        self.funcionarios_controller = funcionarios_controller
        self.view = view

    def handle_menu_login(self):
        while True:
            self.view.menu_login()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                return self.handle_login()
            elif opcao == "2":
                return self.handle_cadastrar()
            elif opcao == "3":
                self.view.display_mensagem("Saindo do sistema...")
                break
            else:
                self.view.display_mensagem("Opção inválida. Por favor, tente novamente.")

    def handle_login(self):
        self.view.display_mensagem("Login")
        login = self.view.get_input("Digite seu login: ")
        senha = self.view.get_input("Digite sua senha: ")

        funcionario = self.funcionarios_controller.buscar_funcionario(login)

        if funcionario is not None:
            if funcionario.check_password(senha):
                self.view.display_mensagem("Login efetuado com sucesso!")
                return True
            else:
                self.view.display_mensagem("Senha incorreta. Por favor, tente novamente.")
        return False

    def handle_cadastrar(self):
        self.view.display_mensagem("Cadastrar")
        nome = self.view.get_input("Digite seu nome: ")
        cpf = self.view.get_input("Digite seu CPF: ")
        telefone = self.view.get_input("Digite seu telefone: ")
        cargo = self.view.get_input("Digite seu cargo: ")
        login = self.view.get_input("Digite seu login: ")
        senha = self.view.get_input("Digite sua senha: ")

        funcionario = Funcionario(self.funcionarios_controller.calculate_id(self.funcionarios_controller.funcionarios), nome, cpf, telefone, cargo, login, senha)
        self.funcionarios_controller.funcionarios.append(funcionario)

        self.view.display_mensagem("Cadastro efetuado com sucesso!")
        return True
