#12 - Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias. 
# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 

idadedias=(int(input("Digite o valor da idade em dias: ")))
anos, meses, dias = 0, 0, 0

while idadedias >= 30:
    if idadedias >= 365:
        anos = anos + 1
        idadedias = idadedias - 365
    elif idadedias < 365 and idadedias >= 30:
        meses = meses + 1
        idadedias = idadedias - 30
    
dias = idadedias
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")