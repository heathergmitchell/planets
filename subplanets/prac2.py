import itertools
import random

if __name__ == '__main__':
	deck = list(itertools.product(range(1, 14),['Spade', 'Heart', 'Diamond', 'Club']))

	random.shuffle(deck)

	print("You got: ")
	for i in range(7):
		print(deck[i][0], "of", deck[i][1])
