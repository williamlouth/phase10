
import unittest
import numpy as np
from copy import deepcopy
from phase import *

class TestHandSuite(unittest.TestCase):
    def test_NotSet(self):
        h = Hand(np.ones(10, dtype=int))
        g = PhaseGoal(False, 3)
        self.assertFalse(isWinningHand(h,[g]))
    def test_IsSet(self):
        h = Hand(np.array([0,0,2,2,2,2,2,0,0,0], dtype=int))
        g = PhaseGoal(False, 2)
        self.assertTrue(isWinningHand(h,[g]))
    def test_IsSetWithJoker(self):
        h = Hand(np.array([1,0,2,2,2,2,2,0,0,0], dtype=int))
        g = PhaseGoal(False, 3)
        self.assertTrue(isWinningHand(h,[g]))
    def test_NotRun(self):
        h = Hand(np.array([0,0,0,0,0,0,10,0,0,0], dtype=int))
        g = PhaseGoal(True, 3)
        self.assertFalse(isWinningHand(h,[g]))
    def test_IsRun(self):
        h = Hand(np.array([0,0,0,1,1,1,0,0,0,7], dtype=int))
        g = PhaseGoal(True, 3)
        self.assertTrue(isWinningHand(h,[g]))
    def test_IsRunShort(self):
        h = Hand(np.array([0,0,0,0,0,0,1,1,0,0], dtype=int))
        g = PhaseGoal(True, 2)
        self.assertTrue(isWinningHand(h,[g]))
    def test_IsRunStart(self):
        h = Hand(np.array([0,1,1,1,0,0,0,0,0,7], dtype=int))
        g = PhaseGoal(True, 3)
        self.assertTrue(isWinningHand(h,[g]))
    def test_IsRunEnd(self):
        h = Hand(np.array([0,0,1,1,0,5,0,1,1,1], dtype=int))
        g = PhaseGoal(True, 3)
        self.assertTrue(isWinningHand(h,[g]))
    def test_IsRunJokers(self):
        h = Hand(np.array([1,0,0,1,0,1,0,0,0,7], dtype=int))
        g = PhaseGoal(True, 3)
        self.assertTrue(isWinningHand(h,[g]))
    def test_IsTwoRuns(self):
        h = Hand(np.array([0,0,1,1,0,0,1,1,0,0], dtype=int))
        g1 = PhaseGoal(True, 2)
        g2 = PhaseGoal(True, 2)
        self.assertTrue(isWinningHand(h,[g1,g2]))
    def test_IsNotTwoRuns(self):
        h = Hand(np.array([1,0,1,1,1,0,1,0,0,4], dtype=int))
        g1 = PhaseGoal(True, 3)
        g2 = PhaseGoal(True, 4)
        self.assertFalse(isWinningHand(h,[g1,g2]))
    def test_IsTwoSets(self):
        h = Hand(np.array([0,0,3,3,0,0,0,0,0,0], dtype=int))
        g1 = PhaseGoal(False, 3)
        g2 = PhaseGoal(False, 3)
        self.assertTrue(isWinningHand(h,[g1,g2]))
    def test_IsTwoSetsJoker(self):
        h = Hand(np.array([1,0,2,0,0,1,1,1,0,1,0,3,0], dtype=int))
        g1 = PhaseGoal(False, 3)
        g2 = PhaseGoal(False, 3)
        self.assertTrue(isWinningHand(h,[g1,g2]))
    def test_IsNotTwoSets(self):
        h = Hand(np.array([0,0,3,2,2,0,0,0,0,0], dtype=int))
        g1 = PhaseGoal(False, 3)
        g2 = PhaseGoal(False, 3)
        self.assertFalse(isWinningHand(h,[g1,g2]))
    def test_IsSetAndRun(self):
        h = Hand(np.array([0,0,3,0,0,1,1,1,0,0], dtype=int))
        g1 = PhaseGoal(False, 3)
        g2 = PhaseGoal(True, 3)
        self.assertTrue(isWinningHand(h,[g1,g2]))
    def test_IsNotSetAndRun(self):
        h = Hand(np.array([0,0,3,0,0,1,0,1,1,0], dtype=int))
        g1 = PhaseGoal(False, 3)
        g2 = PhaseGoal(True, 3)
        self.assertFalse(isWinningHand(h,[g1,g2]))
    def test_IsSetAndRunJokerRun(self):
        h = Hand(np.array([1,0,3,0,0,1,0,1,0,0], dtype=int))
        g1 = PhaseGoal(False, 3)
        g2 = PhaseGoal(True, 3)
        self.assertTrue(isWinningHand(h,[g1,g2]))
    def test_IsSetAndRunJokerSet(self):
        h = Hand(np.array([1,0,2,0,0,1,1,1,0,0], dtype=int))
        g1 = PhaseGoal(False, 3)
        g2 = PhaseGoal(True, 3)
        self.assertTrue(isWinningHand(h,[g1,g2]))
    def test_IsNotSetAndRunJoker(self):
        h = Hand(np.array([1,0,2,0,0,1,0,1,0,0], dtype=int))
        g1 = PhaseGoal(False, 3)
        g2 = PhaseGoal(True, 3)
        self.assertFalse(isWinningHand(h,[g1,g2]))

if __name__ == '__main__':
    unittest.main()
















