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
		self.exp = 0
		self.level = round((self.exp/200) + 1)
		if self.level > 20:
			self.level = 20
		self.moves = []
		for i in self.job.moves:
			if i.level <= self.level:
				i.append
		self.inventory = []

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