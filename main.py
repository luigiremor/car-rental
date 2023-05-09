from model.cliente import Cliente
from controller.aplicacao_controller import AplicacaoController
from model.funcionario import Funcionario
from model.locacao import Locacao
from model.reserva import Reserva
from model.veiculo import Veiculo

def main():
    controller = AplicacaoController()

    clientes = [
        Cliente(1, "João Silva", "123.456.789-00", "(11) 99999-9999", "Rua A, 123"),
        Cliente(2, "Maria Santos", "987.654.321-00", "(11) 88888-8888", "Rua B, 456"),
        Cliente(3, "Pedro Souza", "111.222.333-44", "(11) 77777-7777", "Rua C, 789"),
        Cliente(4, "Ana Oliveira", "555.666.777-88", "(11) 66666-6666", "Rua D, 1010"),
        Cliente(5, "Lucas Pereira", "999.888.777-66", "(11) 55555-5555", "Rua E, 1111")
    ]

    for cliente in clientes:
        controller.clientes_controller.clientes.append(cliente)


    funcionarios = [
        Funcionario(1, "João Silva", "123.456.789-00", "(11) 99999-9999", "Gerente", "joao.silva", "senha123"),
        Funcionario(2, "Maria Santos", "987.654.321-00", "(11) 88888-8888", "Vendedor", "maria.santos", "senha456"),
        Funcionario(3, "Pedro Souza", "111.222.333-44", "(11) 77777-7777", "Estoquista", "pedro.souza", "senha789"),
        Funcionario(4, "Ana Oliveira", "555.666.777-88", "(11) 66666-6666", "Caixa", "ana.oliveira", "senha1011"),
        Funcionario(5, "Lucas Pereira", "999.888.777-66", "(11) 55555-5555", "Assistente", "lucas.pereira", "senha1213")
    ]
    

    for funcionario in funcionarios:
        controller.funcionarios_controller.funcionarios.append(funcionario)

    
    veiculos = [
        Veiculo(1, "Volkswagen", "Gol", 2021, "ABC-1234", "Preto", "Hatch", 80.00, True),
        Veiculo(2, "Fiat", "Uno", 2020, "DEF-5678", "Branco", "Hatch", 70.00, True),
        Veiculo(3, "Ford", "Ka", 2019, "GHI-9012", "Vermelho", "Hatch", 75.00, False),
        Veiculo(4, "Chevrolet", "Onix", 2021, "JKL-3456", "Prata", "Sedan", 90.00, True),
        Veiculo(5, "Renault", "Sandero", 2022, "MNO-7890", "Azul", "Hatch", 85.00, False)
    ]

    for veiculo in veiculos:
        controller.veiculos_controller.veiculos.append(veiculo)
        

    reservas = [
        Reserva(1, "01/06/2023", "03/06/2023", clientes[0], veiculos[0]),
        Reserva(2, "15/06/2023", "18/06/2023", clientes[1], veiculos[1]),
        Reserva(3, "20/06/2023", "25/06/2023", clientes[2], veiculos[2]),
        Reserva(4, "10/07/2023", "15/07/2023", clientes[3], veiculos[3]),
        Reserva(5, "25/07/2023", "30/07/2023", clientes[4], veiculos[4])
    ]

    for reserva in reservas:
        controller.reservas_controller.reservas.append(reserva)

    locacoes = [
        Locacao(1, "01/06/2023", "03/06/2023", clientes[0], veiculos[0], funcionarios[0]),
        Locacao(2, "15/06/2023", "18/06/2023", clientes[1], veiculos[1], funcionarios[1]),
        Locacao(3, "20/06/2023", "25/06/2023", clientes[2], veiculos[2], funcionarios[2]),
        Locacao(4, "10/07/2023", "15/07/2023", clientes[3], veiculos[3], funcionarios[3]),
        Locacao(5, "25/07/2023", "30/07/2023", clientes[4], veiculos[4], funcionarios[4])
    ]

    for locacao in locacoes:
        controller.locacoes_controller.locacoes.append(locacao)
    
    controller.run()


if __name__ == "__main__":
    main()
