import zombiedice
import random
import sys

"""
In order to make this module work:

- install zombiedice with: pip install zombiedice

- run this script

"""

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:

        """
        BotSelector
        
        Index of bot algorythms. set the variable BotSelection with the correspondent number.
        
        1. after the first roll, randomly decides if it will continue or stop
        2. stops rolling after it has rolled two brains
        3. stops rolling after it has rolled two shotguns
        4. initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
        5. A bot that stops rolling after it has rolled more shotguns than brains
        """
        
        botSelector = 5
        
        brains = 0

        if botSelector == 1:
            # Bot 1: 
            # after the first roll, randomly decides if it will continue or stop

            while diceRollResults is not None: 

                brains += diceRollResults['brains']

                play = random.randint(0, 1)

                if play == 0:
                    print("Keep playing one more time...")
                    diceRollResults = zombiedice.roll() # roll again

                else:
                    print("Stop playing.")
                    break

        elif botSelector == 2:
            # Bot 2: 
            # stops rolling after it has rolled two brains

            while diceRollResults is not None: 

                brains += diceRollResults['brains']

                if brains < 2:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break

        elif botSelector == 3:

            # Bot 3
            # stops rolling after it has rolled two shotguns

            while diceRollResults is not None:
                brains += diceRollResults['brains']

                if diceRollResults['shotgun'] == 2:
                    break
                else:
                    diceRollResults = zombiedice.roll() # roll again


        elif botSelector == 4:

            #Bot 4
            #initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns

            rolls = random.randint(1,4) # set how many times will roll

            while diceRollResults is not None:
                brains += diceRollResults['brains']

                if diceRollResults['shotgun'] == 2:
                    break
                
                if rolls > 0:
                    diceRollResults = zombiedice.roll() # roll again
                    rolls -= 1
                    
                else:
                    break


        elif botSelector == 5:

            #Bot 5
            # A bot that stops rolling after it has rolled more shotguns than brains

            while diceRollResults is not None:
                brains += diceRollResults['brains']

                if diceRollResults['shotgun'] > diceRollResults['brains']:
                    break
                else:
                    diceRollResults = zombiedice.roll() # roll again

        else:
            print('botSelector is not set properly.')
            sys.exit()
            

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1Shotgun', minShotguns=1),
    MyZombie(name='Zombot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=100)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)