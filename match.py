
from game import *
from randomPlayer import RandomPlayer
from willPlayer import WillPlayer
from juliaPlayer import JuliaPlayer


if __name__ == '__main__':
    willWin = 0
    juliaWin = 0
    for i in range(500):
        p1 = WillPlayer("will")
        p2 = JuliaPlayer("julia")
        g = Game([p1,p2])
        winner = g.runGame()
        if(winner == "will"):
            willWin += 1
        elif(winner == "julia"):
            juliaWin += 1

    print("will win", willWin)
    print("julia win", juliaWin)








