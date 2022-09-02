"""
Algoritmo que recebe uma lista de valores e retorna a soma e a média
Autor:Vinicius Guedes
Data:02/09/2022 10:15
"""

#Definição da função
def soma(numeros):
    soma = sum(numeros)
    print(f'A soma é {soma}')

#Função da média
def media(valores):
    avg = sum(valores) / len(valores)
    print(f'\nA média é {avg}')
    
#Criação da lista
lista=[]

for a in range(5):
    lista.append(int(input('Entre com um número: ')))
soma(lista)
media(lista)

