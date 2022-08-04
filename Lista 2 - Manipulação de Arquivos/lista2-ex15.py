#15- Mostre todos os filmes menos o “The Revenant”.

import pandas as pd

arquivo = pd.read_csv("ganhadoresoscar.csv", encoding="UTF-8", sep=",")
print(arquivo.loc[arquivo["Movie"] != "The Revenant",["Movie"]])