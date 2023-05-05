from model.cliente import Cliente
from model.funcionario import Funcionario
from model.reserva import Reserva
from model.veiculo import Veiculo


class Locacao(Reserva):
    """
    Classe Locacao que herda da classe Reserva.
    Representa uma locação no sistema de locação de veículos.
    """

    def __init__(self, id, data_inicio, data_fim, cliente: Cliente, veiculo: Veiculo, funcionario: Funcionario):
        super().__init__(id, data_inicio, data_fim, cliente, veiculo)
        self.funcionario = funcionario
        self.valor_total: float = self.calcular_valor_total()

    def __str__(self):
        return f"ID: {self.get_id()} | Cliente: {self.cliente.get_nome()} | Veículo: {self.veiculo.get_modelo()} | Data de Início: {self.get_data_inicio()} | Data de Fim: {self.get_data_fim()} | Funcionário: {self.funcionario.get_nome()} | Valor Total: {self.get_valor_total()}"

    def get_funcionario(self):
        return self.funcionario

    def get_valor_total(self):
        return self.valor_total

    def set_funcionario(self, funcionario):
        self.funcionario = funcionario

    def calcular_valor_total(self):
        """
        Calcula o valor total da locação de acordo 
        com o valor da diária do veículo e a quantidade de dias da reserva.
        """
        dias_reserva = self.calcular_dias_reserva()
        valor_diaria = self.veiculo.get_valor_diaria()
        return valor_diaria * dias_reserva
