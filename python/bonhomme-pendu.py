import random
def jeu(motOrdi,motCache, essaiRate, essais, essaisRestants, lettresDejaJouees):
	lettreJoueur = input ("\n Choisis une lettre: ")[0]
	while (lettreJoueur in lettresDejaJouees):
		lettreJoueur = input ("Choisis une lettre: ")[0]
	lettresDejaJouees.append(lettreJoueur)
	
	


	lettreTrouvee = False
	for index in range (0,len(motOrdi)):

		if (lettreJoueur == motOrdi[index]):
			lettreTrouvee = True
			
			if(index==0):
				motCache =  (lettreJoueur + motCache[index+1:len(motOrdi)] )
			else:
				motCache = (motCache [0:index] + lettreJoueur + motCache[index+1:len(motOrdi)])
		
	
	if(lettreTrouvee == False):
		print ("essaye encore!")
		essaiRate = essaiRate +1
		essaisRestants -=1
		
	
		

		affichePendu(essaiRate)
		print ("essais restants: "+str(essaisRestants))
	else:
		print ("Tu as raison")
		

	print ("motOrdi: "+ motCache)
	essais +=1
	print ("Lettres déjà choisies: " + str(lettresDejaJouees))
	return motCache, essaiRate, essais, essaisRestants, lettresDejaJouees

def affichePendu(essaiRate):
	
	
	
	
	pendu = """
 ______
 |    
 |    
 |    
 |    
_|_____
	"""
	
	pendu1 = """
 ______
 |    |
 |    
 |    
 |    
_|_____
	"""
	
	pendu2 = """
 ______
 |    |
 |    o
 |    
 |    
_|_____
	"""
	
	pendu3 = """
 ______
 |    |
 |    o
 |    |
 |    
_|_____
	"""
	
	pendu4 = """
 ______
 |    |
 |    o
 |   `|
 |    
_|_____
	"""
	
	pendu5 = """
 ______
 |    |
 |    o
 |   `|´
 |    
_|_____
	"""
	
	pendu6 = """
 ______
 |    |
 |    o
 |   `|´
 |   ´ 
_|_____
	"""
	
	pendu7 = """
 ______
 |    |
 |    o
 |   `|´
 |   ´ `
_|_____
	"""
	
	pendu8 = """
 ______
 |    |
 |    o
 |   `|´
 |   ´ `
_|____^
	"""
	
	pendu9 = """
 ______
 |    |
 |    o
 |   `|´
 |   ´ `
_|___^^
	"""
  
	pendu10 = """

 ______
 |    |
 |    o
 |   `|´
 |   ´ `
_|___^^^
	"""
	
	if(essaiRate ==0):
		print (pendu)
	elif (essaiRate ==1):
		print (pendu1)
	elif (essaiRate == 2):
		print (pendu2)
	elif (essaiRate ==3):
		print (pendu3)
	elif (essaiRate == 4):
		print (pendu4)
	elif (essaiRate == 5):
		print (pendu5)
	elif (essaiRate == 6):
		print (pendu6)
	elif (essaiRate == 7):
		print (pendu7)
	elif (essaiRate == 8):
		print (pendu8)
	elif (essaiRate == 9):
		print (pendu9)
	
	else
		print (pendu10)



fichier = open("listeMots.txt","r")
motOrdi = random.choice(fichier.readlines())
motOrdi=motOrdi.replace ("\n", "")
motCache = "*" * len(motOrdi)

print ("L'ordi a choisi un mot: " + motCache)
print ("Le mot contient " + str(len(motOrdi)) + " lettres")

essais = 0
essaiRate =0
essaisRestants = 10
affichePendu(0)
lettresDejaJouees = []

print ("essais restants: "+str(essaisRestants))


while((motCache != motOrdi) and essaiRate < 10):

	
motCache,essaiRate, essais, essaisRestants, lettresDejaJouees =jeu(motOrdi,motCache, essaiRate, essais, essaisRestants,lettresDejaJouees)
	
	

if(motCache == motOrdi):
	print ("Tu as gagné en " + str(essais) + " essais")
else: #si essais ==9
	print ("Tu as perdu")
	print ("Le mot choisi était: " + motOrdi)

