# 7- Crie um programa que contêm uma função que receba dois parâmetros inteiros e retorna a média dos dois valores

def media():
    n1=int(input("Digite o primeiro número: "))
    n2=int(input("Digite o segundo número: "))
    m=(n1+n2)/2
    return m

print(f"A média dos dois valores é igual a {media()}")