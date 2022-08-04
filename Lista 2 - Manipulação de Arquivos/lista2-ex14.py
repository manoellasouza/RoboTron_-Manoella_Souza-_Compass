# 14- Printe todos os nomes e as idades dos atores que ganharam o oscar de 1987 até 1999.

import pandas as pd

arquivo = pd.read_csv("ganhadoresoscar.csv", encoding="UTF-8", sep=",")

print(arquivo.loc[(arquivo["Year"] >= 1987) & (arquivo["Year"] <= 1999),["Age", "Name"]])