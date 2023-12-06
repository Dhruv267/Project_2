# author : Dhruv Parmar, Vindhya Umesh, Anita Ershadi
# Date : 12/02/2023
# Description : Implementation of FieldInhabitant class
# GitHub : https://github.com/Dhruv267/Project_2


class FieldInhabitant:

    # Defining Constructor
    def __init__(self, inhabitant):
        """
        constructor for FieldInhabitant class
        : param inhabitant : The symbol to represent the field inhabitant
        : type inhabitant : String
        """
        # protected variable to store symbol
        self._symbol = inhabitant 

    # Defining Getter Method
    def getSymbol(self):
        """
        getter method for the symbol of the field inhabitant
        : return : A string symbol representing the field inhabitant.
        """
        return self._symbol

    # Defining Setter Method
    def setSymbol(self, inhabitant):
        """
        setter method to update symbol of the field inhabitant.
        : param inhabitant : The new symbol to set.
        : type inhabitant : String
        """
        self._symbol = inhabitant

