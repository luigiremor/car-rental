
class Veiculo():

    def __init__(self, id, marca, modelo, ano, placa, cor, categoria, valor_diaria, is_disponivel):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.categoria = categoria
        self.is_disponivel = is_disponivel
        self.valor_diaria = valor_diaria

    def __str__(self):
        return f"Modelo: {self.modelo} | Ano: {self.ano} | Placa: {self.placa} | Cor: {self.cor} | Categoria: {self.categoria} | Valor da Diária: {self.valor_diaria}"
    

    def get_id(self):
        return self.id
    
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo
    
    def get_ano(self):
        return self.ano
    
    def get_placa(self):
        return self.placa
    
    def get_cor(self):
        return self.cor
    
    def get_categoria(self):
        return self.categoria
    
    def get_is_disponivel(self):
        return self.is_disponivel
    
    def get_valor_diaria(self):
        return self.valor_diaria
    
    def set_marca(self, marca):
        self.marca = marca
    
    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_ano(self, ano):
        self.ano = ano

    def set_placa(self, placa):
        self.placa = placa

    def set_cor(self, cor):
        self.cor = cor

    def set_categoria(self, categoria):
        self.categoria = categoria

    def set_is_disponivel(self, is_disponivel):
        self.is_disponivel = is_disponivel

    def set_valor_diaria(self, valor_diaria):
        self.valor_diaria = valor_diaria

    