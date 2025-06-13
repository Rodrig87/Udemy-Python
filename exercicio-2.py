nome = input("Digite seu nome: ")
peso = float(input ("Digite seu peso: "))
altura = float(input ("Digite sua altura: "))
imc = peso / (altura * altura)

print (f"{nome} tem {altura} de altura, pesa {peso}KG e seu IMC é: {imc:.2f}")
