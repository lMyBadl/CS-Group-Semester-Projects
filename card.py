class Card:

    #five suits for us, hearts, diamonds, spades, clubs, and JOKERS
    suits = {"heart", "diamond", "spade", "club", "joker"}
    def __init__(self, value, suit):
        suit = suit.lower

        #checks for unvalid inputs and doesn't enter values if not in ranges
        if(value > 15 or value < 1):
            return "Number not valid."
        if suit not in self.suits:
            return "Suit not valid."
        
        self.value = value
        self.suit = suit

#modifier methods
    def changeSuit(self, suit):
        self.suit = suit
        
    def changeValue(self, value):
        self.value = value