class Item(object):
	value = 0
	weight = 0

	def __init__(self, valuea, weighta):
		self.value = valuea
		self.weight = weighta

	def weight(self):
		return self.weight

	def value(self):
		return self.value