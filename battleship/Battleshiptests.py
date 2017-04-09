from Board import *
from Boat import *
from ArrangeBoardAndBoats import *
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

    def test_validation_fails_for_to_long_column(self):
        arrangements=ArrangeBoardAndBoats()
        boat=Boat()
        boatlist=boat.createBoat(1, 6, "A")
        self.assertFalse(arrangements.validate(self.emptymatrix,boatlist[0],1,2,9))

    def test_validation_fails_for_to_long_row(self):
        arrangements=ArrangeBoardAndBoats()
        boat=Boat()
        boatlist=boat.createBoat(1, 6, "A")
        self.assertFalse(arrangements.validate(self.emptymatrix,boatlist[0],0,9,5))

    def test_validation_is_ok(self):
        arrangements=ArrangeBoardAndBoats()
        boat=Boat()
        boatlist=boat.createBoat(1, 6, "A")
        self.assertTrue(arrangements.validate(self.emptymatrix,boatlist[0],0,2,3))

    def test_boards_creation(self):
        arrangements=ArrangeBoardAndBoats()
        boards=arrangements.placeBoats()
        self.assertIsNotNone(boards)



if __name__ == "__main__":
    unittest.main()