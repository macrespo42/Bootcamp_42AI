import sys

if (len(sys.argv) == 2):
	try:
		nb = int(sys.argv[1])
	except:
		print("ERROR", end="");
	if (nb == 0):
		print("I'm Zero", end="")
	elif (nb % 2 == 0):
		print("I'm Even", end="")
	else:
		print("I'm Odd", end="")
else:
	print("ERROR", end="")
