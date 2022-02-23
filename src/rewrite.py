import datetime

x = datetime.datetime(2021, 6, 19)

puzzleNumber = 0
with open("../data/answersNew.txt", 'r') as answerWords:
	words = answerWords.readlines()[0].strip().split(" ")
with open('../data/searchableAnswersNew.txt', 'w') as outfile:
	for word in words:
		outfile.write(str(puzzleNumber) + ": ")
		outfile.write(x.strftime("%B %d, %Y "))
		outfile.write(word)
		outfile.write('\n')
		x += datetime.timedelta(days=1)
		puzzleNumber += 1