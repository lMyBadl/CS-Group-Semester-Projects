import random #random for list shuffling

#imports Card class from card.py
from card import Card
class Deck:
    

    #default deck without jokers for checking
    validValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #in case we haven't converted to ints yet
    faceCards = ["jack", "queen", "king"]
    validSuits = {"hearts", "diamonds", "spades", "clubs"}

    def checkValidCard(self, value: int, suit: str) -> str:
        if value < 1 or value > 13:
            return "Value out of bounds."
        elif str not in self.validSuits:
            return "Suit not valid."
        
    #default suits, values, and number of decks
    def __init__(self, wantsJokers: bool, suits: list = validSuits, values: list = validValues, numDecks: int = 1):
        
        #empty deck for customization later
        self.deck = []

        #I don't need to check for bounds because the creation of Card objects will automatically throw errors
        if numDecks < 1:
            raise Exception("Number of decks cannot be less than one.")
            
        #adding the suits and values wanted to the deck
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))
                
        #adds jokers if wanted
        if wantsJokers:
            self.deck.extend([Card(1, "joker"), Card(2, "joker")])
            
        #stores inputs in case they're different from default
        self.wantsJokers = wantsJokers
        self.suits = suits
        self.values = values

        originalDeck = self.deck.copy()
        for x in range(1, numDecks):
            self.deck.extend(originalDeck)

    def __str__(self):
        suit = self.deck[0].suit
        output = ""
        for card in self.deck:
            if suit != card.suit:
                output += suit + "\n"
                suit = card.suit
            output += str(card.value) + " "
        output += self.deck[self.deck.__len__() - 1].suit
        return output

    #removes a card of certain value and suit
    def removeCard(self, value, suit):
        card = Card(value, suit)
        if self.deck.__contains__(card):
            self.deck.remove(card)
            return "".join(self.value + " of " + self.suit + " removed.")
        raise Exception("Card not found.")
        
    #shuffle deck
    def shuffleDeck(self):
        random.shuffle(self.deck)
        return "Shuffled successfully"

    def drawCard(self):
        if not self.deck:
            raise Exception("Deck is empty")
        return self.deck.pop()