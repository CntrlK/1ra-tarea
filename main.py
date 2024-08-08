meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GG": "Bien jugado o bien juego",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Algo aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            "ROFL": "Una respuesta a una broma",
            }

for i in range(4):

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        if word == 'CRINGE':
            print("Cringe: Algo excepcionalmente raro o embarazoso")
        if word == 'LOL':
            print("LOL : Una respuesta común a algo gracioso")
        if word == 'GG':
            print("GG : Bien jugado o bien juego")
        if word == 'GG':
            print("GG : Bien jugado o bien juego")
        if word == 'SHEESH':
            print("SHEESH : Ligera desaprobación")
        if word == 'CREEPY':
            print("CREEPY : Algo aterrador, siniestro")
        if word == 'AGGRO':
            print("AGGRO : Ponerse agresivo/enojado")
        if word == 'ROFL':
            print("ROFL : Una respuesta a una broma")
    else:
        print('Creo que haz escrito mal la palabra...')
        # ¿Qué hacer si no se encuentra la palabra?
