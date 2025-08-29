class Produto:

     #A.Metodo construtor com pelo menos quatro atributos (string, int, float, int)
    def __init__(self, nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

    # b. Métodos gets (consultar) de todos os atributos
    def get_nome(self):
        return self.nome

    def get_codigo(self):
        return self.codigo

    def get_preco(self):
        return self.preco

    def get_quantidade(self):
        return self.quantidade

    # c. Métodos sets (alterar) de todos os atributos
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_codigo(self, novo_codigo):
        self.codigo = novo_codigo

    def set_preco(self, novo_preco):
        self.preco = novo_preco

    def set_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    # d. Metodo funcional adicional: Calcular o valor total em estoque
    # Enunciado do problema: "Calcular o valor total de um produto em estoque multiplicando o preço pela quantidade."
    def calcular_valor_total(self):
        return self.preco * self.quantidade


# e. Metodo main para testar a classe
def main():
    # Instanciando pelo menos três objetos da classe Produto
    produto1 = Produto("Notebook", 101, 2500.50, 10)
    produto2 = Produto("Mouse", 202, 50.00, 50)
    produto3 = Produto("Teclado", 303, 150.75, 25)

    # Testando os métodos gets e o metodo funcional para o primeiro objeto
    print("--- Detalhes do Produto 1 ---")
    print(f"Nome: {produto1.get_nome()}")
    print(f"Código: {produto1.get_codigo()}")
    print(f"Preço: R$ {produto1.get_preco():.2f}")
    print(f"Quantidade: {produto1.get_quantidade()}")
    print(f"Valor Total em Estoque: R$ {produto1.calcular_valor_total():.2f}\n")

    # Testando os métodos sets para o segundo objeto
    print("--- Alterando dados do Produto 2 ---")
    print(f"Preço original do Mouse: R$ {produto2.get_preco():.2f}")
    produto2.set_preco(55.00)
    print(f"Novo Preço do Mouse: R$ {produto2.get_preco():.2f}")

    print(f"Quantidade original do Mouse: {produto2.get_quantidade()}")
    produto2.set_quantidade(45)
    print(f"Nova Quantidade do Mouse: {produto2.get_quantidade()}\n")

    # Chamando todos os métodos para o segundo objeto após a alteração
    print(f"Nome atualizado: {produto2.get_nome()}")
    print(f"Código: {produto2.get_codigo()}")
    print(f"Preço atualizado: R$ {produto2.get_preco():.2f}")
    print(f"Quantidade atualizada: {produto2.get_quantidade()}")
    print(f"Novo Valor Total em Estoque: R$ {produto2.calcular_valor_total():.2f}\n")

    # Chamando todos os métodos para o terceiro objeto
    print("--- Detalhes do Produto 3 ---")
    print(f"Nome: {produto3.get_nome()}")
    print(f"Código: {produto3.get_codigo()}")
    print(f"Preço: R$ {produto3.get_preco():.2f}")
    print(f"Quantidade: {produto3.get_quantidade()}")
    print(f"Valor Total em Estoque: R$ {produto3.calcular_valor_total():.2f}")


# Executando a função main
if __name__ == "__main__":
    main()

