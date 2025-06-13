import os

lista = []
while True:
    
    try:
        menu = input(str("SELECIONE UMA OPÇÃO.\n[I]nserir - [A]pagar - [L]istar: "))

        if menu.upper() == "I":
                valor = input("Valor a ser inserido: ")
                lista.append(valor)
                os.system("cls")

        elif menu.upper() == "A":
                remover = int(input("Diga o valor do produto que você quer apagar: "))
                lista.pop(remover)
                os.system("cls")

        elif menu.upper() == "L":
                for indice, produtos in enumerate(lista):
                        print(indice, produtos)
        else:
                continue

    except:
           continue
    

    
    
    


