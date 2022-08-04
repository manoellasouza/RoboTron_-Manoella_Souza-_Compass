# 8- Abra o arquivo CSV com pandas e guarde em uma variável de sua escolha e printe o conteúdo no terminal

import pandas as pd

arquivo = pd.read_csv("ganhadoresoscar.csv", encoding="UTF-8", sep=",")
print(arquivo)