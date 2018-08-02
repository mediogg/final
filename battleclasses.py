class Job:

	def __init__(self, jobname, stats, moves = []):
		self.name = jobname
		self.stats = stats
		#Stats are HP, Attack, Magic, MP, Defense, and Speed
		self.moves = moves


class Character:

	def __init__(self, name):
		self.name = name
		self.inventory = []
		self.level = 1

class Player(Character):

	def __init__(self, name, job):
		super().__init__(name)
		self.job = job
		self.stats = job.stats
		self.currentHP = self.stats[0]
		self.exp = 0
		self.level = round((self.exp/200) + 1)
		self.moves = []
		for m in self.moves:
			if m.level <= self.level:
				self.moves.append(m)

	def exp_gain(self, exp):
		if self.level != 20:
			self.exp += exp
			print(self.name + " recieved " + str(exp) + " experience points.")
			lvl = self.level
			self.level = round((self.exp/200) +1)
			if self.level != lvl:
				print("Level up! " + self.name + " reached level " + str(self.level) + "!")
				for s in self.stats:
					s += 2
				for m in self.job.moves:
					if m.level == self.level:
						self.moves.append(m)
						print(self.name + " learned " + m.name + "!")



class Enemy(Character):

	def __init__(self, name, levelrange, area, stats, moves):
		super().__init__(name)
		self.area = area
		self.stats = stats
		self.moves = moves
		self.levelrange = levelrange 

class Changer:

	def __init__(self, name, effect, power):
		self.name = name
		self.power = power
		self.effect = effect
		#Effects list: Damage, Heal, Buff, Debuff, Chip Damage, Chip Heal, Dodge, Immobilize

class Item(Changer):

	def __init__(self, name, effect, power, area, uses = "infinite"):
		super().__init__(name, effect, power)
		self.area = area
		self.uses = uses

class Move(Changer):

	def __init__(self, name, effect, power, level, stat, cost = 0):
		super().__init__(name, effect, power)
		self.level = level
		self.stat = stat
		self.cost = cost