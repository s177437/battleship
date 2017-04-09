import random
import time
from Scorestat import *
from ArrangeBoardAndBoats import *

class GameLogic():


    def play(self, board, player,speed=0):
        time.sleep(speed)
        scorestat = Scorestat()
        arrangementsforboardandboats=ArrangeBoardAndBoats()
        print \
            "______________________________________________________________________"
        scorestat.checkForWinner()
        print "Board", player, "turn"
        for line in board:
            print line
        rownumber = random.randint(1, 10) - 1
        columnumber = random.randint(1, 10) - 1
        if board[rownumber][columnumber] == "  ":
            board[rownumber][columnumber] = "**"
            print "HIT blank field,", board[rownumber][
                columnumber], "at location", rownumber, ",", \
                columnumber, "no boat in sight"
        elif board[rownumber][columnumber] == "**":
            # print "This field is already taken, trying again",
            # board[rownumber][columnumber]
            self.play(board, player,speed)
        elif board[rownumber][columnumber] == "--":
            # print "This part of the boat is already blown up,
            # trying again"
            self.play(board, player,speed)
        else:
            oldvalue = board[rownumber][columnumber]
            board[rownumber][columnumber] = "--"
            boat_stil_exist = arrangementsforboardandboats.check_if_boat_is_blown_up(
                oldvalue,
                board)
            if boat_stil_exist:
                print "BOOM boat is gone", oldvalue
                boardplayer = "board" + str(player)
                scorestat.updateScoreStats(boardplayer, oldvalue)
            else:
                print "Hit part of boat", oldvalue
            self.play(board, player,speed)
