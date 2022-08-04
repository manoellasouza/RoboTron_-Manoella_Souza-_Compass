#B) Listar todos os dados de determinado elemento, buscando através do seu símbolo.

import pandas as pd

arquivo = pd.read_csv("elementos.csv", encoding="UTF-8", sep=",")

print("Escolha um dos símbolos abaixo para buscar os dados desse elemento:")
lista= arquivo["Simbolo"].tolist()
print(lista)
print(" ")

simb=input("Digite o símbolo escolhido: ")
print(" ")
print(arquivo[arquivo["Simbolo"] == (simb)])
