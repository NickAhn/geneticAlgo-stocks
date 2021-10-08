from random import random

import numpy as np

from Chromossome import Chromossome


def readFile(fileName):
    try:
        file = open(fileName + ".txt", "r")
    except OSError:
        print("Could not open/read file: " + fileName)
        return None

    arr = []
    for line in file:
        temp = line.split()
        arr.append(temp)

    return np.array(arr)


# Validate a string as being a numeric_type
def validate_numeric(value_string, numeric_type=int):
    try:
        return numeric_type(value_string)
    except ValueError:
        raise


def generateChromossomes(PopulationSize, data):
    chromossomeList = []
    for count in range(PopulationSize):
        chromossomeList.append(Chromossome(data))

    return np.array(chromossomeList)


# output: array of Chromossomes selected through Elitist Algorithm
def elitistSelection(chromossomeList, numOfSelectedChromossomes):
    list = chromossomeList.copy()
    sortedChromossomes = sorted(list, reverse=True)

    selectedChromossomes = []
    for x in range(numOfSelectedChromossomes):
        selectedChromossomes.append(sortedChromossomes[x])

    return selectedChromossomes





class GeneticAlgorithm:
    chromossomes = []

    # should be controllable:
    #   - fineName
    #   - number of Chromossomes in each Generation
    #   - number of Generations that algorithms will run before terminating
    #   - which selection algorithm to use (elitist/tournament)
    #   - What percentage of the next generation should be formed using selection
    #       - ex: 40% of 150 = 60 chromos cloned, 90 generated from crossover
    #       - mutation is applied randomly
    #   - Which crossover algorithm to use (uniform or kpoint).
    #   - The initial mutation rate and how much to change the mutation rate each generation
    #       – it should be possible to have a fixed mutation rate or to have a mutation rate
    #           that gradually decreases (without reaching zero).
    def __init__(self):
        self.file = None
        self.chromossomes = []
        self.numOfSelectedChromossomes = 0
        # self.runTest()

    def run(self):
        # asking for user for a data file
        while self.file is None:
            fileName = input("Name of the file to be used (without extension): ")
            self.file = readFile(fileName)
        # file = readFile("genAlgData1")
        print(self.file)

        # asking for number of chromossomes in each generation
        while True:
            chromNum = input("How many Chromossomes should each Generation have?: ")
            try:
                result = validate_numeric(chromNum, int)
            except ValueError:
                print("You did not input a number, try again.")
                continue
            else:
                break

        return 0

    def runTest(self):
        self.file = readFile("genAlgData1")

        populationSize = 4;
        self.chromossomes = generateChromossomes(4, self.file)

        self.numOfSelectedChromossomes = 2;

        selectionType = "Elitist"

        nextGen = elitistSelection(self.chromossomes, self.numOfSelectedChromossomes)


