# author : Dhruv Parmar, Vindhya Umesh, Anita Ershadi
# Date : 12/02/2023
# Description : Implementation of GameEngine class and its methods
# GitHub : https://github.com/Dhruv267/Project_2

# import libraries and modules 
import random
import pickle
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie
from Snake import Snake

# defining GameEngine class
class GameEngine:

    # defining private constants
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    # defining constructor for GameEngine
    def __init__(self):
        """
        constructor for GameEngine class
        """
        # declaring and initialising member variables
        self._field = []
        self._rabbits = []
        self._captain = None
        self._snake = None
        self._possible_veggies = []
        self._score = 0

    # defining initVEggies function
    def initVeggies(self):
        """
        initialize vegetables in the game
        : return : None
        """

        # looping until receiving correct file name
        while True:
            try:
                inputfile = input("Please enter the name of the vegetable point file: ")
                with open(inputfile, 'r') as file:
                    lines = file.readlines()

                    # reading first line to get dimentions of the field 
                    firstLine = lines[0].strip().split(",")
                    height = int(firstLine[1])
                    width = int(firstLine[2])

                    # setting up field
                    self._field = [[None for _ in range(width)] for _ in range(height)]

                    # reading remaining lines to get veggie informations
                    for line in lines[1:]:
                        name, symbol, value = line.strip().split(',')
                        veggie = Veggie(name, symbol, int(value))
                        self._possible_veggies.append(veggie)

                    # plant all 30 vegetable in the field
                    for _ in range(self.__NUMBEROFVEGGIES):

                        # loop until empty space is found to plant a vegatable
                        while True:
                            x_coordinate, y_coordinate = random.randint(0, height - 1), random.randint(0, width - 1)
                            if self._field[x_coordinate][y_coordinate] is None:
                                self._field[x_coordinate][y_coordinate] = random.choice(self._possible_veggies)
                                break

            # raise exception if file not found
            except FileNotFoundError:
                print(f"{inputfile} does not exist! ")
                continue
            else:
                break

    # defining initCaptiain function to randomly place captain in the field
    def initCaptain(self):
        """
        initialize the Captain object
        : return : None
        """
        
        # loop until empty space is found for captain
        while True:
            x_coordinate, y_coordinate = random.randint(0, len(self._field) - 1), random.randint(0, len(self._field[0]) - 1)
            if self._field[x_coordinate][y_coordinate] is None:
                self._captain = Captain(x_coordinate, y_coordinate)
                self._field[x_coordinate][y_coordinate] = self._captain
                break

    # defining function to initialise Rabbit objects and place them randomly in the field
    def initRabbits(self):
        """
        initialize Rabbit objects and randomly place them in field
        : return : None
        """
        # loop till all the rabbits are placed (here 5 rabbits)
        for _ in range(self.__NUMBEROFRABBITS):
            # loop until empty space is found for rabbit
            while True:
                x_coordinate, y_coordinate = random.randint(0, len(self._field) - 1), random.randint(0, len(self._field[0]) - 1)
                if self._field[x_coordinate][y_coordinate] is None:
                    rabbit = Rabbit(x_coordinate, y_coordinate)
                    self._rabbits.append(rabbit)
                    self._field[x_coordinate][y_coordinate] = rabbit
                    break


