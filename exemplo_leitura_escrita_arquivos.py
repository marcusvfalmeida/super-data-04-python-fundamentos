# Exemplo_leitura_escrita_arquivos.py

# Modos de abertura de arquivos com open():
#
# r  -> leitura (read). O arquivo deve existir.
# w  -> escrita (write). Cria o arquivo ou sobrescreve o conteúdo existente.
# a  -> anexar (append). Cria o arquivo ou adiciona conteúdo ao final.
# x  -> criação exclusiva. Cria um novo arquivo e gera erro se ele já existir.
#
# Modificadores:
# t  -> modo texto (padrão).
# b  -> modo binário (ex.: imagens, PDFs).
# +  -> permite leitura e escrita.
#
# Exemplos:
# open("arquivo.txt", "r")   # leitura
# open("arquivo.txt", "w")   # escrita/sobrescrita
# open("arquivo.txt", "a")   # adicionar ao final
# open("arquivo.txt", "r+")  # leitura e escrita
# open("arquivo.txt", "rb")  # leitura binária

from pathlib import Path
from datetime import date
from typing import Union

def criar_arquivo_txt():
    with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Olá mundo Marcus\n")
        arquivo.write("O céu está lindo\n")
        arquivo.write("Hoje não choveu")
        print("Arquivo 'mensagem.txt' criado com sucesso")


def ler_arquivo_txt():
    with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
        # Ler o arquivo por completo armazendado na variável conteudo (str)
        conteudo = arquivo.read()
    print("Conteúdo do arquivo 'mensagem.txt':")
    print(conteudo)


def adicionar_linha_arquivo_txt():
    with open("mensagem.txt", "a", encoding="utf-8") as arquivo:
        mensagem = input("Digite uma mensagem: ")
        arquivo.write(f"\n{mensagem}\n")
        print("Arquivo 'mensagem.txt' modificado com sucesso")

def ler_linhas_arquivo_txt():
    # Criar um vetor e jogar par dentro do vetor cada uma das linhas
    linhas_arquivo: list[str] = []
    with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha_limpa = linha.replace("\n", "")
            linhas_arquivo.append(linha_limpa)
        return linhas_arquivo

#if __name__ == "__main__":
    #adicionar_linha_arquivo_txt()

#if __name__ == "__main__":
    #linhas = ler_linhas_arquivo_txt()
    #print(linhas)

# ==============================================================

def criar_arquivo_csv():
    personagem = input("Digite um personagem: ")
    quantidade_missoes = int(input("Digite a quantidade de missões da noite: "))

    # Guarda a data atual
    data_hoje = date.today()

    # Define o caminho do arquivo csv
    caminho = Path("personagens.csv")

    # Verifica se o arquivo personagens.csv já existe
    if caminho.exists():
        # Informa que o arquivo já existe
        print("Arquivo de missões existe")

        # Abre o arquivo em mode de adição
        with open("personagens.csv", "a", encoding="utf-8") as arquivo:
            # Escreve uma nova linha com os dados da missão
            arquivo.write(f"{data_hoje},{personagem},{quantidade_missoes}\n")

        print("Missão registrada com sucesso")

    else:
        # Informa que o arquivo ainda não existe
        print("Não exista o arquivo de missões")

        print("Criando o arquivo de missões")

        # Abre o arquivo em modo de escrita
        with open("personagens.csv", "w", encoding="utf-8") as arquivo:
            # Escreve o cabeçalho do arquivo csv
            arquivo.write("data;personagem;quantidade\n")

            # Escreve a primeira linha com os dados da missão
            arquivo.write(f"{data_hoje},{personagem},{quantidade_missoes}\n")

        # Informa que o arquivo foi criado
        print("Arquivo de missões criado com sucesso!")

#if __name__ == "__main__":
    #criar_arquivo_csv()

# =============================================================

class Missao:
    def __init__(self, data: str, personagem: str, quantidade: int):
        self.data = data
        self.personagem = personagem
        self.quantidade = quantidade

    def __repr__(self):
        return f"Missao(data={self.data},personagem={self.personagem},quantidade={self.quantidade})"

def obter_missoes() -> list[Missao]:
    missoes: list[Missao] = []

    with open("personagens.csv", "r", encoding="utf-8") as arquivo:
        indice = 0
        for linha in arquivo:
            if indice == 0:
                indice = indice + 1
                continue
            linha = linha.replace("\n", "")
            partes = linha.split(",")

            data = partes[0]
            personagem = partes[1]
            quantidade = partes[2]
            #data, personagem, quantidade = partes

            missao: Missao = Missao(data, personagem, quantidade)
            missoes.append(missao)

            indice = indice + 1
    return missoes

def calcular_media_missoes(missoes: list[Missao]) -> float:
    soma: float = 0
    # Percorrer cada uma das missões
    for missao in missoes:
        soma = soma + missao.quantidade

    media: float = soma / len(missoes)

    return media

def descobrir_maior_quantidade_missoes(missoes: list[Missao]) -> Union[int, str]:
    maior_quantidade = 0
    personagem_maior_quantidade = ""
    for missao in missoes:
        if missao.quantidade > maior_quantidade:
            maior_quantidade = missao.quantidade
            personagem_maior_quantidade = missao.personagem
    return maior_quantidade, personagem_maior_quantidade


if __name__ == "__main__":
    missoes = obter_missoes()

    media: float = calcular_media_missoes(missoes)
    print("Média: ", media)

    maior_quantidade_missoes, personagem = descobrir_maior_quantidade_missoes
    print(personagem, "maior quantidade de missoes: ", maior_quantidade_missoes)