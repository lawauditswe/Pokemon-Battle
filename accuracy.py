# Accuracy checks 
from random import randint
import random

def accuracy(move):
	miss = random.randint(1,100)
	if miss > move.accuracy:
		return 0
	return 1