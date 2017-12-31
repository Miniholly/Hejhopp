name = input("Whats's your name?")
pokemon = 123

charmanderStats = {
	'str' : 50,
	'def' : 30,
	'speed' : 20,
	'evasion' : 10,
}

squirtleStats = {
	'str' : 60,
	'def' : 20,
	'speed' : 30,
	'evasion' : 5,
}

bulbasaurStats = {
	'str' : 40,
	'def' : 40,
	'speed' : 10,
	'evasion' : 20,
}


activePokemon = 1
activeOpponent = 1
battle = True

while battle == True:
	
	menu = {}
	menu['1']= 'Attack',
	menu['2']= 'Nothing',
	menu['3']= 'Run',
	options=menu.keys()
	for entry in options:
		print(entry, menu[entry])


	move = input('Pick your move:')
	if move == '1':
		attackmenu = {}
		attackmenu['1']='Tackle'
		attackmenu['2']='test'
		attack=attackmenu.keys()
		for entry in attack	:
			print(entry, attackmenu[entry])
			
		PickedAttack = input('Pick your attack:')
		if PickedAttack == '1':
			print('superduper attack')

		break