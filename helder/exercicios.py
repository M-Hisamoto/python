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

A = 5
B = 1
C = True
D = False

print(A > B and C or D)