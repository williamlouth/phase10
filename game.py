import numpy as np
from copy import deepcopy

i = np.array([0,1,1])

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.jokers = cards[0]

    def addCard(self, card):
        self.cards[card] += 1
        if(card == 0):
            self.jokers += 1
    
    def discardCard(self, card):
        if self.cards[card] <= 0:
            print(self.cards, card)
            assert self.cards[card] > 0

        self.cards[card] -= 1

    def numberCards(self):
        return self.cards[1:]

    def trimHand(self, number, count):
        assert self.cards[number] >= count
        self.cards[number] -= count

    def trimJokers(self, count):
        assert self.jokers > 0 or count == 0
        self.jokers -= count

class PhaseGoal:
    def __init__(self, isRun, goalLength):
        self.isRun = isRun
        self.goalLength = goalLength
        

def completeSets(hand, goal):
    hands = []
    for idx, number in enumerate(hand.numberCards()):
        for num in range(0, number+1):
            for jokers in range(0,hand.jokers+1):
                if num + jokers >= goal.goalLength:
                    shrunkHand = deepcopy(hand)
                    shrunkHand.trimHand(idx+1, num)
                    shrunkHand.trimJokers(jokers)
                    hands.append(shrunkHand)
    return hands

def completeRuns(hand, goal):
    hands = []
    for idx in range(0,len(hand.numberCards())-goal.goalLength + 1):
        for runLen in range(goal.goalLength, len(hand.numberCards())+1 - idx):
            for j in range(0,hand.jokers+1):
                sumVal = np.sum(hand.numberCards()[idx:idx+runLen] > 0)
                if  sumVal + j >= runLen:
                    shrunkHand = deepcopy(hand)
                    for trimIdx in range(idx+1, idx+runLen+1):
                        if shrunkHand.cards[trimIdx] > 0:
                            shrunkHand.trimHand(trimIdx, 1)
                    shrunkHand.trimJokers(j)
                    hands.append(shrunkHand)
    return hands

def isWinningHand(hand, phaseGoals):
    if(not phaseGoals):
        return True;

    shrunkHands = []
    if(phaseGoals[0].isRun):
        shrunkHands = completeRuns(hand, phaseGoals[0])
    else:
        shrunkHands = completeSets(hand, phaseGoals[0])
    if(not shrunkHands):
        return False
    for shrunkHand in shrunkHands:
        if(len(phaseGoals) == 1):
            return True;
        if(isWinningHand(shrunkHand, phaseGoals[1:])):
            return True
    return False

class Deck:
    def __init__(self):
        self.cards = 8 * np.ones(13)
        self.cardValues = np.arange(13)

    def draw(self, discardPile):
        if np.sum(self.cards) == 0:
            for dcard in discardPile.stack:
                self.cards[dcard] += 1
            discardPile.empty()

        card = np.random.choice(a=self.cardValues,size=1, p=self.cards / np.sum(self.cards))
        self.cards[card] -= 1
        return card

class DiscardPile:
    def __init__(self):
        self.stack = []
    
    def discard(self,card):
        self.stack.append(card)

    def empty(self):
        self.stack = []

    def draw(self):
        return self.stack.pop(-1)
    
class Game:
    def __init__(self, players):
        self.players = players
        self.winner = ""
        self.phases = [[PhaseGoal(False,3),PhaseGoal(False,3)],[PhaseGoal(False,3),PhaseGoal(True,4)],[PhaseGoal(False,4),PhaseGoal(True,4)],[PhaseGoal(True,7)],[PhaseGoal(True,8)],[PhaseGoal(True,9)],[PhaseGoal(False,4),PhaseGoal(False,4)],[PhaseGoal(False,5),PhaseGoal(False,2)],[PhaseGoal(False,5),PhaseGoal(False,3)]]

    def runRound(self):
        self.deck = Deck()
        self.discardPile = DiscardPile()
        
        for player in self.players:
            player.hand = Hand(np.zeros(13, dtype=int))
            player.jokers = 0
            for i in range(10):
                player.drawCard(self.deck.draw(self.discardPile))

        won = False
        while(won == False):
            for player in self.players:
                if(player.playTurn(self.deck, self.discardPile)):
                    won = True
                    player.phase += 1
                    self.winner = player.name
                    if(player.phase == len(self.phases)):
                        return False
                    player.phaseGoals = self.phases[player.phase]
                    break
        return True
            
            
    def runGame(self):
        for player in self.players:
            player.phaseGoals = self.phases[0]
            player.phase = 0
        running = True
        while(running):
            running = self.runRound();
        return self.winner

if __name__ == '__main__':
    p1 = Player("will")
    p2 = Player("julia")
    g = Game([p1,p2])
    g.runGame()








