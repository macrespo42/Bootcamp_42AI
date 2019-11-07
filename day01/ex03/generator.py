def generator(text, sep=" ", option=None):
	if not (isinstance(text, str)):
		return ("ERROR")
	if (option == None or option == "shuffle"):
		lst = text.split(sep)
	elif (option == "ordered"):
		lst = sorted(text.split(sep))
	elif (option == "unique"):
		lst = list(dict.fromkeys(text.split(sep)))
	elif (option == "shuffle"):
		lst = set(text.split(sep))
	else:
		print("This option doesn't exist")
		return (None)
	for i in lst:
		yield i

gen = "Hello les amis"
for i in generator(gen, option="shuffle"):
	print(i);
