import random

class Deck:
    pass

# Creating a deck of cards
card_values = [x for x in range(2, 11)] + ["Ace", "Jack", "Queen", "King"]
card_suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
cards = [[[value, "of " + suit] for suit in card_suits] for value in card_values]

shuffled_cards = []

for card_suit in cards:
    for card in card_suit:
        shuffled_cards.append(card)

random.shuffle(shuffled_cards)
# print(shuffled_cards)

# Dealing two cards in the deck for the player
player_real_hand = []
player_real_hand.append(shuffled_cards[:2])
print("Player hand... ")
print(player_real_hand)
print("")

# Dealing the next two cards in the deck for the dealer
dealer_real_hand = []
dealer_real_hand.append(shuffled_cards[2:4])
print("Dealer hand... ")
print(dealer_real_hand)
print("")

# getting the values of the player cards into a list
player_hand = []
for card in player_real_hand:
    for value in card:
        player_hand.append(value[0])
#print(player_hand)

# getting the values of the dealer cards into a list
dealer_hand = []
for card in dealer_real_hand:
    for value in card:
        dealer_hand.append(value[0])
#print(dealer_hand)

print("=" * 20)

#Adding up the value of the players cards.
player_hand_value = 0

for item in player_hand:
    if item in ["King", "Queen", "Jack"]:
        player_hand_value += 10
    elif item == "Ace":
        if player_hand_value + 11 > 21:
            player_hand_value += 1
        else:
            player_hand_value += 11
    else:
        player_hand_value += item


if player_hand_value > 21:
    print("Player Hand Value...")
    print(player_hand_value)
    print("Busted!")
else:
    print("Player Hand Value...")
    print(player_hand_value)

dealer_hand_value = 0

for item in dealer_hand:
    if item in ["King", "Queen", "Jack"]:
        dealer_hand_value += 10
    elif item == "Ace":
        if dealer_hand_value + 11 > 21:
            dealer_hand_value += 1
        else:
            dealer_hand_value += 11
    else:
        dealer_hand_value += item


if dealer_hand_value > 21:
    print("Dealer Hand Value...")
    print(dealer_hand_value)
    print("Busted!")
else:
    print("Dealer Hand Value...")
    print(dealer_hand_value)


print("=" * 20)
while player_hand_value < 21:
# Dealing two cards in the deck for the player
    player_decision = input("Player press H for 'Hit' and press S for 'stay':").lower()
    print("=" * 20)
    if player_decision == "h":
        player_real_hand.append(shuffled_cards[5:6])
        print("Player hand... ")
        print(player_real_hand)
        print("")
    else:
        pass
    if player_hand_value > 21:
        print("Player Hand Value...")
        print(player_hand_value)
        print("Busted!")
    elif dealer_hand_value < 17:
        dealer_real_hand.append(shuffled_cards[7:8])
        print("Dealer hand... ")
        print(dealer_real_hand)
        print("")
    for item in player_hand:
        if item in ["King", "Queen", "Jack"]:
            player_hand_value += 10
        elif item == "Ace":
            if player_hand_value + 11 > 21:
                player_hand_value += 1
            else:
                player_hand_value += 11
        else:
            player_hand_value += item
    for item in dealer_hand:
        if item in ["King", "Queen", "Jack"]:
            dealer_hand_value += 10
        elif item == "Ace":
            if dealer_hand_value + 11 > 21:
                dealer_hand_value += 1
            else:
                dealer_hand_value += 11
        else:
            dealer_hand_value += item

    print("Player Hand Value...")
    print(player_hand_value)
    print("Dealer Hand Value...")
    print(dealer_hand_value)