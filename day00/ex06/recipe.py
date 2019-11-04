import sys

def print_recipe(cookbook, recipe):
	printed = False
	for keys, values in cookbook.items():
		if (keys == recipe):
			printed = True
			print("The recipe {} :".format(keys))
			i = 0
			while (i < len(values[0])):
				print("Ingredient {} : {}".format(i, values[0][i]))
				i += 1
			print("for : {}\nTime to prepare : ".format(values[1], values[2]))
	if not (printed):
		print("This recipe is not in cookbook")

def delete_recipe(cookbook, recipe):
	if recipe in cookbook.keys():
		del cookbook[recipe]
	else:
		print("This recipe is not in cookbook")

def add_recipe(cookbook, key, value):
	try:
		cookbook.update({key:value})
	except:
		print("Bad arguments, can't create recipe")

def print_cookbook(cookbook):
	for keys, values in cookbook.items():
		print("The recipe {} :".format(keys))
		i = 0
		while (i < len(values[0])):
			print("Ingredient {} : {}".format(i, values[0][i]))
			i += 1
		print("for : {}\nTime to prepare : {} ".format(values[1], values[2]))

cookbook = {"sandwich":[["ham", "bread", "cheese", "tomatoes"], "lunch", 10],
"cake":[["flour", "sugar", "eggs"], "dessert", 60],
"salad":[["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15]
}

txt_choice = "\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: quit\n"
end = True
while (end):
	valid_choice = False
	while (valid_choice == False):
		choice = input("Please select an option by typing the corresponding number:" + txt_choice)
		try:
			choice = int(choice)
		except:
			print("This option does not exist, please type the corresponding number.")
			choice = 42
		if (choice > 0 and choice <= 5):
			valid_choice = True
	if (choice == 1):
		key = input("Enter the name of the recipe : ")
		value = [input("Enter the ingredients format like (steak,pasta ...)").split(",")]
		value.append(input("the recipe is for dessert, lunch ... ? "))
		try:
			value.append(int(input("Time needed for cook the recipe : ")))
		except:
			print("Invalid time")
			add_recipe(cookbook, key, value)
	elif (choice == 2):
		recipe_to_del = input("wich recipe you want remove ?")
		delete_recipe(cookbook, recipe_to_del)
	elif (choice == 3):
		recipe_to_print = input("wich recipe you want print ?")
		print_recipe(cookbook, recipe_to_print)
	elif (choice == 4):
		print_cookbook(cookbook)
	elif (choice == 5):
		print("Bye !")
		end = False
