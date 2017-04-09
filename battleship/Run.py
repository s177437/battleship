from ArrangeBoardAndBoats import *
from GameLogic import  *
from Scorestat import *
class Run() :

    def runBattleShip(self):
        arrangelogic=ArrangeBoardAndBoats()
        boards = arrangelogic.placeBoats()
        gamelogic=GameLogic()
        scorestat=Scorestat()
        while True:
            for i, b in enumerate(boards):
                gamelogic.play(b, i)
                print scorestat.get_scoredict()

run=Run()
run.runBattleShip()
