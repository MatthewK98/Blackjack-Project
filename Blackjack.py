import random
dealer_cards = [] #Stores dealer data
player_cards = [] #Stores player data
cards = ["Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ] #All card options

def deal_cards(players):
	for player in players:
		player.append(random.choice(cards))
		player.append(random.choice(cards))

def display_hands(players,show_dealer_cards = False): #Optional argument
	dealer = players[0]
	all_players = players[1:]
	if len(dealer) != 2 or show_dealer_cards:
		print("Dealer has cards:", ", ".join(dealer),f"({score(dealer)})")
	else:
		print("Dealer has card X and",dealer[1],f"({score(dealer[1:])})")
	for player in all_players:
		print("Your cards are:", ", ".join(player), f"({score(player)})")

def game(players):
	dealer = players[0]
	all_players = players[1:]
	for player in all_players:
		while not bust(player):
			display_hands(players) #Showing the whole game
			choice_of_play = stay_or_hit()
			if choice_of_play == "h":
				player_cards.append(random.choice(cards))
			else:
				break
		if bust(player):
			display_hands(players)
			print("Your Busted!")
	play_dealer(dealer)
	display_hands(players, show_dealer_cards = True) #Optional argument is true , which gives different message
	winner = show_winner(players)
	if winner is None:
		print("Everyone is Busted!")

	elif winner == 0:
		print("Dealer wins the game!")
	else:
		print(f"Player {winner} wins the game!")


	if blackjack(dealer_cards):
		return "Dealer got blackjack"
	elif bust(dealer_cards):
		return "Dealer bust"
	
def stay_or_hit():
	"""Ask the player if s/he wants to stay or hit.

	The user can enter stay or s or hit or h.
	The function will only return either 's' or 'h'
	"""
	while True:
		choice_of_play = input("Do you want to stay or hit ").lower()
		if choice_of_play in ("hit","stay","h","s"):
			return choice_of_play[0]
		print("Please type hit or stay!")

def blackjack(player):
	return score(player) == 21 

def bust(player):
	return score(player) > 21

def play_dealer(dealer):
	while score(dealer) < 17:
		dealer.append(random.choice(cards))


def show_winner(players):
	best = 0
	best_player = None #Incase everyone is bust
	for idx, player in enumerate(players):
		current_score = score(player)
		if current_score <= 21 and current_score > best:
			best = current_score
			best_player = idx
	return best_player


def score(hand):

	total = 0
	ace = 0
	for card in hand:
		if card == "Ace":
			ace += 1
			total += 11
		elif card in ("Jack","King","Queen"):
			total += 10
		else:
			total += int(card)
	while total > 21  and ace > 0:
		total -= 10
		ace -= 1
	return total


if __name__ == '__main__':
	players = [dealer_cards,player_cards]
	deal_cards(players)
	game(players)