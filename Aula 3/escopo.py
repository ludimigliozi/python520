#!/usr/bin/python3

## Escopoe de variaveis locais e globais

# variavel global
variavel = 3

def muda_variavel():
    # variavel local
    global variavel
    variavel = 2 #escopo local
    print(variavel)

muda_variavel()

print(variavel)