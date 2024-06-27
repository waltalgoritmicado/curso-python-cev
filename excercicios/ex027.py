"""
DESAFIO 027

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último separadamente.

Ex: Ana Maria de Souza

Primeiro = Ana
Último = Souza
"""
nome_completo = str(input('Digite o seu nome completo: ')).strip()
primeiro_nome = nome_completo.split()[0]
ultimo_nome = nome_completo.split()[-1]
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')
