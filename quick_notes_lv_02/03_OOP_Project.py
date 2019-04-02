####################
#### War (Game) ####
####################
#!/usr/bin/python3

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# mycards = [(s,r) for s in SUITE for r in RANKS]
# or,
# mycards = []
# for r in RANKS:
#     for s in SUITE:
#         mycards.append((s,r))
# now i can pass mylist as a pram in Deck init method

class Deck:
    """
    This is the Deck class. This object will create a deck of cards to initiate play.
    You can then use this deck list of cards to split in half and give to the players.
    It will use SUITE to create the deck. It sould also have a method for splitting the
    deck in half and shuffling the deck. 
    """
    def __init__(self):
        print("Creating New Ordered Deck !")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand:
    """
    This the Hand class. Each player has a hand, and can add or remove cards from that hand.
    There should be an add and remove card method here.
    """
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add_cards(self, added_cards):
        self.cards.extend(added_cards)
    
    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand class object.
    The player can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop(x))
            return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0

###################
#### GAME PLAY ####
###################
print("Hello Warrior, Welcome To War, Let's Fight .....")

# Create new deck and split it in half:
d = Deck()
d.shuffle()
half_1, half_2 = d.split_in_half()

# create both players !
cpu = Player("CPU", Hand(half_1))

human = input("What is your name ?")
player_1 = Player(human, Hand(half_2))

total_rounds = 0
war_count = 0

while player_1.still_has_cards() and cpu.still_has_cards():
    total_rounds += 1
    print("Time for a new round")
    print("here are the current standings")
    print(player_1.name + "has the count: " + str(len(player_1.hand.cards)))
    print(cpu.name + "has the count: " + str(len(cpu.hand.cards)))
    print("play a card !")
    print("\n")
    
    table_cards = []

    c_card = cpu.play_card()
    p_card = player_1.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("war !")

        table_cards.extend(player_1.remove_war_cards())
        table_cards.extend(cpu.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            player_1.hand.add_cards(table_cards)
        else:
            cpu.hand.add_cards(table_cards)
    
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            player_1.hand.add_cards(table_cards)
        else:
            cpu.hand.add_cards(table_cards)

print("Game Over !\nNumber of rounds : " + str(total_rounds))
print("A war happened " + str(war_count) + " times")

# Use the 3 classes along with some logic to play a game of war !
