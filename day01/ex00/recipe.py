import sys

class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
		valid = True
		if (type(name) == str):
			self.name = name
		else:
			print("ERROR, name must be a string")
			valid = False
		if (type(cooking_lvl) == int):
			if (cooking_lvl > 0 and cooking_lvl <= 5):
				self.cooking_lvl = cooking_lvl
			else:
				print("ERROR, cooking_lvl must be between 1 and 5")
				valid = False
		else:
			print("ERROR, coooking must be an integer")
			valid = False
		if (type(cooking_time) == int and cooking_time >= 0):
			self.cooking_time = cooking_time
		else:
			print("ERROR, name must be an positive integer")
			valid = False
		if (type(ingredients) == list):
			for elt in ingredients:
				if type(elt) != str:
					print("ERROR,the list must contain only string")
					valid = False
					break
			self.ingredients = ingredients
		else:
			print("ERROR, ingredients must be a list")
			valid = False
		if (type(description) == str):
			self.description = description
		else:
			print("ERROR, description must be a string")
			valid = False
		if (type(recipe_type) == str):
			if (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"):
				self.recipe_type = recipe_type
			else:
				print("ERROR, recipe_type must be equal to starter|lunch|dessert")
				valid = False
		else:
			print("ERROR, recipe_type must be a string")
			valid = False
		if (valid == False):
			sys.exit(0)

	def __str__(self):
		return "name : {}\ncooking_lvl : {}\ncoooking_time : {}\ningredients : {}\nrecipe_type : {}\ndescription : {}".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.recipe_type, self.description)
