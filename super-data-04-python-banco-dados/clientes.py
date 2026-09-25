from banco_dados import conectar


def consultar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, nome, cnpj FROM clientes"
    )
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("Clientes: ")
    for cliente in registros:
        print(cliente[0], "=>", cliente[1], "=>", cliente[2])

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cnpj = input("Digite o CNPJ do cliente: ")
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO clientes (nome, cnpj) VALUEs (%s, %s)", (nome, cnpj)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cliente cadastrado com sucesso")

def apagar_cliente():
    id_cliente = int(input("Digite o ID do cliente para apagar: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("Delete from clientes WHERE id = %s", (id_cliente,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cliente apagado com sucesso")

def editar_cliente():
    id_cliente = int(input("Digite o ID do produto para editar: "))
    novo_nome = input("Digite o nome do cliente: ")
    novo_cnpj = input("Digite o CNPJ: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE clientes SET nome = %s, cnpj = %s WHERE id = %s",
        (novo_nome, novo_cnpj, id_cliente)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto alterado com sucesso")

