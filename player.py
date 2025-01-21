from deck import Deck
class Player:
    def __init__(self, name):
        self.name = name

    def drawCard(self, deck):
        card = deck.drawCard()
        if card:
            self.hand.append(card)