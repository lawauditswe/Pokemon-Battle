# Check if Player has lost the battle

def loss_check(your_team):
	if len(your_team) == 0:
		print('Sorry, you have lost the battle.')
		return True
	return False