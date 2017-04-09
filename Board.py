class Board():
    def createBoard(self):
        rows, columns = 10, 10
        matrix = [["  " for x in range(columns)] for y in range(rows)]
        return matrix

    def createTwoBoards(self):
        board1 = self.createBoard()
        board2 = self.createBoard()
        return [board1, board2]


