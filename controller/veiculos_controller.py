
from model.veiculo import Veiculo
from view.veiculo_view import VeiculoView


class Veiculos_Controller():
    """
    Controller responsável por gerenciar as operações relacionadas aos veículos.
    """

    def __init__(self, view: VeiculoView):
        self.veiculos = []
        self.view = view

    def handle_menu_veiculo(self):
        """
        Exibe um menu de opções para o usuário e executa a operação selecionada.
        """
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
        """
        Obtém informações do usuário para criar um novo veículo e adicioná-lo à lista de veículos.
        """

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
        """
        Obtém a placa do veículo que o usuário deseja editar e exibe um menu de opções para o usuário.
        """
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
        """
        Obtém a placa do veículo que o usuário deseja excluir e o remove da lista de veículos.
        """
        self.view.display_mensagem("Excluir Veículo")
        placa = self.view.get_input("Digite a placa do veículo: ")
        veiculo = self.buscar_veiculo(placa)

        if veiculo is not None:
            self.veiculos.remove(veiculo)
            self.view.display_mensagem("Veículo excluído com sucesso!")
        else:
            self.view.display_mensagem("Veículo não encontrado!")

    def handle_listar_veiculo(self):
        """
        Exibe todos os veículos cadastrados.
        """
        self.view.display_mensagem("Listar Veículo")
        for veiculo in self.veiculos:
            self.view.display_mensagem(veiculo)

    def buscar_veiculo(self, placa) -> Veiculo | None:
        """
        Busca um veículo na lista de veículos pelo número da placa.
        """
        for veiculo in self.veiculos:
            if veiculo.get_placa() == placa:
                return veiculo
        return None

    def calculate_id(self, lista):
        return len(lista) + 1
