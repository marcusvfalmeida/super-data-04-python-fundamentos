# python mysql connector
# py -m install mysql-connector-python

from mysql.connector import connect

def conectar():
    conexao = connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "admin",
        database = "helpdesk_db"
    )
    print("Conexão aberta com sucesso")
    return conexao

def consultar_categoria():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, nome, cor_categoria FROM categorias"
    )
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("Categorias:")
    for categoria in registros:
        print(categoria[0], "=>", categoria[1], "=>", categoria[2])

def cadastrar_categoria():
    nome = input("Digite o nome da categoria: ")
    cor_categoria = input("Digite a cor da categoria: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO categorias (nome, cor_categoria) VALUES (%s, %s)",
        (nome, cor_categoria)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto cadastrado com sucesso")

def limpar_terminal():
    import os
    os.system("cls")

if __name__ == "__main__":
    menu = """MENU:
1   - Consultar categoria
2   - cadastrar categoria
99  - Sair

Digite o menu desejado: """
    menu_escolhido = int(input(menu))

    while menu_escolhido !=99:
        limpar_terminal()
        if menu_escolhido == 1:
            consultar_categoria()
        elif menu_escolhido == 2:
            cadastrar_categoria()
        else:
            print("Opção inválida!")

        menu_escolhido = int(input(menu))