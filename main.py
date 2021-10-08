import random

import numpy as np

import GeneticAlgorithm


# function to read text file and store its data.
# input: text file
# output: array of tuples. Each element in the array contain tuples of the values in each line
from Chromossome import Chromossome


def readFile(filename):
    file = open(filename + ".txt", "r")
    arr = []
    for line in file:
        temp = line.split()
        arr.append(temp)

    return np.array(arr)




# Be sure to seed your random number generator.
def generateInitialPopulation():
    return 0


def fitnessScore(chromossome):
    return chromossome.getThird();

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = readFile("genAlgData1.txt")
    print(data)

    x = Chromossome()
    x.printGenes()

    # for list in data:
    #     print(list[0] + " in range: " + str(x.checkFirst(float(list[0]))))

    x.getFitnessScore(data)







# -------------



# must be controllable:
# • The filename containing the training data.
# •The number of chromosomes in each generation.
# •The number of generations that your algorithm will run before terminating.
#
