from Board import *
from Boat import *
import unittest

class BattleShipTests(unittest.TestCase) :
    emptymatrix=[['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ', ]]
    def test_board_creation(self):
        board=Board()
        boardmatrix=board.createBoard()
        self.assertListEqual(self.emptymatrix,boardmatrix, msg="Test to determine if the generated board contains only empty double spaces")

    def test_board_length(self):
        board=Board()
        boardmatrix=board.createBoard()
        self.assertEqual(len(self.emptymatrix),len(boardmatrix),msg="Test to check length of the genereated board matrix and make sure it is 10X10")

    def test_len_boats(self):
        expected_numbers={1:6,2:4,3:3,3:2}
        boatdict={}
        boat=Boat()
        boatlists=boat.createBoats()
        for boatlist in boatlists :
            for boat in boatlist :
                boatdict[len(boatlist)]=len(boat)
        self.assertDictEqual(expected_numbers,boatdict, msg="Test to se that the correct number of boats are generated")





if __name__ == "__main__":
    unittest.main()