from model.cliente import Cliente
from model.funcionario import Funcionario
from model.reserva import Reserva
from model.veiculo import Veiculo


class Locacao(Reserva):

    def __init__(self, id, data_inicio, data_fim, cliente: Cliente, veiculo: Veiculo, funcionario: Funcionario):
        super().__init__(id, cliente, veiculo, data_inicio, data_fim)
        self.funcionario = funcionario
        self.valor_total = self.calcular_valor_total()

    def __str__(self):
        return f"ID: {self.id} | Cliente: {self.cliente} | Veículo: {self.veiculo} | Data de Início: {self.data_inicio} | Data de Fim: {self.data_fim} | Funcionário: {self.funcionario} | Valor Total: {self.valor_total}"
    
    def get_funcionario(self):
        return self.funcionario
    
    def get_valor_total(self):
        return self.valor_total
    
    def set_funcionario(self, funcionario):
        self.funcionario = funcionario

    def calcular_valor_total(self):
        self.valor_total = self.veiculo.get_valor_diaria() * self.calcular_dias_reserva()
        return self.valor_total