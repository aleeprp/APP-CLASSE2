import json
from urllib.request import urlopen

'''
- **1p** - Mostrar els equips d'una lliga i any en concret (demanat per pantalla a l'usuari).
- **1p** - Mostrar els resultats dels partits d'una lliga i data en concret (demanat per pantalla a l'susuari).
- **5p** - Consultar la classificació final d'una lliga i any en concret (demanat per pantalla a l'usuari). Recordo que un partit guanyat són 3 punts i un empat és 1 punt.
- **2p** - Mostrar una estadística de tots els quips. En concret: gols encaixats, gols marcats, diferència de gols, partits guanyats, empatats i perduts.
- **1p** - Mostrar els 5 millors equips visitants i locals.
'''

# EXCERCICI 1
# Funció per obtenir els clubs d'una lliga i any específics
def obtenirClubs():
    try:
        # Sol·licitar a l'usuari l'any i la lliga
        any = input("Introduïu l'any (format: YYYY-YY): ")
        lliga = input("Introduïu la lliga (exemple: at.1): ").lower()
        print("\n")

        # Construir la URL per a la sol·licitud a github
        url = f"https://raw.githubusercontent.com/openfootball/football.json/master/{any}/{lliga}.clubs.json"
        # Realitzar la sol·licitud 
        resposta = urlopen(url)

        # Llegir la resposta, decodificar-la i convertir-la a un objecte JSON
        dades = json.loads(resposta.read().decode())

        # Iterar sobre cada club en les dades i imprimir el seu nom
        for club in dades['clubs']:
            print(club['name'])
        print("\n")    
    except Exception as e:
        print("\n" + "="*50 + "\n" + "===" + "Error".center(44) + "===" + "\n" + "="*50 + "\n")
        print("¡El any o la lliga que has introduït son incorrectes!\n")

# EXCERCICI 2
# Funció per obtenir els partits i les seves puntuacions d'una lliga específica
def obtenirPartits():
    try:
        # Sol·licitar a l'usuari l'any i la lliga
        any = input("Introduïu l'any (format: YYYY-YY): ")
        lliga = input("Introduïu la lliga (exemple: at.1): ").lower()
        print("\n")

        # Construir la URL per a la sol·licitud a github
        url = f"https://raw.githubusercontent.com/openfootball/football.json/master/{any}/{lliga}.json"
        # Realitzar la sol·licitud 
        resposta = urlopen(url)

        # Llegir la resposta, decodificar-la i convertir-la a un objecte JSON
        dades = json.loads(resposta.read().decode())

        # Iniciar el contador de partits sense puntuació
        partitsSensePuntuacio = 0

        # Iterar sobre cada partit en les dades i imprimir el nom dels equips i la seva puntuació
        for partit in dades['matches']:
            if 'score' in partit:
                equip1 = partit['team1']
                equip2 = partit['team2']
                puntuacio = partit['score']['ft']
                print("=" * 50)
                print(f'{equip1} {puntuacio[0]} - {puntuacio[1]} {equip2}'.center(50))
                print("=" * 50, "\n")
            else:
                # Incrementar el contador de partits sense puntuació
                partitsSensePuntuacio += 1

        # Imprimir el nombre total de partits sense puntuació
        print(f'\nHi ha {partitsSensePuntuacio} partits que no tenen puntuació registrada.\n')
    except Exception as e:
        print("\n" + "="*50 + "\n" + "===" + "Error".center(44) + "===" + "\n" + "="*50 + "\n")
        print("¡El any o la lliga que has introduït son incorrectes!\n")

