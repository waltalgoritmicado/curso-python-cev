"""
DESAFIO 023

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus dígitos separados

Ex:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
num = int(input('Digite um número de 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 100
milhar = num // 1000 % 1000
print(f'''
Você digitou o número {num}...
unidade: {unidade}
dezena: {dezena}
centena: {centena}
milhar: {milhar}
''')
