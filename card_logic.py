import random, pygame
#default deck without jokers for checking
validValues = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] #in case we haven't converted to ints yet
#red = 1 and black = 2 because I don't want to bother adding another thing just for colors

#five suits for us, hearts, diamonds, spades, clubs, and JOKERS
validSuits = {"hearts", "diamonds", "spades", "clubs"}

class Card:
    def __init__(self, value, suit):
        if (self.isValid(value, suit)):
            self.value = value
            self.suit = suit
            if suit == "clubs": s = "Clubs"
            elif suit == "spades": s = "Spades"
            elif suit == "diamonds": s = "Diamonds"
            elif suit == "hearts": s = "Hearts"
            else: s = suit

            if value == "A": v = 1
            elif value == "J": v = 11
            elif value == "Q": v = 12
            elif value == "K": v = 13
            else: v = value
            self.image = pygame.image.load(f"Cards Pack\\Large\\{s} {v}.png")
        
        else:
            raise Exception("Invalid value or suit")
    def __lt__ (self, other):
        if self.a == other.a:
            return self.b < other.b
        return self.a < other.b

    def __gt__ (self, other):
        return other.__lt__(self)

    def __eq__ (self, other):
        return self.value == other.value and self.suit == other.suit

    def __ne__ (self, other):
        return not self.__eq__(other)


    def isValid(self, value, suit):
        global validValues, validSuits
        return value in validValues and suit in validSuits
    
    def __str__(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    def __init__(self, wantsJokers, numDecks = 1):
        global validSuits, validValues
        self.wantsJokers = wantsJokers
        self.numDecks = numDecks
        self.deck = [Card(value, suit) for suit in validSuits for value in validValues]
        #if wantsJokers:
        #    self.deck.append(Card(""))

    def __getitem__(self, item):
        return self.deck[item]
    def removeCard(self, value, suit):
        card = Card(value, suit)
        if(card not in self.deck):
            return False
        self.deck.remove(card)
        return True
    
    def drawCard(self):
        return self.deck.pop()
    
    def shuffleDeck(self):
        random.shuffle(self.deck)
    
    def __str__(self):
        output = ""
        for card in self.deck:
            output += str(card) + " "
        return output