from model.pessoa import Pessoa


class Cliente(Pessoa):
    """
    Classe Cliente que herda da classe Pessoa.
    Representa um cliente no sistema de locação de veículos.
    """

    def __init__(self, id, nome, cpf, telefone, endereco):
        super().__init__(id, nome, cpf, telefone)
        self.endereco = endereco

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf} | Telefone: {self.telefone} | Endereço: {self.endereco}"

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco
