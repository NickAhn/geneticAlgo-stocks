import random
import numpy as np


# output: tuple (x, y) where x < y.
def generateRange():
    mu, sigma = 0.0, 1.5

    x = np.random.normal(0.0, 1.5)
    y = np.random.normal(0.0, 1.5)

    # if x<y, x is lower bound and y is upper bound
    if x < y:
        return x, y

    return y, x


# defining sell/short with a 50/50 probability
# output: 0 = sell, 1 = buy
def generateBuySell():
    x = 0
    if random.uniform(0, 1) <= 0.5:
        return 0
    else:
        return 1


class Chromossome:

    # • The first number represents the percentage price change from one day to the next of the S&P 500 stock index.
    # •The second number represents the percentage price change on the following day.
    # •The third number represents the profit in dollars that you would have made if you had bought an ETF
    #       of the stock market index and held it for one day (negative numbers represent losing money).
    def __init__(self):
        (one, two) = generateRange()
        three, four = generateRange()
        five = generateBuySell()

        self.genes = [one, two, three, four, five]

    def printGenes(self):
        print(self.genes)

    def getFifth(self):
        return self.genes[-1]

    def getFitnessScore(self, arr):
        # if no data matches with fitness test, return -5000 as fitness score.
        score = 0;

        # for every list of data in arr
        for list in arr:
            # if the first and second prices ranges fall within the ranges in gene 1,2 and 3,4 respectivelly:
            if self.checkFirst(float(list[0])) and self.checkSecond(float(list[1])):
                # check gene 5 to see if it's a buy or sell
                if self.genes[4] == 0:
                    score = score + float(list[2]) * (-1)
                else:
                    score = score + float(list[2])

        print("- fitness score: " + str(score))

        # if score == 0:
        #     return -5000
        # else:
        return score

    def checkFirst(self, first):
        return self.genes[0] < first < self.genes[1]

    def checkSecond(self, second):
        return self.genes[2] < second < self.genes[3]

