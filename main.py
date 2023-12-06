# author : Dhruv Parmar, Vindhya Umesh, Anita Ershadi
# Date : 12/02/2023
# Description : main function that combines all the elements of the game and run it
# GitHub : https://github.com/Dhruv267/Project_2

# import GameEngine Module
from GameEngine import GameEngine

# defining function that runs GameEngine
def main():
    # initialise gameEngine Object
    new_game = GameEngine()

    # initialize the game
    new_game.initializeGame()

    # display game introduction and rule sets
    new_game.intro()

    # get the initial number of remaining vegetables
    veggies_in_field = new_game.remainingVeggies()

    # loop till there remain no veggies in field
    while veggies_in_field > 0:
        # print game stats
        print(f"\n{veggies_in_field} veggies remaining. Current Score: {new_game.getScore()}")

        # print the field representation
        new_game.printField()

        # move the rabbits
        new_game.moveRabbits()

        # move Captain
        new_game.moveCaptain()

        # update the number of remaining vegetables in the field
        veggies_in_field = new_game.remainingVeggies()

        # move Snake
        new_game.moveSnake()

    # display game over info
    new_game.gameOver()

    # update and print high scores
    new_game.highScore()


main()
