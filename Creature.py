# author : Dhruv Parmar, Vindhya Umesh, Anita Ershadi
# Date : 12/02/2023
# Description : Implementation of Creature class
# GitHub : https://github.com/Dhruv267/Project_2

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        """
        constructor of Creature class
        : param x : x-coordinate of the creature
        : type x : integer
        : param y :  y-coordinate of the creature
        : type y : integer
        : param symbol : symbol representing the creature
        : type symbol : string
        """

        # calling constructor method of superclass (FieldInhabitant)
        super().__init__(symbol)

        # protected variable to store X coordinate of Creature
        self._x = x

          # protected variable to store Y coordinate of Creature
        self._y = y

    # defining getter method for x co-ordinate
    def getX(self):
        """
        getter method for the x-coordinate of the creature
        : return : integer 
        """
        return self._x

    # defining setter method for x co-ordinate
    def setX(self, x):
        """
        setter method for the x-coordinate of the creature
        : param x : new x-coordinate to update
        : type x : integer
        """
        self._x = x

    # defining getter method for y co-ordinate
    def getY(self):
        """
        getter method for the y-coordinate of the creature
        : return : integer 
        """
        return self._y

    # defining setter method for y co-ordinate
    def setY(self, y):
        """
        setter method for the y-coordinate of the creature
        : param y : new y-coordinate to update
        : type y : integer
        """
        self._y = y

