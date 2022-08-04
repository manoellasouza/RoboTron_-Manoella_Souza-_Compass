# 9- Usando Pandas, leia apenas os dados da coluna Age do CSV

import pandas as pd

arquivo = pd.read_csv("ganhadoresoscar.csv", encoding="UTF-8", sep=",")
print(arquivo["Age"])