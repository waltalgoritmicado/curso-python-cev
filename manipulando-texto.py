"""
Manipulando Textos
Curso em Vídeo
"""
frase = 'Curso em Vídeo Python'
print(frase)
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise
print(len(frase))
# Case-sensitive
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print('Hello' in frase)
print('Walt' in frase)

# Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

new_frase = '   Aprenda Python  '
print(new_frase)
print(new_frase.strip())
print(new_frase.rstrip())
print(new_frase.lstrip())

# Divisão
print(frase.split())
# Junção
print('-'.join(frase))

# PRÁTICA
