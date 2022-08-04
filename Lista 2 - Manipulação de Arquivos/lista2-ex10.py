# 10- Usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.

import pandas as pd

arquivo = pd.read_csv("ganhadoresoscar.csv", encoding="UTF-8", sep=",")
#Buscando pelo filme The Pianist:
print(arquivo.loc[75,["Movie"]])
