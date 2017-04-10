import random
from Board import *

class Boat():
    @classmethod
    def create_boat(self, number, length, symbol_to_represent_boat):
        """
        :param number:
        :param length:
        :param symbol_to_represent_boat:
        :return: list_of_boats
        Function to create given number of boats with a given length.
        """
        list_of_boats = []
        for i in range(number):
            boat = [symbol_to_represent_boat + str(i) for x in
                    range(length)]
            list_of_boats.append(boat)
        return list_of_boats

    @classmethod
    def create_boats(self):
        """
        :return: fullboatlist:
        Method to create lists with boats, as according to the battleship instructions.
        """
        fullboatlist = []
        boatlist1 = self.create_boat(1, 6, "A")
        boatlist2 = self.create_boat(2, 4, "B")
        boatlist3 = self.create_boat(3, 3, "C")
        boatlist4 = self.create_boat(3, 2, "D")
        fullboatlist.append(boatlist1)
        fullboatlist.append(boatlist2)
        fullboatlist.append(boatlist3)
        fullboatlist.append(boatlist4)
        return fullboatlist

