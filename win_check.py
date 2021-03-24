# Check to see if the Player has won

def win_check(oppo_pokemon,oppo_team_copy):
	if len(oppo_team_copy) == 0:
		print('Congratulations, you have won the battle!')
		return True
	return False
