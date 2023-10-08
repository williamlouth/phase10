import numpy as np
from copy import deepcopy
from basePlayer import Player

class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def draw(self, deck, discardPile):
        self.drawCard(deck.draw(discardPile))

    def discard(self, discardPile):
        numbNumberCards = np.sum(self.hand.cards)-self.hand.jokers

        cardValues = np.arange(1,13)
        discard = np.random.choice(a=cardValues,size=1, p=self.hand.numberCards() / np.sum(self.hand.numberCards()))
        return discard
    


