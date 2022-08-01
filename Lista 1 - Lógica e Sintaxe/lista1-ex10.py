# 10- Crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores ["maça", "banana", "pera"]
# Referência: https://www.delftstack.com/pt/howto/python/compare-lists-python/

i, x = 0, 0
lista1=["maça", "banana", "pera"]; lista2=[]

while i < 3:
    lista2.append(input(f"Digite o nome da {i+1}ª fruta: "))
    i+=1

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

if lista1 == lista2:
    print(" ")
    print("As duas listas são iguais!")
else:
    print(" ")
    print("As duas listas não são iguais!")
    while x < 3:
        if lista2[x] in lista1:
            print(" ")
            print(f"A fruta {lista2[x]} está nas duas listas:")
            print(f"Primeira lista: Posição {lista1.index(lista2[x])} | Segunda lista: Posição {lista2.index(lista2[x])}")
        x+=1