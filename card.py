class Card:
    #default deck without jokers for checking
    validValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #in case we haven't converted to ints yet
    faceCards = ["jack", "queen", "king"]

    #five suits for us, hearts, diamonds, spades, clubs, and JOKERS
    validSuits = {"hearts", "diamonds", "spades", "clubs", "joker"}

    def __init__(self, value, suit):
        suit = suit.lower()

        #checks for unvalid inputs and doesn't enter values if not in ranges
        self.checkValidCard(value, suit)

        if value in self.faceCards:
            if value == "jack":
                self.value = 11
            elif value == "queen":
                self.value = 12
            else:
                self.value = 13

        self.suit = suit

    #toString method
    def __str__(self):
        if self.value > 10:
            if self.value == 11:
                output = "jack of " + self.suit
            
            elif self.value == 12:
                output = "queen of " + self.suit
            else:
                output = "king of " + self.suit
        else:
            output = str(self.value) + " of " + self.suit
        return ''.join(output)

    #checks if the suit is a real card suit
    def checkSuit(self, suit: str):
        suit = suit.lower()
        if suit not in self.validSuits:
            print(suit)
            raise Exception('Suit is not "hearts", "diamonds", "spades", "clubs", or "joker".')
        return True
    
    #return True if it is a card value
    def checkValue(self, value):

        #if not string and int then proceed
        if not isinstance(value, str) and not isinstance(value, int):
            print(value, isinstance(value, str), isinstance(value, int))
            raise Exception("Not a valid value.")
        
        elif isinstance(value, str):
            value.lower()

            if value not in self.faceCards:
                raise Exception("Not a face card.")
            
        elif value not in self.validValues:
            raise Exception("Not a valid value.")
        return True
    
    #changes suit of card
    def changeSuit(self, suit):
        oldSuit = self.suit

        if self.checkSuit(suit):
            self.suit = suit

            return self.value, "'s suit changed from", oldSuit, "to", suit
        #no error message here b/c if checksuit fails then it will throw an exception

    #changes value of card
    def changeValue(self, value):
        oldValue = self.value

        if self.checkValue(value):
            self.value = value

            #checks if the value is a face card, and if so stores it as an int
            if value in self.faceCards:
                self.value = self.convertFacetoInt(value)

            return self.suit, "'s value changed from", oldValue, "to", value
        raise Exception("Value not in bounds.")

    #converts from a face card to an int for easier processing
    def convertFacetoInt(self, value: str):
        value = value.lower()
        if value not in self.faceCards:
            raise Exception("Not a face card.")
        
        if value == "jack":
            return 11
        
        if value == "queen":
            return 12
        return 13
    
    #checks card validity
    def checkValidCard(self, value, suit: str):
        return self.checkSuit(suit) and self.checkValue(value)
    #if it is not a real card then the check__ methods will throw error so no need to check