# EXCERCICI 3
# Funció per obtenir els partits i les seves puntuacions d'una lliga específica
def obtenirPuntuacions():
    try:
        # Sol·licitar a l'usuari l'any i la lliga
        any = input("Introduïu l'any (format: YYYY-YY): ")
        lliga = input("Introduïu la lliga (exemple: at.1): ").lower()
        print("\n")

        # Construir la URL per a la sol·licitud a github
        url = f"https://raw.githubusercontent.com/openfootball/football.json/master/{any}/{lliga}.json"
        # Realitzar la sol·licitud 
        resposta = urlopen(url)

        # Llegir la resposta, decodificar-la i convertir-la a un objecte JSON
        dades = json.loads(resposta.read().decode())

        # Iniciar un diccionario per emmagatzemar les puntuacions dels equips
        puntuacions = {}

        # Iterar sobre cada partit en las dades y sumar puntos a los equipos
        for partit in dades['matches']:
            if 'score' in partit:
                equip1 = partit['team1']
                equip2 = partit['team2']
                puntuacio = partit['score']['ft']
                
                # Iniciar las puntuaciones de los equipos si aún no están en el diccionario
                if equip1 not in puntuacions:
                    puntuacions[equip1] = 0
                if equip2 not in puntuacions:
                    puntuacions[equip2] = 0    

                # Sumar puntos a los equipos en función del resultado del partido    
                if puntuacio[0] > puntuacio[1]:  # Si el equipo 1 gana
                     puntuacions[equip1] += 3           
                elif puntuacio[0] < puntuacio[1]:  # Si el equipo 2 gana
                     puntuacions[equip2] += 3    
                else:  # Si hay empate
                    puntuacions[equip1] += 1
                    puntuacions[equip2] += 1                

        # Imprimir las puntuaciones finales de los equipos ordenadas de forma descendente (el orden aleatorio me da TOC)
        for equip, puntuacio in sorted(puntuacions.items(), key=lambda item: item[1], reverse=True):
            print("=" * 50)
            print((f'{equip}: {puntuacio} punts').center(50))
            print("=" * 50, "\n")
        print("\n")    
    except Exception as e:
        print("\n" + "="*50 + "\n" + "===" + "Error".center(44) + "===" + "\n" + "="*50 + "\n")
        print("¡El any o la lliga que has introduït son incorrectes!\n")

# EXERCICI 4
def estadistiquesEquips():
    try:
        any = input("Por favor, introduce el año (formato: YYYY-YY): ")
        lliga = input("Por favor, introduce la liga (ejemplo: at.1): ").lower()
        print("\n")

        url = f"https://raw.githubusercontent.com/openfootball/football.json/master/{any}/{lliga}.json"
        resposta = urlopen(url)

        dades = json.loads(resposta.read().decode())

        estadisticas = {}

        for partit in dades['matches']:
            if 'score' in partit:  # Verificar si la clave 'score' existe (si el partido tiene puntuación)
                equip1 = partit['team1']
                equip2 = partit['team2']
                gols_equip1 = partit['score']['ft'][0]
                gols_equip2 = partit['score']['ft'][1]

                if equip1 not in estadisticas:
                    estadisticas[equip1] = {'gols_marcats': 0, 'gols_encaixats': 0, 'diferencia_gols': 0, 'guanyats': 0, 'empatats': 0, 'perduts': 0}
                if equip2 not in estadisticas:
                    estadisticas[equip2] = {'gols_marcats': 0, 'gols_encaixats': 0, 'diferencia_gols': 0, 'guanyats': 0, 'empatats': 0, 'perduts': 0}

                estadisticas[equip1]['gols_marcats'] += gols_equip1
                estadisticas[equip1]['gols_encaixats'] += gols_equip2
                estadisticas[equip2]['gols_marcats'] += gols_equip2
                estadisticas[equip2]['gols_encaixats'] += gols_equip1

                # Calcula la diferencia de goles (el numero se mostrara siemppre positivo) y específica si es a favor o en contra
                if estadisticas[equip1]['gols_marcats'] > estadisticas[equip1]['gols_encaixats']:
                    estadisticas[equip1]['diferencia_gols'] = f"{abs(estadisticas[equip1]['gols_marcats'] - estadisticas[equip1]['gols_encaixats'])} (a favor)"
                else:
                    estadisticas[equip1]['diferencia_gols'] = f"{abs(estadisticas[equip1]['gols_marcats'] - estadisticas[equip1]['gols_encaixats'])} (en contra)"

                if estadisticas[equip2]['gols_marcats'] > estadisticas[equip2]['gols_encaixats']:
                    estadisticas[equip2]['diferencia_gols'] = f"{abs(estadisticas[equip2]['gols_marcats'] - estadisticas[equip2]['gols_encaixats'])} (a favor)"
                else:
                    estadisticas[equip2]['diferencia_gols'] = f"{abs(estadisticas[equip2]['gols_marcats'] - estadisticas[equip2]['gols_encaixats'])} (en contra)"

                if gols_equip1 > gols_equip2:
                    estadisticas[equip1]['guanyats'] += 1
                    estadisticas[equip2]['perduts'] += 1
                elif gols_equip1 < gols_equip2:
                    estadisticas[equip1]['perduts'] += 1
                    estadisticas[equip2]['guanyats'] += 1
                else:
                    estadisticas[equip1]['empatats'] += 1
                    estadisticas[equip2]['empatats'] += 1

        for equip, stats in estadisticas.items():
            print(f'{equip}:')
            print("-" * 35)
            print(f"  Gols marcats: {stats['gols_marcats']}")
            print(f"  Gols encaixats: {stats['gols_encaixats']}")
            print(f"  Diferencia de gols: {stats['diferencia_gols']}")
            print(f"  Partits guanyats: {stats['guanyats']}")
            print(f"  Partits empatats: {stats['empatats']}")
            print(f"  Partits perduts: {stats['perduts']}\n")
        print("\n")    
    except Exception as e:
        print("\n" + "="*50 + "\n" + "===" + "Error".center(44) + "===" + "\n" + "="*50 + "\n")
        print("¡El any o la lliga que has introduït son incorrectes!\n")

