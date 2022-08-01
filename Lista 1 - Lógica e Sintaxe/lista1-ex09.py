# 9- Crie um programa que recebe 15 valores e armazena em uma lista, e no final da execução mostre os valores da lista do último para o primeiro

i = 0; c = 1
lista=[]; novalista=[]

while i < 15:
    lista.append(int(input(f"Digite o {i+1}º valor: ")))
    i+=1

while c <= 15:
    novalista.append(lista[len(lista) - c])
    c+=1

print(f"Lista com os valores do último para o primeiro: {novalista}")

