#!/usr/bin/env python
# This project is a easy guessing game. Users will guess the side of the coin and the game
# can keep the highest score.

from random import choice

def coin_flip():
	coinSide = choice(["heads", "tails"])
	return coinSide

# --------------------- Main Program Below ------------------------
f = open("highestScore.txt", "r+")
d = open("highestScoreOwnerName.txt", "r+")

highestScoreOwnerName = d.read()
highestScore = f.read()

print("This is a coin guessing game. All time highest score: {}.(by {})" \
.format(highestScore, highestScoreOwnerName))

name = raw_input("What\'s your name? ")
score = 0

while True:
	guess = raw_input("Please predict heads or tails ")
	coinSide = coin_flip()
	guess = guess[0].lower()
	
	if guess != 'h' and guess != 't':
		print("Every coin only have two sides, heads and tails.")
		break
	
	if guess == coinSide[0]:
		score += 1
		print("That\'s right! +1!!! Present score: {}".format(score))
	else:
		print("That\'s wrong. Game over. Good luck next time. Final score: {}".format(score))
		break
	
if score >= int(highestScore):
	f.seek(0)
	f.write(str(score))
	d.seek(0)
	d.write(name)
	print("Congratulations, you break the records!!! New highest score: {}".format(score))
			
		