import datetime

class Book:
	def __init__(self, name):
		if (type(name) == str):
			self.name = name
		else:
			print("ERROR, name must be a string")
			sys.exit(0)
		self.last_update = datetime.datetime.now()
		self.creation_date = datetime.datetime.now()
		self.recipes_list = {"starter":[], "lunch":[], "dessert":[]}

	def get_recipe_by_name(self, name):
		for recipe_type in self.recipes_list.values():
			for elt in recipe_type:
				if (elt.name == name):
					print (elt)
					return (elt)
		print("ERROR, they are no recipe with this name in this cookbook")
		return (None)

	def get_recipes_by_types(self, recipe_type):
		if recipe_type in self.recipes_list.keys():
			for elt in self.recipes_list[recipe_type]:
				print(elt)
		else:
			print("ERROR, this recipe type doesn't exist")

	def add_recipe(self, recipe):
		if (isinstance(recipe, recipe.Recipe)):
			self.recipes_list[recipe.recipe_type].append(recipe)
		else:
			print("ERROR, the recipe must be an instance of Recipe class")
		self.last_update = datetime.datetime.now()

	def __str__(self):
		return "name : {}\ncreation date : {}\nlast update {}\n".format(self.name, self.creation_date, self.last_update)
