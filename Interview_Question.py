"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

"""
        Convert non-adjacent ones to zero and return this array.
"""

class Corner:

    def __init__(self, array):
        self.array = array
        self.cornerList = []
        self.neighbors = [] # all connect item
        self.catchCoordinate = [] # catch this time
        self.lastCatchCoordinate = [] # last catch

    def findCorner(self):
        for y, line in enumerate(self.array):
            for x, value in enumerate(line):
                if value:
                    if (x == 0 or x == 5) or (y == 0 or y == 5):
                            self.cornerList.append([y,x])
                    else:
                        pass
                else:
                    pass
        self.neighbors = self.cornerList.copy()
        self.lastCatchCoordinate = self.cornerList.copy()

    #   Find neighbot with recursion
    def findNeighbor(self):
        for coordinate in self.lastCatchCoordinate:
            self.checkUp(coordinate[1], coordinate[0])

        self.lastCatchCoordinate = self.catchCoordinate
        self.neighbors += self.catchCoordinate

        if self.catchCoordinate:
            self.catchCoordinate = []
            self.findNeighbor()

    #   Convert 1 to 0 non-neighbor numbers
    def processArray(self):

        for y, line in enumerate(self.array):
            for x, value in enumerate(line):
                if not [y,x] in self.neighbors:
                    self.array[y][x] = 0

        return self.array

    def checkUp(self, x, y):
        if not y == 0:
            if self.array[y - 1][x]:
                if not [y-1, x] in self.neighbors:
                    self.catchCoordinate.append([y-1, x])
                self.checkLeft(x, y)
            else:
                self.checkLeft(x, y)
        else:
            self.checkLeft(x, y)

    def checkLeft(self, x, y):
        if not x == 0:
            if self.array[y][x - 1]:
                if not [y, x-1] in self.neighbors:
                    self.catchCoordinate.append([y, x-1])
                self.checkRight(x, y)
            else:
                self.checkRight(x, y)
        else:
            self.checkRight(x, y)

    def checkRight(self, x, y):
        if not x == 5:
            if self.array[y][x + 1]:
                if not [y, x+1] in self.neighbors:
                    self.catchCoordinate.append([y, x+1])
                self.checkDown(x, y)
            else:
                self.checkDown(x, y)
        else:
            self.checkDown(x, y)

    def checkDown(self, x, y):
        if not y == 5:
            if self.array[y + 1][x]:
                if not [y+1, x] in self.neighbors:
                    self.catchCoordinate.append([y+1, x])
                return
            else:
                return

        else:
            return


if __name__ == '__main__':

    givenArray = [[1,0,0,0,0,0],
                   [0,1,0,1,1,1],
                   [0,0,1,0,1,0],
                   [1,1,0,0,1,0],
                   [1,0,1,1,0,0],
                   [1,0,0,0,0,1]]

    corner = Corner(givenArray)
    corner.findCorner()
    corner.findNeighbor()
    corner.processArray()
    for line in corner.processArray():
        print(line)
