import random
from Board import *

class Boat():
    def createBoat(self, number, length, symbol_to_represent_boat):
        list_of_boats = []
        for i in range(number):
            boat = [(symbol_to_represent_boat + str(i)) for x in
                    range(length)]
            list_of_boats.append(boat)
        return list_of_boats

    def createBoats(self):
        fullboatlist = []
        boatlist1 = self.createBoat(1, 6, "A")
        boatlist2 = self.createBoat(2, 4, "B")
        boatlist3 = self.createBoat(3, 3, "C")
        boatlist4 = self.createBoat(3, 2, "D")
        fullboatlist.append(boatlist1)
        fullboatlist.append(boatlist2)
        fullboatlist.append(boatlist3)
        fullboatlist.append(boatlist4)
        return fullboatlist

