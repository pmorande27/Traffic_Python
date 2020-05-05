import random as r
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
from matplotlib import patches


class Road(object):
    def __init__(self, iterations, length_of_road, NofCars):
        self.car_positions = []
        if (length_of_road < NofCars):
            raise Exception("The Number of cars cannot be larger than the length of the road")
        self.iterations = iterations
        self.length = length_of_road
        self.NofCars = NofCars
        self.road = self.setUpRoad()
        self.historical = [self.road[:]]

    def setUpRoad(self):
        available_positions = list(range(0, self.length))
        road = []
        for i in range(self.NofCars):
            random_position = r.choice(available_positions)
            self.car_positions.append(random_position)
            available_positions.remove(random_position)
        for j in range(self.length):
            if j in self.car_positions:
                road.append(1)
            else:
                road.append(0)
        print(road)
        self.car_positions.sort()
        return road


    def Iterate(self):

        for i in range(self.iterations):

            moves = 0
            new_carPositions = []
            for j in self.car_positions:

                if j == self.length-1:
                    if self.road[0] == 0:
                        moves += 1
                        self.road[j] = 0
                        self.road[0] = 1
                        new_carPositions.append(0)
                    else:
                        new_carPositions.append(j)
                else:
                    if self.road[j+1] == 0:
                        moves += 1
                        self.road[j] = 0
                        self.road[j+1] = 1
                        new_carPositions.append(j+1)

                    else:
                        self.road[j] = 1
                        new_carPositions.append(j)
            new_carPositions.sort()
            self.car_positions = new_carPositions[:]
            self.historical += [self.road[:]]
            print(moves/self.NofCars)
            print(self.road)




def main():
    a = Road(200,1000,750)
    a.Iterate()

main()