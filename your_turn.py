from attack import *
from accuracy import *
from damage_multipliers import *

def your_turn(your_pokemon,oppo_pokemon,player_choice):
	if player_choice == 1: 
		your_move = your_pokemon.move1
	elif player_choice == 2:
		your_move = your_pokemon.move2
	elif player_choice == 3:
		your_move = your_pokemon.move3
	elif player_choice == 4:
		your_move = your_pokemon.move4

	print(f'{your_pokemon.name} used {your_move.name}!\n')

# if your Pokemon is attacking (using a physical or special attack)
	if your_move.category == 'physical' or your_move.category == 'special':
		damage = attack(your_pokemon,oppo_pokemon,your_move)

		if accuracy(your_move) != 0:
			if effectiveness(your_move,oppo_pokemon) == 2 or effectiveness(your_move,oppo_pokemon) == 4:
				print("It's super effective!\n")
			elif effectiveness(your_move,oppo_pokemon) == 0.5 or effectiveness(your_move,oppo_pokemon) == 0.25:
				print("It's not very effective...\n")
			elif effectiveness(your_move,oppo_pokemon) == 0:
				print(f'The opposing {oppo_pokemon.name} was immune to the attack!\n')
		else:
			print(f'{oppo_pokemon.name} avoided the attack!\n')
			damage = 0

		oppo_temp = oppo_pokemon.hp_stat
		oppo_pokemon.hp_stat = oppo_pokemon.hp_stat - damage

		if oppo_pokemon.hp_stat <= 0:
			print(f'The opposing {oppo_pokemon.name} lost {oppo_temp} HP.\n')
			print(f'The opposing {oppo_pokemon.name} has fainted.\n')

		else:
			print(f'The opposing {oppo_pokemon.name} lost {damage} HP.\n')
			print(f'The opposing {oppo_pokemon.name} has {oppo_pokemon.hp_stat} HP remaining!\n')


