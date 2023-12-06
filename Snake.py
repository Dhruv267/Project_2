# author : Dhruv Parmar, Vindhya Umesh, Anita Ershadi
# Date : 12/02/2023
# Description : Module to set-up new creature which is snake in our game
# GitHub : https://github.com/Dhruv267/Project_2

# import creature module
from Creature import Creature
from Captain import Captain
import random

# defining snake class
class Snake(Creature):
    def __init__(self, x, y):
        """
        constructor for Snake class.
        : param x : initial x-coordinate of the snake
        : type x : int 
        : param y: initial y-coordinate of the snake
        : type y : int 
        """
        # calling superclass constructor with "S" as symbol for snake
        super().__init__(x, y, 'S')  

    
    #defining function that moves snake closer to captain 
    def move(self, x_coordinate_captain, y_coordinate_captain, field):
        """
        move the snake closer to the captain
        : param x_coordinate_captain : x-coordinate of the captain
        : type x_coordinate_captain :  int
        : param y_coordinate_captain : y-coordinate of the captain
        : type y_coordinate_captain :  int
        """
        # find difference in x & y coordinates distance
        x_difference = x_coordinate_captain - self.getX()
        y_difference = y_coordinate_captain - self.getY()

        # move in the direction of larger difference direction
        if abs(x_difference) > abs(y_difference):
            new_x = self.getX() + (1 if x_difference > 0 else -1)
            new_y = self.getY()
        else:
            new_x = self.getX()
            new_y = self.getY() + (1 if y_difference > 0 else -1)

        # check for validity of new coordinates
        if 0 <= new_x < len(field) and 0 <= new_y < len(field[0]):
            # if new coordinates is a empty space
            if field[new_x][new_y] is None:
                # Move the snake to the new position
                field[self.getX()][self.getY()] = None
                self.setX(new_x)
                self.setY(new_y)
                field[new_x][new_y] = self
            # if next location is Captain, remove last 5 veggies from captain and relocate snake to a new position    
            elif isinstance(field[new_x][new_y], Captain):
                captain = field[new_x][new_y]
                captain.loseLastFiveVeggies()
                # reset the snake to a new random location
                self.resetRandomPosition(field)
            # if next location is Rabbit or Veggie, do not move snake

    # defining a function that resets snakes position randomly after it gets captain
    def resetRandomPosition(self, field):
        """
        function to place snake to a new random position on the field
        : param field : current state of the field
        : type field :  List[List[FieldInhabitant]]
        """
        # loop till new place is found for snake
        while True:
            updated_snake_x, updated_snake_y = random.randint(0, len(field) - 1), random.randint(0, len(field[0]) - 1)
            if field[updated_snake_x][updated_snake_y] is None:
                # reset snake's previous position to None
                field[self.getX()][self.getY()] = None
                self.setX(updated_snake_x)
                self.setY(updated_snake_y)
                field[updated_snake_x][updated_snake_y] = self
                break
