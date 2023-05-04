
from model.funcionario import Funcionario
from view.aplicacao_view import AplicacaoView


class FuncionariosController():

    def __init__(self):
        self.funcionarios = []
        self.view = AplicacaoView()

    def handle_menu_funcionarios(self):
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
                break
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


        self.funcionarios.append(Funcionario(self.calculate_id(self.funcionarios), nome, cpf, telefone, cargo, login, senha))

        self.view.display_mensagem("Cadastro efetuado com sucesso!")

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


    def handle_excluir_funcionario(self):
        self.view.display_mensagem("Excluir Funcionário")
        login = self.view.get_input("Digite o login do funcionário: ")
        funcionario = self.buscar_funcionario(login)

        if funcionario is not None:
            self.funcionarios.remove(funcionario)
            self.view.display_mensagem("Funcionário excluído com sucesso!")
        else:
            self.view.display_mensagem("Funcionário não encontrado.")

    
    def handle_listar_funcionario(self):
        self.view.display_mensagem("Listar Funcionários")
        for funcionario in self.funcionarios:
            self.view.display_funcionario(funcionario)

    def calculate_id(self, lista):
        return len(lista) + 1
    
    def buscar_funcionario(self, login):
        for funcionario in self.funcionarios:
            if funcionario.get_login() == login:
                return funcionario
        return None
    