from attack import *
from accuracy import *
from damage_multipliers import *
from oppo_attack import *

def oppo_turn(your_pokemon, oppo_pokemon):

	oppo_pokemon_moveset = [oppo_pokemon.move2,oppo_pokemon.move3,oppo_pokemon.move4]

	max_damage = oppo_attack(oppo_pokemon,your_pokemon,oppo_pokemon.move1)
	oppo_move = oppo_pokemon.move1
	for move in oppo_pokemon_moveset:
		if move != None:
			move_damage = oppo_attack(oppo_pokemon,your_pokemon,move)
			if move_damage > max_damage:
				max_damage = move_damage
				oppo_move = move

	print(f'{oppo_pokemon.name} used {oppo_move.name}!\n')

	crit_damage = int(max_damage * critical_hit())
	if crit_damage != max_damage:
		print('A critical hit!\n')

	max_damage = int(crit_damage * random_number())
	max_damage = int(max_damage * stab(oppo_pokemon,move))

	if accuracy(oppo_move) != 0:
		if effectiveness(oppo_move,your_pokemon) == 2 or effectiveness(oppo_move,your_pokemon) == 4:
			print("It's super effective!\n")
		elif effectiveness(oppo_move,your_pokemon) == 0.5 or effectiveness(oppo_move,your_pokemon) == 0.25:
			print("It's not very effective...\n")
		elif effectiveness(oppo_move,your_pokemon) == 0:
			print(f'The opposing {oppo_pokemon.name} was immune to the attack!\n')
	else:
		print(f'{your_pokemon.name} avoided the attack!\n')
		max_damage = 0

	your_temp = your_pokemon.hp_stat
	your_pokemon.hp_stat = your_pokemon.hp_stat - max_damage

	if your_pokemon.hp_stat <= 0:
		print(f'{your_pokemon.name} lost {your_temp} HP.\n')
		print(f'{your_pokemon.name} has fainted.\n')

	else:
		print(f'{your_pokemon.name} lost {max_damage} HP.\n')
		print(f'{your_pokemon.name} has {your_pokemon.hp_stat} HP remaining.\n')

