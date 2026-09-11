# exemplo_dicionarios.py

def exemplo_dicionario_simples():
    # Dicionário um lugar onde é possível armazenar valor utilizando uma chave
    # dict[chave, valor]
    carros: dict[str, str] = {}

    # Armazenar um dado no dicionário passando o nome da chave "vw"
    carros["vw"] = "Fusca"
    carros["gm"] = "Opala"
    carros["byd"] = "Dolphin"

    # Acessar o valor armazenado na chave "vw"
    print("Valores armazendados nos dicionários: ")
    print(carros["vw"])
    print(carros["gm"])
    print(carros["byd"])

    print("\n\n")
    print("Chaves: ", carros.keys())
    print("valores: ", carros.values())


def exemplo_dicionario_complexo():
    alunos: dict[str, dict[str | int]] = {}

    alunos["855224"] = {
        "nome": "Pedro",
        "idade": 23,
        "cpf": "001.001.001-01",
    }

    alunos["855225"] = {
        "nome": "Judity",
        "idade": 39,
        "cpf": "999.999.999-99"
    }

    print("Nome da Judity: ", alunos["855225"]["nome"])
    print("Idade da Judity: ", alunos["855225"]["idade"])
    print("CPF da Judity: ", alunos["855225"]["cpf"])

if __name__ == "__main__":
    exemplo_dicionario_complexo()