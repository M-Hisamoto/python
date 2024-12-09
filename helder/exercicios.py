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
'''
word = input('digite uma palavra: ')
print(word[::2])
'''
'''
str1 = input('string1: ')
str2 = input('string2: ')

print(str1[1:] + str2[1:])
'''
'''
word = input('escreva uma palavra: ')
print(word[-2:]*3)
'''
'''
nickname = input('usuario: ')
print(nickname)
'''
'''
nome = input('escreva seu nome: ')
idade = int(input('escreva sua idade: '))

print(f'Olá meu nome é {nome}, e tenho {idade} anos.')
'''
'''
n1 = int(input("digite um numero inteiro: "))
n2 = int(input("digite outro numero inteiro: "))

print(n1 + n2)
'''
'''
anos = int(input('digite a quantidade de anos de serviço: '))
bonus = anos * 1230
print(bonus)
'''
'''
m = float(input('digite um valor em metros: '))
mm = m / 0.001
print(f"o valor em milímetros é: {mm}")
'''
'''
dias = int(input('dias: '))
horas = int(input('horas: '))
minu = int(input('minutos: '))
seg = int(input('segundos: '))

dias_seg = dias * 86400
horas_seg = horas * 3600
minu_seg = minu * 60

soma = seg + dias_seg + horas_seg + minu_seg

print(f"a conversão desse tempo para segundos é: {soma} segundos.")
'''
'''
sal = float(input("digite o salário: "))
aume = float(input('digite a pocentagem do aumento: '))

porcentagem = aume * 0.01
aumento = sal + (sal * porcentagem)
print(f"seu novo salário é: {aumento}")
'''
'''
preco = float(input("digite o preço: "))
desc = float(input('digite a pocentagem do desconto: '))

porcentagem = desc * 0.01
desconto = preco * porcentagem
novo_preco = preco - desconto
print(f"o desconto é de: R${desconto}, o novo preço a pagar é R${novo_preco}.")
'''
'''
s = float(input("digite aqui a distancia da viagem em KM: "))
v = float(input("digite aqui a velocidade média esperada da viagem(KM/h): "))
t = s/v

print(f"a viagem vai demorar aproximadamente {t:.2f}h.")
'''
'''
c = float(input("digite a tmperatura em °C: "))

f = ((9*c) / 5) + 32
print (f"resultado em °F: {f}")
'''
'''
km = float(input("quantidade de KMs percorridos: "))
dias = int(input("quantidade de dias usados: "))

prec_dias = dias * 60
prec_km = km * 0.15
soma = prec_dias + prec_km

print(f"o preço total foi de : R${soma:.2f}")
'''
'''
cigarros = int(input("quantos cigarros fuma por dia? "))
anos = float(input("quantos anos fumando? "))

min_perd_d = cigarros * 10
min_perd_a = (365 * anos) * min_perd_d
dias_perd = min_perd_a / 1440

print(f'parabens voce perdeu {dias_perd:.0f} dias da sua vida por fumar.')
'''
'''
n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))

if n1 % 2 == 0 and n2 % 2 == 0 or n1 % 2 != 0 and n2 % 2 != 0: 
    print(False)
else:
    print(True)
'''     
'''
vel = int(input('qual é a sua velocidade em Km/h: '))

if vel > 80:
    multa = (vel - 80) *5
    print(f'você foi multado em R${multa}')
else:
    print('ok está tudo na lei')
'''
'''
primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

maior = primeiro
menor = segundo


if (primeiro < menor):
     menor = primeiro
if (terceiro < menor):
        menor = terceiro

if (segundo > maior):
     maior = segundo
if (terceiro > maior):
        maior = terceiro

print(f'Maior: {maior} \nMenor: {menor}')
'''
'''
sal = int(input('insira o seu salário: '))

if sal > 1250:
    aum = sal * 0.10
    print(f'o aumento será de {aum}')
else:
    aum = sal * 0.15
    print(f'o aumento será de {aum}')
'''
'''
num = int(input('digite um numero: '))

if num % 2 == 0 and num < 100:
    print('é par e menor que 100')
elif num % 2 == 0 and num >= 100:
    print('é par e maior ou igual a 100')

if num % 2 != 0 and num < 100:
    print('é impar e menor que 100')
elif num % 2 != 0 and num >= 100:
    print('é impar e maior ou igual a 100')
'''
'''
km = float(input('digite aqui a kilometragem: '))

if km > 200:
    print(f'Preço da passagem ficou: {km*0.45}')
else:
    print(f'Preço da passagem ficou: {km*0.5}')
'''
'''
nome = input("digite seu nome: ")
print(len(nome))
print(nome[:1])
'''
'''
word = input("digite uma palavra: ")
print(word[::-1])
'''
'''
p1 = input("digite uma palavra: ")
p2 = input("digite uma palavra: ")

print(p1[1:]+p2[1:])
'''
'''
word = input("digite uma palavra: ")
print(word[-2:]*3)
'''
'''
nome1 = 'Maria'
ano = 2000
print(f'{nome1} e {'joão'} nasceram em {ano:int}')
'''
'''
a = int(input("digite um número: "))
b = int(input("digite um número: "))

if a>b:
    print(a)
else:
    a = b
    print(a)
'''
'''
def conc_nomes(n1, n2):
    nomes = [n1, n2]
    nomes.sort()
    return ' '.join(nomes)

n1 = input("digite um nome: ")
n2 = input("digite um nome: ")


print(conc_nomes(n1, n2))
'''
'''
casa = float(input("qual é o valor da casa? "))
salario = float(input("digite seu salário: "))
anos = float(input("anos a pagar? ")) 

meses = anos * 12
prest = casa / meses

if prest > salario * 0.3:
    print("por enquanto num dá")
else:
    print("muito bem tá de casa nova")
'''
'''
energia = int(input("digite o consumo de kWh: "))
tipo = input("tipo de instalação, R para residências, I para indústrias e C para comércios: ")

if tipo == 'r' or tipo == 'R':
    if energia <= 500:
        pagar = energia * 0.4
        print(f"pague {pagar}")
    else:
        pagar = energia * 0.65
        print(f"pague {pagar}")

if tipo == 'c' or tipo == 'C':
    if energia <= 1000:
        pagar = energia * 0.55
        print(f"pague {pagar}")
    else:
        pagar = energia * 0.6
        print(f"pague {pagar}")

if tipo == 'i' or tipo == 'I':
    if energia <= 5000:
        pagar = energia * 0.55
        print(f"pague {pagar}")
    else:
        pagar = energia * 0.6
        print(f"pague {pagar}")
'''
'''
t1 = float(input("digite o primeiro termo: "))
r = float(input("digite a razão: "))

for i in range (1, 5):
    print("{:.2f}".format(t1))
    t1 = t1*r
'''
'''
str1 = input("digite algo mínimo 15 caracteres: ")
str2 = input("digite algo mínimo 15 caracteres: ")

if len(str1) >= 15 and len(str1) >= 15:
    print(str1[5:]+str2[:-10])
else:
    print("mais de 15...")
'''
'''
s = input("string: ")
x = input("caractere: ")
i = int(input("inteiro entre 0 e o comprimento da string: "))

if i <= len(s) and i > 0:
    i = s[i-1:i]
    s = s.replace(i, x, 1)
    print(s)
'''
'''
str = "abcdef"

print(str[3:] + str[:3:])
'''
'''
from  datetime import datetime
import datetime

data = input("insira uma data maior no formato AAAA/MM/DD: ")
data2 = input("insira uma data menor no formato AAAA/MM/DD: ")

year, month, day = map(int, data.split('-'))
year2, month2, day2 = map(int, data2.split('-'))

d1 = datetime.date(year, month, day)
d2 = datetime.date(year2, month2, day2)

difference = d1 - d2

print(difference.days)
'''
'''
cpf = input('escreva um cpf: ')

multa = int(cpf[0:1])*10
multb = int(cpf[1:2])*9
multc = int(cpf[2:3])*8
multd = int(cpf[3:4])*7
multe = int(cpf[4:5])*6
multf = int(cpf[5:6])*5
multg = int(cpf[6:7])*4
multh = int(cpf[7:8])*3
multi = int(cpf[8:9])*2
soma1 = (multa+multb+multc+multd+multe+multf+multg+multh+multi)
r1 = soma1%11


if r1 == 0 or r1 == 1:
        d1 = 0
        
else:
        d1 = 11-r1

multb2 = int(cpf[1:2])*10
multc2 = int(cpf[2:3])*9
multd2 = int(cpf[3:4])*8
multe2 = int(cpf[4:5])*7
multf2 = int(cpf[5:6])*6
multg2 = int(cpf[6:7])*5
multh2 = int(cpf[7:8])*4
multi2 = int(cpf[8:9])*3
multj2 = d1*2
soma2 = (multb2+multc2+multd2+multe2+multf2+multg2+multh2+multi2+multj2)
r2 = soma2%11

if r2 == 0 or r2 == 1:
        d2 = 0
        
else:
        d2 = 11-r2

if d1 == int(cpf[9:10]) and d2 == int(cpf[10:11]):
    regiao = cpf[8:9]

    match regiao:
        case '1':
            regiao = 'DF, GO, MS, MT ou TO'
        case '2':
            regiao = 'AC, AM, AP, PA, RO ou RR'
        case '3':
            regiao = 'CE, MA ou PI'
        case '4':
            regiao = 'AL, PB, PE ou RN'
        case '5':
            regiao = 'BA ou SE'
        case '6':
            regiao = 'MG'
        case '7':
            regiao = 'ES ou RJ'
        case '8':
            regiao = 'SP'
        case '9':
            regiao = 'PR ou SC'
        case '0':
            regiao = 'RS'
        case _:
            regiao = 'regiao invalido'

    print(f"cpf válido, a região emitida é {regiao}")
else:
    print(False)
'''
'''
x = 50
while x <= 100:
    print(x)
    x = x + 1
'''
'''
x = 10
while x >= 0:
    print(x)
    x = x - 1
print('fogo')
'''
'''
nt = int(input("digite um numero: "))
x = 2

while x <= nt:
    print(x)
    x = x + 2
'''
'''
nt = int(input("digite um numero: "))
x = 1

while x <= nt:
    print(x)
    x = x + 2
'''
'''
nt = int(input("digite um numero: "))
pt = int(input("primeiro termo: "))

soma = 0

for i in range(pt, nt + 1):
    if i % 2 == 0:
        soma += i

print(soma)
'''
notas = [8, 9, 7, 8.9, 6.5, 10, 10]

soma = 0

for i in range(len(notas)):


































