class BaseView:
    """
    View base para as demais views.
    """

    def get_input(self, mensagem):
        return input(mensagem)

    def display_mensagem(self, mensagem):
        print(mensagem)
