import matplotlib.pyplot as plt

alphabet = "abcdefghijklmnopqrstuvwxyz"

letters = list(alphabet)
# from https://www.lexico.com/explore/which-letters-are-used-most
occurance = [8.4966, 2.0720, 4.5388, 3.3844, 11.1607, 1.8121, 2.4705, 3.0034, 7.5448, 0.1965, 1.1016, 5.4893, 3.0129, 6.6544, 7.1635, 3.1671, 0.1962, 7.5809, 5.7351, 6.9509, 3.6308, 1.0074, 1.2899,0.2902, 1.7779, 0.2722]
plt.bar(letters, occurance)
plt.title('Letter Frequencies in English Language')
plt.xlabel('letter')
plt.ylabel('frequency')
plt.savefig("englishTotal.png")


