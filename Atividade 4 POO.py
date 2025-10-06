# funcionario
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    # Métodos get
    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    # Métodos set
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_salario(self, novo_salario):
        self.salario = novo_salario

#Gerente
class Gerente:
    def __init__(self, nome, salario, quantidade_funcionarios):
        self.nome = nome
        self.salario = salario
        self.quantidade_funcionarios = quantidade_funcionarios

    # Métodos get
    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def get_quantidade_funcionarios(self):
        return self.quantidade_funcionarios

    # Métodos set
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_salario(self, novo_salario):
        self.salario = novo_salario

    def set_quantidade_funcionarios(self, nova_quantidade):
        self.quantidade_funcionarios = nova_quantidade

#Contém o código principal (main) para instanciar, testar e alterar os objetos.
# main.py

from funcionario import Funcionario, Gerente

if __name__ == '__main__':
    # Criando dois objetos da classe Funcionario
    f1 = Funcionario("Ana", 3000)
    f2 = Funcionario("Bruno", 4500)

    print("Funcionário 1:", f1)
    print("Funcionário 2:", f2)

    # Testando os métodos get
    print("Nome do funcionário 1:", f1.get_nome())
    print("Salário do funcionário 1:", f1.get_salario())

    print("Nome do funcionário 2:", f2.get_nome())
    print("Salário do funcionário 2:", f2.get_salario())

    # Alterando com os métodos set
    f1.set_nome("Ana Paula")
    f1.set_salario(3500)
    print("Funcionário 1 atualizado:", f1.get_nome(), "-", f1.get_salario())

    # Criando dois objetos da classe Gerente
    g1 = Gerente("Carlos", 6000, 5)
    g2 = Gerente("Daniela", 7500, 10)

    print("Gerente 1:", g1)
    print("Gerente 2:", g2)

    # Testando os métodos get
    print("Nome do gerente 1:", g1.get_nome())
    print("Salário do gerente 1:", g1.get_salario())
    print("Quantidade que gerencia:", g1.get_quantidade_funcionarios())

    # Alterando com os métodos set
    g2.set_nome("Daniela Souza")
    g2.set_salario(8000)
    g2.set_quantidade_funcionarios(12)
    print("Gerente 2 atualizado:", g2.get_nome(), "-", g2.get_salario(), "-", g2.get_quantidade_funcionarios())
