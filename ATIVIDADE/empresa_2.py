print ("Bem-vindo a Loja de Gelados da Emily Lima")

print ("-------------------Cardápio------------------"); #Itens do cardápio
print ("-" * 45)
print ("---| Tamanho | Cupuaçu (CP) | Açai (AC) | ---")
print ("---|    P    |   R$ 9.00    | R$ 11.00  | ---")
print ("---|    M    |   R$ 14.00   | R$ 16.00  | ---")
print ("---|    G    |   R$ 18.00   | R$ 20.00  | ---")
print ("-" * 45)

total = 0    # Variável para somar o total dos pedidos

while True:     # Loop principal para processar os pedidos
    while True:
        sabor = input('\nQual sabor você deseja (CP / AC)? ')   # Escolha do sabor
    
        if sabor == "CP" or sabor == "AC":
            break
        else:
         print('Sabor inválido. Tente novamente')   #Caso o cliente erre o sabor

    
    while True:
        tamanho = input('Qual tamanho você deseja (P / M / G)? ')# Escolha do tamanho
    
        if tamanho == "P" or tamanho == "M" or tamanho == "G":
            break
        else:
             print('Tamanho inválido. Tente novamente')     #Caso o cliente erre o tamanho

    if sabor == "CP":       # Determinado o valor do pedido de acordo com o tamanho
        if tamanho == "P":
            print("Você pediu um CUPUAÇU no tamanho P: R$9.00")     #Imprime o pedido
            total += 9
        elif tamanho == "M":
            print("Você pediu um CUPUAÇU no tamanho M: R$14.00")
            total += 14
        elif tamanho == "G":
            print("Você pediu um CUPUAÇU no tamanho G: R$18.00")
            total += 18

    if sabor == "AC":  
        if tamanho == "P":
            print("Você pediu um AÇAI no tamanho P: R$11.00")
            total += 11
        elif tamanho == "M":
            print("Você pediu um AÇAI no tamanho M: R$16.00")
            total += 16
        elif tamanho == "G":
            print("Você pediu um AÇAI no tamanho G: R$20.00")
            total += 20

    valor = input("\nDeseja mais alguma coisa? (S / N): ")  # Pergunta se o clienter quer pedir algo mais
    if valor == "S":
        continue    # Volta para o início e começa um novo pedido
    elif valor == "N":
        print(f"\nValor total a ser pago: R${total:.2f}")
        print('Obrigado pela compra!')
        exit()  # Encerra o programa
    else:
        print("Opção inválida! Digite S para continuar ou N para encerrar")
