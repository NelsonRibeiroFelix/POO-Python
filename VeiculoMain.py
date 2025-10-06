
from aVeiculo import Veiculo
from aVeiculo import Carro

if __name__ == '__main__':

    veiculo1 = Veiculo(35000, 45000)
    veiculo2 = Veiculo(58000, 22000)


    print("Veículo 1: valor =", veiculo1.get_valor(), "km =", veiculo1.get_km())
    print("Veículo 2: valor =", veiculo2.get_valor(), "km =", veiculo2.get_km())


    veiculo1.set_valor(36000)
    veiculo1.set_km(43000)

    print("Veículo 1 atualizado: valor =", veiculo1.get_valor(), "km =", veiculo1.get_km())

    carro1 = Carro(120000, 80000, 4)
    carro2 = Carro(85000, 60000)

    print(carro1.get_valor, carro1.get_km, carro1.get_qtd_portas())
    print(carro1.get_valor, carro1.get_km, carro1.get_qtd_portas())

    carro1.set_qtd_portas(2)
    carro2.set_valor(150000)


    print(carro1.get_valor(), carro1.get_km(), carro1.get_qtd_portas())
    print(carro2.get_valor(), carro2.get_km(), carro2.get_qtd_portas())
