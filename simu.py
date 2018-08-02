import battleclasses as clo
from random import *

#enemy keyword construction

party = []
jobs = []
jobnames = []
items = []
itemnames = []
players = []
playernames = []
areas = []
enemies = []
enemynames = []
moves = []
effects = ["damage", "heal", "buff", "debuff", "chip damage", "chip heal", "dodge", "immobilize"]
stats = ["hp", "attack", "magic", "mp", "defense", "speed"]
menuf = "main"

frommain = ["jobs", "players", "enemies", "items", "areas", "party", "exit"]
fromjobs = ["new job", "back"]
fromplayers = ["new player", "back"]
fromenemies = ["new enemy", "back"]
fromitems = ["new item", "back"]
fromparty = ["add party member", "remove party member", "back"]
fromturn = ["fight", "item", "end battle"]

def load_data():
	save =  open("savedata.txt", 'r')
	read = ""
	readzline = 0
	move = False
	line = save.readline()
	line = line.replace("\n", '')
	while line:
		jobappend = False
		if line == "job":
			read = "job"
			readzline = 0
			stats = []
			moves = []
		elif line == "item":
			read = "item"
			readzline = 0
			effect = []
		elif line == "enemy":
			read = "enemy"
			readzline = 0
			rang = []
			stats = []
			moves = []
		elif line == "player":
			read = "player"
			readzline = 0
			inventory = []
		elif line == "party":
			read = "party"
			readzline = 0
		elif line == "move":
			move = True
			moveline = 0
			effects = []
		elif line == "fileend":
			read = "end"
		else:
			if read == "job":
				if readzline == 1:
					name = line
				elif readzline > 1 and readzline < 8:
					stats.append(int(line))
				elif move == True:
					moveline += 1
					if moveline == 1:
						movename = line
					elif moveline == 2:
						power = int(line)
					elif moveline == 3:
						lvl = int(line)
					elif moveline == 4:
						stat = line
					elif moveline == 5:
						cost = int(line)
					elif line == "end":
						move = False
						mov = clo.Move(movename, effects, power, lvl, stat, cost)
						moves.append(mov)
					else:
						effects.append(line)

				if line == "endl":
					job = clo.Job(name, stats, moves)
					jobs.append(job)
					jobnames.append(job.name)
					fromjobs.append(job.name)
					read = ''

			if read == "enemy":
				if readzline == 1:
					name = line
				elif readzline > 1 and readzline < 8:
					stats.append(int(line))
				elif readzline == 8 or readzline == 9:
					rang.append(line)
				elif readlinez == 10:
					area = line
					if not area in areas:
						areas.append(area)
				elif move == True:
					moveline += 1
					if moveline == 1:
						movename = line
					elif moveline == 2:
						power = int(line)
					elif moveline == 3:
						lvl = int(line)
					elif moveline == 4:
						stat = line
					elif moveline == 5:
						cost = int(line)
					elif line == "end":
						move = False
						mov = clo.Move(movename, effects, power, lvl, stat, cost)
						moves.append(mov)
					else:
						effects.append(line)

				if line == "endl":
					enemy = clo.Enemy(name, rang, area, stats, moves)
					enemies.append(enemy)
					enemynames.append(enemy.name)
					fromenemies.append(enemy.name)
					read = ''

			if read == "item":
				if readzline == 1:
					name = line
				elif readzline == 2:
					power = int(line)
				elif readzline == 3:
					area = line
					if not area in areas:
						areas.append(area)
				elif readzline == 4:
					if line == "infinite":
						uses = line
					else:
						uses = int(line)
				elif line == "endl":
					item = clo.Item(name, effect, power, area, uses)
					items.append(item)
					itemnames.append(item.name)
					fromitems.append(item.name)
					read = ''
				else:
					effect.append(line)

			if read == "player":
				if readzline == 1:
					name = line
				elif readzline == 2:
					for i in jobs:
						if i.name == line:
							job = i
							break
				elif readzline == 3:
					exp = int(line)

				elif line == "endl":
					player = clo.Player(name, job)
					player.inventory = inventory
					player.exp = exp
					player.level = round((player.exp/200) +1)
					for m in player.job.moves:
						if m.level > player.level:
							player.moves.append(m)
					players.append(player)
					playernames.append(player.name)
					fromplayers.append(player.name)
					read = ''

				else:
					for i in items:
						if line == i.name:
							inventory.append(i)

			if read == "party":
				for i in players:
					if i.name == line:
						party.append(i)

		readzline += 1
		line = save.readline()
		line = line.replace("\n", '')


