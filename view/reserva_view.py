from view.base_view import BaseView


class ReservaView(BaseView):
    """
    View responsável por exibir informações relacionadas a reservas.
    """

    def menu_reservas(self):
        print("1 - Cadastrar Reserva")
        print("2 - Alterar Reserva")
        print("3 - Excluir Reserva")
        print("4 - Listar Reservas")
        print("5 - Buscar Reserva")
        print("6 - Voltar ao Menu Principal")
        print("")