import random
from Board import *
from Boat import *
class ArrangeBoardAndBoats() :


    def check_if_boat_is_blown_up(self, boatid, board):
        for line in board:
            if boatid in line:
                return False
        return True

    def placeBoats(self):
        boatclass=Boat()
        boardclass=Board()
        boardlist = boardclass.createTwoBoards()
        fullboatlist = boatclass.createBoats()
        newboardlist = []
        for boardindex, board in enumerate(boardlist):
            for boatlists in fullboatlist:
                for boat in boatlists:
                    vertical_or_horizontal = random.randint(0, 1)
                    placement_ok = False
                    while not placement_ok:
                        a = random.randint(1, 10) - 1
                        b = random.randint(1, 10) - 1
                        placement_ok = self.validate(board, boat,
                                                     vertical_or_horizontal,
                                                     a, b)
                    board, placement_ok = self.place_out_boats(board, boat,
                                                     vertical_or_horizontal,
                                                     a, b)
            newboardlist.append(board)
        return newboardlist

    def validate(self, board, boat, direction, row, column):
        if direction == 1 and len(boat) + row > 10:
            return False
        elif direction == 1 and len(boat) + column > 10:
            return False
        elif direction == 0 and len(boat) + column > 10:
            return False
        elif direction == 0 and len(boat) + row > 10:
            return False
        else:
            if direction == 1:
                for i, element in enumerate(boat):
                    if board[row][column + i] != "  ":
                        return False
            else:
                for i, element in enumerate(boat):
                    if board[row + i][column] != "  ":
                        return False
        return True

    def place_out_boats(self, board, boat, direction, row, column):
        validate = True
        if direction == 1:
            for i, element in enumerate(boat):
                if board[row][column + i] != "  ":
                    validate = False
                else:
                    board[row][column + i] = boat[i]
        else:
            for i, element in enumerate(boat):
                if board[row + i][column] != "  ":
                    validate = False
                else:
                    board[row + i][column] = boat[i]
        return board, validate
