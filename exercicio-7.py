while True:

    try:
        n1 = int(input('Digita o primeiro número: '))  
        n2 = int(input('Digita o segundo número: '))
        operacao = input ("Digite o operador: [+] para somar, [-] subtrair, [*] multiplicar, [/] dividir:  ")

        

        if operacao == '+':
                somar = n1 + n2
                print(f'O resultado da sua soma é: {somar}')

        elif operacao == '-':
                subtracao = n1 - n2
                print(f'O resultado da sua subtração é: {subtracao}')

        elif operacao == '*':
                multiplicacao = n1 * n2
                print(f'O resultado da sua multiplicação é: {multiplicacao}')

        elif operacao == '/':
                divicao = n1 / n2
                print(f'O resultado da sua multiplicação é: {divicao}')
        
        else:
            print("Operador inválido")
            continue
                    
                
        sair = input("Você deseja fazer mais calculos? [N]ão: ").lower().startswith('n')

        if sair is True:
                break
    except:
        print("Você precisa digitar números inteiros.")
        
    

