#imports Card class from card.py
from card import Card

class Deck:
    deck = []
    jokers = [Card("red", "joker"), Card("black", "joker")]

    def __init__(self, jokers):
        self.jokers = jokers
        
    #adds jokers if needed
    if(jokers == True):
            deck.extend(jokers)

#return size of deck
    def __sizeof__(self):
        return len(self.deck)

#removes cards, "*" for any amount of cards
    def removeCards(*cards):
        return "Removed successfully"
        
#shuffle deck
    def shuffleDeck(self):
        return "Shuffled successfully"

    
