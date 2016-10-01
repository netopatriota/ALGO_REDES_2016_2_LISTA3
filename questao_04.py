"""
Você foi contratado como desenvolvedor da empresa EMC que está com a necessidade de, utilizando listas em python 3.5,
desenvolver um programa que faça a classificação de seus usuários quanto ao conhecimento desses usuários em Informática.
 Para isso você vai escrever um programa que faça 5 (cinco) perguntas aos usuários. As perguntas são:
a) "Sabe ligar um computador ?"
b) "Já trabalhou com o Windows 3.5 ?"
c) "Já usou disquete ?"
d) "Sabe desligar o computador ?”
e) Sabe programar em python ?"
O programa deve no final emitir uma classificação sobre o conhecimento a pessoa em Informática. Se a pessoa responder
positivamente “sim” a 5 questões ela deve ser classificada como "Hacker", entre 3 e 4 como "Sabe alguma coisa", se ela
responder “sim” para 2 respostas deve ser classificada como "Tá aprendendo" e se responder somente um único “sim” exibir
a mensagem “Sabe de nada, inocente!!!”.
"""

print('Olá, estamos fazendo um questionário com os usuarios da empresa EMC para medir o nível de conhecimento em informática. Gostaria que você participasse respondendo o questionário a seguir com SIM OU NAO')

perguntas = ["Sabe ligar um computador?",
             "Já trabalhou com o Windows 3.5?",
             "Já usou disquete?",
             "Sabe desligar o computador?",
             "Sabe programar em python?"]
soma = 0

for contador in range(5):
    print(perguntas[contador])
    resposta = input("Responda, sim ou nao: ")
    if resposta == "sim":
        soma = soma + 1

if soma == 5:
    print("Hacker")
elif soma == 3 or soma == 4:
    print("Sabe alguma coisa")
elif soma == 1:
    print("Tá aprendendo")
else:
    print("Sabe de nada, inocente!!!")