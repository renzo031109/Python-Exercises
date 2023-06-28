import random

class guessing:    
	def __init__(self,word):
		self.word = word
		self.count = 3
		self.guesses = []
		self.done = False
		

	def game(self):
		print(self.word)
		while not self.done:
			for char in self.word:
				if char.upper() in self.guesses:
					print(char, end=" ")
				else:
					print("_", end=" ")	
			

			guess = input("\nInput a letter : ")
			self.guesses.append(guess.upper())
			print()
			

			if guess.upper() not in self.word.upper():
				self.count -= 1	
				self.done = False
				if self.count <= 0:
					break
			self.done = True
			for char in self.word:
				if char not in self.guesses:
					self.done = False
	
		if self.done:
			print("You WIN")
		else:
			print("You LOSE")
			
words = ['RENAN','URIEL','RAIN','ANALYN']
word = random.choice(words)
g = guessing(word)
g.game()
