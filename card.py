class Card:
    #default deck without jokers for checking
    validValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #in case we haven't converted to ints yet
    #red = 1 and black = 2 because I don't want to bother adding another thing just for colors
    faceCards = ["jack", "queen", "king"]

    #five suits for us, hearts, diamonds, spades, clubs, and JOKERS
    validSuits = {"Hearts", "Diamonds", "Spades", "Clubs", "Joker"}

    def __init__(self, value, suit):
        suit = suit.lower()

        self.value = value
        self.suit = suit
        #checks for unvalid inputs and doesn't enter values if not in ranges
        self.checkValidCard()

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
            self.convertCardFromIntToFace()
            output = self.value + " of " + self.suit
        elif self.suit == "joker":
            if self.value == 1:
                output = "red joker"
            else:
                output = "black joker"
        else:
            output = str(self.value) + " of " + self.suit
        return ''.join(output)

    #checks if the suit is a real card suit
    def checkSuit(self):
        if not isinstance(self.suit, str):
            raise Exception("Suit is not a string.")
        self.suit = self.suit.lower()
        if self.suit not in self.validSuits:
            raise Exception('Suit is not "hearts", "diamonds", "spades", "clubs", or "joker".')
        return True
    
    #return True if it is a card value
    def checkValue(self):

        #if not string and int then proceed
        if not isinstance(self.value, str) and not isinstance(self.value, int):
            raise Exception("Not a valid value.")
        
        elif isinstance(self.value, str):
            self.value.lower()

            if self.value not in self.faceCards:
                raise Exception("Not a face card.")
            
        elif self.value not in self.validValues:
            raise Exception("Not a valid value.")
        return True
    
    #changes suit of card
    def changeSuit(self, suit: str):
        oldSuit = self.suit
        self.suit = suit.lower()

        if suit == "joker":
            raise Exception("Suit cannot be changed to joker. Use changeToJoker instead.")

        if self.checkSuit():
            return self.value, "'s suit changed from", oldSuit, "to", suit
        #no error message here b/c if checksuit fails then it will throw an exception

    #changes value of card
    def changeValue(self, value):
        oldValue = self.value
        if oldValue in self.faceCards:
            self.convertCardFromIntToFace()
        self.value = value

        if isinstance(value, str):
            self.convertCardFromFaceToInt()

        if self.checkValue():
            #checks if the value is a face card, and if so stores it as an int
            return self.suit, "'s value changed from", oldValue, "to", value

    #changes a card to a joker
    def changeToJoker(self, color:str):
        if color != "red" and color != "black":
            raise Exception("Color is not red or black.")
        self.changeToJoker(color)

    #changes a card to a regular card
    def changeFromJoker(self, value, suit: str):
        self.changeValue(value)
        self.changesuit(suit)

    #converts from a face card to an int for easier processing
    def convertCardFromFaceToInt(self):
        if not isinstance(self.value, str):
            raise Exception("Not a string")
        
        if self.value not in self.faceCards:
            raise Exception("Not a face card.")
        
        if self.value == "jack":
            self.changeValue(11)
        
        if self.value == "queen":
            self.changeValue(12)
        else:
            self.changeValue(13)
    
    #converts from int to face
    def convertCardFromIntToFace(self):
        if self.value > 10 and self.value <= 13:
            if self.value == 11:
                self.value = "jack"
            
            elif self.value == 12:
                self.value = "queen"
            else:
                self.value = "king"
        else:
            raise Exception("Not a face card numerical value.")
        
    #checks card validity
    def checkValidCard(self):
        return self.checkSuit() and self.checkValue()
    #if it is not a real card then the check__ methods will throw error so no need to check