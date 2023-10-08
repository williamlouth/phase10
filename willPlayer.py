import numpy as np
from copy import deepcopy
from basePlayer import Player
from game import *

class WillPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def draw(self, deck, discardPile):
        self.drawCard(deck.draw(discardPile))

    def goalsContainSet(self):
        containsSet = False
        for goal in self.phaseGoals:
            if not goal.isRun:
                containsSet = True
        return containsSet


    def discard(self, deck, discardPile):
        if(not self.goalsContainSet()):
            return self.runDiscard()

        remainingHand = self.discardPhase0()

        cardValues = np.arange(1,len(self.hand.numberCards()) + 1)
        discard = np.random.choice(a=cardValues,size=1, p=remainingHand.numberCards() / np.sum(remainingHand.numberCards()))
        return discard

    def runDiscard(self):
        for idx, i in enumerate(self.hand.numberCards()):
            if i > 1:
                return idx + 1

        if self.hand.numberCards()[0] == 1:
            return 1
        if self.hand.numberCards()[11] == 1:
            return 12
        if self.hand.numberCards()[1] == 1:
            return 2
        if self.hand.numberCards()[10] == 1:
            return 11
        if self.hand.numberCards()[2] == 1:
            return 3
        if self.hand.numberCards()[9] == 1:
            return 10
        if self.hand.numberCards()[3] == 1:
            return 4
        if self.hand.numberCards()[8] == 1:
            return 9

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



