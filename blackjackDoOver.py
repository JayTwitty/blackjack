
import random
# ASKING THE PLAYER FOR THEIR NAME AND CREATING A SHUFFLED DECK OF CARDS CALLED 'self.cards'

player = input("Player 1, What is your name? ")

print("=" * 20)


class Deck:
    def __init__(self):
        self.card_values = [x for x in range(2, 11)] + ["Ace", "Jack", "Queen", "King"]
        self.card_suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        self.cards = [[[value, "of " + suit] for suit in self.card_suits] for value in self.card_values]

        shuffled_cards = []

        for card in self.cards:
            for x in card:
                shuffled_cards.append(x)
                random.shuffle(shuffled_cards)
        self.cards = shuffled_cards

# CREATING AN INSTANCE OF THE DECK CLASS CALLED "game_deck"

game_deck = Deck()

# print(game_deck.cards)  # HIDDEN OPTION TO PRINT THE DECK OF CARDS

# CREATING THE INITIAL HAND FOR THE PLAYER AND THE DEALER

player_real_hand = []
dealer_real_hand = []
for x in range(2):
    player_real_hand.append(game_deck.cards.pop())
    dealer_real_hand.append(game_deck.cards.pop())
game = True
counter = 0
while True:
    print("Round: {}".format(counter + 1))
    print("{} your hand is...".format(player))
    print(player_real_hand)
    print("The Dealer\'s hand is...")
    print(dealer_real_hand)
# GAME LOGIC: START OUT WITH FINDING THE VALUE OF THE DEALER AND PLAYER HAND
    index = counter % 2
    player_values = []
    dealer_values = []
    player_hand_value = 0
    dealer_hand_value = 0
    for x in player_real_hand:
        player_values.append(x[0])
    for x in dealer_real_hand:
        dealer_values.append(x[0])
    for item in player_values:
        if item in ["King", "Queen", "Jack"]:
            player_hand_value += 10
        elif item == "Ace":
            if player_hand_value + 11 > 21:
                player_hand_value += 1
            else:
                player_hand_value += 11
        else:
            player_hand_value += item
    for item in dealer_values:
        if item in ["King", "Queen", "Jack"]:
            dealer_hand_value += 10
        elif item == "Ace":
            if dealer_hand_value + 11 > 21:
                dealer_hand_value += 1
            else:
                dealer_hand_value += 11
        else:
            dealer_hand_value += item
    print("\n")
    print("{}, your card value is: {} ".format(player,player_hand_value))
    print("The dealer's card value is: {}".format(dealer_hand_value))
    print("-" * 20)
    if index == 0:
        player_decision = input("{} it's YOUR TURN, Press h for 'Hit' and Press s for 'Stay'".format(player)).lower()
        if player_decision == "h":
            player_real_hand.append(game_deck.cards.pop())
            print("{} chose to Hit".format(player))
            print("=" * 20)
        else:
            print("Player Stays at {}".format(player_hand_value))
            print("=" * 20)
        counter += 1
        continue
    else:
        if dealer_hand_value < 17:
            print("It's the Dealer's turn...")
            dealer_real_hand.append(game_deck.cards.pop())
            print("Dealer chose to Hit!")
            print("=" * 20)
        else:
            print("It's the Dealer's turn...")
            print("Dealer Stays at {}".format(dealer_hand_value))
            print("=" * 20)
        counter += 1
    continue

