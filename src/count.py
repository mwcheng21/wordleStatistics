import matplotlib.pyplot as plt


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


for n in range(1, 6):
	plt.figure(n)
	letters = list(alphabet)
	occurance = [placements[str(n)][letter] for letter in list(alphabet)]
	totalLetters = sum(occurance)
	frequencies = [(x/totalLetters)*100 for x in occurance]
	plt.bar(letters, frequencies)
	plt.title('Letter Frequencies for Position ' + str(n))
	plt.xlabel('letter')
	plt.ylabel('frequencies (\%)')
	plt.savefig("../img/" + str(n) + ".png")


frequencies = [totalOccurances[letter] for letter in list(alphabet)]
totalLetters = sum(frequencies)
frequencies = [(x/totalLetters)*100 for x in frequencies]
plt.figure(6)
letters = list(alphabet)
plt.bar(letters, frequencies)
plt.title('Letter Frequencies for 5-letter Words')
plt.xlabel('letter')
plt.ylabel('frequencies (\%)')
plt.savefig("../img/total.png")


