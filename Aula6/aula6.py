"""
Variaveis

"""
nome = input('Digite seu nome:\n')
idade = input('Digite sua idade:\n')
altura = float(input('Digite sua altura:\n'))
peso = int(input('Digite seu peso:\n'))

imc = peso/ (altura * altura )

if(imc<16):
    print(nome, 'tem', idade,'anos de idade e seu imc é', imc,'Magreza grave')
elif(imc>15 and imc<17):
    print(nome, 'tem', idade,'anos de idade e seu imc é', imc,'Magreza moderada')
elif(imc>16 and imc<18.5):
    print(nome, 'tem', idade,'anos de idade e seu imc é', imc,'Magreza leve')
elif(imc>18.4 and imc<25):
    print(nome, 'tem', idade,'anos de idade e seu imc é', imc,'Saudável!')
elif(imc>=25 and imc<31):
    print(nome, 'tem', idade,'anos de idade e seu imc é', imc,'Sobrepeso')
elif(imc>30 and imc<36):
    print(nome, 'tem', idade,'anos de idade e seu imc é', imc,'Obesidade grau 1')
elif(imc>35 and imc<40):
    print(nome, 'tem', idade,'anos de idade e seu imc é', imc,'Obesidade grau 2 (Severa)')
else:
    print(nome, 'tem', idade,'anos de idade e seu imc é', imc,'Obesidade grau 3 (mórbida)')

