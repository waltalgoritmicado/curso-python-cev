"""
DESAFIO 024

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""

nome_cidade = str(input('Diga o nome da cidade: ')).strip().upper()
v_nome_cidade = nome_cidade.split()
print('SANTO' in v_nome_cidade[0])
