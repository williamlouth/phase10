import numpy as np
from copy import deepcopy
from basePlayer import Player

class JuliaPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def draw(self, deck, discardPile):
        self.drawCard(deck.draw(discardPile))

    def discard(self, discardPile):
        discard = self.bestNumberToDiscard(self.hand.cards, self.phaseGoals)
        return discard
    


    def tryGoal(self, hand, goalLength, idx, isRun):
        newHand = hand.copy()
        if isRun:
            run = np.array([x >= idx and x < idx + goalLength for x in range(hand.size)])
            newHand -= run
        else:
            newHand[idx] -= goalLength
    
        #replace with jokers if something was missing
        for i in range(1, newHand.size):
            if newHand[i] < 0:
                newHand[0] += newHand[i]
                newHand[i] = 0
        return newHand
    
    def valueHand(self, hand, goals, goalIdx):
        possibleHands = []
        goal = goals[goalIdx]
    
        for i in range(1, hand.size):
            if not goal.isRun or i + goal.goalLength <= hand.size:
                newHand = self.tryGoal(hand, goal.goalLength, i, goal.isRun)
                if goalIdx + 1 >= len(goals): possibleHands.append(newHand)
                else: possibleHands += self.valueHand(newHand, goals, goalIdx + 1)
    
        return possibleHands
    
    def bestNumberToDiscard(self ,hand, goals):
        res = np.array(self.valueHand(hand, goals, 0))
        sorted = res[res[:, 0].argsort()[::-1]]
    
        bestJoker = sorted[0,0]
        lastCombinedRows = np.repeat(0,13)
        for i in range(1, sorted.shape[0]):
            combinedRows = np.min(sorted[:i], 0)
            if combinedRows[1:].sum() <= 0:
            # if we haven't reached the end of the same best joker rows
                if sorted[i, 0] == bestJoker:
                    lastCombinedRows = np.repeat(0,13)
                break
            lastCombinedRows = combinedRows
    
        while lastCombinedRows[1:].sum() == 0:
        # print("\n bestJoker i now: " + str(bestJoker))
            for i in range(0, sorted.shape[0]):
          # print(sorted[i])
                if not sorted[i, 0] >= bestJoker:
                    bestJoker = sorted[i,0]
                    break
                lastCombinedRows += sorted[i]
    
        return np.argmax(lastCombinedRows)
