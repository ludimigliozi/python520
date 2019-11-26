#!/usr/bin/python3

###########
### Operadores Aritiméticos
###########

### Variáveis por nomeclatura podem ter no
### no máximo 16 caracters

num1 = 6 # numero 1
num2 = 8 # numero 2
adicao =  num1 + num2 #adiçao
subtracao = num1 + num2 #subtração
multiplicacao = num1 * num2 #multiplicação
divisao = num1 / num2 # divisão
result_div_int = num1 // num2 # Resultado de uma divisão inteira
resto_div_int = num1 % num2 # Resta de uma divisão inteira (Módulo)

# Operadores de forma abreviada
# Péga o valor atual do número e realiza um calculo
# Atribuindo oo resultado a variável

numero = 1
numero += 3 #1+2        numero = numero + 3
numero -= 4 # 4 -3      numero = numero - 3
numero *= 4 # 1 -4      numero = numero * 4
numero /= 2 # 4 / 2     numero = numero / 2
numero //=2 # 2 // 2 = 1numero = numero // 2
numero %= 2 # 2 % 2 = 0 numero = numero % 2

######
### Operadores relacionais
######

# Operadores relacionais servem para comparação entre fatores
# Retorna valores Booleanos  (true e (false)
numero1 = 6
numero2 = 9
numero3 = numero1

print(numero1 == numero2) # falso
print(numero1 != numero2) # verdadeiro
print(numero1 < numero2)  # verdadeiro
print(numero1 <= numero2) # verdadeiro
print(numero1 > numero2)  # falso
print(numero1 >= numero2) # falso
print(numeo2 is numero3)  # compara se estão alocados no mesmo bloco de memória (veradeiro)

listas1 = ['Item 1', 'Item 2', 'Item 3']
print'Item 1' in lista # Compara existências de valores em lista verdadeiro