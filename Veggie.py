# author : Dhruv Parmar, Vindhya Umesh, Anita Ershadi
# Date : 12/02/2023
# Description : Implementation of Veggie class
# GitHub : https://github.com/Dhruv267/Project_2

from FieldInhabitant import FieldInhabitant

# Defining Veggie class 
class Veggie(FieldInhabitant):

    # defining constructor for Veggie class
    def __init__(self, name, symbol, value):
        """
        constructor for Veggie class
        : param name : name of the vegetable.
        : type name : String
        : param symbol : symbol to represent vegetable
        : type symbol : String
        : param value : value of each vegetable.
        : type value: String
        """

        # calling constructor method of superclass (FieldInhabitant)
        super().__init__(symbol)
        
        # protected variable to store name of veggie
        self._name = name

        # protected variable to store points of veggie
        self._points = value

    
    # overloading string function to provide veggie object info
    def __str__(self):
        """
        string method to print all the Information of vegitables in the game
        : return : String 
        """
        return f"{self._symbol}: {self._name} {self._points} points"

    # getter method to get name of veggie
    def getName(self):
        """
        getter method for the name of the veggie
        : return : string 
        """
        return self._name

    # setter method to set name of veggie
    def setName(self, name):
        """
        setter method for the name parameter of the veggie
        : param name : new name to set.
        : type name : string
        """
        self._name = name

    # getter method to get points of vegetable
    def getPoints(self):
        """
        getter method for the points of the vegetable.
        : return : integer 
        """
        return self._points

    # setter method to set value of vegetable
    def setPoints(self, value):
        """
        setter function for the points of the vegetable.
        : param value : The new points to set
        : type value: integer
        """
        self._points = value
