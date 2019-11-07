

class Evaluator():
	def zip_evaluate(coefs, words):
		if (len(coefs) != len(words)):
			return (-1)
		sum = 0
		result = zip(words, coefs)
		for word, coef in result:
			sum += len(word) * coef
		return (sum)

	def enumerate_evaluate(coefs, words):
		if (len(coefs) != len(words)):
			return (-1)
		sum = 0
		for count, elt in enumerate(words):
			sum += len(elt) * coefs[count]
		return (sum)
