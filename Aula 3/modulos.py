#!/usr/bin/python3

# import modulos.calculadora as calculadora

# soma = calculadora.somar(1,2)
# print(soma)

# from modulos.calculadora import * #somar,subtrai
# soma - somar(1,2)
# print(soma)

# print(subtrai(5,5))
# print(multiplica(3,9))

import random   # aleatório
import os       # sistema operacional
import sys      # variaveis do sistema
import datetime # data/hora
import json     # codifica/decodifica arquivo .JSON
import csv      # trabalha com planilhas   

# print(os.listdir('/home/developer/'))
# print(random.randint(1,90))

# os.system('ps -aux')
# print(sys.builtin_module_names)
# print(sys.argv)
# print(datetime.datetime.now())

# acesso = datetime.datetime(2019,1,22,00,00,00)
# atual = datetime.datetime(2019,1,22,1,00,00,00)

# print(atual - acesso)
# print(atual)

# if (atual - acesso).total_seconds() > 3600:
#         print('Seu token expirou')
# else:
#         print('acesso liberado')

#json

print(json.dumps({"nome":"Daniel", "sobrenome":"Silva"}))

print(json.loads('{"nome":"Daniel", "sobrenome":"Silva"}'))