def save_data():

	save = open("savedata.txt", "w")
	save.write("SAVE DATA\n")
	save.close
	save = open("savedata.txt", "a+")
	for w in jobs:
		save.write("job\n")
		save.write(w.name + "\n")
		for q in w.stats:
			save.write(str(q) + "\n")
		for u in w.moves:
			save.write("move\n")
			save.write(u.name + "\n")
			save.write(str(u.power) + "\n")
			save.write(str(u.level) + "\n")
			save.write(u.stat + "\n")
			save.write(str(u.cost) + "\n")
			for i in u.effect:
				save.write(i + "\n")
			save.write("end\n")
		save.write("endl\n")

	for x in items:
		save.write("item\n")
		save.write(x.name + "\n")
		save.write(str(x.power) + "\n")
		save.write(x.area + "\n")
		save.write(str(x.uses) + "\n")
		for q in x.effect:
			save.write(q + "\n")
		save.write("endl\n")

	for y in enemies:
		save.write("enemy\n")
		save.write(y.name + "\n")
		for q in y.stats:
			save.write(str(q) + "\n")
		for q in y.range:
			save.write(str(q) + "\n")
		save.write(y.area + "\n")
		for u in w.moves:
			save.write("move\n")
			save.write(u.name + "\n")
			save.write(str(u.power) + "\n")
			save.write(str(u.level) + "\n")
			save.write(u.stat + "\n")
			save.write(str(u.cost) + "\n")
			for i in u.effect:
				save.write(i + "\n")
			save.write("end\n")
		save.write("endl\n")

	for z in players:
		save.write("player\n")
		save.write(z.name + "\n")
		save.write(z.job.name + "\n")
		save.write(str(z.exp) + "\n")
		for i in z.inventory:
			save.write(i.name + "\n")
		save.write("endl\n")
		
			
def encounter():

	narea = False
	while narea == False:
		print("What area do you want the encounter to be from?")
		for i in areas:
			print(i)
		area = input("Area: ").upper()
		if area in areas:
			narea = True
		else:
			print("That's not a valid area. Here is a list of areas:")
			for i in areas:
				print(i)
	tipo = False
	while tipo == False:
		type = input("What type of encounter do you want? (enemy, item, or random): ").lower()
		if type == "enemy":
			enemy_enc(area)
			tipo == True
		elif type == "item":
			item_enc(area)
			tipo == True
		elif type == "random":
			rand_enc(area)
			tipo == True
		else:
			print("That is not a valid encounter type.")

def enemy_enc(area, enemy = ""):

	print("Enemy encounters under construction.")

def true_enc(area, enemy = ""):

	if enemy == "":
		arealist = []
		for i in enemies:
			if i.area == area:
				arealist.append(i)

		length = len(arealist) -1
		randomize = randint(0, length)
		enimy = arealist[randomize]
	else:
		enimy = enemy

	enimy.currentHP = enimy.stats[0]

	print("You encountered " + enimy.name + "!")
	characters = [enimy]
	for p in party:
		characters.append(p)

	sortedchars = []

	while characters != []:
		mem = 0
		for c in characters:
			if c.stats[5] > mem:
				mem = c
		characters.remove(mem)
		sortedchars.append(mem)

	end = False
	while end == False:
		for s in sortedchars:
			if isinstance(s, clo.Player):
				turn = True
				while turn:
					print(s.name + "'s turn.")
					print("What would you like to do?")
					print(">FIGHT\n>ITEM\n>END BATTLE")
					chmenu = menuit(fromturn)
					next = 0
					if chmenu == "fight":
						print(">NORMAL ATTACK")
						frommoves = []
						for m in s.moves:
							print(">" + m.name)
							frommoves.append(m.name)
						print(">Back")
						movech = menuit(frommoves, ["normal attack", "back"])
						move = 0
						if movech in frommoves:
							for m in s.moves:
								if m.name == movech:
									move = m
						if movech == "normal attack":
							move = clo.Move("regular", "damage", 20, 1, "attack", 0)

						if movech == "back":
							continue


def item_enc(area, item = ""):

	if item == "":
		arealist = []
		for i in items:
			if i.area == area:
				arealist.append(i)

		length = len(arealist) - 1
		randomize = randint(0, length)
		itemb = arealist[randomize]
	else:
		itemb = item

	vowel = False
	for q in ['a', 'e', 'i', 'o', 'u']:
		if itemb.name[0] == q:
			vowel == True
	if vowel == True:
		print("You found an " + itemb.name + "!")
	else:
		print("You found a " + itemb.name + "!")

	veh = False
	while veh == False:
		playeradd = input("Who will you give this item to?: ")
		exists = False
		for w in party:
			if playeradd == w.name:
				exists = True
				player = w
		if exists == True:
			veh = True
			player.inventory.append(itemb)
			print(str(itemb.name) + " given to " + playeradd + ".")
		else:
			print("That's not a valid player.")

