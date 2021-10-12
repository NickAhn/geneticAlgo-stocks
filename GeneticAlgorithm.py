import random

import numpy as np
from pip._internal.utils.misc import enum

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


# Output: array of Chromossomes selected through Elitist Algorithm
def elitistSelection(chromossomeList, numOfSelectedChromossomes):
    list = chromossomeList.copy()
    sortedChromossomes = sorted(list, reverse=True)

    selectedChromossomes = []
    for x in range(numOfSelectedChromossomes):
        selectedChromossomes.append(sortedChromossomes[x])

    return selectedChromossomes


def tournamentSelection(chromossomeList, numOfSelectedChromossomes):
    selectedChromossomes = []
    for x in range(numOfSelectedChromossomes):
        #tuple of random chromossomes:
        randChromossome = (chromossomeList[random.randrange(len(chromossomeList))],
                           chromossomeList[random.randrange(len(chromossomeList))])
        if randChromossome[0].getFitnessScore() > randChromossome[1].getFitnessScore():
            selectedChromossomes.append(randChromossome[0])
        else:
            selectedChromossomes.append(randChromossome[1])

    return selectedChromossomes


# Iterate over each of the 5 genes and randomly select whether to use the value
# from the first parent chromosome or the second parent chromosome
# Input: parents = array of chromossomes
def crossoverUniform(parents, offspringSize):
    temp = parents.copy()

    for x in range(offspringSize):
        # randomly select parent one and two for crossover
        rand1 = random.randrange(len(parents))
        rand2 = random.randrange(len(parents))

        parentOne = parents[rand1]
        parentTwo = parents[rand2]

        temp.append(uniformUtil(parentOne, parentTwo))

    return temp

# Take the first 2 genes from the first parent chromosome and the last 3 genes
# from the second parent chromosome to form a child chromosome.
# In this case you don’t need to worry about creating an invalid chromosome.
def crossoverOnePoint(parents, offspringSize):
    temp = parents.copy()

    for x in range(offspringSize):
        parentOne = parents[random.randrange(len(parents))]
        parentTwo = parents[random.randrange(len(parents))]

        for gene in range(2, 5):
            parentOne.setGene(gene, parentTwo.getGene(gene))
            parentOne.printGenes()

        temp.append(parentOne)

    return temp


# input: Two Chromossomes
# output: single chromossome with random genes from parents
def uniformUtil(one, two):
    temp = one
    for x in range(5):
        prob = random.uniform(0, 1)
        # 50/50 probability of choosing gene 2
        if random.randint(0, 1) == 1:
            # print("--parente2")
            # newGene = one.getGene(x)
            temp.setGene(x, two.getGene(x))

    temp.fixRanges()
    # temp.printGenes()
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


