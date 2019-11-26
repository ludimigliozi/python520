#!/usr/bin/python3

###### manipulando arquivos com Python
### Abrir um arquivo para modificação
### Método não recomendado

# ponteiro = open('nomedoarquivo.txt','a')
#escrita de arquivos, o modo utlizado é o read plus (que serve para leitura e escrita).
# Possuimos varios modos de acesso, por exemplo: 
# w = escrita
# r = somente leitura
# r+ = abre um arquivo para atualiação (acrescenta e modifica)
# a = complemento
# x = criação
#este método não é recomendado porque o ponteiro sempre necessit
#ser encerrado com o close, isso foi substituido com a adição do comando with
# ponteiro.write('Olá mundo\n')
# ponteiro.read()
# ponteiro.close()

### Método Usual ###
with open('nomedoarquivo2.txt','a') as arquivo:
    arquivo.write('Olá Mundo\n')
with open('nomedoarquivo2.txt','r') as arquivo:
    letras = arquivo.read()

print(letras)