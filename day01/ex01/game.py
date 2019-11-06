class GotCharacter:

	def __init__(self, first_name):
		self.first_name = first_name
		self.is_alive = True

class Stark(GotCharacter):

	"""
		A class representing the Stark family. Or when bad things happen to good
		people.
	"""

	def __init__(self, first_name):
		GotCharacter.__init__(self, first_name)
		self.family_name = 'Stark'
		self.house_word = "Winter is coming"

	def print_house_word(self):
		print(self.house_word)

	def die(self):
		self.is_alive = False
