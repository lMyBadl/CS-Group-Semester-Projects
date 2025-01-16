import random #random for list shuffling

#imports Card class from card.py
from card import Card
class Deck:
    #default deck without jokers
    validSuits = ["hearts", "diamonds", "spades", "clubs"]
    validValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "jack", "queen", "king"] #in case we haven't converted to ints yet

    #empty deck for customization later
    deck = []
    
    #if it is not a valid card, returns True, otherwise a blank string means False
    def checkNonValidCard(self, value: int, suit: str) -> str:
        if value not in self.validValues:
            return "Value out of bounds."
        elif str not in self.validSuits:
            return "Suit not valid."
        return ""
#                               default suits                            default values
    def __init__(self, jokers: bool, suits: list = validSuits, values: list = validValues):
        
        # check for correct suits
        for suit in suits:
            if suit not in self.validSuits:
                raise Exception('Inputted suit is not "hearts", "diamonds", "spades", and/or "clubs".')
        
        #check for values in bound
        for value in values:
            if type(value) != int:
                raise Exception("Value not of type int.")
            elif(value < 1 or value > 13):
                raise Exception("Value not in bounds.")
        """    
        #check for correct jokers type
        if(type(jokers) != bool):
            return "Argument for Jokers needs to be a boolean."
        """
            
        #adding the suits and values wanted to the deck
        for suit in suits:
            for value in self.validValues:
                self.deck.append(Card(value, suit))
                
        #adds jokers if wanted
        if jokers:
            self.deck.extend(Card("red", "joker"), Card("black", "joker"))
            
        #stores inputs in case they're different from default
        self.jokers = jokers
        self.suits = suits
        self.values = values

    #removes a card of certain value and suit
    def removeCards(self, value, suit):
        if self.checkNonValidCard(value, suit) == False:
            if self.deck.__contains__(Card(value, suit)):
                self.deck.remove(Card(value, suit))
                return value, "of", suit, "removed."
        raise Exception(self.checkValidCard(value, suit))
        
    #shuffle deck
    def shuffleDeck(self):
        random.shuffle(self.deck)
        return "Shuffled successfully"

