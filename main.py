# coding: utf-8

import json
from collections import OrderedDict    
import string
from collections import Counter


data = json.load(open("dados.json"))



def qtdCompradores():
    
    tmp  = []
    cont = 0

    for line in data:
        tmp.append(line['Login'])
    tmp = list(OrderedDict.fromkeys(tmp))    
    
    for line in tmp:
        cont += 1    
    
    print("Quantidade de Compradores!", cont)


qtdCompradores()


def qtdItensExclusivos():

    itens = []
    cont = 0
    for line in data:
        itens.append(line['Item ID'])
    
    for line in itens:
        if itens.count(line) == 1:
            cont += 1

    print("Quantidade de itens exclusivos!", cont)

qtdItensExclusivos()


def precoMediodeCompra():

    som = 0
    cont = 0
    for  line in data:
        som += line['Valor']
        cont += 1
    
    print("Preço médio de todos os produtos: R$ ", (som/cont))
    print("Quantidade de itens comprados: ", cont)
    print("Rendimento total: R$ ", som)

precoMediodeCompra()



def porcentQtdMascFemeOutros():

    qtdSex = {
    
        "M": 0,
        "F": 0,
        "X": 0
    }
    precoMedio = {

        "M": 0,
        "F": 0,
        "X": 0
    }

    for line in data:
        sex = line['Sexo']
        if sex == "Masculino":
        
            qtdSex['M'] += 1
            precoMedio['M'] += line['Valor']
        
        elif sex == "Feminino":
        
            qtdSex['F'] += 1
            precoMedio['F'] += line['Valor']
        
        else:
        
            qtdSex['X'] += 1
            precoMedio['X'] += line['Valor']


    print("Porcentagem de compradores - MASCULINO:", 100 * qtdSex['M'] / len(data), "%")
    print("Porcentagem de compradores - FEMININO:", 100 * qtdSex['F'] / len(data), "%")
    print("Porcentagem de compradores - OUTROS:", 100 * qtdSex['X'] / len(data), "%")

    print("Quantidade de compras - MASCULINO:", qtdSex['M'])
    print("Quantidade de compras - FEMININO:", qtdSex['F'])
    print("Quantidade de compras - OUTROS:", qtdSex['X'])

    print("Preço médio  - MASCULINO:", (precoMedio['M'] / qtdSex['M']))
    print("Preço médio  - FEMININO:", (precoMedio['F'] / qtdSex['F']))
    print("Preço médio  - OUTROS:", (precoMedio['X'] / qtdSex['X']))

    print("Valor total de compras - MASCULIO:", precoMedio['M'])
    print("Valor total de compras - FEMININO:", precoMedio['F'])
    print("Valor total de compras - OUTROS:", precoMedio['X'])

porcentQtdMascFemeOutros()
'''



'''


def listPrincipaisCompradores():
    
    dados = {}
    for line in data:
        dados.update({line['Valor']: line})

    for line in dados:
        pass
        #print(line)
    print(dados.pop(max(dados)))
    print(max(dados))

listPrincipaisCompradores()

