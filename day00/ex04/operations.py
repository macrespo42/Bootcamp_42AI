import sys

error = False
if (len(sys.argv) > 3):
	print("InputError: too many arguments")
	error = True
if (len(sys.argv) < 3):
	error = True
if (error == True):
	print("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")
	sys.exit(0)
try:
	nb1 = int(sys.argv[1])
	nb2 = int(sys.argv[2])
except:
	print("Bad arguments")
	sys.exit(0)
print("Sum:\t\t{}".format(nb1 + nb2))
print("Difference: {}".format(nb1 - nb2))
print("Product\t {}".format(nb1 * nb2))
try:
	print("Quotient: {}".format(float(nb1) / float(nb2)))
except ZeroDivisionError:
	print("ERROR (div by zero)")
except TypeError:
	print("Bad input")
try:
	print("Quotient: {}".format(nb1 % nb2))
except ZeroDivisionError:
	print("ERROR (modulo by zero)")
