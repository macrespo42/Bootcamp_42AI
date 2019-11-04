phrase = "The right format"
phrase_len = len(phrase)
diff = 42 - phrase_len
fill = []
i = 0
while (i < diff):
	fill.append("-")
	i += 1
print("".join(fill) + phrase, end="")
