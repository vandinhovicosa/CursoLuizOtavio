"""
Formatando Strings
"""
nome = 'Vanderson'
idade = 41
altura = 1.75
peso = 76
ano_atual = 2021
imc = peso / (altura **2)
nasceu = ano_atual - idade

print('{} nasceu em {} e tem {} de altura.'.format(nome, nasceu, altura))
print('{} tem {} anos de idade e seu imc é {:.2f} tendo Obesidade grau 3 (mórbida)'.format(nome, idade, imc))

