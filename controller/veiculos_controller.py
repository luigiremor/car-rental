
from model.veiculo import Veiculo
from view.aplicacao_view import AplicacaoView


class Veiculos_Controller():

    def __init__(self):
        self.veiculos = []
        self.view = AplicacaoView()

    def handle_menu_veiculo(self):
        while True:
            self.view.menu_veiculos()
            opcao = self.view.get_input("Digite sua opção: ")

            if opcao == "1":
                self.handle_cadastrar_veiculos()
            elif opcao == "2":
                self.handle_editar_veiculo()
            elif opcao == "3":
                self.handle_excluir_veiculo()
            elif opcao == "4":
                self.handle_listar_veiculo()
            elif opcao == "5":
                placa = self.view.get_input("Digite a placa do veículo: ")
                self.buscar_veiculo(placa)
            elif opcao == "6":
                break
            else:
                self.view.display_mensagem(
                    "Opção inválida. Por favor, tente novamente.")

    def handle_cadastrar_veiculos(self):
        self.view.display_mensagem("Cadastrar Veículo")
        marca = self.view.get_input("Digite a marca do veículo: ")
        modelo = self.view.get_input("Digite o modelo do veículo: ")
        placa = self.view.get_input("Digite a placa do veículo: ")
        cor = self.view.get_input("Digite a cor do veículo: ")
        categoria = self.view.get_input("Digite a categoria do veículo: ")
        ano = self.view.get_input("Digite o ano do veículo: ")
        valor_diaria = float(self.view.get_input(
            "Digite o valor do veículo: "))
        disponivel = self.view.get_input(
            "Digite se o veículo está disponível: (S/N)")
        is_disponivel = disponivel.lower() == "s"

        self.veiculos.append(Veiculo(self.calculate_id(
            self.veiculos), marca, modelo, ano, placa, cor, categoria, valor_diaria, is_disponivel))

        self.view.display_mensagem("Cadastro efetuado com sucesso!")

    def handle_editar_veiculo(self):
        self.view.display_mensagem("Editar Veículo")
        placa = self.view.get_input("Digite a placa do veículo: ")
        veiculo = self.buscar_veiculo(placa)

        if veiculo is not None:
            marca = self.view.get_input("Digite a marca do veículo: ")
            modelo = self.view.get_input("Digite o modelo do veículo: ")
            cor = self.view.get_input("Digite a cor do veículo: ")
            categoria = self.view.get_input("Digite a categoria do veículo: ")
            ano = self.view.get_input("Digite o ano do veículo: ")
            valor_diaria = float(self.view.get_input(
                "Digite o valor do veículo: "))
            disponivel = self.view.get_input(
                "Digite se o veículo está disponível: (S/N)")
            is_disponivel = disponivel.lower() == "s"

            veiculo.set_marca(marca)
            veiculo.set_modelo(modelo)
            veiculo.set_cor(cor)
            veiculo.set_categoria(categoria)
            veiculo.set_ano(ano)
            veiculo.set_valor_diaria(valor_diaria)
            veiculo.set_is_disponivel(is_disponivel)

            self.view.display_mensagem("Veículo editado com sucesso!")

    def handle_excluir_veiculo(self):
        self.view.display_mensagem("Excluir Veículo")
        placa = self.view.get_input("Digite a placa do veículo: ")
        veiculo = self.buscar_veiculo(placa)

        if veiculo is not None:
            self.veiculos.remove(veiculo)
            self.view.display_mensagem("Veículo excluído com sucesso!")
        else:
            self.view.display_mensagem("Veículo não encontrado!")

    def handle_listar_veiculo(self):
        self.view.display_mensagem("Listar Veículo")
        for veiculo in self.veiculos:
            self.view.display_veiculo(veiculo)

    def buscar_veiculo(self, placa) -> Veiculo | None:
        for veiculo in self.veiculos:
            if veiculo.get_placa() == placa:
                return veiculo
        return None

    def calculate_id(self, lista):
        return len(lista) + 1
