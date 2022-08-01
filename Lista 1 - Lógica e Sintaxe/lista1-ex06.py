# 6- Construa um programa que receba uma valor inteiro maior que 2 em uma variavel x e apresenta os impares entre 0 e x
# Referência: Curso em Vídeo - https://youtu.be/Qws8-E-YrlY

x= 0

while x < 2:
    x=int(input("Digite um valor inteiro maior ou igual a 2: "))

print(f"Ímpares entre 0 e {x}:")

for i in range(0,x+1):
    if i % 2 == 1:
        print(i, end=" ")
        
