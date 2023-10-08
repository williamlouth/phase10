import numpy as np
from copy import deepcopy
from basePlayer import Player

class WillPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def draw(self, deck, discardPile):
        self.drawCard(deck.draw(discardPile))


    def discard(self, discardPile):
        if(self.phase == 0):
            return self.discardPhase0()

        numbNumberCards = np.sum(self.hand.cards)-self.hand.jokers

        cardValues = np.arange(1,13)
        discard = np.random.choice(a=cardValues,size=1, p=self.hand.numberCards() / np.sum(self.hand.numberCards()))
        return discard

    def discardPhase0(self):
        for idx, i in enumerate(self.hand.numberCards()):
            if i == 4:
                return idx + 1

        for idx, i in enumerate(self.hand.numberCards()):
            if i == 1:
                return idx + 1

        for idx, i in enumerate(self.hand.numberCards()):
            if i == 5:
                return idx + 1

        for idx, i in enumerate(self.hand.numberCards()):
            if i == 2:
                return idx + 1

        for idx, i in enumerate(self.hand.numberCards()):
            if i > 0:
                return idx + 1
    
    


