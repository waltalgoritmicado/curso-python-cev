"""
DESAFIO 020

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
"""

from random import shuffle

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista_alunos)
print(f'A ordem de apresentação será a seguinte:\n{lista_alunos}')
