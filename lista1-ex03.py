# 3- Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
soma = n1+n2

print ('Resultado:', soma)

if soma % 2 == 0:
    print ("O valor da soma é PAR!")
else:
    print ("O valor da soma é ÍMPAR!")