def rand_enc(area):

	combine = []
	for i in enemies:
		if enemy.area == area:
			combine.append(i)
	for i in items:
		if item.area == area:
			combine.append(i)

	length = len(combine) - 1
	random = randint(0, length)
	chosen = combine[random]
	if isinstance(chosen, clo.Item):
		item_enc("", chosen)
	if isinstance(chosen, clo.Enemy):
		enemy_enc("", chosen)

def party_print(seet = "Name"):

	if party != []:
		for q in party:
			if seet != "Title":
				print(q.name)
			else:
				print(q.job.name + " " + q.name)
	else:
		print("There are no party members.")

def get_stats():
	statsloc = []
	for e in stats:
		eep = False
		while eep == False:
			ans = input(e.upper() + " stat from 1 to 7, choose 'random' to randomize: ")
			if ans.lower() == "random":
				ans = randint(1, 7)
				eep = True
			elif ans.isnumeric() and (int(ans) <= 7 and int(ans) >= 1):
				ans = int(ans)
				eep = True
			if eep == False:
				print("That's not a valid answer.")
			else:
				statsloc.append(ans)

	return statsloc

def new_move(enemy = False):
	moives = []
	movech = input("Would you like to add a move?: ")
	if movech.lower() == "yes":
		movemaking = True
		meffec = []
		while movemaking == True:
			movename = input("What would you like to name the move?: ")
			effecting = True
			while effecting == True:
				effect = input("What effect does this move have? (Damage, Heal, Buff, Debuff, Chip Damage, Chip Heal, Dodge, Immobilize): ").lower()
				okay = False
				for w in effects:
					if effect == w:
						okay = True
						break

				if not okay:
					print("That's not a valid effect.")
					continue
				else:
					if "buff" in effect:
						sep = False
						while sep == False:
							statbuff = input("What stat does this move change?: ").lower()
							for h in stats:
								if statbuff == h:
									sep = True
									break
							if not sep:
								print("That's not a valid stat. (Stats are HP, Attack, Magic, MP, Defense, and Speed.)")
							else:
								effect += " " + statbuff

					meffec.append(effect)
				cont = input("Would you like to add another effect?: ").lower()
				if cont != "yes":
					effecting = False

			if enemy == False:
				lep = False
				while lep == False:
					lvl = input("What level is this move learned at? (Level cap is 20): ")
					if not lvl.isnumeric() or (lvl.isnumeric() and (int(lvl) > 20 or int(lvl) < 1)):
						print("That's not a number from 1 to 20!")
					else:
						lep = True
			else:
				lvl = 1
			mpp = False
			while mpp == False:
				power = input("What is this move's power?: ")
				if not power.isnumeric():
					print("That's not a number!")
				else:
					mpp = True

			st = False
			while st == False:
				stat = input("What stat does this move use, magic or attack?: ").lower()
				if stat == "magic" or stat == "attack":
					st = True
				else:
					print("Type in magic or attack.")
			mep = False
			while mep == False:
				cost = input("How much MP does this attack cost?: ")
				if not cost.isnumeric():
					print("That's not a number!")
				else:
					mep = True

			mover = clo.Move(movename, meffec, power, lvl, stat, cost)

			moives.append(mover)

			more = input("Would you like to continue to make more moves?: ")
			if more.lower() != "yes":
				movemaking = False

	return moives

def new_job():
	jobname = input("What do you want to name the job?: ")

	statsloc = get_stats()

	job = clo.Job(jobname, statsloc)

	moives = new_move()

	if moives != []:
		job.moves.extend(moives)
	jobs.append(job)
	jobnames.append(job.name)
	fromjobs.append(job.name)

	return "jobs"

def new_player():
	if jobs == []:
		print("No jobs available. Create a job first!")

	else:
		name = input("Choose a name: ")
		feemo = False
		jobbo = ""
		while feemo == False:
			print("Choose a job.")
			for j in jobnames:
				print(">" + j)
			choose = input("Job: ")
			beep = False
			for w in jobnames:
				if choose ==  w:
					beep = True
					break
			if beep == False:
				print("That's not a valid job!")
			else:
				for j in jobs:
					if j.name == choose:
						jobbo = j
			feemo = True

		player = clo.Player(name, jobbo)
		players.append(player)
		playernames.append(player.name)
		fromplayers.append(player.name)

	return "players"

