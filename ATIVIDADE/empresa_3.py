print("Bem-vindo a Copiadora da Emily Lima")

def escolha_de_servico():   # Função para escolha de serviços

    serviços = {    # Dicionário de serviços
        "DIG": 1.10,
        "ICO": 1.00,
        "IPB": 0.40,
        "FOT": 0.20
    }
       
    while True:
        print("\nEntre com o tipo de serviço desejado") # Imprime as opções
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Foto Cópia")

        escolha_servico = input("Qual o serviço desejado: ").strip() .upper()   # Solicita a escolha ao usuário

        if escolha_servico in serviços:
             return serviços [escolha_servico]  # Retorna a escolha válida para ser usada depois
        else:
            print("Escolha inválida, entre com o tipo de serviço novamente")    #Caso o cliente erre o serviço
preco_servico = escolha_de_servico()
    
def num_pagina():   # Função para escolha de serviços
    while True:
        try:
            num_pagina = int(input("\nQual o número de páginas? "))     # Solicita a escolha ao usuário
            if num_pagina < 20:     # Verifica o número de páginas
                return  num_pagina
            elif 20 <= num_pagina < 200:
                return num_pagina * 0.85
            elif 200 <= num_pagina < 2000:
                return num_pagina * 0.80
            elif 2000 <= num_pagina <20000:
                return num_pagina * 0.75
            else:
                print("Não aceitamos tantas páginas de uma vez!")   #Caso o cliente erre o número de páginas
                print("Tente novamente!")
        except ValueError:
            print("Erro! Digite um número válido")  #Caso o cliente erre o número de páginas
servico_selecionado = num_pagina()

def servico_extra():    # Função para escolha de serviços

    serviços2 = {   #
        
        "0": 0,
        "1": 15.00,
        "2": 40.00
    }
        
    while True:
        print("\n Deseja adicionar algum serviço?") # Imprime as opções
        print("01 - Encardenação Simples - R$15.00")
        print("02 - Encardenação Capa Dura - R$40.00")
        print("00 - Não Desejo mais nada")

        escolha_servico2 = input("Qual o adicional desejado? ") # Solicita a escolha ao usuário
        if escolha_servico2 in serviços2:
            return float(serviços2[escolha_servico2])   # Retorna a escolha válida para ser usada depois
        else:
            print("Escolha inválida, entre com o tipo de serviço novamente")    #Caso o cliente erre o serviço
selecionado_extra = servico_extra()  # Chama a função para escolha de serviços
total = (preco_servico * servico_selecionado) + selecionado_extra
print(f"\nTotal: R${total:.2f} \nServiço: {preco_servico:.2f} * Páginas: {servico_selecionado:.2f} + Extra: {selecionado_extra:.2f}")   # Imprime o total

            
         

    

