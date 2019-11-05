import sys
import string

def error():
	print("ERROR")
	sys.exit(0)

if (len(sys.argv) == 3):
	try:
		min = int(sys.argv[2])
	except:
		error()
	for ch in string.punctuation:
		sys.argv[1] = sys.argv[1].replace(ch, "")
	lst = sys.argv[1].split(" ")
	final = []
	for elt in lst:
		if (len(elt) > min):
			final.append(elt)
else:
	error()
print(final)
