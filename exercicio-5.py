"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


try:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f"{numero} é um número par.")

    else:
        print(f"{numero} é um número ímpar.")

except:
    print("Você não digitou um número inteiro")





hora = float(input("Digite a hora: "))
try:
    if hora >= 0 and hora <= 11:
        print("Bom dia!")

    elif hora > 11 and hora <= 17:
        print("Boa tarde!")

    elif hora > 17 and hora <= 23:
        print("Boa noite!")

    else:
        print("Essa hora não existe")
except:
    print("Você precisa digitar numero inteiros")



nome = input("Digite seu primeiro nome: ")
cont = len(nome)

if cont < 5:
    print(f"{nome}, seu nome é curto")

elif cont < 7:
    print(f"{nome}, seu nome é normal")

else:
    print(f"{nome}, seu nome é grande")

