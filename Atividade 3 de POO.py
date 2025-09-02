class veiculo:
        def __init__(self, modelo, ano, valor):
            self.modelo = modelo          
            self.ano = ano
            self.valor = valor
        
        #Métodos get
        def get_modelo(self):
            return self.modelo
        def get_ano(self):
            return self.ano
        def get_valor(self):
             return self.valor
        
        #Métodos set
        def set_modelo(self, novo_modelo):
             self.modelo = novo_modelo
        def set_ano(self, novo_ano):
             self.ano = novo_ano
        def set_valor(self, novo_valor):
             self.valor = novo_valor
        
        def mostra_dados(self):
            print(f"Modelo: {self.modelo}")
            print(f"Ano {self.ano}")
            print(f"Valor:R$ `{self.valor:.2f}")
        def aumenta_valor(self, valor_aumentado):
             self.valor = self.valor + valor_aumentado

if __name__ == '__main__':
     carro1 = veiculo('HB20', 2022, 80000.00)
     print("Carro 1 objeto:", carro1)
     carro2 = veiculo('Corolla', 2024, 190000.00)
     print("Carro 2 objeto:", carro2)

     print (carro1)
     print(type(carro1))
     retorno= carro1.get_modelo()
     print("Dados do carro 1: \nModelo:", retorno)
     print("Dados do carro 1:\nModelo:", carro1.get_modelo())
     
     #CONSULTA
     print("Ano:", carro1.get_ano())
     print(f"Valor:R$ {carro1.get_valor():.2f}")
     print("Dados do carro 2: \nModelo:", carro2.get_modelo())
     print("Ano:", carro2.get_ano())
     print(f"Valor:R$ {carro2.get_valor():.2f}")
     
     #Altera o valor e confirma a alteração
carro1.set_modelo('HB20')
print("Modelo atualizado:", carro1.get_modelo())
    
    #Altera o valor e confirma a alteração
carro2.set_valor(122000.00)
print("Valor atualizado:R$",carro2.get_valor())

carro1.mostra_dados()
carro2.mostra_dados()

#Passa o argumento do novo valor
carro1.aumenta_valor(1900.00)

#Confirma
print("Valor atualizado:", carro1.get_valor())

vl_aumento = float(input("Valor aumentado:"))
print("Valor atualizado com input:", carro2.get_valor())