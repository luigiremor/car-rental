from model.pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, id, nome, cpf, telefone, cargo, login, senha):
        super().__init__(id, nome, cpf, telefone)
        self.cargo = cargo
        self.login = login
        self.senha = senha

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf} | Telefone: {self.telefone} | Cargo: {self.cargo} | Login: {self.login} | Senha: {self.senha}"
    
    def get_cargo(self):
        return self.cargo
    
    def get_login(self):
        return self.login
    
    def get_senha(self):
        return self.senha
    
    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_login(self, login):
        self.login = login

    def set_senha(self, senha):
        self.senha = senha

    def check_password(self, senha):
        return self.senha == senha