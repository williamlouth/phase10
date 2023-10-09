import numpy as np
from copy import deepcopy
from basePlayer import Player

class JuliaPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def draw(self, deck, discardPile):
        self.pullACard(deck, discardPile, self.hand.cards, self.phaseGoals)

    def discard(self, deck, discardPile):
        discard = self.bestNumberToDiscard(deck, self.hand.cards, self.phaseGoals)
        if (self.hand.cards[discard] <= 0):
            print("Tried to discard a card that I didn't have")
            discard = np.nonzero(self.hand.cards)[0][0]
        return discard
    


    def tryGoal(self, deck, hand, goalLength, idx, isRun):
        newHand = hand.copy().astype(float)
        if isRun:
            run = np.array([x >= idx and x < idx + goalLength for x in range(hand.size)])
            newHand -= run
        else:
            newHand[idx] -= goalLength
    
        for i in range(1, newHand.size):
            if newHand[i] < 0:
                for j in range(-int(newHand[i])):
                    newHand[0] *= (max(0, float(deck.cards[i] - j)) / float(deck.cards.sum()))
                newHand[i] = 0
        return newHand
        
    
    def valueHand(self, deck, hand, goals, goalIdx):
        possibleHands = []
        goal = goals[goalIdx]
    
        for i in range(1, hand.size):
            if not goal.isRun or i + goal.goalLength <= hand.size:
                newHand = self.tryGoal(deck, hand, goal.goalLength, i, goal.isRun)
                if goalIdx + 1 >= len(goals): possibleHands.append(newHand)
                else: possibleHands += self.valueHand(deck, newHand, goals, goalIdx + 1)
    
        return possibleHands
    
    def bestNumberToDiscard(self, deck ,hand, goals):
        handCopy = hand.copy()
        handCopy[0] = 1

        res = np.array(self.valueHand(deck, handCopy, goals, 0))
        sorted = res[res[:, 0].argsort()[::-1]]
    
        lastCombinedRows = np.repeat(0,13)
        for i in range(1, sorted.shape[0]):
            combinedRows = np.min(sorted[:i], 0)
            if combinedRows[1:].sum() <= 0:
                break
            lastCombinedRows = combinedRows

        return np.argmax(lastCombinedRows)

    def pullACard(self, deck, discardPile, hand, goals):
        # choose last discard if it improves the situation..
        handCopy = hand.copy()
        handCopy[0] = 1
        res = np.array(self.valueHand(deck, handCopy, goals, 0))
        sorted = res[res[:, 0].argsort()[::-1]]
        currentBestValue = sorted[0,0]

        handCopy[0] = 1
        handCopy[discardPile.top()] += 1
        res = np.array(self.valueHand(deck, handCopy, goals, 0))
        sorted = res[res[:, 0].argsort()[::-1]]
        bestValueAfterPickup = sorted[0,0]

        if bestValueAfterPickup > currentBestValue:
            self.drawCard(discardPile.draw())
        else:
            self.drawCard(deck.draw(discardPile))
        
        return hand