# EXERCICI 5
def mejoresEquipos():
    try:
        # Solicitar al usuario el año y la liga
        any = input("Introduïu l'any (format: YYYY-YY): ")
        lliga = input("Introduïu la lliga (exemple: at.1): ").lower()
        print("\n")

        # Construir la URL para la solicitud a github
        url = f"https://raw.githubusercontent.com/openfootball/football.json/master/{any}/{lliga}.json"
        # Realizar la solicitud 
        resposta = urlopen(url)

        # Leer la respuesta, decodificarla y convertirla a un objeto JSON
        dades = json.loads(resposta.read().decode())

        # Iniciar diccionarios para almacenar las puntuaciones de los equipos locales y visitantes
        puntuacions_locales = {}
        puntuacions_visitantes = {}

        # Iterar sobre cada partido en las dades y sumar puntos a los equipos
        for partit in dades['matches']:
            if 'score' in partit:
                equip_local = partit['team1']
                equip_visitante = partit['team2']
                puntuacio = partit['score']['ft']
                
                # Iniciar las puntuaciones de los equipos si aún no están en los diccionarios
                if equip_local not in puntuacions_locales:
                    puntuacions_locales[equip_local] = 0
                if equip_visitante not in puntuacions_visitantes:
                    puntuacions_visitantes[equip_visitante] = 0    

                # Sumar puntos a los equipos en función del resultado del partido    
                if puntuacio[0] > puntuacio[1]:  # Si el equipo local gana
                     puntuacions_locales[equip_local] += 3           
                elif puntuacio[0] < puntuacio[1]:  # Si el equipo visitante gana
                     puntuacions_visitantes[equip_visitante] += 3    
                else:  # Si hay empate
                    puntuacions_locales[equip_local] += 1
                    puntuacions_visitantes[equip_visitante] += 1    

        # Crear listas para los 5 mejores equipos locales y visitantes
        mejores_locales = sorted(puntuacions_locales.items(), key=lambda x: x[1], reverse=True)[:5]
        mejores_visitantes = sorted(puntuacions_visitantes.items(), key=lambda x: x[1], reverse=True)[:5]
        print('Millors equips locals:', mejores_locales)
        print('Mejores equipos visitantes:', mejores_visitantes) 
        print("\n")     
    except Exception as e:
        print("\n" + "="*50 + "\n" + "===" + "Error".center(44) + "===" + "\n" + "="*50 + "\n")
        print("¡El any o la lliga que has introduït son incorrectes!\n")
