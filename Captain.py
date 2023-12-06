# author : Dhruv Parmar, Vindhya Umesh, Anita Ershadi
# Date : 12/02/2023
# Description : Implementation of Captain class
# GitHub : https://github.com/Dhruv267/Project_2

from Creature import Creature

# defining Captain class
class Captain(Creature):

    # defining constructor method for captain class
    def __init__(self, x, y):
        """
        constructor for Captain class
        : param x : x-coordinate of the captain in the beggining of the game
        : type x : integer
        : param y : y-coordinate of the captain in the beggining of the game
        : type y : integer
        """
        # calling constructor method of super class and passing 'V' as the symbol for the veggie captain
        super().__init__(x, y, 'V')  

        # protected variable to store list of veggies collected by captain
        self._collected_veggies = []

    # defining method to add veggies in collected_veggies list
    def addVeggie(self, veggie):
        """
        add a Veggie object to the list of collected veggies
        : param veggie : Veggie object to add to the collection
        : type veggie : Object
        """
        self._collected_veggies.append(veggie)

    # defining getter method to return veggie list
    def getCollectedVeggies(self):
        """
        getter method for the list of collected veggies
        : return : list
        """
        return self._collected_veggies
    
    # defining a function to remove last added 5 vegetables from Captain's bucket
    def loseLastFiveVeggies(self):
        """
        function to remove last added 5 vegetables from Captain's bucket
        : return : None
        """
        if len(self._collected_veggies) >= 5:
            # get the last five vegetables
            lost_veggies = self._collected_veggies[-5:]
            print(f"Snake Bite! The captain lost : {', '.join([veggie.getName() for veggie in lost_veggies])}")

            # update vegetable list
            self._collected_veggies = self._collected_veggies[:-5]

        else:
            # captain looses all veggies
            lost_veggies = self._collected_veggies
            self._collected_veggies = []
            print(f"Snake Bite! The captain lost : {', '.join([veggie.getName() for veggie in lost_veggies])}")


