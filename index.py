class Colaborador:
    # Construtor
    def __init__(self, nome: str, idade: int, peso: float, tem_ferias: bool):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tem_ferias = tem_ferias
        # Calculando e armazenando dentro de um atributo do objeto
        self.ano_nascimento = 2026 - self.idade

# Função sem parâmetros
def exemplo_colaborador():
    # Instância(criar) um objeto da classe Colaborador
    #         Colaborador(nome, idade, peso, tem_ferias)
    antonio = Colaborador("Antônio", 38, 108, True)


    # Calculando o ano de nascimento do Antônio
    #antonio_ano_nascimento = 2026 - antonio.idade


    marcus = Colaborador("Marcus", 40, 80, False)
    #marcus_ano_nascimento = 2026 - marcus.idade

    print("Colaborador 01: ", antonio.nome)
    print("Idade: ", antonio.idade)
    print("Ano de Nascimento: ", antonio.ano_nascimento)
    print("Peso: ", antonio.peso)
    print("Tem Férias: ", antonio.tem_ferias, end="\n\n\n")

    print("Colaborador 02: ", marcus.nome)
    print("Idade: ", marcus.idade)
    print("Ano de Nascimento: ", marcus.ano_nascimento)
    print("Peso: ", marcus.peso)
    print("Tem Férias: ", marcus.tem_ferias, end="\n\n\n")


