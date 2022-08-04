#6- Faça com que o programa printe apenas os primeiros dados dentro de edicao_atual, fase_atual, rodada_atual usando o JSON 2.

import json

def retornar_json():
    with open("campeonato.json", encoding="UTF-8") as json_normal:
        #o load vai carregar o JSON normal e transformar ele em dict:
        json_manipulavel= json.load(json_normal)
        return json_manipulavel 

json_retornado=retornar_json()

edicao= json_retornado["edicao_atual"]
print("Edição id: ",edicao["edicao_id"])
print("Temporada: ",edicao["temporada"])

fase= json_retornado["fase_atual"] 
print("Fase atual: ",fase["fase_id"])
print("Nome: ",fase["nome"])

rodada=json_retornado["rodada_atual"]
print("Nome: ",rodada["nome"])
print("Slug: ",rodada["slug"])

