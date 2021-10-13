**Project2: Genetic Algorithm**

Running the program:
* Run main.py
* The command line will ask user input for:
  * Name of the file to be used (without extension)
  * How many Chromossomes should each Generation have?:
  * How many Chromossomes should be selected to the next generation?
  * how many runs before the program should terminate?
  * What type of selection do you want? Elitist [1] or Tournament [2]
    * Enter 1 for Elitist Selection, 2 for Tournament Selection
  * What type of Crossover do you want? Uniform [1] One-Point [2]
    * Enter 1 for Uniform Crossover, 2 for One-Point Crossover
  * Would you like a flat mutation rate [1] or a gradual decrease [2]?
    * Enter 1 for a flat (fixed) mutation rate and 2 for a gradual decrease.
    * The mutation rate decreases by 10% each time. To change it, go to line 322 in GeneticAlgorithm.py
* The program will run after all inputs are received
