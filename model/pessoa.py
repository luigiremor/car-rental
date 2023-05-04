class Pessoa():

    def __init__(self, id, nome, cpf, telefone):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf} | Telefone: {self.telefone}"

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_telefone(self):
        return self.telefone

    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_telefone(self, telefone):
        self.telefone = telefone
