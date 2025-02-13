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
'''
notas = [8, 9, 7, 8.9, 6.5, 10, 10]

soma = sum(notas)

media = soma / len(notas)

print(f'{media:.1f}')
'''
'''
n = int(input("digite um número prara saber a tabuada: "))
nt = int(input("digite o número de termos que quer mostrar: "))
t = 1

for i in range (1, nt + 1):
     mult = n * t
     print(mult)
     t = t + 1
'''
'''
n1 = int(input("digite um número aqui: "))
n2 = int(input("digite outro número aqui: "))
soma = 0 
for i in range(1, n2 + 1):
    soma += n1

print(soma)
'''
'''
dp = float(input("digite o depósito inicial: "))
tj = float(input("taxa de juros: "))
dpm = float(input("digite o depósito mensal: "))

porcentagem = tj / 100
juros = (dp + dpm) * porcentagem
parcela = dp + juros + dpm
soma = 0
c = 1

for i in range(1, 25):
     print(f'a parcela {c} é: {parcela:.2f}')
     parcela = parcela + juros
     soma += parcela
     c += 1

print(f'total ganho com juros é R${soma - (dp * 24):.2f}')
'''
'''
div = float(input("digite o valor inicial da dívida: "))
jm = float(input("digite o valor do juros mensal: "))
pago = float(input("digite o valor pago mensal: "))
juros = jm / 100
cont = 0

while div > 0:
    div = (div + juros) - pago
    cont += 1

print(f'serão necessários {cont} mes(es) para pagar a dívida.')
print(div)
'''
'''
c = 20

while True:
    print(c)
    c -= 1
    if c < 0:
        break
'''
'''
while True:
    v = int(input("digite um número para continuar ou 0 para parar: "))
    if v == 0:
        break
'''
'''
n = []
c = 0
while True:
    v = int(input("digite um número para continuar ou 0 para parar: "))
    if v == 0:
        break
    n.append(v)
    c += 1

print(f'quantidade de números digitados: {c}, soma: {sum(n)}, média aritmética: {sum(n)/len(n):.2f}, lista: {n}')
'''
'''
print('
    Código  Preço
       1     0,50
       2     1,00
       3     4,00
       5     7,00
       9     8,00
')

total = 0

while True:
    cod = int(input("digite o código do produto ou zero para finalizar: "))
    if cod == 0:
        break
    match cod:
        case 1:
            fruta = 0.5
        case 2:
            fruta = 1
        case 3:
            fruta = 4
        case 5:
            fruta = 7
        case 9:
            fruta = 8
        case _:
            print('Código inválido')
            break
    quant = int(input("digite a quantidade do produto: "))
    preco = fruta  * quant
    total += preco

if total != 0:
    print(f'o total é de R${total}')
'''
'''
c = 1
while c <= 30:
    print("* "*c)
    c += 1
'''  
'''
populacao_a = 80000
taxa_a = 0.03         
populacao_b = 200000
taxa_b = 0.015
anos = 0

while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_a
        populacao_b += populacao_b * taxa_b
        anos += 1

print(f'anos {anos}')
'''
'''
# Função para calcular a soma dos n primeiros termos da sequência de Fibonacci
def soma_fibonacci(n):
    # Se n for 0, a soma é 0
    if n == 0:
        return 0
    # Se n for 1, a soma é 1 (somente o primeiro termo)
    elif n == 1:
        return 1

    # Inicializando os dois primeiros termos da sequência de Fibonacci
    a, b = 0, 1
    soma = a + b  # A soma inicial é 0 + 1 = 1

    print(b)   
    print(a)   
    
    # Calculando os termos subsequentes e somando
    for _ in range(2, n):  # Começando do terceiro termo até o n-ésimo
        c = a + b
        soma += c
        a = b
        b = c
        print(c)
    
    return soma

# Leitura do número n
n = int(input("Digite o número de termos da sequência de Fibonacci: "))

# Calculando e exibindo a soma dos n primeiros termos
resultado = soma_fibonacci(n)
print(f"A soma dos {n} primeiros termos da sequência de Fibonacci é: {resultado}")
'''
'''
num = int(input("digite para multiplicação: "))
vezes = int(input("digite para multiplicação: "))

multiplicacao = 0

for i in range (1, vezes +1 ):
    multiplicacao =  multiplicacao + num

print(multiplicacao)
'''
'''
num = int(input("digite para divisão: "))
divisor = int(input("digite para divisão: "))
divisao = 0

while num > 0:
    num = num - divisor
    divisao += 1
    if num < 0:
        divisao -= 1
        divisao += 0.5

print(float(divisao))
'''
'''
while True:
    op = input("digite a operação ou 0 pra sair: ")
    if op == '0':
        break
    match op:
        case "+":
            print("ok")
        case "-":
            print("ok")
        case "/":
            print("ok")
        case "*":
            print("ok")
        case _:
            print("tente novamente")
'''
'''
num = int(input("digite um número: "))

def is_prime(num):
    if num < 2:
        print("não é primo")
        return False
    elif num == 2:
        print("é primo")
        return True
    elif num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
    return True


if is_prime(num):
     print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
'''
'''
def linha():
     print(30*"-")

linha()
'''
'''
def calcular_media(notas):
    if len(notas) == 0:
        print('sua lista está vazia')
    soma = sum(notas)
    media = soma / len(notas)
    return media

notas = [2.1, 8, 9.5, 7.5, 10, 4, 7.3, 8.2]
media = calcular_media(notas)
print(f"a média das notas é {media:.2f}")
'''
'''
n = int(input("digite um número: "))
c = int(input("digite um inicio: "))
fim = int(input("digite um término para a tabuada: "))
n1 = n

while  c <= fim:
    print(f'{c} X {n1} = {c*n1}')
    c = c + 1
'''
'''
def palindromo(num):
    if num == num[::-1]:
        return True
    else:
        return False

num = input('digite um numero: ')

if palindromo(num) is True:
    print('é um palindromo')
else:
    print('não é um palindromo')
'''
'''
a = 80000
b = 200000
taxa_A = 0.03
taxa_B = 0.015
anos = 0

while a < b:
    a *= (1 + taxa_A)
    b *= (1 + taxa_B)
    c = c + 1

print (anos)
print (a)
print (b)
'''
'''
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

n = 10
result = fibonacci(n)
print(result)
'''
'''
nomes = []

while True:
    nome = input('digite um nome: ')
    nomes.append(nome)
    if nome == '0':
        break
 
print(nomes)
'''
'''
import random

jogadas = int(input('digite o número de jogadas que deseja fazer: '))
c = 0
historico = []

while c < jogadas: 
    moeda = random.randint(1, 2)
    if moeda == 1:
        historico.append('cara')
    elif moeda == 2:
        historico.append('coroa')
    c += 1

print(historico)
'''
'''
from time import sleep

print('Loading', end='\r')
sleep(1)
print('Loading.', end='\r' )
sleep(1)
print('Loading..', end='\r')
sleep(1)
print('Loading...')
'''
'''
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input('digite um numero inteiro: '))
print(fatorial(n))
'''
'''
senha = input('digite uma senha: ')

while True:
    conf_senha = input('confirme a senha: ')
    print('a senha não é compativel')
    if conf_senha == senha:
        print('as senhas batem')
        break
'''
'''
import random

soma = 0

while True:
    n = random.randint(1, 10)
    soma += n
    if n == 5:
        break

print(soma)
'''
'''
nomes = ['matheus', 'gabriel', 'duda', 'roberto', 'duda']
idades = ['23', '14', '110', '30']
palavra = 'chocolate'

nomes.extend(idades)
nomes.extend(palavra)
print(nomes)
print(nomes.index('duda'))
'''
'''
n = int(input("Digite um número: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  
'''
'''
notas = []

while True:
    n = float(input('Digite um número(float ou digite 0 para sair): '))
    if n == 0:
        break
    notas.append(n)

soma = sum(notas)
media = soma / len(notas)

print(media)
print(notas)
print(len(notas))
print(soma)
'''
'''
l1 = []
l2 = []

print('-'*15, 'lista 1', '-'*15)
for i in range(0, 5):
    n = int(input('Digite um numero inteiro: '))
    l1.append(n)

print('-'*15, 'lista 2', '-'*15)
for i in range(0, 5):
    n = int(input('Digite um numero inteiro: '))
    l2.append(n)


iguais = [x for x in l1 if x in l2]
        
if iguais:
    print (f'os elementos iguais são {iguais}')
else:
    print("Não há elementos em comum entre as listas.")
'''
'''
linha = int(input('digite o tamanho da largura: '))
colunas = int(input('digite o tamanho da altura: '))
c = 1

while c <= colunas:
    print('#' * linha)
    c += 1
'''
'''
for hora in range(24):
    for minuto in range(60):        
        print(f"{hora:02}:{minuto:02}")
'''
'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del list[2]
list.remove(5)
list.append(11)
list.append(12)
list.insert(0, 0)

