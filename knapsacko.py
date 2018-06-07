class Knapsack(object):
	cap = None
	itensAmount = None

	#Construtor
	def __init__(self, itensAmount, capa):
		self.itensAmount = itensAmount
		self.cap = capa

	def cap(self):
		return self.cap

	def itensAmount(self):
		return self.itensAmount