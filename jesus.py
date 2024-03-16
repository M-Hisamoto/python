'''
a = int(input("var a:"))
if a == 0:
    print("c=-bx")
b = int(input("var b:"))
c = int(input("var c:"))
# calcule a função a*x**2+b*x+c
delta=b**2-4*a*c
x=(-b+delta**0.5)/(2*a)
y=(-b-delta**0.5)/(2*a)
print(f"{x}\n{y}")
'''
"""
salario=int(input("seu salario:"))
r = (salario/100)*15
print(r+salario)
"""
tempo=int(input("segundos:"))
segundos=tempo%60
a=tempo//60
minutos=a%60
b=a//60
horas=b%24
dias=b//24
print(tempo,dias,horas,minutos,segundos)