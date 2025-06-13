import os

lista = []
while True:
    
        menu = input(str("SELECIONE UMA OPÇÃO.\n[I]nserir - [A]pagar - [L]istar: "))

        if menu.upper() == "I":
                valor = input("Valor a ser inserido: ")
                lista.append(valor)
                os.system("cls")

        elif menu.upper() == "A":
                remover = int(input("Diga o valor do produto que você quer apagar: "))
                try:
                        lista.pop(remover)
                        os.system("cls")
                except ValueError:
                        print("Você precisa digitar um número inteiro.")

                except IndexError:
                        print("Esse indice não foi encontrado.")

        elif menu.upper() == "L":
                os.system("cls")
                
                if len(lista) == 0:
                        print("Nada para listar")
                
                for indice, produtos in enumerate(lista):
                        print(indice, produtos)
        else:
                print("Digite: I, A ou L: ")

    
