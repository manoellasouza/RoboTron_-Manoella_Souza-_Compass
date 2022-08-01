# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas. 
# Entrada:A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo. Saída: Apresente a duração do jogo.
# Referência: https://programadoresdepre.com.br/como-calcular-data-e-hora-em-python/

import datetime

horainicio = int(input("Hora do início do jogo: "))
horafim = int(input("Hora do fim do jogo: "))

diajogo1 = datetime.datetime(2022,8,29,horainicio,00)

#Tratamento caso o jogo dure até o dia seguinte:
if horafim > horainicio:
    diajogo2 = datetime.datetime(2022,8,29,horafim,00)
else:
    diajogo2 = datetime.datetime(2022,8,30,horafim,00)

res = (diajogo2-diajogo1)
segundos = res.total_seconds()
horas = segundos/(60*60)
    
print(f"O jogo durou {int(horas)} horas")