# print the Max Min and Median fitness scores every 10 runs
def printMaxMinAvg(population, runs):
    if runs % 10 == 0:
        #finding max:
        print("\n--- Max, Min and Median Fitness Scores after " + str(runs) + " runs ---")
        print(" Max fitness score: " + str(population[0].getFitnessScore()))
        print(" Min fitness score: " + str(population[-1].getFitnessScore()))

        center = np.take(population, len(population)/2)
        print(" Median fitness score: " + str(center.getFitnessScore()))

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

    def runTest(self):
        self.file = readFile("genAlgData1")

        populationSize = 8;
        self.chromossomes = generateChromossomes(populationSize, self.file)
        for x in range(len(self.chromossomes)):
            self.chromossomes[x].printGenes()

        self.numOfSelectedChromossomes = 4;

        selectionType = "Elitist"

        # print("\n-- ELITIST SELECTION --")
        # # array of chromossomes
        # parents = elitistSelection(self.chromossomes, self.numOfSelectedChromossomes)
        # for x in range(len(parents)):
        #     parents[x].printGenes()

        print("\n-- TOURNAMENT SELECTION --")
        # list of chromossomes
        parents = tournamentSelection(self.chromossomes, self.numOfSelectedChromossomes)
        for x in range(len(parents)):
            parents[x].printGenes()

        offspringSize = populationSize - self.numOfSelectedChromossomes

        print("\n-- UNIFORM CROSSOVER --")
        #uniform Crossover
        # nextGen = crossoverUniform(parents, offspringSize)

        #one point crossover
        nextGen = crossoverOnePoint(parents, offspringSize)

        print("\n Next gen: ")
        # print(len(nextGen))
        for x in range(len(nextGen)):
            nextGen[x].printGenes()

        print("\n-- MUTATION --")
        mutate(nextGen, 0.1)

    # should be controllable:
    #   - fineName:String = name of the file
    #   - popSize:int = number of Chromossomes in each Generation
    #   - runs:int = number of Generations that algorithms will run before terminating
    #   - selectionType:String = which selection algorithm to use (elitist/tournament)
    #   - selectionProb:float  = What percentage of the next generation should be formed using selection
    #       - ex: 40% of 150 = 60 chromos cloned, 90 generated from crossover
    #       - mutation is applied randomly
    #   - crossoverType:String = Which crossover algorithm to use (uniform or kpoint).
    #   - mutationProb:float = The initial mutation rate and how much to change the mutation rate each generation
    #       – it should be possible to have a fixed mutation rate or to have a mutation rate
    #           that gradually decreases (without reaching zero).
    def run(self):
        # 1. asking for user for a data file: String
        while self.file is None:
            fileName = input("Name of the file to be used (without extension): ")
            self.file = readFile(fileName)


        # 2. asking for number of chromossomes in each generation (population):int
        while True:
            popSize = input("How many Chromossomes should each Generation have?: ")
            try:
                result = validate_numeric(popSize, int)
            except ValueError:
                print("You did not input a number, try again.")
                continue
            else:
                break

        self.popSize = int(popSize)
        #generating initial population
        initialPop = generateChromossomes(self.popSize, self.file)

        # asking for number of selected chromossomes:int
        self.numOfSelectedChromossomes = int(input("How many Chromossomes should be selected to the next generation?"))

        # Ask for how many runs before the program should terminate
        self.totalRuns = int(input("how many runs before the program should terminate?"))

        # asking selection type and prob:String
        self.selectionType = int(input("What type of selection do you want? Elitist [1] or Tournament [2]"))

        # self.selectionProb = input("What should be the ")  this is numOfSelectedChromossomes

        #Asking for crossover Type
        self.crossoverType = int(input("What should be the crossover type be? Uniform [1]"))


        #Mutation Rate
        mutationProb = 0.1

        #Ask if there should be decreasae in mutation rate
        foo = input("Would you like a flat mutation rate [1] or a gradual decrease [2]?")
        if foo == 1:
            self.mutationVariation = False
        else:
            self.mutationVariation = True

        self.runAlgoRecursive(0, initialPop, mutationProb)

    # input:
    #   - run: int = run number
    #   - population : List<Chromossomes> = list of current population of chromossomes
    #   - mutationProb : float = probability for a gene mutation
    #   - gradualDecrease : Boolean = whether or not the mutation rate is flat.
    # Output:
    #   - print max, min and avg fitness scores after each generation
    #   - At final generation: print Chromossome with highest fitness score and its score
    def runAlgoRecursive(self, run, population, mutationProb):
        # print("----RECURSIVE: RUNS = " + str(runs))
        if run == self.totalRuns:
            print("\n--- Final Generation ---\n")
            print(" Highest fit chromossome = ")
            population[0].printGenes()
            print(" Fitness score = " + str(population[0].getFitnessScore()))
            return

        ## Step 1: Selection
        if self.selectionType == 1:
            # list of Chromossomes selected by Elitist selection
            parents = elitistSelection(population, self.numOfSelectedChromossomes)

        # number of offsprings to be created
        offspringSize = self.popSize - self.numOfSelectedChromossomes

        ## Step 2: Crossover
        #list containing the parent Chromossomes and offsprings
        if self.crossoverType == 1:
            nextGen = crossoverUniform(parents, offspringSize)

        ## Step 3: Mutation
        mutate(nextGen, mutationProb)
        if self.mutationVariation is True:
            mutationProb = mutationProb - (mutationProb*0.10)

        mutate(nextGen, mutationProb)

        printMaxMinAvg(population, run)

        self.runAlgoRecursive(run+1, nextGen, mutationProb)






