import random

class guessing:    
	# initializing the variables needed
	def __init__(self,word):
		self.word = word
		self.count = 5
		self.guesses = []
		self.done = False
		

	def game(self):
		# Loop of the program
		print(self.word)
		while not self.done:
			for char in self.word:
				if char.upper() in self.guesses:
					print(char, end=" ")
				else:
					print("_", end=" ")	
			
			# get an input from the user
			guess = input("\nInput a letter : ")
			self.guesses.append(guess.upper())
			print()
			
			# compare if guess is in the word
			if guess.upper() not in self.word.upper():
				self.count -= 1	
				self.done = False
				if self.count <= 0:
					break
			self.done = True
			for char in self.word:
				if char not in self.guesses:
					self.done = False
		# out of loop
		if self.done:
			print(f"You WIN!!! - You got the word {self.word}")
		else:
			print(f"You LOSE - The correct word is {self.word}")
			

# source of data from file text.txt
with open("text.txt","r") as w:
	words = w.readlines()

# select a word from text.txt
word = random.choice(words)[:-1]

# create an instance
g = guessing(word.upper())
g.game()
