# Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Gerenciamento de Livros! Desenvolvido por [Seu Nome]")

# Lista para armazenar os livros e variável global para controle de IDs
lista_livro = []
id_global = 0

def cadastrar_livro(id):
    """Função para cadastrar um livro no sistema."""
    try:
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o nome do autor: ")
        editora = input("Digite o nome da editora: ")
        livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
        lista_livro.append(livro.copy())
        print("Livro cadastrado com sucesso!\n")
    except OSError as e:
        print(f"Erro de entrada/saída: {e}")

def consultar_livro():
    """Função para consultar livros no sistema."""
    while True:
        print("\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor\n4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            for livro in lista_livro:
                print(livro)
        elif opcao == "2":
            try:
                id_consulta = int(input("Digite o ID do livro: "))
                livro_encontrado = next((livro for livro in lista_livro if livro["id"] == id_consulta), None)
                if livro_encontrado:
                    print(livro_encontrado)
                else:
                    print("Livro não encontrado.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
        elif opcao == "3":
            autor_consulta = input("Digite o nome do autor: ")
            livros_autor = [livro for livro in lista_livro if livro["autor"] == autor_consulta]
            if livros_autor:
                for livro in livros_autor:
                    print(livro)
            else:
                print("Nenhum livro encontrado para esse autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

def remover_livro():
    """Função para remover um livro pelo ID."""
    while True:
        try:
            id_remover = int(input("Digite o ID do livro a ser removido: "))
            for livro in lista_livro:
                if livro["id"] == id_remover:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!\n")
                    return
            print("ID inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Menu principal
while True:
    print("\nMENU PRINCIPAL")
    print("1. Cadastrar Livro\n2. Consultar Livro\n3. Remover Livro\n4. Encerrar Programa")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida.")