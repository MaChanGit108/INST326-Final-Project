'''
Name: Biniyam Assefa
Directory ID: 115318656
Date: 2019-04-01
Assignment: Homework 3
'''

def main():


    class RPG:

            #The attributes below are metadata about a player's character. Health and Below are all nominal values ranging from 0 -1000
        def __init__(self, first, last, health, attack):
            self.first = first
            self.last = last
            self.health = health
            self.attack = attack
            '''
            self.speed = speed
            self.stamina = stamina
            self.magic = magic
            self.magical_defense = magical_defense
            self.perception = perceptiion
            '''
            # Creates a combined name for the player
        def player_name(self):
            return '{} {}'.format(self.first, self.last)

    #Creates a subclass of player
    class Knight(RPG):
        def __init__(self, first, last, health, attack, speed, stamina, magic, magical_defense, perception, weapons_arsenal=None):
            #Inherits the characteristics of the RPG class
            super().__init__(first, last, health, attack, speed, stamina, magic, magical_defense, perception)
            #Stats of the knight class.
            self.attack = 100
            self.health = 100


        def sword_and_shield(self):
            #15% chance of not getting any damage

    class Archer(RPG):
        def __init__(self, first, last, health, attack, speed, stamina, magic, magical_defense, perception, weapons_arsenal=None):
            #Inherits the characteristics of the RPG class
            super().__init__(first, last, health, attack, speed, stamina, magic, magical_defense, perception)
            #Stats of the archer class.
            self.attack = 75
            self.health = 120


        def longbow(self):
            #3 attacks, 40% decrease of hitting per turn (1st: 100%, 2nd:70% 3rd:40%)

    class Wizard(RPG):
        def __init__(self, first, last, health, attack, speed, stamina, magic, magical_defense, perception, weapons_arsenal=None):
            #Inherits the characteristics of the RPG class
            super().__init__(first, last, health, attack, speed, stamina, magic, magical_defense, perception)
            #Stats of the wizard class.
            self.health = 50
            self.attack = 150


        def ancient_staff(self):
            #When health below 10%, 50% chance of one-hit kill


if __name__ == '__main__':
    main()
