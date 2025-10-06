class Veiculo:
    def __init__(self, valor, km):
        self.valor = valor
        self.km = km

    def get_valor(self):
        return self.valor

    def get_km(self):
        return self.km

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def set_km(self, novo_km):
        self.km = novo_km

class Carro(Veiculo):
    def __init__(self, valor, km, qtd_portas=4):
        super().__init__(valor, km)
        self.qtd_portas = qtd_portas

    def get_qtd_portas(self):
        return self.qtd_portas

    def set_qtd_portas(self, qtd_portas):
        self.qtd_portas = qtd_portas
