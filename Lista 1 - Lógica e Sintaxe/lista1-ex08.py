# 8- Crie um programa que lê 1 valor inteiro para X. Se o valor for par, calcular o fatorial de x em uma função e apresentar o resultado fora da função. 
# Se o valor for impar, apresentar em uma função a tabuada de 1 a 10 de X
# Referência: https://www.pythonprogressivo.net/2018/05/Calcular-Fatorial-Python-FOR-WHILE.html

x=int(input("Digite um número inteiro: "))

def fat (y):
    r, c = 1, 1 
    while c <= y:
        r = r * c
        c = c + 1
    return r

def tab (y):
    i=1
    print(f"Tabuada de {y}:")
    while i < 11:
        print(f"{y} x {i} = {(y*i)}")
        i+=1      

if x % 2 == 0:
    print(f"O fatorial de {x} é igual a {fat(x)}")
else:
    tab(x)
