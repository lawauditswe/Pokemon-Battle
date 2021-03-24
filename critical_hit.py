# Critical hit 
import random
from random import randint

def critical_hit():
	crit = random.randint(1,240000)

	if crit % 24 == 0:
		return 6144/4096
	return 1
