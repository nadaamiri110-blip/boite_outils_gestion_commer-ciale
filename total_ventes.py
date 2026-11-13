# Calcul du total et de la moyenne des ventes depuis ventes.csv

import csv

ventes = []

try:
    with open("ventes.csv", "r", encoding="utf-8", newline="") as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            ventes.append(float(ligne["ventes"]))

    if len(ventes) == 0:
        print("Aucune vente trouvée.")
    else:
        total = sum(ventes)
        moyenne = total / len(ventes)

        print(f"Total des ventes : {total:.2f} DT")
        print(f"Moyenne des ventes : {moyenne:.2f} DT")

except FileNotFoundError:
    print("Erreur : le fichier ventes.csv est introuvable.")
except (ValueError, KeyError):
    print("Erreur : vérifiez le contenu du fichier ventes.csv.")
