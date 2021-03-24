# Switching Pokemon

def your_switch(team, pokemon_out, pokemon_in):

	team.append(pokemon_out)

	team.remove(pokemon_in)

	print(f'{pokemon_out.name}, come back!\n')
	print(f'Go! {pokemon_in.name}!')

	return team