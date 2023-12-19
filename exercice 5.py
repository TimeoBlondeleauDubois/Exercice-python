import random

hp_du_perso_max = 1000
hp_du_perso = 1000
atk = 100
magie = 100
lvl = 1
fuite = 0
xp = 0

def reset_stats():
    return [
        {"nom": "acheron", "hp": 2000, "atk": 75, "xp": 100},
        {"nom": "bloodlust", "hp": 800, "atk": 60, "xp": 80},
        {"nom": "kenos", "hp": 1300, "atk": 50, "xp": 85},
        {"nom": "arcturus", "hp": 1690, "atk": 69, "xp": 90},
        {"nom": "zodiac", "hp": 2500, "atk": 25, "xp": 75},
        {"nom": "Void Wave", "hp": 2000, "atk": 25, "xp": 70},
        {"nom": "Abyss Of Darkness", "hp": 3000, "atk": 60, "xp": 95}
    ]

def faire_combat():
    global fuite
    global hp_du_perso
    global atk
    global lvl
    global magie
    global xp

    monstre_actuel = None  # Placez cette ligne en dehors de la boucle

    while hp_du_perso > 0:
        if monstre_actuel is None: 
            monstre_actuel = random.choice(reset_stats())
            print("Vous tombez sur un", monstre_actuel["nom"], "sauvage.")
            print("\nQue voulez-vous faire?")

        print("Vos points de vie:", hp_du_perso, "/", hp_du_perso_max)
        print("Ses points de vie:", monstre_actuel["hp"], "pv")

        print("\n1: Attaquer - Votre attaque =", atk, "d'attaque")
        print("2: Magie - Votre magie =", magie, "de magie")
        print("3: Potion de soin - (restaure 10% de santé totale)")
        print("4: Fuir - Vous fuyez")

        choix = input("Choix: ")
        if choix == "1":
            print("\nVous attaquez", monstre_actuel["nom"])
            monstre_actuel["hp"] -= atk
            print(monstre_actuel["nom"], "a", monstre_actuel["hp"], "pv")
        elif choix == "2":
            print("\nVous lancez un sort de magie")
        elif choix == "3":
            hp_du_perso += hp_du_perso_max * 0.1
            if hp_du_perso > hp_du_perso_max:
                hp_du_perso = hp_du_perso_max
            print("\nVous avez restauré 10% de votre vie, il vous reste", hp_du_perso)
            print("/", hp_du_perso_max, "pv")
        elif choix == "4":
            print("\nVous fuyez")
            break
        else:
            print("\nChoix invalide")
            continue

        if monstre_actuel["hp"] <= 0:
            print("\nVous avez gagné")
            lvl += 1
            xp += monstre_actuel["xp"]
            print("Vous avez gagné", monstre_actuel["xp"], "points d'expérience")
            monstre_actuel = None
            break

        print("\nTour du monstre")
        hp_du_perso -= monstre_actuel["atk"]
        print("Il vous a infligé", monstre_actuel["atk"], "de dégâts")

        if hp_du_perso <= 0:
            print("\nVous avez perdu")
            break

    hp_du_perso = hp_du_perso_max
    return hp_du_perso, atk, magie, lvl, xp

faire_combat()
faire_combat()
faire_combat()
faire_combat()
faire_combat()
