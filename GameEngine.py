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
    # defining function to initialise Snake objects and place them randomly in the field
    def initSnake(self):
        """
        instantiate a new Snake object in a random, unoccupied slot in the field
        : return : None
        """
        while True:
            random_x, random_y = random.randint(0, len(self._field) - 1), random.randint(0, len(self._field[0]) - 1)
            if self._field[random_x][random_y] is None:
                self._snake = Snake(random_x, random_y)
                self._field[random_x][random_y] = self._snake
                break

    # defining function to set-up initial game field
    def initializeGame(self):
        """
        initialize the game field
        """
        # populate field with veggies, rabbits and captain
        self.initVeggies()
        self.initRabbits()
        self.initSnake()
        self.initCaptain()

    # defining function which counts number of remaining veggies in the field at a particular point
    def remainingVeggies(self):
        """
        function counts number of remaining veggies in the field
        : return : int
        """
        # variable to store remaining veggies
        remaining_Veggies = 0
        for field_row in self._field:
            for land in field_row:
                if isinstance(land, Veggie):
                    remaining_Veggies += 1
        return remaining_Veggies

    # defining function which explains rules of the game to player
    def intro(self):
        """
        display the game introduction and rule sets
        : return : None
        """
        print("\nWelcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest as many vegetables as possible before the rabbits eat them all!" 
        "\nEach vegetable is worth a different number of points so go for the high score!")

        print("\nThe vegetables are :")
        # print all veggie object details
        for veggie in self._possible_veggies:
            print(veggie)
        print(f"\nCaptain Veggie is {self._captain.getSymbol()}, and the rabbits are {self._rabbits[0].getSymbol()}'s")
        print("\nGood Luck!")

    # defining function which prints representation of current field
    def printField(self):
        """
        print the current state of the field
        """
        # print upper border 
        print("#" * ((len(self._field[0]) * 3) + 3 ))  
        for field_row in self._field:
            print("#", end=" ")
            for landspace in field_row:
                # check if landspace is empty
                if landspace is None:
                    print("  ", end=" ")
                # if land space is not empty, print the sybol of object which occupied the land
                else:
                    print(f"{landspace.getSymbol()} ", end=" ")
            print("#")
        # print lower border
        print("#" * ((len(self._field[0]) * 3) + 3 ))  


    # defining function which returns current score in the game 
    def getScore(self):
        """
        function to the current score.
        : return : int
        """
        if self._captain is not None:
            # count the points of all collected veggies by the Captain
            veggies_points = sum(veggie.getPoints() for veggie in self._captain.getCollectedVeggies())
            self._score = veggies_points
            return veggies_points
        else:
            self._score = 0
            return 0

    # defining function which randomely allocates new places to each rabit ni the field
    def moveRabbits(self):
        """
        move Rabbit objects around the field in random direction by 1 step only
        : return : None
        """
        # loop for each rabbit in the field
        for rabbit in self._rabbits:
            # loop till rabbit moves sucessfully 
            while True:
                new_x, new_y = rabbit.getX() + random.randint(-1, 1), rabbit.getY() + random.randint(-1, 1)
                if 0 <= new_x < len(self._field) and 0 <= new_y < len(self._field[0]) and ((self._field[new_x][new_y] is None) or (isinstance(self._field[new_x][new_y], Veggie))):
                    # update previous slot as empty slot
                    self._field[rabbit.getX()][rabbit.getY()] = None
                    # move rabbit to new slot
                    rabbit.move(new_x, new_y)
                    # mark that field space as occupied by Rabbit
                    self._field[new_x][new_y] = rabbit
                    break

    # function to move caption in vertical directions
    def moveCptVertical(self, vertical_movement):
        """
        move Captain vertically
        : param vertical_movement: vertical movement amount
        : type vertical_movement : int
        """
        updated_x = self._captain.getX() + vertical_movement
        y = self._captain.getY()
        self.moveCaptainHelper(updated_x, y)

    # function to move caption in horizontal directions
    def moveCptHorizontal(self, horizontal_movement):
        """
        move Captain horizontally
        : param horizontal_movement: horizontal movement amount
        : type horizontal_movement : int
        """
        new_x = self._captain.getX()
        new_y = self._captain.getY() + horizontal_movement
        self.moveCaptainHelper(new_x, new_y)


    # defining function to control captain's movement
    def moveCaptain(self):
        """
        function that takes input from user and moves captain in such directions
        : return : None
        """
        # prompt user for direction
        direction = input("Would you like to move up(W), down(S), left(A), or right(D): ")
        if direction.upper() == 'W':
            # update x coordinate to -1
            self.moveCptVertical(-1)
        elif direction.upper() == 'S':
            # update x coordinate to +1
            self.moveCptVertical(1)
        elif direction.upper() == 'A':
            # update y coordinate to -1
            self.moveCptHorizontal(-1)
        elif direction.upper() == 'D':
            # update y coordinate to +1
            self.moveCptHorizontal(1)
        else:
            # print invalid input
            print(f"{direction} is not valid option.")
    
    # defining function to control snake's movement
    def moveSnake(self):
        """
        function to move the snake towards Captain
        : return : None
        """
        if self._snake is not None and self._captain is not None:
            self._snake.move(self._captain.getX(), self._captain.getY(), self._field)


    # define function that outputs result of the game
    def gameOver(self):
        """
        display player performance and score of the game
        : return : None
        """
        print("\nGAME OVER!")
        print("You managed to harvest the following vegetables: ")
        for vegetable in self._captain.getCollectedVeggies():
            print(f"{vegetable.getName()}")
        print(f"Your score was: {self._score}")

    # defining function which updates score board of the game
    def highScore(self):
        """
        function to keep track of high scores and update scores in file
        """
        # list variable to store scores extracted from file
        high_scores = []
        try:
            with open(self.__HIGHSCOREFILE, 'rb') as file:
                high_scores = pickle.load(file)
        except FileNotFoundError:
            pass

        # variable to store user's initials
        initials = input("Please enter your three initials to go on the scoreboard: ").upper()[:3]
        playerscore = (initials, self._score)

        # if empty list then simply add the scores
        if not high_scores:
            high_scores.append(playerscore)
        
        # if list is not empty, add scores to appropreate place 
        else:
            index = 0
            while index < len(high_scores) and playerscore[1] < high_scores[index][1]:
                index += 1
            high_scores.insert(index, playerscore)

        print("\nHIGH SCORES : ")
        print("Name | Score")
        for data in high_scores:
            print(f"{data[0]:<5}| {data[1]}")

        # open file to write updated score data
        with open(self.__HIGHSCOREFILE, 'wb') as file:
            pickle.dump(high_scores, file)


    # funtion to update captains position in the field
    def moveCaptainHelper(self, new_x, new_y):
        """
        function to update captains position in the field
        : param new_x : new x-coordinate of captain
        : type new_x : int
        : param new_y : new y-coordinate of captain
        : type new_y : int
        """
        # check if new positions are valid field position
        if 0 <= new_x < len(self._field) and 0 <= new_y < len(self._field[0]):
            if self._field[new_x][new_y] is None:
                # move captain to an empty slot and update previous position as empty land field
                self._field[self._captain.getX()][self._captain.getY()] = None
                self._captain.setX(new_x)
                self._captain.setY(new_y)
                self._field[new_x][new_y] = self._captain
            elif isinstance(self._field[new_x][new_y], Veggie):
                # caption finds a veggie and collects it
                veggie = self._field[new_x][new_y] #veggie is temp variable to store vegetable details found by captain
                self._field[self._captain.getX()][self._captain.getY()] = None
                self._captain.setX(new_x)
                self._captain.setY(new_y)
                self._field[new_x][new_y] = self._captain
                self._score += veggie.getPoints()
                print(f"Yummy! A delicious {veggie.getName()}!")
                # add collected vegetable to captain's bucket
                self._captain.addVeggie(veggie)
            elif isinstance(self._field[new_x][new_y], Rabbit):
                # when captain tries to step on the rabbits
                print("Don't step on the bunnies!")
        else:
            print("You can't move that way!")


