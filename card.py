class Card:
    #five suits for us, hearts, diamonds, spades, clubs, and JOKERS
    suits = {"heart", "diamond", "spade", "club", "joker"}
    def __init__(self, value, suit):
        suit = suit.lower

        #checks for unvalid inputs and doesn't enter values if not in ranges
        if(value > 13 or value < 1):
            return "Number not valid."
        if suit not in self.suits:
            return "Suit not valid."
        
        self.value = value
        self.suit = suit

#modifier methods
    def changeSuit(self, suit):
        oldSuit = self.suit
        if suit in self.suits:
            self.suit = suit
            return self.value, "'s suit changed from", oldSuit, "to", suit
        return 'Suit is not "heart", "diamond", "spade", "club", or "joker".'
        
    def changeValue(self, value):
        oldValue = self.value
        if value <= 13 or value >= 1:
            self.value = value
            return self.suit, "'s value changed from", oldValue, "to", value
        return "Value not in bounds."