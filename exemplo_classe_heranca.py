#from datetime import datetime
import datetime


class ContaBancaria: # classe pai
    def __init__(self, cliente: str, saldo_inicial: float, numero: str):
        self.cliente = cliente
        self.saldo = saldo_inicial
        # encapsulamento publico
        self.numero = numero
        # encapsulamento privado fora da classe n ter acesso
        self.__quantidade_saque = 0

    def sacar(self, valor: float):
        # Ao realizar o 3 saque no mês deve gerar uma cobrança de 1,50

        if self.__quantidade_saque >= 3:
            valor = valor + 1.50

        if valor > self.saldo:
            print("Saque não realizado por falta de saldo")
            return

        self.saldo = self.saldo - valor
        print("Realizado saque de R$ ", valor, end="\n\n")
        # Incrementar a variável quantidade de saques
        self.__quantidade_saque = self.__quantidade_saque + 1

# Herança é capacidade de herdar  propiedades (caracteristicas) e função/método ( comportamentos)
# ContaCorrente é uma classe "filha" da classe ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self, cliente: str, saldo_inicial: float, numero: str, limite_credito: float):
        super().__init__(cliente, saldo_inicial, numero)
        self.limite_credito = limite_credito

    def apresentar_extrato(self):
        data_hora_atual = datetime.datetime.now() #import datetime
        # data_hora_atual = datetime.now() #import datetime from datetime

        print("Extrato: ", data_hora_atual.strftime("%d/%m/%Y %H:%M"))
        print("Cliente: ", self.cliente)
        print("Número: ", self.numero)
        print("Saldo: ", self.saldo)
        print("Limite de crédito: ", self.limite_credito, end="\n\n")


class ContaSalario(ContaBancaria):
    def __init__(self, cliente: str, saldo_inicial: float, numero: str):
        super().__init__(cliente, saldo_inicial, numero)
    # Gerar extrato
    # transferência
    # sacar

def exemplo_contas():
    conta_zeh = ContaCorrente("Zeh", 5000, "1234", 2000)
    conta_zeh.apresentar_extrato()
    conta_zeh.sacar(1000)
    conta_zeh.apresentar_extrato()

    conta_judity = ContaSalario("Judity", 145_945.00, "1235")
    conta_judity.sacar(30_000)
    # ContaSalario não tem a função apresentar_extrato, pois pertence a classe ContaCorrente
    # conta_judity.apresentar_extrato()


#=======================================================================

class Animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Nome do animal: ", self.nome)
        print("Idade do animal: ", self.idade)


class Cachorro(Animal):
    def __init__(self, nome: str, idade: int, raca: str):
        super().__init__(nome, idade)
        self.raca = raca

    def latir(self):
        print("Au Au!")

class Gato(Animal):
    def __init__(self, nome: str, idade: int, cor: str):
        super().__init__(nome, idade)
        self.cor = cor

    def miar(self):
        print("Miau!")

def exemplo_animal():
    cachorro = Cachorro("Bob", 3, "Labrador")
    cachorro.apresentar()
    cachorro.latir() 

    gato = Gato("Mingau", 2, "Branco")
    gato.apresentar()
    gato.miar()

#=================================================================

class Veiculos:
    def __init__(self, marca: str, modelo: str, velocidade_inicial: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade_inicial
        self.velocidade_inicial = 0

    def acelerar(self, valor: int):
        self.velocidade = 50
        self.nova_velocidade_acelerada = self.velocidade + valor

        print("Acelerou: ", self.nova_velocidade_acelerada)

    def frear(self, valor: int):
        if valor > 30:
            return 0
        else:
            self.velocidade = 30
            self.nova_velocidade_freada = self.velocidade - valor
            print("Freou: ", self.nova_velocidade_freada)

class Carro(Veiculos):
    def __init__(self, marca: str, modelo: str, velocidade_inicial: int, quantidade_portas: int):
        super().__init__(marca, modelo, velocidade_inicial)
        self.quantidade_portas = quantidade_portas

    def apresentar_dados(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Quantidade de portas: ", self.quantidade_portas)
        print("Velocidade atual: ", self.velocidade)

class Moto(Veiculos):
    def __init__(self, marca: str, modelo: str, velocidade_inicial: int, cilindradas: int):
        super().__init__(marca, modelo, velocidade_inicial)
        self.cilindradas = cilindradas

    def apresentar_dados(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Cilindradas", self.cilindradas)
        print("Valocidade atual: ", self.velocidade)

def exemplo_veiculos():
    carro = Carro("Volkswagen", "Golf", 0, 4)
    carro.apresentar_dados()
    carro.acelerar(20)
    carro.frear(30)

    moto = Moto("Honda", "CB 500", 0, 500)
    moto.apresentar_dados()
    moto.acelerar(30)
    moto.frear(20)


if __name__ == "__main__":
    exemplo_veiculos()


