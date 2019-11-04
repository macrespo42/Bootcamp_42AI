import sys

if (len(sys.argv) == 2):
	try:
		nb = int(sys.argv[1])
	except:
		print("ERROR");
	if (nb == 0):
		print("I'm Zero")
	elif (nb % 2 == 0):
		print("I'm Even")
	else:
		print("I'm Odd")
else:
	print("ERROR")
