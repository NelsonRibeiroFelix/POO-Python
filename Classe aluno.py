class Aluno (object):
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    def get_nome(self):
        return self.nome
    def get_mensalidade(self):
        return self.mensalidade
    def get_idade(self):
        return self.idade
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_mensalidade(self, nova_mensalidade):
        self.mensalidade = nova_mensalidade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def aumento_mensalidade(self, aumento_mensalidade):
        self.mensalidade += aumento_mensalidade

if __name__ == '__main__':
    aluno1 = Aluno('Paulo', 1100.00, 21)
    aluno2 = Aluno('Emily', 1300.00, 20)

    print("- Aluno 1:")
    print("Nome:", aluno1.get_nome())
    print("Mensalidade:", aluno1.get_mensalidade())
    print("Idade:", aluno1.get_idade())


    print("- Aluno 2:")
    print("Nome:", aluno2.get_nome())
    print("Mensalidade:", aluno2.get_mensalidade())
    print("Idade:", aluno2.get_idade())


    aluno1.set_nome("Carlos")
    aluno1.set_mensalidade(1500.00)
    aluno1.set_idade(30)
    aluno1.aumento_mensalidade(200)

    aluno2.set_nome("Ana")
    aluno2.set_mensalidade(1500.00)
    aluno2.set_idade(30)
    aluno2.aumento_mensalidade(500)

    print("\nApós alteração com set_nome:")
    print("\nAluno 1 nome:", aluno1.get_nome())
    print("Aluno 1 mensalidade:", aluno1.get_mensalidade())
    print("Aluno 1 idade:", aluno1.get_idade())


    print("\nAluno 2 nome:", aluno2.get_nome())
    print("Aluno 2 idade:", aluno2.get_idade())
    print("Aluno 2 mensalidade:", aluno2.get_mensalidade())


