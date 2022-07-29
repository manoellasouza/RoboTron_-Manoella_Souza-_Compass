# 2- Construa um programa que armazena em duas variaveis duas notas e apresenta a média entre as duas

n1 = float (input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))
m = (n1+n2) / 2
print ('A média entre as notas {} e {} é de {:.1f}'.format(n1, n2, m))
