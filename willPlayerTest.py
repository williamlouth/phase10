
import unittest
import numpy as np
from copy import deepcopy
from phase import *
from willPlayer import *

class TestPlayerSuite(unittest.TestCase):
    def checkAndTrim(self, p, discardPile, val):
        discard =  p.discard(discardPile)
        self.assertEqual(discard,val)
        p.hand.trimHand(discard,1)
        
    def test_DiscardCorrectInRun(self):
        p = WillPlayer("will")
        p.phaseGoals = [PhaseGoal(True,7)]
        p.hand = Hand(np.array([0,0,0,1,1,1,1,1,3,2,0,2,2,0,0],dtype = int))
        discardPile = DiscardPile()
        self.checkAndTrim(p, discardPile, 8)
        self.checkAndTrim(p, discardPile, 8)
        self.checkAndTrim(p, discardPile, 9)
        self.checkAndTrim(p, discardPile, 11)
        self.checkAndTrim(p, discardPile, 12)

    def test_ContainsSet(self):
        p = WillPlayer("will")
        g = Game([p])
        runPhases = [3,4,5]
        for i in range(0,9):
            p.phaseGoals = g.phases[i]
            print(i, p.goalsContainSet())

if __name__ == '__main__':
    unittest.main()
















