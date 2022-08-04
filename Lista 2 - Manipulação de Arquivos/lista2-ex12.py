#12- Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.

import pandas as pd

arquivo = pd.read_csv("ganhadoresoscar.csv", encoding="UTF-8", sep=",")

print(arquivo.loc[(arquivo["Year"] == 1991) | (arquivo["Year"] == 2016),["Name"]])