def new_enemy():

	name = input("Choose a name: ")

	bep = False
	while bep == False:
		btm = input("What's the enemy's bottom level range (1-20)? ")
		if not btm.isnumeric() or (btm.isnumeric() and (int(btm) > 20 or int(btm) < 1)):
			print("That's not a number from 1 to 20!")
		else:
			bep = True
	tep = False
	while tep == False:
		tp = input("What's the enemy's top level range (1-20)?: ")
		if not tp.isnumeric() or (tp.isnumeric() and (int(tp) > 20 or int(tp) < 1)):
			print("That's not a number from 1 to 20!")
		else:
			tep = True

	area = input("What area is this enemy found in?: ").upper()
	if not (area in areas):
		areas.append(area)

	statos = get_stats()
	moves = new_move(True)

	enemy = clo.Enemy(name, [btm, tp], area, statos, moves)
	enemies.append(enemy)
	enemynames.append(enemy.name)
	fromenemies.append(enemy.name)

	return "enemies"

def new_item():

	ieffec = []
	itemname = input("What would you like to name the item?: ")
	effecting = True
	while effecting == True:
		effect = input("What effect does this item have? (Damage, Heal, Buff, Debuff, Chip Damage, Chip Heal, Dodge, Immobilize): ").lower()
		okay = False
		for w in effects:
			if effect == w:
				okay = True
				break

		if not okay:
			print("That's not a valid effect.")
			continue
		else:

			if "buff" in effect:
				sep = False
				while sep == False:
					statbuff = input("What stat does this item change?: ").lower()
					for h in stats:
						if statbuff == h:
							sep = True
							break
					if not sep:
						print("That's not a valid stat. (Stats are HP, Attack, Magic, MP, Defense, and Speed.)")
					else:
						effect += " " + statbuff

			ieffec.append(effect)

		cont = input("Would you like to add another effect to your item?: ").lower()
		if cont != "yes":
			effecting = False

	mpp = False
	while mpp == False:
		power = input("What is this item's strength (number)?: ")
		if not power.isnumeric():
			print("That's not a number!")
		else:
			mpp = True

	area = input("What area is this item found in?: ").upper()
	if not (area in areas):
		areas.append(area)

	mpp = False
	while mpp == False:
		uses = input("How many uses does this item have? (0 for infinite): ")
		if not uses.isnumeric():
			print("That's not a number!")
		if uses == '0':
			uses = "infinite"
			mpp = True
		else:
			mpp = True
			uses = int(uses)

	item = clo.Item(itemname, ieffec, power, area, uses)
	items.append(item)
	itemnames.append(item.name)
	fromitems.append(item.name)

	return "items"

def new_party():

	if players == []:
		print("There are no players to choose from.")
	else:
		for i in playernames:
			print(i)
		beef = True
		while beef == True:
			choose = input("Who do you want to add?: ")
			for q in players:
				if q.name == choose:
					party.append(q)
					beef = False
					break
			if beef == True:
				print("That is not a player name.")

	return "party"

def remove_party():

	if party == []:
		print("There are no party members.")
	else:
		party_print()
		reed = True
		while reed == True:
			remove = input("Who would you like to remove?: ")
			for i in party:
				if i.name == remove:
					reed = False
					party.remove(i)
			if reed == True:
				print("That is not a player name.")

	return "party"


def menuit(menus, second = []):

	second.extend(menus)
	for i in second:
		i = i.lower()
	chmenu = input("Type which menu to go to: ")
	anyupper = False
	for q in second:
		for p in q:
			if p.isupper():
				anyupper = True
				break
		if anyupper == True:
			break

	if anyupper == False:
		chmenu = chmenu.lower()

	if chmenu in second:
		return chmenu
	else:
		print("Menu does not exist.")
		return "Nah"

