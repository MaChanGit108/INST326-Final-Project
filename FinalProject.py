#!/usr/bin/env python3
# Final Project
# INST326
# Matthew Chan, Biniyam Assefa, Eymen Yagar, Frazer Workneh

import random
# from random(file name w/out .py) import *

move_inputs = "12345q"

class Player():
    def __init__(self, name):
        # Set health to 100
        self.health = 100
        # Set attack to random integer between 1 and 20
        self.attack = random.randint(1,20)
        # Starting position is 0
        self.pos = 0
        # Starting kills is 0
        self.kills = 0

    # Player attack method against target
    def attacks(self, target):
        # Target's health is subtracted by attack of Soldier
        target.health -= self.attack

    # Player drink method of potion
    def drink(self, target):
        # Add and set potion of either add or subtract 25 health from player
        # health
        self.health += target.healtheffect
        # If new added health is greater than max health
        if self.health > self.maxhealth:
            # Set max health to player health
            self.health = self.maxhealth

    # Player display stats of health, position, and kills
    def display_stats(self):
        print("Player health {}, position {}, kills {} ".format(self.health,
        self.pos, self.kills))
        print("")

# Knight Class subclass of Player
class Knight(Player):
    def __init__(self, name):
        #Stats of the knight class.
        self.health = 150
        self.maxhealth = 150
        self.attack = 100
        self.name = name
        super(Player, self)

# Potential future feature to be added
#    def sword_and_shield(self):
        #15% chance of not getting any damage

# Archer Class subclass of Player
class Archer(Player):
    def __init__(self, name):
        #Stats of the archer class.
        self.health = 120
        self.maxhealth = 120
        self.attack = 75
        self.name = name

# Potential future feature to be added
#    def longbow(self):
        #3 attacks, 40% decrease of hitting per turn (1st: 100%, 2nd:70% 3rd:40%)

# Wizard Class subclass of Player
class Wizard(Player):
    def __init__(self, name):
        #Stats of the wizard class.
        self.health = 50
        self.maxhealth = 50
        self.attack = 150
        self.name = name

# Potential future feature to be added
#    def ancient_staff(self):
        #When health below 10%, 50% chance of one-hit kill

# Parent class Enemy
class Enemy():
    # Attack method subtracting enemy attack on player
    def attacks(self, target):
        target.health -= self.attack
    # Display enemy encountered
    def display_enemy(self):
        print("")
        print("You've encountered a {}".format(self))

# Goblin class subclass of Enemy
class Goblin(Enemy):
    def __init__(self):
        self.health = 100
        # Random attack damage between 1 and 5
        self.attack = random.randint(1,5)
    def __repr__(self):
        return "Goblin"

# Troll class subclass of Enemy
class Troll(Enemy):
    def __init__(self):
        self.health = 200
        # Random attack damage between 1 and 15
        self.attack = random.randint(1,15)
    def __repr__(self):
        return "Troll"

# GoblinKing class subclass of Enemy
class GoblinKing(Enemy):
    def __init__(self):
        self.health = 300
        # Random attack damage between 1 and 30
        self.attack = random.randint(1,30)
    def __repr__(self):
        return "GoblinKing"

# Treasure class of healing
class Treasure():
    def __init__(self):
        self.healtheffect = 25

# PoisonTreasure subclass of Treasure of poison
class PoisonTreasure(Treasure):
    def __init__(self):
        self.healtheffect = -25

# Map of empty list
map = []

# Creation of map, setting random items, enemies, and spaces within 100 spaces
for x in range(100):
    choice = random.randint(1, 10)
    if choice < 6:
        map.append(None)
    elif choice < 7:
        map.append(Treasure())
    elif choice < 8:
        map.append(Goblin())
    elif choice < 9:
        map.append(Troll())
    elif choice < 10:
        map.append(GoblinKing())
    else:
        map.append(PoisonTreasure())

# Creation of Player, input name, choosing b/w knight, archer, or wizard
def generate_Player():
    player_name = input("Enter your name: ")
    print("Your name is {}.".format(player_name))
    player_class = input("Chose your class: Knight, Archer, Wizard: ")
    if player_class == 'Knight':
        p = Knight(player_name)
        print("")
        print("You are now Sir Knight {}.".format(player_name))
        print("Now escape the dungeon or face your doom!")
        print("")
    elif player_class == 'Archer':
        p = Archer(player_name)
        print("")
        print("You are now infamous Archer {}.".format(player_name))
        print("Now escape the dungeon or face your doom!")
        print("")
    elif player_class == 'Wizard':
        p = Wizard(player_name)
        print("")
        print("You are now magical Wizard {}.".format(player_name))
        print("Now escape the dungeon or face your doom!")
        print("")
    p.pos = 0
    p.kills = 0
    return p

# Fight function of fighting between Player and Enemy encountered
def fight(p, e):
    # Display enemy encountered
    e.display_enemy()
    while p.health > 0 and e.health > 0:
        p.attacks(e)
        e.attacks(p)
    # If Player health greater than 0 after fight, Player wins
    if p.health > 0:
        return 'win'
    # Else, Player loses fight
    else:
        print("Player loses fight!")
        return 'lose'

def main():

    p = generate_Player()

    while True:
        user_input = input(
        'Player Position: {}, Enter steps to move (b/w 1 to 5) or q to quit: '
        .format(p.pos))
        # Check if user entered 1 to 5 or q
        while user_input not in move_inputs:
            user_input = input('You must enter 1 to 5 or q: ')
        # Quit game if Player entered q before game ended
        if user_input == 'q':
            print("")
            print("You gave up and took the easy way out...")
            break
        else:
            # Player position increases based on Player input
            p.pos += int(user_input)
            # Try/except set thing_encountered to map position or exit if
            # outside index
            try:
                thing_encountered = map[p.pos]
            except IndexError:
                break
            # If thing_encountered is nothing or empty, continue asking input
            if thing_encountered == None:
                print("")
                print("We must press forward and escape. Onward!")
                continue
            # If thing_encountered is a subclass of Enemy
            elif issubclass(type(thing_encountered), Enemy):
                # Result of fight
                result = fight(p, thing_encountered)
                # If Player won, display Player stats and continue
                if result == 'win':
                    print("Player wins fight!")
                    p.kills += 1
                    p.display_stats()
                else:
                    #If lost fight
                    break
            # If thing_encountered is a Treasure
            elif type(thing_encountered) == Treasure() or issubclass(
                                            type(thing_encountered), Treasure):
                print("You found a potion!")
                # Drink potion and display Player stats
                p.drink(thing_encountered)
                p.display_stats()
    # If Player health is greater than 0 and Player position is greater than 100
    # Player has won!
    if p.health > 0 and (p.pos >= 100):
        print("")
        print("You have escaped the dungeon! You win!!!")
        print("You escaped with {} health left and had {} kills!"
        .format(p.health, p.kills))
    # If Player health is less than 0, Player has lost
    elif p.health <= 0:
        print("")
        print("You died at position {}, better luck in the afterlife."
        .format(p.pos))
    # If Player quit game before game ended, display current Player position and
    # number of kills
    else:
        print("")
        print("You moved {} steps and killed {} monsters."
        .format(p.pos, p.kills))

if __name__ == '__main__':
  main()
