"""
DESAFIO 022

Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras total  (sem considerar espaços)
Quantas letras tem o primeiro nome
"""

nome_completo = str(input('Digite o seu nome completo: '))
maiusculas_nome_completo = nome_completo.upper()
minusculas_nome_completo = nome_completo.lower()
q_letras_nome_completo = len(nome_completo.strip())
Dq_letras_primeiro_nome = nome_completo.split()
q_letras_primeiro_nome = len(Dq_letras_primeiro_nome[0])


print(f'''
O nome digitado é: {nome_completo}
O seu nome com todas as letras MAÍUSCULAS {maiusculas_nome_completo}
O seu nome com todas as letras minúsculas {minusculas_nome_completo}
O seu nome completo tem {q_letras_nome_completo}  letras.
O seu primeiro nome tem {q_letras_primeiro_nome} letras.
''')
