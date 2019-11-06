import sys

class Vector:

	def __init__(self, values):
		self.values = []
		self.length = 0
		if isinstance(values, list):
			for elt in values:
				if not isinstance(elt, float):
					print("Error, elements must be all float")
					sys.exit(0)
			self.values = values
			self.length = len(values)
		elif isinstance(values, int):
			for i in range(0, values):
				self.values.append(float(i))
				self.length += 1
		elif isinstance(values, tuple):
			if not (len(values) == 2):
				print("Error, tuple must be len of 2")
				sys.exit(0)
			for i in range(values[0], values[1]):
				self.values.append(float(i))
			self.length = len(values)
		else:
			print("ERROR, bad arguments")
			sys.exit(0)

	def __add__(self, new_value):
		new_values = []
		if isinstance(new_value, float):
			for value in self.values:
				new_values.append(value + float(new_value))
			new_vector = Vector(new_values)
			return (new_vector)
		else:
			print("ERROR, new value must be an float")
			sys.exit(0)

	def __radd__(self, new_value):
		if isinstance(new_value, float):
			return (self.__add__(new_value))
		else:
			print("ERROR, new value must be an float")
			sys.exit(0)

	def __sub__(self, value_to_sub):
		new_values = []
		if isinstance(value_to_sub, float):
			for value in self.values:
				new_values.append(value - float(value_to_sub))
			new_vector = Vector(new_values)
			return (new_vector)
		else:
			print("ERROR, new value must be an float")
			sys.exit(0)

	def __rsub__(self, value_to_sub):
		if isinstance(value_to_sub, float):
			return (self.__sub__(value_to_sub))
		else:
			print("ERROR, new value must be an float")
			sys.exit(0)

	def __truediv__(self, value_to_div):
		new_values = []
		if (isinstance(value_to_div, float) and value_to_div != 0.0):
			for value in self.values:
				new_values.append(value / float(value_to_div))
			new_vector = Vector(new_values)
			return (new_vector)
		else:
			print("ERROR, new value must be an float")
			sys.exit(0)

	def __rtruediv__(self, value_to_div):
		if isinstance(value_to_div, float):
			return (self.__truediv__(value_to_div))
		else:
			print("ERROR, value_to_div must be an float")
			sys.exit(0)

	def __mul__(self, val_to_mul):
		new_values = []
		if isinstance(val_to_mul, float):
			for value in self.values:
				new_values.append(value * float(val_to_mul))
			new_vector = Vector(new_values)
			return (new_vector)
		else:
			print("ERROR, new value must be an float")
			sys.exit(0)

	def __rmul__(self, val_to_mul):
		if isinstance(val_to_mul, float):
			return (self.__mul__(val_to_mul))
		else:
			print("ERROR, val_to_mul must be an float")
			sys.exit(0)

	def __repr__(self):
		return "Values : {}\nlength : {}\n".format(self.values, self.length)

	def __str__(self):
		return (self.__repr__())
