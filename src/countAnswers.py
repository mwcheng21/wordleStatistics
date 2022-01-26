import matplotlib.pyplot as plt
import numpy as np


with open("../data/answers.txt", 'r') as answerWords:
	words = answerWords.readlines()[0].strip().split(" ")

alphabet = "abcdefghijklmnopqrstuvwxyz"

placements = {
			"1": {},
			"2": {},
			"3": {},
			"4": {},
			"5": {}
			}
totalOccurances = {}

for letter in alphabet:
	for i in range(1, 6):
		placements[str(i)][letter] = 0
	totalOccurances[letter] = 0

for word in words:
	for i in range(1, 6):
		placements[str(i)][word[i-1:i]] += 1
		totalOccurances[word[i-1:i]] += 1

# Plot positions 1-5
for n in range(1, 6):
	plt.figure(n)
	letters = list(alphabet)
	occurance = [placements[str(n)][letter] for letter in list(alphabet)]
	totalLetters = sum(occurance)
	frequencies = [(x/totalLetters)*100 for x in occurance]
	frequencies, letters = zip(*sorted(zip(frequencies, letters), reverse=True))
	plt.bar(letters, frequencies)
	plt.title('Letter Frequencies of Answers for Position ' + str(n))
	plt.xlabel('letter')
	plt.ylabel('frequencies (%)')
	plt.savefig("../img/answers" + str(n) + ".png")

# Plot total frequencies for 5 letter words
frequencies = [totalOccurances[letter] for letter in list(alphabet)]
totalLetters = sum(frequencies)
frequencies = [(x/totalLetters)*100 for x in frequencies]
plt.figure(6)
letters = list(alphabet)
frequencies, letters = zip(*sorted(zip(frequencies, letters), reverse=True))
plt.bar(letters, frequencies)
plt.title('Letter Frequencies for All Answers')
plt.xlabel('letter')
plt.ylabel('frequencies (%)')
plt.savefig("../img/answersTotal.png")
