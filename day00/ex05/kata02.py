t = (12, 42, 1999, 3, 30)
date = []
time = []
i = 0
while (i < 3):
	date.append(str(t[i]))
	i += 1
date = "/".join(date) + " "
while (i < 5):
	if t[i] < 10:
		time.append("0" + str(t[i]))
	else:
		time.append(str(t[i]))
	i+= 1
time = ":".join(time)
print("{} {}".format(date, time))
