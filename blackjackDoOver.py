
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
counter = 0     #counter created to show alternate turns
player_decision = "h"
while game:
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
    if index == 0 and player_decision == "h" and player_hand_value < 22:
        player_decision = input("{} it's YOUR TURN, Press h for 'Hit' and Press s for 'Stay'".format(player)).lower()
        if player_decision == "h":
            player_real_hand.append(game_deck.cards.pop())
            print("{} chose to Hit".format(player))
            print("=" * 20)
        elif player_decision != "s" and player_hand_value < 22 :
            print("{} Stays at {}".format(player, player_hand_value))
            print("=" * 20)
        else:
            print("{} you have bust".format(player))
        counter += 1
    elif index == 1 or player_decision == "s":
        if dealer_hand_value < 17:
            print("It's the Dealer's turn...")
            dealer_real_hand.append(game_deck.cards.pop())
            print("Dealer chose to Hit!")
            print("=" * 20)
        elif 17 <= dealer_hand_value < 22:
            print("It's the Dealer's turn...")
            print("Dealer Stays at {}".format(dealer_hand_value))
            print("=" * 20)
            if player_decision == "s":
                if dealer_hand_value == player_hand_value:
                    print("You tie")
                    game = False
                elif dealer_hand_value > player_hand_value:
                    print("The Dealer wins")
                    game = False
                else:
                    print("You win!")
                    game = False
        else:
            print("The dealer has bust")
            if player_hand_value < 22:
                print("You win!")
                game = False
            else:
                print("You both Bust. Game is a Push.")
                game = False
        counter += 1
    elif player_decision == "s" and dealer_hand_value > 16:
        if 22 > player_hand_value > dealer_hand_value > 16:
            print("{}, you Win with {} points. The Dealer only has {}".format(player, player_hand_value, dealer_hand_value))
            game = False
        if 16 < player_hand_value < dealer_hand_value < 22 and player_decision == "s":
            print("Sorry, {} you lose to the Dealer".format(player))
            game = False
    elif player_hand_value > 21:
        print("You Bust")
        if dealer_hand_value < 22:
            print("The Dealer wins")
            game= False
    elif player_hand_value == dealer_hand_value and player_decision == "s" and dealer_hand_value > 16:
            print("The game was a tie")
            game = False
    elif player_hand_value == 21 and dealer_hand_value < 21:
            print("You win")
            game = False
