# Faça um programa que crie uma matriz aleatoriamente.
# O tamanho da matriz deve ser informado pelo usuário.

import random

l = int(input("Número de linhas: "))
c = int(input("Número de colunas: "))

ma = [[random.randint(0, 100) for _ in range(c)] for _ in range(l)]

print("\nMatriz aleatória:  ")
for linha in ma:
    print(linha)
