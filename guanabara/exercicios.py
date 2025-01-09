"""
import time

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
"""
'''
for i in range(0, 51, 2):
    print(i)
'''
'''
for i in range(0, 501):
    mut = i % 3
    if i % 2 != 0 and mut == 0:
        print(i)
'''    
'''
n = int(input('digite para saber a tabuada de um número: '))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
'''
'''
soma = 0
for i in range(1, 7):
    n = int(input('digite um número: '))
    if n % 2 == 0:
        soma = soma + n
print(f'a soma dos números pares é = {soma}')
'''
'''
t1 = int(input("digite o primeiro termo para uma PA: "))
r = int(input("digite a razão de uma PA: "))


for i in range (1, 11):
    print(t1)
    t1 = t1 + r
'''
"""
n = int(input("Digite um número para saber se ele é primo: "))

is_prime = True

for i in range(2, n):
    if n % i == 0:  
        is_prime = False
        break

if is_prime and n > 1:
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
"""
'''
import string
import re
 
phrase = input("é um palíndromo? ")
phrase = phrase.strip()
phrase = phrase.translate(str.maketrans("", "", string.punctuation))
phrase = phrase.lower()
phrase = " ".join(phrase.split())
print(phrase.replace(" ", "")[::-1])
'''
'''
for i in range (1, 8):
    an = int(input('digite seu ano de nascimento: '))
    id = 2024 - an
    if id >= 18:
        print("maior de idade")
    else:
        print("menor de idade")
'''
'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print(lanche[1])
'''
'''
numeros =  (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

n = int(input('digite um numero de 0 a 20: '))

if n > 20 or n < 0:
    while n > 20 or n < 0:
        n = int(input('tente novamente, digite um numero de 0 a 20: '))

print(n)
'''
'''
def linha():
     print(30*"-")

linha()
'''
'''
def placa(frase):
    print(30*'-')
    print(frase)
    print(30*'-')

fraseA = 'matheus hisamoto'
fraseB = 'fui na praia ontem'
fraseC = 'o mar está bom'

placa(fraseA)
placa(fraseB)
placa(fraseC)
'''
'''
def soma(a, b):
    s = int(a) + int(b)
    return s

while True:
    a = (input('digite um número ou digite sair: '))
    if a == 'sair':
        break
    b = (input('digite um número: '))
    print(soma(a, b))
'''
'''
def area(b, h):
    arear = b * h 
    return arear

def mensagem( b, h, area): 
    print(f'A área de um terreno {b}X{h} é de {area}m².')


b = float(input("digite o tamanho em metros da base do seu terreno: "))
h = float(input("digite o tamanho em metros da altura do seu terreno: "))

mensagem(b, h, area(b, h))
'''
'''
def escreva(frase, tam):
    print((tam + 2)*'~')
    print(f' {frase} ')
    print((tam + 2)*'~')
    

frase = input('digite uma frase: ')
tam = len(frase)

escreva(frase, tam)
'''
'''
inicio = 1
fim = 11
passo = 1
def contagem(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        print(i)

contagem(inicio, fim, passo)

inicio1 = 10
fim1 = -1
passo1 = -2
def contagem1(inicio1, fim1, passo1):
    for i in range(inicio1, fim1, passo1):
        print(i)

contagem1(inicio1, fim1, passo1)


inicio2 = int(input("digite um inicio inteiro: "))
fim2 = int(input("digite um fim inteiro: "))
passo2 = int(input("digite um passo inteiro: "))

if fim2 > 0:
    fim2 = fim2 + 1
else:
    fim2 = fim2 - 1


if inicio2> fim2:
    passo2 = passo2*(-1)

if passo2 == 0:
    passo2 = 1
    
def contagem2(inicio2, fim2, passo2):
    for i in range(inicio2, fim2, passo2):
        print(i)

contagem2(inicio2, fim2, passo2)
'''



























