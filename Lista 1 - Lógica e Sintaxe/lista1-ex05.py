# 5- Construa um programa que recebe 20 valores para X e no final apresenta a média aritmética dos valores pares digitados
# Referência: CFB Cursos - https://youtu.be/AqvSMMcybTI

soma, media, i, par = 0, 0, 0, 0
pares=[]

while i < 20:
    x=int(input(f"Digite o {i+1}º valor: "))
    if x % 2 == 0:
        pares.append(x)
        soma = soma + x
        par = par + 1
    i+=1

media=soma/par

print(f"Números pares digitados: {pares}")
print(f"Média dos valores pares digitados: {media:.2f}")