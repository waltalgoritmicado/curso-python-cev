"""
DESAFIO 026

Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A".
Em que posição ela aparece na primeira vez
Em que posição ela aparece na última vez
"""
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A primeira letra "A" apareceu na posição {frase.find("A")+1}.')
print(f'A última letra "A" apareceu na posição {frase.rfind("A")+1}')
