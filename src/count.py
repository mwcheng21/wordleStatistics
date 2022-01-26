import matplotlib.pyplot as plt
import numpy as np

with open("../data/words.txt", 'r') as allWords:
	words = allWords.readlines()[0].strip().split(" ")


with open("../data/answers.txt", 'r') as answerWords:
	words += answerWords.readlines()[0].strip().split(" ")

alphabet = "abcdefghijklmnopqrstuvwxyz"

placements = {
			"1": {},
			"2": {},
			"3": {},
			"4": {},
			"5": {}
			}
totalOccurances = {}

for word in words:
	for i in range(1, 6):
		placements[str(i)][word[i-1:i]] = 0 if word[i-1:i] not in placements[str(i)] else placements[str(i)][word[i-1:i]] + 1
		totalOccurances[word[i-1:i]] = 0 if word[i-1:i] not in totalOccurances else totalOccurances[word[i-1:i]] + 1

# Plot positions 1-5
for n in range(1, 6):
	plt.figure(n)
	letters = list(alphabet)
	occurance = [placements[str(n)][letter] for letter in list(alphabet)]
	totalLetters = sum(occurance)
	frequencies = [(x/totalLetters)*100 for x in occurance]
	frequencies, letters = zip(*sorted(zip(frequencies, letters), reverse=True))
	plt.bar(letters, frequencies)
	plt.title('Letter Frequencies for Position ' + str(n))
	plt.xlabel('letter')
	plt.ylabel('frequencies (\%)')
	plt.savefig("../img/" + str(n) + ".png")

# Plot total frequencies for 5 letter words
frequencies = [totalOccurances[letter] for letter in list(alphabet)]
totalLetters = sum(frequencies)
frequencies = [(x/totalLetters)*100 for x in frequencies]
plt.figure(6)
letters = list(alphabet)
frequencies, letters = zip(*sorted(zip(frequencies, letters), reverse=True))
plt.bar(letters, frequencies)
plt.title('Letter Frequencies for 5-letter Words')
plt.xlabel('letter')
plt.ylabel('frequencies (\%)')
plt.savefig("../img/total.png")

# Plot frequencies for all english words
plt.figure(7)
letters = list(alphabet)
# from https://www.lexico.com/explore/which-letters-are-used-most
occurance = [8.4966, 2.0720, 4.5388, 3.3844, 11.1607, 1.8121, 2.4705, 3.0034, 7.5448, 0.1965, 1.1016, 5.4893, 3.0129, 6.6544, 7.1635, 3.1671, 0.1962, 7.5809, 5.7351, 6.9509, 3.6308, 1.0074, 1.2899,0.2902, 1.7779, 0.2722]
occurance, letters = zip(*sorted(zip(occurance, letters), reverse=True))
plt.bar(letters, occurance)
plt.title('Letter Frequencies in English Language')
plt.xlabel('letter')
plt.ylabel('frequency')
plt.savefig("../img/englishTotal.png")



# Plot total frequencies of both
plt.figure(8)
ind = np.arange(26)
width = 0.3
letters = list(alphabet)
# from https://www.lexico.com/explore/which-letters-are-used-most
englishFreq = [8.4966, 2.0720, 4.5388, 3.3844, 11.1607, 1.8121, 2.4705, 3.0034, 7.5448, 0.1965, 1.1016, 5.4893, 3.0129, 6.6544, 7.1635, 3.1671, 0.1962, 7.5809, 5.7351, 6.9509, 3.6308, 1.0074, 1.2899,0.2902, 1.7779, 0.2722]
frequencies = [totalOccurances[letter] for letter in list(alphabet)]
totalLetters = sum(frequencies)
frequencies = [(x/totalLetters)*100 for x in frequencies]
plt.bar(ind, frequencies, width, label="5-letter Words")
plt.bar(ind+width, englishFreq, width, label="All English Words")
plt.xticks(ind + width / 2, letters)
plt.legend(loc='best')
plt.title('Letter Frequencies')
plt.xlabel('letter')
plt.ylabel('frequency')
plt.savefig("../img/compTotal.png")