def main(menu):
	menuf = menu

	if menu == "main" or menu == "back":
		print("Main menu:\n>Jobs\n>Players\n>Enemies\n>Items\n>Areas\n>Party\n>exit")
		mench = menuit(frommain)
		if mench != "Nah":
			menuf = mench

	if menu == "exit":
		save_data()
		exit()

	if menu == "jobs":
		print("Job Menu:\n>New Job")
		for q in jobs:
			print(">" + q.name)
		print(">Back")
		mench = menuit(fromjobs)
		if mench != "Nah":
			menuf = mench

	if menu == "players":
		print("Player Menu:\n>New Player")
		for q in players:
			print(">" + q.name)
		print(">Back")
		mench = menuit(fromplayers)
		if mench != "Nah":
			menuf = mench

	if menu == "enemies":
		print("Enemy Menu:\n>New Enemy")
		for q in enemies:
			print(">" + q.name)
		print(">Back")
		mench = menuit(fromenemies)
		if mench != "Nah":
			menuf = mench

	if menu == "items":
		print("Items Menu:\n>New Item")
		for q in items:
			print(">" + q.name)
		print(">Back")
		mench = menuit(fromitems)
		if mench != "Nah":
			menuf = mench

	if menu == "areas":
		if areas != []:
			print("Areas:")
			for i in areas:
				print(">" + i)
			print(">Back")
			mench = menuit(areas, ["back"])
			if mench != "Nah":
				menuf = mench
		else:
			print("No areas have been made.")
			menuf = "main"

	if menu == "party":
		emp = ["partymenu"]
		for i in party:
			emp.append(i.name)
		print("Party Members:")
		if party != []:
			party_print("Title")
			print(">Remove Party Member")

		print(">Add Party Member")
		print(">Back")
		mench = menuit(fromparty)
		if mench != "Nah":
			menuf = mench

	if menu == "new job":
		menuf = new_job()

	if menu == "new player":
		menuf = new_player()

	if menu == "new enemy":
		menuf = new_enemy()

	if menu == "new item":
		menuf = new_item()

	if menu == "add party member":
		menuf = new_party()

	if menu == "remove party member":
		menuf = remove_party()

	if menu in jobnames:
		for i in jobs:
			if menu == i.name:
				print("Name: " + str(i.name))
				print("HP: " + str(i.stats[0]))
				print("ATK: " + str(i.stats[1]))
				print("MAG: " + str(i.stats[2]))
				print("MP: " + str(i.stats[3]))
				print("DEF: " + str(i.stats[4]))
				print("SPD: " + str(i.stats[5]))
				if i.moves != []:
					print("Moves:")
					for p in i.moves:
						print(p.name + ": " + str(p.power) + " power")
						print("Effect(s):")
						for e in p.effect:
							print(e)
		menuf = "jobs"

	if menu in playernames:
		for q in players:
			if menu == q.name:
				print("Name: " + str(q.name))
				print("HP: " + str(q.stats[0]))
				print("ATK: " + str(q.stats[1]))
				print("MAG: " + str(q.stats[2]))
				print("MP: " + str(q.stats[3]))
				print("DEF: " + str(q.stats[4]))
				print("SPD: " + str(q.stats[5]))
				print("Job: " + q.job.name)
				print("Level " + str(q.level))
				print("Experience Points: " + str(q.exp))
				if q.inventory != []:
					print("Inventory:")
					for i in inventory:
						print(i.name)

		menuf = "players"

	if menu in itemnames:
		for i in items:
			if menu == i.name:
				print("Name: " + str(i.name) + ": " + str(i.power) + " power")
				print("Uses: " + str(i.uses))
				print("Effect(s):")
				for h in i.effect:
					print(h)
				print("Found in " + i.area)

		menuf = "items"

	if menu in enemynames:
		for w in enemies:
			if menu == w.name:
				print("Name: " + str(w.name))
				print("HP: " + str(w.stats[0]))
				print("ATK: " + str(w.stats[1]))
				print("MAG: " + str(w.stats[2]))
				print("MP: " + str(w.stats[3]))
				print("DEF: " + str(w.stats[4]))
				print("SPD: " + str(w.stats[5]))
				print("Levels " + str(w.levelrange[0]) + " to " + str(w.levelrange[1]))
				if w.moves != []:
					print("Moves:")
					for p in w.moves:
						print(p.name + ": " + str(p.power) + " power")
						print("Effect(s):")
						for e in p.effect:
							print(e)
				print("Found in " + w.area)

		menuf = "enemies"

	if menu in areas:
		print("Enemies in " + menu + ":")
		beepo = False
		for w in enemies:
			if w.area == menu:
				print(w.name)
				beepo = True
		if beepo == False:
			print("No enemies in area.")
		print("Items in " + menu + ":")
		beepo = False
		for d in items:
			if d.area == menu:
				print(d.name)
				beepo = True
		if beepo == False:
			print("No items in area.")

		menuf = "areas"

	print()
	return menuf

if __name__ == '__main__':

	load_data()

	while True:
		menuf = main(menuf)