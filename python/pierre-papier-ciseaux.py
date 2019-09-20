import random

def afficherScore(scoreJoueur,scoreOrdi):
	print ("[Joueur: " + str(scoreJoueur) + "]" + " ___ " + "[Ordi: " +  str(scoreOrdi) + "]")

def jeu(scoreJoueur, scoreOrdi):
	choixOrdi = random.choice(maListe)

	choixJoueur =""
	while (choixJoueur != "pierre" and choixJoueur != "papier" and choixJoueur != "ciseaux"):
		choixJoueur = input("\n Choisissez un symbole: pierre, papier, ciseaux \n ")
		choixJoueur= choixJoueur.lower()
	
	# print ("Le choix du joueur est: " + choixJoueur)
	print ("Le choix de l'ordi est: " + choixOrdi)

	if (choixJoueur == choixOrdi):
		print ("Egalite, recommencez")
		afficherScore(scoreJoueur,scoreOrdi)

	
	elif ((choixJoueur == "pierre" and choixOrdi == "ciseaux") or (choixJoueur == "ciseaux" and choixOrdi == "pierre")):
		if (choixJoueur == "pierre"):
			print ("Le joueur  l'emporte")
			scoreJoueur = scoreJoueur +1
			afficherScore(scoreJoueur,scoreOrdi)
		else:
			print ("L'ordi l'emporte")
			scoreOrdi = scoreOrdi + 1
			afficherScore(scoreJoueur,scoreOrdi)
		
	
	elif ((choixJoueur == "pierre" and choixOrdi == "papier") or (choixJoueur == "papier" and choixOrdi == "pierre")):
		if (choixJoueur == "papier"):
			print ("Le joueur l'emporte")
			scoreJoueur = scoreJoueur+1
			afficherScore(scoreJoueur,scoreOrdi)
		else:
			print ("L'ordi l'emporte")
			scoreOrdi = scoreOrdi + 1
			afficherScore(scoreJoueur,scoreOrdi)
		
	elif ((choixJoueur == "ciseaux" and choixOrdi == "papier") or (choixJoueur == "papier" and choixOrdi == "ciseaux")):
		if (choixJoueur == "ciseaux"):
			print ("Le joueur l'emporte")
			scoreJoueur = scoreJoueur+1
			afficherScore(scoreJoueur,scoreOrdi)
		else:
			print ("L'ordi l'emporte")
			scoreOrdi = scoreOrdi + 1
			afficherScore(scoreJoueur,scoreOrdi)
	return (scoreJoueur,scoreOrdi)
	
maListe = list()
maListe = ["pierre", "papier", "ciseaux"]


recommencer ="oui"
while (recommencer == "oui"):
	scoreJoueur = 0
	scoreOrdi = 0
	
	while (scoreJoueur < 3 and scoreOrdi < 3):
	
		scoreJoueur,scoreOrdi=jeu(scoreJoueur,scoreOrdi)
				
	if (scoreJoueur == 3):
		print ("Le joueur gagne la partie")
	else:
		print ("L'ordi gagne la partie")
		
		
	recommencer=input ("Voulez-vous rejouer? oui-non " )

print ("Au revoir, merci d'avoir joué avec moi :)")
