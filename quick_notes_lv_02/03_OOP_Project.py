####################
#### War (Game) ####
####################

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck class. This object will create a deck of cards to initiate play.
    You can then use this deck list of cards to split in half and give to the players.
    It will use SUITE to create the deck. It sould also have a method for splitting the
    deck in half and shuffling the deck. 
    """
    pass

class Hand:
    """
    This the Hand class. Each plauer has a hand, and can add or remove cards from that hand.
    There should be an add and remove card method here.
    """
    pass

class player:
    """
    This is the Player class, which takes in a name and an instance of a Hand class object.
    The player can then play cards and check if they still have cards.
    """
    pass

###################
#### GAME PLAY ####
###################
print("Hello Warrior, Welcome To War, Let's Fight .....")

# Use the 3 classes along with some logic to play a game of war !