class Aluno:
    #Método construtor
    def __init__(self, nome: str, nota1: float, nota2: float, nota3: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        #self.media = (self.nota1 + self.nota2 + self.nota3) / 3

    def calcular_media(self) -> float:
        media: float = (self.nota1 + self.nota2 + self.nota3) / 3
        return media


def exemplo_aluno():

    matheus: Aluno = Aluno("Matheus da Silva", 7, 4.5, 10)

    lukas: Aluno = Aluno("Lukas Pettry", 9.5, 9.8, 0)

    #matheus_media = (matheus.nota1 + matheus.nota2 + matheus.nota3) / 3
    matheus_media = matheus.calcular_media()

    #lukas_media = (lukas.nota1 + lukas.nota2 + lukas.nota3) / 3
    lukas_media = lukas.calcular_media()

    matheus_status = ""
    if matheus_media < 7:
        mathues_status = "Reprovado"
    else:
        matheus_status = "Aprovado"

    lukas_status = ""
    if lukas_media < 7:
        lukas_status = "Reprovado"
    else:
        lukas_status = "Aprovado"

    print("Aluno: ", matheus.nome)
    print(" Nota 1: ", matheus.nota1)
    print(" Nota 2: ", matheus.nota2)
    print(" Nota 3: ", matheus.nota3)
    print(" Média: ", matheus_media)
    print(" Status: ", matheus_status)

    print("Aluno: ", lukas.nome)
    print(" Nota 1: ", lukas.nota1)
    print(" Nota 2: ", lukas.nota2)
    print(" Nota 3: ", lukas.nota3)
    print(" Média: ", lukas_media)
    print(" Status: ", lukas_status)



class Brinquedo:
    def __init__(self, marca: str, nome: str, classificacao: int, preco: float):
        self.marca = marca
        self.nome = nome
        self.classificacao = classificacao
        self.preco = preco

def exemplo_brinquedo():

    hotwheels: Brinquedo = Brinquedo("Hotwheels", "Porsche 911", 4, 154.34)
    boneca: Brinquedo = Brinquedo("Barbie", "Barbie Princesa", 3, 224.49)

    preco_total_brinquedo: float = hotwheels.preco + boneca.preco

    print("=== Brinquedo 1 ===")
    print(f"Marca: {hotwheels.marca}")
    print(f"Nome: {hotwheels.nome}")
    print(f"Classificação: {hotwheels.classificacao}")
    print(f"Preço: {hotwheels.preco:.2f}")


    print("\n=== Brinquedo 2 ===")
    print(f"Marca: {boneca.marca}")
    print(f"Nome: {boneca.nome}")
    print(f"Classificação: {boneca.classificacao}")
    print(f"Preço: {boneca.preco:.2f}")

    print(f"\nPreço total dos brinquedos: R$ {preco_total_brinquedo:.2f}")

# Ponto de início da aplicação
#if __name__ == "__main__":
    # Executar a função do Colaborador
    exemplo_brinquedo()
    #py index.py


class Flor:
    def __init__(self, nome: str, cor: str):
        self.nome = nome
        self.cor = cor

def exemplo_flor():

    rosa: Flor = Flor("Rosa", "Vermelha")
    violeta: Flor = Flor("Violeta", "Roxa")

    print("=== Flor 1 ===")
    print("Flor: ", rosa.nome)
    print("Cor: ", rosa.cor)

    
    print("\n=== Flor 2 ===")
    print("Flor: ", violeta.nome)
    print("Cor: ", violeta.cor)

#if __name__ == "__main__":
    exemplo_flor()


class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.paginas = paginas

def exemplo_livros():

    hp: Livro = Livro("Harry Potter e o Enigma do Príncipe", "J. K. Rowling", 2005, 472)

    got: Livro = Livro("Game of Thrones: A Tormenta de Espadas", "George R. R. Martin", 2000, 800)

    total_de_paginas = hp.paginas + got.paginas

    print("=== Sexto Livro de Harry Potter ===")
    print(f"Título: {hp.titulo}")
    print(f"Autor: {hp.autor}")
    print(f"Ano de publicação: {hp.ano}")
    print(f"Número de páginas: {hp.paginas}")

    
    print("\n=== Terceiro Livro de Game of Thrones ===")
    print(f"Título: {got.titulo}")
    print(f"Autor: {got.autor}")
    print(f"Ano de publicação: {got.ano}")
    print(f"Número de páginas: {got.paginas}")

    print(f"\nTotal de páginas dos livros: {total_de_paginas}")

#if __name__ == "__main__":
    exemplo_livros()


class PesquePague:
    def __init__(self, nome: str, peso: float, preco: float):
        self.nome = nome
        self.peso = peso
        self.preco = preco

    def calcular_total_peixe(self) -> float:
        total: float = self.peso * self.preco
        return total


def exemplo_pesquepague():

    peixe1: PesquePague = PesquePague("Tilápia", 1, 20)
    peixe2: PesquePague = PesquePague("Tainha", 1.5, 29)
    peixe3: PesquePague = PesquePague("Salmão", 2.5, 79)

    #preco_peixe1 = peixe1.peso * peixe1.preco
    preco_peixe1 = peixe1.calcular_total_peixe()

    #preco_peixe2 = peixe2.peso * peixe2.preco
    preco_peixe2 = peixe2.calcular_total_peixe()

    #preco_peixe3 = peixe3.peso * peixe3.preco
    preco_peixe3 = peixe3.calcular_total_peixe()

    total_pedido = preco_peixe1 + preco_peixe2 + preco_peixe3

    print("\n=== Peixe 1 ===")
    print(f"Peixe: {peixe1.nome}")
    print(f"Peso (KG): {peixe1.peso}")
    print(f"Preço (KG): R$ {peixe1.preco:.2f}")
    print(f"Preço total: R$ {preco_peixe1:.2f}")

    
    print("\n=== Peixe 2 ===")
    print(f"Peixe: {peixe2.nome}")
    print(f"Peso (KG): {peixe2.peso}")
    print(f"Preço (KG): R$ {peixe2.preco:.2f}")
    print(f"Preço total: R$ {preco_peixe2:.2f}")


    print("\n=== Peixe 3 ===")
    print(f"Peixe: {peixe3.nome}")
    print(f"Peso (KG): {peixe3.peso}")
    print(f"Preço (KG): R$ {peixe3.preco:.2f}")
    print(f"Preço total: R$ {preco_peixe3:.2f}")

    print(f"\nPreço total do pedido: R$ {total_pedido:.2f}\n")



class Calculadora:
    def __init__(self, n1: float, n2: float):
        self.n1 = n1
        self.n2 = n2

    def somar(self) -> float:
        soma: float = self.n1 + self.n2
        return soma

    def subtrair(self) -> float:
        subtracao: float = self.n1 - self.n2
        return subtracao

    def multiplicar(self) -> float:
        multiplicacao: float = self.n1 * self.n2
        return multiplicacao

    def dividir(self) -> float:
        divisao: self.n1 / self.n2
        return self.dividir

def exemplo_calculadora():

    n1 = input("Insira o primeiro número: ")
    n2 = input("Insira o segundo número: ")







if __name__ == "__main__":
    exemplo_calculadora()