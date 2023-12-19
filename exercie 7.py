import sqlite3

def creer_table():
    connexion = sqlite3.connect("clinique_veterinaire.db")
    curseur = connexion.cursor()

    curseur.execute("""
        CREATE TABLE IF NOT EXISTS chiens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            age TEXT,
            race TEXT
        )
    """)

    connexion.commit()
    connexion.close()

def ajouter_chien():
    nom = input("Nom du chien : ")
    age = input("Age du chien : ")
    race = input("Race du chien : ")

    connexion = sqlite3.connect("clinique_veterinaire.db")
    curseur = connexion.cursor()

    curseur.execute("INSERT INTO chiens (nom, age, race) VALUES (?, ?, ?)", (nom, age, race))

    connexion.commit()
    connexion.close()

    print("Le chien a été ajouté avec succès.")

def liste_chiens():
    connexion = sqlite3.connect("clinique_veterinaire.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM chiens")
    chiens = curseur.fetchall()

    if not chiens:
        print("Aucun chien enregistré.")
    else:
        print("Liste des chiens :")
        for chien in chiens:
            print(f"ID : {chien[0]}, Nom : {chien[1]}, Age : {chien[2]}, Race : {chien[3]}")

    connexion.close()

creer_table()

while True:
    print("\nMenu :")
    print("1. Ajout d'un chien")
    print("2. Liste des chiens")
    print("3. Quitter")

    choix = input("Veuillez choisir une option : ")

    if choix == "1":
        ajouter_chien()
    elif choix == "2":
        liste_chiens()
    elif choix == "3":
        print("Programme terminé.")
        break
    else:
        print("Option invalide. Veuillez choisir à nouveau.")
