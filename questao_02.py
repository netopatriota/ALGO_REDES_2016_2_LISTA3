"""
Faça um programa que leia 20 (vinte) números inteiros usando uma estrutura de repetição em python 3.5 (for para python)
e armazene-os num vetor (lista). Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os
três vetores (listas).
"""
numeros = []
par = []
impar = []

for i in range(20):
    numero_digitado = int(input('Por favor, digite um número inteiro: '))
    numeros.append(numero_digitado)

    if numero_digitado % 2 == 0:
        par.append(numero_digitado)
    else:
        impar.append(numero_digitado)

print('Esses são os números pares: ', par)
print('Esses são os números ímpares: ', impar)
print('Esses são todos os números digitados: ', numeros)
