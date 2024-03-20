from futbol import *

def main():
    while True:
        print("\n" + "*"*50)
        print("***" + "PR2-UF3. JSON i accés a dades".center(44) + "***")
        print("*"*50)
        print("\nExercici 1: (Mostrar els equips d'una lliga i any en concret)")
        print("Exercici 2: (Mostrar els resultats dels partits d'una lliga i data en concret)")
        print("Exercici 3: (Consultar la classificació final d'una lliga i any en concret)")
        print("Exercici 4: (Mostrar una estadística de tots els equips)")
        print("Exercici 5: (Mostrar els 5 millors equips visitants i locals)")
        print("Sortir")

        opcion = input("\nEscull una opció: ")

        if opcion == "1":
            obtenirClubs()
        elif opcion == "2":
            obtenirPartits()
        elif opcion == "3":
            obtenirPuntuacions()
        elif opcion == "4":
            estadistiquesEquips()
        elif opcion == "5":
            mejoresEquipos()
        elif opcion == "6":
            break
        else:
            print("Aquesta opció no válida. Escull una opció del 1 al 6.")

if __name__ == "__main__":
    main()