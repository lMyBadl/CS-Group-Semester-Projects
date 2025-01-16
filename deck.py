from card import Card #imports Card class from card.py
import random #random for list shuffling

class Deck:
    deck = []
    jokers = [Card("red", "joker"), Card("black", "joker")]

    def __init__(self, jokers):
        if(jokers.type() != bool):
            return "Argument for Jokers needs to be a boolean."
        self.jokers = jokers
        
    #adds jokers if needed
    if(jokers == True):
            deck.extend(jokers)

#removes cards, "*" for any amount of cards
    def removeCards(self, *cards):
        return "Removed successfully"
        
#shuffle deck
    def shuffleDeck(self):
        random.shuffle(self.deck)
        return "Shuffled successfully"
