# Import des blibliothèques nécessaires
from math import *

# Récupération des données fournies en entrées
nbLettres = int(input())

# Créations de variables utiles
longueurCote = 2 * (nbLettres - 1) + 1
longueurBloc = ceil(longueurCote / 2)
indiceLigneMilieu = longueurBloc - 1
panneau = [""] * longueurCote
alphabet = "abcdefghijklmnopqrstuvwxyz"
lettres_utiles = ""
for idLettre in range(nbLettres):
    lettres_utiles += alphabet[idLettre]


# Création d'une fonction utile
def remplacer_dernier_car(ligne_a_changer, prochain_car, dernier_car):
    ligne_a_changer = list(ligne_a_changer)
    # print("Voici la ligne à changer : ", ligne_a_changer)
    for idCar in range(len(ligne_a_changer)):
        if ligne_a_changer[idCar] == dernier_car:
            ligne_a_changer[idCar] = prochain_car
    return str("".join(ligne_a_changer))


""" On va créer la ligne du milieu et on va la mettre sur la ligne au-dessus et en-dessous en remplaçant la lettre la
plus "dernière" de notre "alphabet" par l'avant-dernière.

Ensuite, on va procéder de même en remplaçant à chaque fois une lettre par une autre."""

# Création de la ligne du milieu
ligneMilieu = lettres_utiles

for loop1 in range(len(lettres_utiles) - 1):
    ligneMilieu = ligneMilieu + lettres_utiles[len(lettres_utiles) - loop1 - 2]
panneau[indiceLigneMilieu] = ligneMilieu

# On prend la ligne du milieu comme modèle pour les lignes du dessus et du dessous
ligne = ligneMilieu

# On a besoin de transformer lettres_utiles en liste pour modifier les caractères
lettres_utiles = list(lettres_utiles)

# Remplissage du panneau
for loop2 in range(longueurBloc - 1):
    panneau[indiceLigneMilieu - loop2 - 1] = remplacer_dernier_car(ligne, lettres_utiles[-2], lettres_utiles[-1])
    panneau[indiceLigneMilieu + loop2 + 1] = remplacer_dernier_car(ligne, lettres_utiles[-2], lettres_utiles[-1])
    # print("Ok")
    del lettres_utiles[-1]
    # print("lettres_utiles = ", lettres_utiles)
    ligne = panneau[indiceLigneMilieu - loop2 - 1]

for loop3 in range(longueurCote):
    print(panneau[loop3])
