t = (19, 42, 21)
tmp = []
try:
	t_len = str(len(t))
except TypeError:
	sys.exit(0)
for element in t:
	tmp.append(str(element))
str = "The " + t_len + " numbers are : " + " , ".join(tmp)
print(str)
