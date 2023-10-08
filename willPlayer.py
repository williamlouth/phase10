import numpy as np
from copy import deepcopy
from basePlayer import Player
from game import *

class WillPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def draw(self, deck, discardPile):
        self.drawCard(deck.draw(discardPile))


    def discard(self, discardPile):
        remainingHand = self.discardPhase0()

        cardValues = np.arange(1,13)
        discard = np.random.choice(a=cardValues,size=1, p=remainingHand.numberCards() / np.sum(remainingHand.numberCards()))
        return discard

    def discardPhase0(self):
        shrunkHand = deepcopy(self.hand)
        for goal in self.phaseGoals:
            if goal.isRun:
                shrunkenHands = completeRuns(shrunkHand, goal)
                if(shrunkenHands):
                    shrunkHand = shrunkenHands[0]
            else:
                shrunkenHands = completeSets(shrunkHand, goal)
                if(shrunkenHands):
                    shrunkHand = shrunkenHands[0]

        return shrunkHand



