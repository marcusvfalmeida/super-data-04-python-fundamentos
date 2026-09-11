def exemplo_lista_simples():
    #CRUD Create, Read, Update e Delete

    # Criando uma lista com um elemento
    colegas: list[str] = ["Pedro"]
    # Adicionar elementos na lista/vetor
    colegas.append("Judity")
    colegas.append("Juliana")
    colegas.append("Francisco")

    # Remover elemento da lista
    colegas.remove("Francisco")

    # Alterando o nome da Juliana da terceira posição
    colegas[2] = "Liana"

    # Apresentando a quantidade de elementos da lista
    print("Quantidade de colegas: ", len(colegas))

    # Apresentar os elementos da lista
    print("Primeiro colega: ", colegas[0])
    print("Segundo colega: ", colegas[1])
    print("Terceiro colega: ", colegas[2])

#if __name__ == "__main__":
    #exemplo_lista_simples()


def exemplo_lista_simples_int():
    numeros: list[int] = []

    # Solicitar um número e adicionar na lista(posição 0)
    numeros.append(int(input("Digite um número: ")))
    numeros.append(int(input("Digite um número: ")))
    numeros.append(int(input("Digite um número: ")))

    soma: int = numeros[0] + numeros[1] + numeros[2]
    print("Soma: ", soma)

# =======================================================

def exemplo_lista_simples_percorrendo():
    salarios: list[float] = []

    # quantidade_desejada: int = int(input("Digite a quantidade de salários: "))

    # Solicitar para o usuário 4 salários
    for i in range(0, 4):
        salario = float(input("Digite o salário: "))

        salarios.append(salario)

    # soma = salario[0] + salario[1] + salario[2] + salario[3]
    soma: float = 0
    for i in range(0, 4):
        soma = soma + salarios[i]

    # Qual o maior salário
    maior_salario: float = 0
    for i in range(0, 4):
        salario_atual = salarios[i]
        if salario_atual > maior_salario:
            maior_salario = salario_atual

    # Qual o menor salário
    menor_salario: float = 999999999999
    for i in range(0, 4):
        salario_atual = salarios[i]
        if salario_atual < menor_salario:
            menor_salario = salario_atual

    media: float = soma / len(salarios)

    # Apresentar os salários
    for i in range(0, 4):
        salario_atual: float = salarios[i]
        print(f"Salário {i + 1}º: R$ {salario_atual}")

    print("Soma: ", soma)
    print("Média: ", media)
    print("Menor salário: ", menor_salario)
    print("Maior salário: ", maior_salario)

# ================= Exercício 01 ==================

def exemplo_lista_produtos():
    produtos: list[str] = []

    produtos.append("Coca-Cola")
    produtos.append("Ovomaltine")
    produtos.append("Chocoleite")
    produtos.append("Oreo")
    produtos.append("Doritos")

    print("Lista de produtos: ", produtos)

    produtos[4] = "Fandangos"
    produtos.remove("Ovomaltine")
    produtos.append("Kinder Ovo")
    produtos.append("Monster")

    print("Nova lista: ", produtos)
    print("A quantidade de produtos da nova lista: ", len(produtos))

# =========================== Exercício 02 ================================

def exemplo_jogos():
    jogos: list[str] = []
    precos: list[float] = []

    for i in range (0, 4):
        jogo = str(input("Digite um jogo: "))
        preco = float(input("Digite o preço: "))

        jogos.append(jogo)
        precos.append(preco)


    #print("Jogos da lista: ", jogos)
    #print("O preços dos jogos: ", )

    for i in range(0, 4):
        jogo: str = jogos[i]
        preco: float = precos[i]
        print(f"\nJogo: {jogo} -> Preço: R$ {preco:.2f}\n")

    somar_preco = 0
    for i in range (0, 4):
        somar_preco = somar_preco + precos[i]

    print(f"Total de preços dos jogos: R$ {somar_preco:.2f}\n")

if __name__ == "__main__":
    exemplo_jogos()