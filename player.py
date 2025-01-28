from card_logic import Deck, Card

class Player:
    def __init__(self):
        self.hand = []
        
    def drawCard(self, deck):
        self.hand.append(deck.drawCard())
