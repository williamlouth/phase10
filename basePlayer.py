import numpy as np
from copy import deepcopy
from game import *

class Player:
    def __init__(self, name):
        self.hand = Hand(np.zeros(13,dtype=int))
        self.phaseGoals = []
        self.name = name
        self.phase = 0

    def drawCard(self,card):
        self.hand.addCard(card)

    def draw(self, deck, discardPile):
        raise NotImplementedError("need to decide what to draw")

    def discard(self, discardPile):
        raise NotImplementedError("need to decide what to discard")
    
    def playTurn(self, deck, discardPile):
        self.draw(deck, discardPile)
        if(isWinningHand(self.hand, self.phaseGoals)):
            return True
    
        discard = self.discard(self)

        self.hand.discardCard(discard)
        discardPile.discard(discard)
        return False





