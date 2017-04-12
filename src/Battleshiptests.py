from Board import *
from Boat import *
from ArrangeBoardAndBoats import *
import unittest

class BattleShipTests(unittest.TestCase) :
    """
    Test class for the battleship game. This class will contain unittests for different functions implemented in the
    battleship code.
    """
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
        """"
        Function to test if a blank board can be created.
        """
        board=Board()
        boardmatrix=board.create_board()
        self.assertListEqual(self.emptymatrix,boardmatrix, msg="Test to determine if the generated board contains only empty double spaces")

    def test_board_length(self):
        """
        :return:
         Test to validate that the generated board is 10X10.
        """
        board=Board()
        boardmatrix=board.create_board()
        self.assertEqual(len(self.emptymatrix),len(boardmatrix),msg="Test to check length of the genereated board matrix and make sure it is 10X10")

    def test_len_boats(self):
        """
        :return:
         Test to see if the length of the generated boats is correct.
        """
        expected_numbers={1:6,2:4,3:3,3:2}
        boatdict={}
        boat=Boat()
        boatlists=boat.create_boats()
        for boatlist in boatlists :
            for boat in boatlist :
                boatdict[len(boatlist)]=len(boat)
        self.assertDictEqual(expected_numbers,boatdict, msg="Test to se that the correct number of boats are generated")

    def test_validation_fails_for_to_long_column(self):
        """
        Test to see that validation fails for a boat that intends to be placed with to high column numbers.
        """
        arrangements=ArrangeBoardAndBoats()
        boat=Boat()
        boatlist=boat.create_boat(1, 6, "A")
        self.assertFalse(arrangements.validate_placement_coordinates(self.emptymatrix, boatlist[0], 1, 2, 9))

    def test_validation_fails_for_to_long_row(self):
        """
        Test to see that validation fails for a boat that intends to be placed with to high row numbers.
        """
        arrangements=ArrangeBoardAndBoats()
        boat=Boat()
        boatlist=boat.create_boat(1, 6, "A")
        self.assertFalse(arrangements.validate_placement_coordinates(self.emptymatrix, boatlist[0], 0, 9, 5))

    def test_validation_is_ok(self):
        """
        Test to see that a boat can be placed with valid rows and column coordinates.
        :return:
        """
        arrangements=ArrangeBoardAndBoats()
        boat=Boat()
        boatlist=boat.create_boat(1, 6, "A")
        self.assertTrue(arrangements.validate_placement_coordinates(self.emptymatrix, boatlist[0], 0, 2, 3))

    def test_boards_creation(self):
        """
        Test to see that boards where boats are placed out are not empty
        """
        arrangements=ArrangeBoardAndBoats()
        boards=arrangements.place_boats()
        self.assertIsNotNone(boards)




if __name__ == "__main__":
    unittest.main()