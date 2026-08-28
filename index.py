class Colaborador:
    # Construtor
    def __init__(self, nome: str, idade: int, peso: float, tem_ferias: bool):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tem_ferias = tem_ferias

# Função sem parâmetros
def exemplo_colaborador():
    # Instância(criar) um objeto da classe Colaborador
    #         Colaborador(nome, idade, peso, tem_ferias)
    antonio = Colaborador("Antônio", 38, 108, True)


    # Calculando o ano de nascimento do Antônio
    antonio_ano_nascimento = 2026 - antonio.idade

    marcus = Colaborador("Marcus", 40, 80, False)

    print("Colaborador 01: ", antonio.nome)
    print("Idade: ", antonio.idade)
    print("Ano de Nascimento: ", antonio_ano_nascimento)
    print("Peso: ", antonio.peso)
    print("Tem Férias: ", antonio.tem_ferias, end="\n\n\n")

    print("Colaborador 02: ", marcus.nome)
    print("Idade: ", marcus.idade)
    print("Peso: ", marcus.peso)
    print("Tem Férias: ", marcus.tem_ferias, end="\n\n\n")



# Ponto de início da aplicação
if __name__ == "__main__":
    # Executar a função do Colaborador
    exemplo_colaborador()