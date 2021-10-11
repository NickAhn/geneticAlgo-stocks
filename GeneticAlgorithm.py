import random

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


# Generate Initial Population of Chromossomes
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


# Iterate over each of the 5 genes and randomly select whether to use the value
# from the first parent chromosome or the second parent chromosome
# Input: parents = array of chromossomes
def crossoverUniform(parents, offspringSize):
    temp = parents.copy()
    # arraySize = len(temp)
    # for parent in parents:
    #     temp.append(parent)
    for x in range(offspringSize):
        # randomly select parent one and two for crossover
        print("-- picking crossover: --")
        rand1 = random.randrange(len(parents))
        rand2 = random.randrange(len(parents))
        print(rand1)
        print(rand2)


        # parentOne = parents[random.randrange(len(parents))]
        # parentTwo = parents[random.randrange(len(parents))]

        parentOne = parents[rand1]
        parentTwo = parents[rand2]

        # add offspring born from the crossover of parentOne and parentTwo
        temp.append(uniformUtil(parentOne, parentTwo))

    return temp


# input: Two Chromossomes
# output: single chromossome with random genes from parents
def uniformUtil(one, two):
    temp = one
    for x in range(5):
        prob = random.uniform(0, 1)
        # 50/50 probability of choosing gene 2
        if random.randint(0, 1) == 1:
            print("--parente2")
            # newGene = one.getGene(x)
            temp.setGene(x, two.getGene(x))

    temp.fixRanges()
    temp.printGenes()
    return temp


# Iterate through each gene of each chromossome and mutate gene with a X probability.
# input: list of Chromossomes, probability

# The initial mutation rate and how much to change the mutation rate each generation
# – it should be possible to have a fixed mutation rate or to have a mutation rate that gradually decrease
def mutate(chromossomes, prob):
    for x in range(len(chromossomes)):
        for gene in range(5):
            if random.random() <= prob:
                chromossomes[x].mutateGene(gene)


class GeneticAlgorithm:
    # chromossomes = []

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

        populationSize = 8;
        self.chromossomes = generateChromossomes(populationSize, self.file)

        self.numOfSelectedChromossomes = 4;

        selectionType = "Elitist"

        print("\n-- ELITIST SELECTION --")
        # array of chromossomes
        parents = elitistSelection(self.chromossomes, self.numOfSelectedChromossomes)
        for x in range(len(parents)):
            parents[x].printGenes()

        offspringSize = populationSize - self.numOfSelectedChromossomes

        print("\n-- UNIFORM CROSSOVER --")
        #uniform Crossover
        nextGen = crossoverUniform(parents, offspringSize)

        print("\n Next gen: ")
        # print(len(nextGen))
        for x in range(len(nextGen)):
            nextGen[x].printGenes()

        print("\n-- MUTATION --")
        mutate(nextGen, 0.1)


