from Pokemon_class import *
from pokemon import *
from Move_class import *
from attack import *
from random import randint
import random
from accuracy import *
from your_turn import *
from oppo_turn import *
from oppo_attack import *
from loss_check import *
from faint_check import *
from win_check import *
from your_switch import *
from your_active_pokemon import *

play_again = True

your_name = input('What is your username?\n\n')
print(f'Battle started between {your_name} and your opponent!\n')

your_team = [bulbasaur, staryu, ponyta]
oppo_team = [pikachu, geodude, dratini]
temp_your_team = your_team
temp_oppo_team = oppo_team

# your_party_assignment = dic{your_pokemon1: your_team[0], your_pokemon2: your_team[1], your_pokemon3: your_team[2]}
# oppo_party_assignment = dic{oppo_pokemon1: oppo_team[0], oppo_pokemon2: oppo_team[1], oppo_pokemon3: oppo_team[2]}

your_pokemon1 = your_team[0]
your_pokemon2 = your_team[1]
your_pokemon3 = your_team[2]
oppo_pokemon1 = oppo_team[0]
oppo_pokemon2 = oppo_team[1]
oppo_pokemon3 = oppo_team[2]

#store your pokemon's default HP into a variable
your_pokemon1_HP = your_pokemon1.hp_stat
your_pokemon2_HP = your_pokemon2.hp_stat
your_pokemon3_HP = your_pokemon3.hp_stat
oppo_pokemon1_HP = oppo_pokemon1.hp_stat
oppo_pokemon2_HP = oppo_pokemon2.hp_stat
oppo_pokemon3_HP = oppo_pokemon3.hp_stat

while play_again == True:

	your_team = temp_your_team[:]
	oppo_team = temp_oppo_team[:]

	game_over = False

	your_team_copy = your_team

	print(f"Your opponent's team: {oppo_pokemon1.name}, {oppo_pokemon2.name}, {oppo_pokemon3.name}.\n")

	print('Please select your lead: \n')
	selection = 1
	for pokemon in your_team:
		print(f'{selection}: {your_team[selection-1].name}\n')
		selection += 1 

	your_lead_choice = input()
	your_lead_choice = int(your_lead_choice)

	while your_lead_choice > len(your_team) or your_lead_choice <= 0:
		print('Invalid selection. Please select again.\n')
		your_lead_choice = input()
		your_lead_choice = int(your_lead_choice)

	# your_pokemon is your active pokemon
	if your_lead_choice == 1:
		your_pokemon = your_pokemon1
	elif your_lead_choice == 2:
		your_pokemon = your_pokemon2
	elif your_lead_choice == 3:
		your_pokemon = your_pokemon3

	your_team_copy.remove(your_pokemon)

	rand_num = random.randint(0,2)
	if rand_num == 0:
		oppo_pokemon = oppo_team[0]
	elif rand_num == 1:
		oppo_pokemon = oppo_team[1]
	elif rand_num == 2:
		oppo_pokemon = oppo_team[2]

	print('\n')
	print(f'Go! {your_pokemon.name}!\n')
	print(f'Your opponent sent out {oppo_pokemon.name}!\n')

	# your_current_pokemon = your_pokemon

	oppo_team_copy = oppo_team
	oppo_team_copy.remove(oppo_pokemon)

	# Turn Number
	turn_number = 1

	while game_over == False:

	# Setting both Pokemon's HP / asking player to select move if neither Mon has fainted

		print(f'Turn {turn_number}\n')
		print(f'{your_pokemon.name}: {your_pokemon.hp_stat} HP')
		print(f'The opposing {oppo_pokemon.name}: {oppo_pokemon.hp_stat} HP\n')
		print('Would you like to attack or switch?')
		print('1) Attack')
		print('2) Switch')

		# if len(your_team_copy) == 0:
		player_option = int(input())
		while player_option != 1 and player_option != 2:
			print('Invalid selection. Please select again.')
			player_option = int(input())

	# If you attack:
		if player_option == 1:
			moves = [your_pokemon.move1, your_pokemon.move2, your_pokemon.move3, your_pokemon.move4]
			your_pokemon_moveset = []
			for move in moves:
				if move != None:
					your_pokemon_moveset.append(move)

			move_option = 1
			for moves in your_pokemon_moveset:
				print(f'{move_option}) {your_pokemon_moveset[move_option-1].name}')
				move_option += 1

			player_choice = int(input())
			print('\n')

			while player_choice > move_option:
				print('Invalid selection. Please select again.')
				player_choice = int(input())
				print('\n')

