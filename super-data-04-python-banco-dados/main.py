# python mysql connector
# py -m pip install mysql-connector-python



from clientes import apagar_cliente, cadastrar_cliente, consultar_cliente, editar_cliente
from fornecedores import cadastrar_fornecedor, consultar_fornecedores
from produtos import apagar_produto, cadastrar_produto, consultar_produtos, editar_produto


def limpar_terminal():
    import os
    os.system("cls")
    
# ==================================================


# ===================================================

if __name__ == "__main__":
    menu = """MENU:
1   - Consultar produtos
2   - Cadastrar produtos
3   - Apagar produtos
4   - Editar produtos
5   - Cadastrar cliente
6   - Apagar cliente
7   - Editar cliente
8   - Consultar cliente
9   - Consultar fornecedores
10  - Cadastrar fornecedores
99  - Sair

Digite o menu desejado:"""
    menu_escolhido = int(input(menu))

    while menu_escolhido != 99:
        limpar_terminal()
        if menu_escolhido == 1:
            consultar_produtos()
        elif menu_escolhido == 2:
            cadastrar_produto()
        elif menu_escolhido == 3:
            apagar_produto()
        elif menu_escolhido == 4:
            editar_produto()
        elif menu_escolhido == 5:
            cadastrar_cliente()
        elif menu_escolhido == 6:
            apagar_cliente()
        elif menu_escolhido == 7:
            editar_cliente()
        elif menu_escolhido == 8:
            consultar_cliente()
        elif menu_escolhido == 9:
            consultar_fornecedores()
        elif menu_escolhido == 10:
            cadastrar_fornecedor()    
        else:
            print("Opção inválida")

        menu_escolhido = int(input(menu))