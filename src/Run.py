from GameLogic import *
from Scorestat import *


class Run:
    def __init__(self):
        pass

    @classmethod
    def run_battleship(cls, speed):
        """
        :param speed(optional):
        This is the run method for the battleship program. It creates an instance for the logic class
        ArrangemenBoardAndBoats, board class, gamelogic, and the scorestat class. The method is constructed to
        run as long as boats exist in the board. When a boat is removed, it is added to a scorestad dictionary.
        The program is created to stop when 9 boats are added to the scorestat. The speed parameter is optional and
        can be added to the logic to slow down the game simulation.
        :return:
        """
        log = Log()
        arrangelogic = ArrangeBoardAndBoats()
        boards = arrangelogic.place_boats()
        gamelogic = GameLogic()
        scorestat = Scorestat()
        while True:
            players = ["Stian", "Bot"]
            for i, b in enumerate(boards):
                if i == 0:
                    player = players[0]
                else:
                    player = players[1]
                gamelogic.play(b, players, i, speed, player=player)
                log.print_log(scorestat.get_scoredict())


run = Run()
run.run_battleship(0)
