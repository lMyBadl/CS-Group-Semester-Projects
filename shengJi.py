import copy
import pygame
from player import Player
from deck import Deck

deck = Deck(True, numDecks = 2)
player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")
player4 = Player("Player 4")

#draws until deck is empty, and if empty then returns false
while deck.cards:
    player1.draw(deck)
    player2.draw(deck)
    player3.draw(deck)
    player4.draw(deck)