print(f'o tamanho da lista é 
{len(list)}')
print(list)
'''
'''
def vazio(list, x):
    if len(list) == 0:
            print('insira os elementos, primeiro')
    else:
        print(x)

print('1. inserir valores')
print('2. Calcular média')
print('3. Calcular soma')
print('4. Calcular o maior')
print('5. Calcular o menor')

list = []

while True:
    opc = str(input('escolha sua opção ou digite s para sair: '))
    match opc:
        case '1':
            val = int(input('digite o número de valores na lista: '))
            for i in range(val):
                n = int(input('digite um numero: '))
                list.append(n)
        case '2':
            vazio(list, "Calculando a média...")
            if len(list) > 0:
                soma = sum(list)
                media = soma / len(list)
                print(f'Média: {media:.2f}')
        case'3':
            vazio(list, "Calculando a soma...")
            if len(list) > 0:
                soma = sum(list)
                print(f'Soma: {soma}')
        case'4':
            vazio(list, "Calculando o maior...")
            if len(list) > 0:
                print(max(list))
        case'5':
            vazio(list, "Calculando o menor...")
            if len(list) > 0:
                print(min(list))
        case's':
            break   
        case _:
            print('opção inválida')
'''

x = ['matheus', 'carol', 'thiago']
y = [956313648, 946532187, 9643125876]

while True:
    print('1. incluir contato')
    print('2. excluir contato')
    print('3. alterar contato')
    print('4. pesquisa de contato')
    print('5. listar')
    print('6. ordenar')
    print('7. para sair')
    opc = int(input('digite o codigo: '))

    match opc:
        case 1:
            nx, ny = input('digite o nome: '), int(input('digite o numero: '))
            x.append(nx)
            y.append(ny)
        case 2:
            i = int(input('digite a posição do contato que deseja excluir: '))
            del x[(i-1)]
            del y[(i-1)]
        case 3:
            i = int(input('digite a posição do contato que deseja alterar: '))
            nx, ny = input('digite o nome para alterar: '), int(input('digite o numero para alterar: '))
            x[(i-1)] = nx
            y[(i-1)] = ny
        case 4:
            i = int(input('1 para pesquisar por posição ou 2 para pesquisar por nome: '))
            if i == 1:
                opc = int(input('digite aqui a posição: '))
                print(x[(opc-1)])
                print(y[(opc-1)])
            elif i == 2:
                opc = (input('digite aqui o nome em minúsculo: '))
                ix = x.index(opc)+1
                if opc in x:
                    print(opc)
                    print(y[ix-1])
        case 5:
            print(x)
            print(y)
        case 6:
            indices = list(range(len(x)))
            indices.sort(key=lambda i: x[i])
            new_x = [x[i] for i in indices]
            new_y = [y[i] for i in indices]
            x = new_x
            y = new_y
            print('ordenada com sucesso')
        case 7:
            break
        case _:
            print('opcao inválida')






















































