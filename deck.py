import random #random for list shuffling
import numpy # numpy for creating values list

#imports Card class from card.py
from card import Card
class Deck:
    suits = ["hearts", "diamonds", "spades", "clubs"]
    jokers = [Card("red", "joker"), Card("black", "joker")]
    
    #empty deck for customization later
    deck = []
    
#                               default suits                                       default values from 1-13
    def __init__(self, jokers, suits = ["hearts", "diamonds", "spades", "clubs"], values = numpy.arange(1,14)):
        # check for correct suits
        for suit in suits:
            if suit not in self.suits:
                return 'Inputted suit is not "hearts", "diamonds", "spades", and/or "clubs".'
            
        #check for correct jokers type
        if(jokers.type() != bool):
            return "Argument for Jokers needs to be a boolean."
            
        #adding the suits and values wanted to the deck
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))
        self.jokers = jokers
        
    #adds jokers if needed
    if(jokers == True):
            deck.extend(jokers)

#removes cards, "*" for any amount of cards
    def removeCards(self, value, suit):
        if self.deck.__contains__(Card(value, suit)):
            self.deck.remove(Card(value, suit))
            return value, "of", suit, "removed."
        return "Card not found."
        
#shuffle deck
    def shuffleDeck(self):
        random.shuffle(self.deck)
        return "Shuffled successfully"