# Speed check: if your Pokemon is faster or it wins the speed tie
			if your_pokemon.spe_stat > oppo_pokemon.spe_stat or your_pokemon.spe_stat == oppo_pokemon.spe_stat and randint(1,10000) % 2 == 0:

			# Player is Attacking
				your_turn(your_pokemon,oppo_pokemon,player_choice)
				faint_check(oppo_pokemon)

				if faint_check(oppo_pokemon) == True:
					# win_check(oppo_pokemon,oppo_team_copy)
					if win_check(oppo_pokemon,oppo_team_copy) == False:
						oppo_pokemon = oppo_team_copy[0]
						print(f'Your opponent sent out {oppo_pokemon.name}!\n')
						oppo_team_copy.remove(oppo_team_copy[0])
					else:
						game_over = True

				# Opponent Pokemon's move:
				else:
					oppo_turn(your_pokemon,oppo_pokemon)
					if faint_check(your_pokemon) == True:
						# loss_check(your_pokemon,your_team_copy)
						if loss_check(your_team_copy) == False:

							if len(your_team_copy) > 1:
								print('Please select your next Pokemon: ')
								option = 1
								for pokemon in your_team_copy[:]:
									print(f'{option}) {pokemon.name}')
									option += 1

								player_choice = input()
								player_choice = int(player_choice)

								your_pokemon = your_team_copy[player_choice-1]
							
								your_team_copy.remove(your_team_copy[player_choice-1])

							else:
								your_pokemon = your_team_copy[0]
								your_team_copy.remove(your_team_copy[0])

							print(f'You sent out {your_pokemon.name}!\n')

						else:
							game_over = True

# If your Pokemon is slower / speed tie is lost
			else:
				oppo_turn(your_pokemon,oppo_pokemon)
				if faint_check(your_pokemon) == True:
					# loss_check(your_pokemon,your_team_copy)
					if loss_check(your_team_copy) == False:

						if len(your_team_copy) > 1:
							print('Please select your next Pokemon: ')
							option = 1
							for pokemon in your_team_copy[:]:
								print(f'{option}) {pokemon.name}')
								option += 1

							player_choice = input()
							player_choice = int(player_choice)

							your_pokemon = your_team_copy[player_choice-1]
						
							your_team_copy.remove(your_team_copy[player_choice-1])

						else:
							your_pokemon = your_team_copy[0]

						print(f'You sent out {your_pokemon.name}!\n')

					else:
						game_over = True

				else:
					your_turn(your_pokemon,oppo_pokemon,player_choice)
					faint_check(oppo_pokemon)
					if faint_check(oppo_pokemon) == True:
						if win_check(oppo_pokemon,oppo_team_copy) == False:
							oppo_pokemon = oppo_team_copy[0]
							print(f'Your opponent sent out {oppo_pokemon.name}!\n')
							oppo_team_copy.remove(oppo_team_copy[0])
						else:
							game_over = True

# Switch
		elif player_option == 2 and len(your_team_copy) > 0:
			switch_option = 0
			for pokemon in your_team_copy[:]:
				print(f'{switch_option+1}) Switch to {pokemon.name}')
				switch_option += 1
			print('\n')

			player_choice = input()
			player_choice = int(player_choice)

			while player_choice > switch_option+1:
				print('Invalid selection. Please select again.')
				player_choice = int(input())

			pokemon_switched_out = your_pokemon
			your_pokemon = your_active_pokemon(your_team_copy[player_choice-1])
			your_team_copy = your_switch(your_team_copy, pokemon_switched_out, your_team_copy[player_choice-1])

			oppo_turn(your_pokemon,oppo_pokemon)

			if faint_check(your_pokemon) == True:
				# your_team_copy = your_team_copy.remove(your_pokemon)
				# print(your_team_copy) # your_team_copy == None

				if loss_check(your_team_copy) == False: 

					if len(your_team_copy) == 1:
						your_pokemon = your_team_copy[0]

					else:
						switch_option = 0
						for pokemon in your_team_copy[:]:
							print(f'{switch_option+1}) Switch to {pokemon.name}')
							switch_option += 1
						print('\n')

						player_choice = input()
						player_choice = int(player_choice)

						while player_choice > switch_option+1:
							print('Invalid selection. Please select again.')
							player_choice = int(input())
						
						your_pokemon = your_team_copy[0]
						print(f'You sent out {your_pokemon.name}!\n')

					your_team_copy.remove(your_team_copy[0])

				else:
					game_over = True

		else:
			print('You have no remaining Pokemon in your party!\n')
			turn_number -= 1

		turn_number += 1

	if game_over == True:
		replay = input('Would you like to play again? Type "y" and press Enter if so. Press any other button to quit the game.\n\n')
		if replay == 'y':
			# reset HP to default HP, i.e. all mons back at full health
			your_pokemon1.hp_stat = your_pokemon1_HP
			your_pokemon2.hp_stat = your_pokemon2_HP
			your_pokemon3.hp_stat = your_pokemon3_HP
			oppo_pokemon1.hp_stat = oppo_pokemon1_HP
			oppo_pokemon2.hp_stat = oppo_pokemon2_HP
			oppo_pokemon3.hp_stat = oppo_pokemon3_HP
			play_again = True

		else:
			play_again = False
			print('Thank you for playing!')