"""
Faça um Programa em python 3.5 que leia um vetor (lista) de 10 (dez) números inteiros, mostre a soma de todos os
números, a multiplicação de todos os números e os próprios números.
"""
numeros = []
soma = 0
multiplicacao = 1

for i in range(5):
    numero_digitado = int(input('Por favor, digite um número inteiro: '))
    numeros.append(numero_digitado)

    soma = soma + numero_digitado
    multiplicacao = multiplicacao * numero_digitado

print('A soma dos números digitados é: ', soma)
print('A multiplicação dos números digitados é: ', multiplicacao)
print('Todos os números digitados são: ', numeros)
