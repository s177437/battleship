import random
from Board import *
from Boat import *


class ArrangeBoardAndBoats():
    @classmethod
    def check_if_boat_is_blown_up(self, boatid, board):
        """
        :param boatid:
        :param board:
        :return: True/False
        Function to check is boat is blown up. If the boatid exist in the board
        """
        for line in board:
            if boatid in line:
                return False
        return True

    def place_boats(self):
        """
        :return listofboards:
         Function to place boat in the board. The function performs a validation(See validation function description below)
         If the validation returns True, the boat is placed on the board, using random generated numbers for column and row.
         The place function is described below.

        """
        boatclass = Boat()
        boardclass = Board()
        boardlist = boardclass.create_two_boards()
        fullboatlist = boatclass.create_boats()
        newboardlist = []
        for boardindex, board in enumerate(boardlist):
            for boatlists in fullboatlist:
                for boat in boatlists:
                    vertical_or_horizontal = random.randint(0, 1)
                    placement_ok = False
                    while not placement_ok:
                        a = random.randint(1, 10) - 1
                        b = random.randint(1, 10) - 1
                        placement_ok = self.validate_placement_coordinates(board, boat,
                                                                           vertical_or_horizontal,
                                                                           a, b)
                    board, placement_ok = self.place_out_boats(board, boat,
                                                               vertical_or_horizontal,
                                                               a, b)
            newboardlist.append(board)
        return newboardlist

    @classmethod
    def validate_placement_coordinates(self, board, boat, direction, row, column):
        """
        :param board:
        :param boat:
        :param direction:
        :param row:
        :param column:
        :return:
         Function to validate that the generated start row and column is within the border of the board. It checks if the
         length of the boat does not exceed the limit of rows and columns. The direction parameter indicates if the check
         should be performed in horizontal or vertical direction.
        """
        if (direction == 1 and len(boat) + column > 10) or (direction == 0 and len(boat) + row > 10):
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

    @classmethod
    def place_out_boats(self, board, boat, direction, row, column):
        """
        :param board:
        :param boat:
        :param direction:
        :param row:
        :param column:
        :return: board,validate(Boolean)
        Function to place out boats on the board based on a random generated row and column. This function is
        executed if the validation function has succeeded. The direction parameter indicates if the boat should
        be placed horizontally or vertically.
        """
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
