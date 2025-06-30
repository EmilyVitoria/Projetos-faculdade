print("Bem-vindo a Livraria da Emily Lima")     #Mensagem de boas-vindas


lista_livro=[]  #Lista para armazenar os livros
id_global=0     #Variavel global para controle de IDs

def cadastrar_livro(id):    #Função para cadastrar um livro no sistema
    print('-' * 44)
    print(" " * 12 ,"MENU CADASTRAR LIVRO")
    print('-' * 44)
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o nome do autor: ')
    editora = input('Digite o nome da editora: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}    #Dicionário para armazenar os dados do livro
    lista_livro.append(livro.copy())    #Adiciona o livro na lista
    print(f'Livro cadastrado com sucesso! ID: {id}\n')
    

def consultar_livro():      #Função para consultar livros no sistema
    while True:
        print('-' * 44)
        print(' ' * 10 + 'MENU CONSULTAR LIVRO')
        print('-' * 44)

        print("\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor\n4. Retornar ao menu")     #Menu
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:      #Opção para consultar todos os livros
            for livro in lista_livro:
                print(f"\nID: {livro['id']}, \nNome: {livro['nome']}, \nAutor: {livro['autor']}, \nEditora: {livro['editora']}")    #Imprime os dados dos livros
        elif opcao == 2:    #Opção para consultar um livro pelo ID
            id = int(input("Digite o ID do livro: "))
            livro_encontrado =  next((livro for livro in lista_livro if livro["id"] == id), None)   #Busca o livro pelo ID
            if livro_encontrado:
                print(f"\nID: {livro_encontrado['id']}, \nNome: {livro_encontrado['nome']}, \nAutor: {livro_encontrado['autor']}, \nEditora: {livro_encontrado['editora']}")
            else:
                print("Livro não encontrado.") 
        elif opcao == 3:    #Opção para consultar livros pelo autor
            autor_consulta = input("Digite o nome do autor: ")
            livro_autor= [livro for livro in lista_livro if livro["autor"] == autor_consulta]   #Busca os livros pelo autor
            if livro_autor:
                for livro in livro_autor:
                    print(f"\nID: {livro['id']}, \nNome: {livro['nome']}, \nAutor: {livro['autor']}, \nEditora: {livro['editora']}")    #Imprime os dados dos livros
            else:
                print('Nenhum livro encontrado para esse autor.')
        elif opcao == 4:    #Opção para sair do menu
            break
        else:
            print("Opção inválida.")
  

def remover_livro():    #Função para remover um livro
    while True:
        try:
            id_remove = int(input("Digite o ID do livro a ser removido: "))    #Recebe o ID do livro
            for livro in lista_livro:
                if livro["id"] == id_remove:        #Verifica se o livro existe
                    lista_livro.remove(livro)       #Remove o livro
                    print("Livro removido com sucesso!\n")
                    return
            print("ID inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

while True:
    print('-' * 44)
    print(" " * 14 ,"MENU PRINCIPAL")
    print('-' * 44)
    print("\n1- Cadastrar Livro\n2- Consultar livro\n3- Remover Livro\n4- Encerrar Programa")   #Opções
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    if opcao == 1:      #Opção para cadastrar um livro
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == 2:    #Opção para consultar livros
        consultar_livro()   
    elif opcao == 3:    #Opção para remover um livro
        remover_livro()
    elif opcao == 4:    #Opção para encerrar o programa
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida.")

