import random
import time
from Scorestat import *
from ArrangeBoardAndBoats import *


class GameLogic():
    """
    author:Stian Strom Anderssen
    Game logic class
    """
    def play(self, board, playerlist, boardid, speed=0, player="",):
        """
        :param board:
        :param boardid:
        :param speed:
        :return:

         This function is the game logic for the battleship game. It changes board values. If the target board value
         is a boat, a -- will be added to the cell, to indicate that a boat was hit. If an empty field is hit, the cell
         will be updated with a **. The logic is constructed with random logic, meaning the program chooses a random
         field to hit without considering the fact that a boat was hit. This also means that sometimes the program tries
         to hit an already hit field. The method is made recursive, and calls itself again to regenerate cell values
         if the generated cell location already is hit. When a boat is hit, the program grant the player another try by
         calling the play function again.
        """
        time.sleep(speed)
        scorestat = Scorestat()
        arrangementsforboardandboats = ArrangeBoardAndBoats()
        print ( \
            "______________________________________________________________________")
        scorestat.check_for_winner(playerlist)
        print("It is "+player+"'s turn to hit board "+ str(boardid))
        for line in board:
            print(line)
        rownumber = random.randint(1, 10) - 1
        columnumber = random.randint(1, 10) - 1
        if board[rownumber][columnumber] == "  ":
            board[rownumber][columnumber] = "**"
            print("HIT blank field,", board[rownumber][
                columnumber], "at location", rownumber, ",", \
                  columnumber, "no boat in sight")
        elif board[rownumber][columnumber] == "**" or board[rownumber][columnumber] == "--" :
            print ("HIT the following field which is already hit", board[rownumber][columnumber], "trying again")
            self.play(board, playerlist, boardid, speed, player)
        else:
            oldvalue = board[rownumber][columnumber]
            board[rownumber][columnumber] = "--"
            boat_stil_exist = arrangementsforboardandboats.check_if_boat_is_blown_up(
                oldvalue,
                board)
            if boat_stil_exist:
                print ("BOOM boat is gone", oldvalue)
                boardplayer = "board" + str(boardid)
                scorestat.update_score_stats(boardplayer, oldvalue)
            else:
                print ("Hit part of boat", oldvalue)
            self.play(board, playerlist, boardid, speed,player)
