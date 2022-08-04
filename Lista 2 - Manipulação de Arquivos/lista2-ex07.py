#7- Percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.

import json

def retornar_json():
    with open("campeonato.json", encoding="UTF-8") as json_normal:
        #o load vai carregar o JSON normal e transformar ele em dict:
        json_manipulavel= json.load(json_normal)
        return json_manipulavel 

json_retornado=retornar_json()

for x in json_retornado.keys():
    print (x)