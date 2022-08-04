# 11- Printe o nome do Ator que ganhou o Oscar em 1993

import pandas as pd

arquivo = pd.read_csv("ganhadoresoscar.csv", encoding="UTF-8", sep=",")

print(arquivo.loc[arquivo["Year"] == 1993,["Name"]])


