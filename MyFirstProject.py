
spell = ""
Pokemon = ""

while spell == "":
	print ("Choose one:\n 1. Charmander \n 2. Bulbasaur \n 3. Squirtle")

	Pokemon = input()
	if Pokemon == "charmander" or Pokemon == "1":
		Pokemon = "charmander"
		spell = "Fireball"
	elif Pokemon == "bulbasaur" or Pokemon == "2":
		Pokemon = "bulbasaur"
		spell = "Razer Leaf"
	elif Pokemon == "squirtle" or Pokemon == "3":
		Pokemon = "squirtle"
		spell = "Water gun"	
	
	

	Pokemon = Pokemon.capitalize()

print ("Choose opponent:\n 1. Rattata \n 2. Martin Röjder \n 3. Ekans")

opponent = input()
if opponent == "rattata" or opponent == "1":
	opponent = "rattata"
elif opponent == "Martin Röjder" or opponent == "2":
	opponent = "Martin Röjder"
elif opponent == "Ekans" or opponent == "3":
	opponent = "Ekans"

print("%s used %s" % (Pokemon, spell))

opponent.capitalize()
from random import *
dmg = randint(40, 80)
print("%s took %s damage from %s" %(opponent, dmg, Pokemon))