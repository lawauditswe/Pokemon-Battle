# Opponent attack

from Pokemon_class import *
from damage_multipliers import *
from accuracy import *
from critical_hit import *
from damage_multipliers import *
from accuracy import *
from pokemon import *
from damage_multipliers import *


def oppo_attack(attacking_Pokemon,target_Pokemon,move):
	level = attacking_Pokemon.level
	power = move.power
	if move.category == 'physical':
		A = attacking_Pokemon.atk_stat
		D = target_Pokemon.def_stat
	elif move.category == 'special':
		A = attacking_Pokemon.spa_stat
		D = target_Pokemon.spd_stat

	oppo_damage = int(int(int(2. * level / 5. + 2.) * power * A / D) / 50.) + 2. # base damage
	
	oppo_damage = int(oppo_damage * random_number())
	oppo_damage = int(oppo_damage * stab(attacking_Pokemon,move))

	if oppo_damage == 0:
		oppo_damage = 1

	oppo_damage = int(oppo_damage * effectiveness(move,target_Pokemon))

	return oppo_damage