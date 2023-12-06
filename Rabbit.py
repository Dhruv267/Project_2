# author : Dhruv Parmar, Vindhya Umesh, Anita Ershadi
# Date : 12/02/2023
# Description : Implementation of Rabbit class
# GitHub : https://github.com/Dhruv267/Project_2

from Creature import Creature

# defining Rabbit class
class Rabbit(Creature):

    # defining constructor for Rabbit class
    def __init__(self, x, y):
        """
        constructor for Rabbit class.
        : param x : x-coordinate of the rabbit
        : type x : integer
        : param y : y-coordinate of the rabbit
        : type y: integer
        """

        # calling constructor method of super class and passing 'R' as the symbol for the Rabbit
        super().__init__(x, y, 'R') 

    # defining setter method for x coordinate of rabbit
    def setX(self, x):
        """
        setter method for the x-coordinate of the rabbit
        : param x : updated x-coordinate
        : type x : integer
        """
        super().setX(x)

    # defining setter method for y coordinate of rabbit
    def setY(self, y):
        """
        setter method for the y-coordinate of the rabbit
        : param y : updated y-coordinate
        : type y : integer
        """
        super().setY(y)
    
    # defining function that updates both co-ordinates together
    def move(self, updated_x, updated_y):
        """
        function to move the rabbit to a new position
        : param  updated_x : new x-coordinate of rabbit
        : type updated_x : int
        : param  updated_y : new y-coordinate of rabbit
        : type updated_y : int
        """
        self.setX(updated_x)
        self.setY(updated_y)

