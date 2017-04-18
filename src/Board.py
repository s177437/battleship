class Board:
    def __init__(self):
        pass

    @classmethod
    def create_board(cls):
        """
        :return: matrix

        Function to create an empty 10X10 board
        """
        rows, columns = 10, 10
        matrix = [["  " for x in range(columns)] for y in range(rows)]
        return matrix

    def create_two_boards(self):
        """
        Function to create two boards
        :return:
        """
        board1 = self.create_board()
        board2 = self.create_board()
        return [board1, board2]
