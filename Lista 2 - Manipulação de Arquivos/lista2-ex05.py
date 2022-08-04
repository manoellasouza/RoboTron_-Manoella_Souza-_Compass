#5- Guarde o arquivo JSON 2 nomeando-o como campeonato em uma variável e printe todos os seus dados.

import json

def retornar_json():
    with open ("campeonato.json", encoding="utf-8") as json_normal:
        #o load vai carregar o JSON normal e transformar ele em dict:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel
    
json_retornado = retornar_json()

campeonato=json_retornado
print(campeonato)
