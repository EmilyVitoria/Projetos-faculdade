print("Bem-vindo a Loja da Emily Lima")

valor = float(input('Valor unitário: '))        # Solicita ao usuário o valor do produto
quantidade = int(input("Quantidade do produto: "))      # Solicita a quantidade de produtos
valor_total =  valor * quantidade       # Valor total da compra antes do desconto
print (f'Valor total SEM desconto: {valor_total:.2f}')

if 2500 <= valor_total <6000:
    desconto= valor_total * (4/100)     # desconto de 4% em compras de 2500 a 5999
    total = valor_total - desconto
    print(f'Valor COM desconto: {total:.2f}')   # valor total da compra com o desconto

elif 6000 <= valor_total < 10000:
    desconto2= valor_total * (7/100)    # desconto de 7% em compras de 6000 a 9999
    total = valor_total - desconto2
    print(f'Valor COM desconto: {total:.2f}')   # valor total da compra com o desconto

elif valor_total > 10000:       # desconto de 7% em compras acima de 10000
    desconto3= valor_total * (11/100)
    total = valor_total - desconto3
    print(f'Valor COM desconto: {total:.2f}')    # valor total da compra com o desconto

else:
    print('Não tem desconto!')      # Compras abaixo de 2500

 




