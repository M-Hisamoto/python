'''
print(10+(20*30))
print((4**2)/30)
print(((9**4)+2*6-1))
'''
'''
print(10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2)
print('Meu nome e Matheus Hisamoto de Souza')
'''
'''
a = 3
b = 5
print((2*a)+(3*b))
'''
'''
a = int(input('digite um valor para variavel: '))
b = int(input('digite um valor para variavel: '))
c = int(input('digite um valor para variavel: '))
print(a+b+c)
'''
'''
b = 4
h = 12
a = b*h
print(f'a Area do retangulo e: {a}')
'''
'''
sal = 1500
print(f'parabens voce foi promovido e seu salario vai aumentar de RS{sal}, para RS{sal+(sal*0.15)}')
'''
'''
dinero = 125
print(f'que pena houve uma redução de cinco por cento no seu bonus {dinero-(dinero*0.05)}')
'''
'''
a = 4
b = 10
c = 5.0
d = 1
f = 5

print(a == c) #False
print(a < b) #True
print(d > b) #False
print(c != f) #False
print(a == b) #False
print(c < d) #False
print(b > a) #True
print(c >= f) #True
print(f >= c) #True
print(c <= c) #True
print(c <= f) #True
'''
'''
na = int(input('sua nota: '))
nb = int(input('sua nota: '))
nc = int(input('sua nota: '))

media = na + nb + nc // 3
if media >= 8:
    print('parabens voce passou')
'''
'''
salario = int(input('seu salário aqui: '))
if salario > 1200:
    print(f'te sobrou so isso aqui cara {salario-(salario*0.17)}')
else:
    print('pois e mano ta foda mesmo fique com seu salario')
'''
'''
a = True
b = False

print(a and b)
print(b and not a)
print(a or b)
print(a and b or not b)
print(not b)
'''
''' 
print('olá gostaria de conseguir um empréstimo?')
idade = int(input('digite sua idade: '))
salario = int(input('digite aqui o seu salário: '))

if idade >= 18 and salario >= 2000:
    print('ok, tudo certo pode pegar seu emprestimo')
else:
    print('perdão, tente novamente mais tarde')
'''
'''
print(5 * 4 < 4 + 3)
print(6 * 2 - 1 > 3 * 1)
print(9 - 4 / 2 <= 7 + 1 or 5 * 2 - 3 != 6)
print(9 / 3 == 3 * 3 and 2 * 3 - 1 >= 8)
'''
'''

A = 5
B = 1
C = True
D = False

print(A > B and C or D)
'''
'''
print('CALCULADOR DE APROVAÇÃO')
print('-'*30)

n1 = int(input('nota1 da materia1: '))
n2 = int(input('nota2 da materia1: '))
n3 = int(input('nota3 da materia1: '))

materia1 = (n1 + (n2*2) + n3) / 4

print('-'*30)

n4 = int(input('nota1 da materia2: '))
n5 = int(input('nota2 da materia2: '))
n6 = int(input('nota3 da materia2: '))

materia2 = (n4 + (n5*2) + n6) / 4

print('-'*30)

n7 = int(input('nota1 da materia3: '))
n8 = int(input('nota2 da materia3: '))
n9 = int(input('nota3 da materia3: '))

materia3 = (n7 + (n8*2) + n9) / 4

print('-'*30)

if materia1 >= 7 and materia2 >= 7 and materia3 >= 7 :
    print('parabens, voce foi aprovado.')
else:
    print('deveria ter estudado mais, foi reprovado.')
'''
'''
nome = input('digite seu nome: ')
print(len(nome))
print(nome[:1])
'''
'''
palavra = 'socorram me subi no onibus em marrocos'

print(palavra[::-1])
'''
'''
word = input('digite uma palavra: ')
print(word[1::2])
'''
#pdf 3 -> Faça um programa que dado uma palavra, retorne os caracteres nas posições ímpares.
#pais maus - mommy called me sheriff
