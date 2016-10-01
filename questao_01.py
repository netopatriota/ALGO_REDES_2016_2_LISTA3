"""
1) Você foi contratado como programador do FBI (Federal Bureau of Investigation) nos EUA que está com a necessidade de
utilizando listas em python 3.5 desenvolver um programa que faça 5 (cinco) perguntas para uma pessoa sobre um crime.
As perguntas são:
a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente (sim) a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".
"""
print('Olá, houve um crime em sua região e estamos coletando informações para tentar encontrar o suspeito. Por favor, responda as perguntas a seguir apenas com SIM ou NAO')


for i in range(10):
    contador_de_sim = 0
    contador_de_nao = 0
    respostas = [input('Telefonou para a vitima? '),
                input('Esteve no local do crime? '),
                input('Mora perto da vitima? '),
                input('Devia para a vitima? '),
                input('Ja trabalhou com a vitima? ')]

    for resposta in respostas:
        if resposta.upper() == 'SIM':
            contador_de_sim = contador_de_sim + 1
        else:
            contador_de_nao = contador_de_nao + 1

    if contador_de_sim == 5:
        print('\nVocê foi considerado como: Assassino \n')
        break
    elif contador_de_sim > 2 and contador_de_sim <= 4:
       print('\nVocê foi considerado como: Cúmplice \n')
    elif cont_sim == 2:
       print('\nCVocê foi considerado como: Suspeito \n')
    else:
       print('\nVocê foi considerado como: Inocente \n')

