from datetime import datetime
from model.cliente import Cliente

from model.veiculo import Veiculo


class Reserva():

    def __init__(self, id, data_inicio, data_fim, cliente: Cliente, veiculo: Veiculo):
        self.id = id
        self.cliente = cliente
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def __str__(self):
        return f"ID: {self.id} | Cliente: {self.cliente} | Veículo: {self.veiculo} | Data de Início: {self.data_inicio} | Data de Fim: {self.data_fim} | Valor Total: {self.valor_total}"

    def get_id(self):
        return self.id

    def get_cliente(self):
        return self.cliente

    def get_veiculo(self):
        return self.veiculo

    def get_data_inicio(self):
        return self.data_inicio

    def get_data_fim(self):
        return self.data_fim

    def get_valor_total(self):
        return self.valor_total

    def set_cliente(self, cliente):
        self.cliente = cliente

    def set_veiculo(self, veiculo):
        self.veiculo = veiculo

    def set_data_inicio(self, data_inicio):
        self.data_inicio = data_inicio

    def set_data_fim(self, data_fim):
        self.data_fim = data_fim

    def set_valor_total(self, valor_total):
        self.valor_total = valor_total

    def calcular_dias_reserva(self):
        data_inicio = datetime.strptime(self.data_inicio, '%d/%m/%Y')
        data_fim = datetime.strptime(self.data_fim, '%d/%m/%Y')
        dias_reserva = (data_fim - data_inicio).days
        return dias_reserva
