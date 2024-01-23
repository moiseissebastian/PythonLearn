#Programa que calcula o IMC do usuário

nome = input('Qual o seu nome? ')
altura = float(input('Qual a sua altura? '))
peso = int(input('Qual o seu peso? '))


imc = peso / altura ** 2

print(f'\n{nome} tem de {altura:.2f},\npesa {peso} quilos e seu IMC é\n{imc:.2f}')