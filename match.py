
from game import *
from randomPlayer import RandomPlayer
from juliaPlayerOld import JuliaPlayerOld
from juliaPlayer import JuliaPlayer
from willPlayer import WillPlayer


if __name__ == '__main__':
    willWin = 0
    juliaOldWin = 0
    juliaWin = 0
    for i in range(100):
        p1 = JuliaPlayerOld("old")
        p2 = JuliaPlayer("julia")
        p3 = WillPlayer("will")
        g = Game([p2, p3])
        winner = g.runGame()
        if(winner == "old"):
            juliaOldWin += 1
        elif(winner == "julia"):
            juliaWin += 1
        elif(winner == "will"):
            willWin += 1

    print("will win", willWin)
    # print("old julia win", juliaOldWin)
    print("julia win", juliaWin)








