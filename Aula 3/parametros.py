#!/usr/bin/python3

''' Parametros Python

Documentação'''

####
## parâmetros de função
####

# def retorna_pessoa(nome,idade=99):
#     print(f'nome: {nome}\n idade: {idade}')

# retorna_pessoa('Daniel',idade='19')

# ### Especificar tipo de parâmetro e retorno

# def retorna_valor_int( inteiro : int) -> int:
#         inteiro int(inteiro)
#         return int(inteiro)

# print(return_valor_int('i'))

#print('olá','mundo')

### Função com multipos fatores

# def funcao_multi_valores(parametros_estaticos,*argumento_variavel):
#     print(parametros_estaticos, 'parametro estático')
#     print(argumento_variavel)
    #Fazendo acesso aos parâmetros
    # for argumento in argumento_variável:
    #     print(argumento)
# funcao_multi_valores('valor estático orbigatório',
#                     'Daniel','Andressa','Lucas')

## Argumentos com palavra cahve -kwargs

# def parametros_chave_valor(**dados):
#     if dados['nome'] == 'Daniel':
#         print('Acesso Negado')
#     else:
#         print('Permitido')


# Execução método 1
# print('Método 1')
# parametros_chave_valor(nome='Daniel',sobrenome='Silva',idade=19,sexo='Masculino')

# # Execução método 2
# print('Método 2')
# dados_requisição = {'nome':'Luciano','Sobrenome':'Silva','Profissao':'Operador'}

# *parametros_chave_valor(**dados_requisição)

## Decoradores de função
# uma função que modificao valor de outra
#declara uma função com uma variavel funcao orbigatoria

def mudaCor(funcao):
    def modificaAzul(retorno_funcao):
        return f'\033[91m{retorno_funcao}\033[0m'
    return modificaAzul
@mudaCor
def log(texto):
    return texto

print(log('oi'))

