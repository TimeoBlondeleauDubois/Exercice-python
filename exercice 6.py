import random, time
import sys


hp_du_perso_max = 1000
hp_du_perso = 1000
atk = 100
magie = 100
lvl = 0
xp = 0
perdu = 0
message = 0
messages = 0
augmenter = 0
gold = 0

def level():
  global lvl
  global xp
  global message
  global augmenter
  global messages
  if xp >= 3000:
      lvl = 5
      message = 5
  elif xp >= 2250:
      lvl = 4
      message = 4
  elif xp >= 1500:
      lvl = 3
      message = 3
  elif xp >= 200:
      lvl = 2
      message = 2
  elif xp >= 100:
      lvl = 1
      message = 1
  if message != messages:
    print("Vous avez gagné un niveau !")
    print("Vous êtes maintenant niveau ", lvl)
    augmenter = 1
  messages = message
  augmenter_les_stats()
  return lvl, augmenter

def augmenter_les_stats():
  global augmenter
  global lvl
  global atk
  global hp_du_perso_max
  global magie
  if augmenter == 1:
    if lvl == 1:
      atk = atk + 5
      magie = magie + 5
      hp_du_perso_max = hp_du_perso_max + 100
    if lvl == 2:
      atk = atk + 7.5
      magie = magie + 8
      hp_du_perso_max = hp_du_perso_max + 150
    if lvl == 3:
      atk = atk + 10
      magie = magie + 10
      hp_du_perso_max = hp_du_perso_max + 200
    if lvl == 4:
      atk = atk + 12.5
      magie = magie + 12.5
      hp_du_perso_max = hp_du_perso_max + 250
    if lvl == 5:
      atk = atk + 15
      magie = magie + 15
      hp_du_perso_max = hp_du_perso_max + 300
    print ("\nvous avez maintenant :" , hp_du_perso_max, " de vie", atk, " d'attaque\n")
    print (magie, " de magie" , " et ", hp_du_perso_max, " de vie")
  augmenter = 0
  return hp_du_perso_max, atk, magie, augmenter



def reset_stats():
    return [
        {"nom": "Acheron", "hp": 2000, "atk": 75, "xp": 100, "gold": 10},
        {"nom": "Bloodlust", "hp": 800, "atk": 60, "xp": 80, "gold": 8},
        {"nom": "Kenos", "hp": 1300, "atk": 50, "xp": 85, "gold": 8.5},
        {"nom": "Arcturus", "hp": 1690, "atk": 69, "xp": 90, "gold": 9},
        {"nom": "Zodiac", "hp": 2500, "atk": 25, "xp": 75, "gold": 7.5},
        {"nom": "Void Wave", "hp": 2000, "atk": 25, "xp": 70, "gold": 7.0},
        {"nom": "Abyss Of Darkness", "hp": 3000, "atk": 60, "xp": 9.5, "gold": 95}
    ]

def faire_combat():
  global hp_du_perso
  global atk
  global lvl
  global magie
  global xp
  global perdu
  global gold
  monstre_actuel = None 

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
          if hp_du_perso <= 0:
              print("\nVous avez perdu")
              perdu = 1
          else:
              print("\nVous avez gagné")
              xp += monstre_actuel["xp"]
              print("\nVous avez gagné", monstre_actuel["xp"], "points d'expérience")
              gold += monstre_actuel["gold"]
              print("Vous avez", gold, "pièces d'or")
              print("Vous êtes à", xp, "d'expérience")
              monstre_actuel = None
          break

      print("\nTour de", monstre_actuel["nom"])
      hp_du_perso -= monstre_actuel["atk"]
      print("Il vous a infligé", monstre_actuel["atk"], "de dégâts")

      if hp_du_perso <= 0:
          print("\nVous avez perdu")
          perdu = 1
          break
  level()
  hp_du_perso = hp_du_perso_max
  return hp_du_perso, atk, magie, xp, hp_du_perso_max, gold

def afficher_texte_progressif(texte):
  for caractere in texte:
      sys.stdout.write(caractere)
      sys.stdout.flush()
      time.sleep(0.04)
  print()

def histoire():
  afficher_texte_progressif("\nVotre quête débute dans les paisibles Terres de l'Aube, où la lumière règne en maître. Votre objectif est clair : retrouver le Livre des Anciens, une relique sacrée qui détient le secret de la purification du Dragon Primordial.")
  time.sleep(1)
  afficher_texte_progressif("\nAlors que vous vous aventurez paisiblement dans les Terres de l'Aube, la brise légère caresse vos joues, et le soleil projette une lumière apaisante sur le paysage. L'atmosphère s'imprègne de sérénité, mais soudain, le ciel lui-même semble s'assombrir. Une ombre massive plane au-dessus de vous, et un grondement guttural brise le calme. Une énergie maléfique émane des ténèbres, annonçant la présence imminente des gardiens corrompus du Dragon Primordial.")
  time.sleep(1)
  afficher_texte_progressif("\nSoudain, des ombres tourbillonnantes émergent des ténèbres, prenant forme sous la commandement du Dragon Primordial. Les gardiens corrompus se dressent devant vous, prêts à défendre leur maître maléfique. Le rugissement du dragon se fait entendre, annonçant le début du combat. Vous vous engagez, déterminé à surmonter chaque défi pour atteindre le sommet de la citadelle.\n")
  time.sleep(1)
  faire_combat()
histoire()