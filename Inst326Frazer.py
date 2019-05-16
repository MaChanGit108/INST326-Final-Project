#import player classes from ben
#import enemy classes from eymen

#backpack =	{"food": "bread", "weapon": "sword", "shield", "aid": "bandage"}
#items = {"food": "bread", "weapon": "sword", "shield", "aid": "bandage"}

#when player meets enemy
    #if player lands on same positional square as enemy
        #request input from player, attack or defend?
            #if player input equals attack
                #import attack class
                    #choose weapon accordingly
            #elif player input equals defend
                #import defend class
                    #choose weapon accordingly
    #else continue

#damage from weapon
    #if player is in attack
        #if enemy class is low-tier boss
            #deduct health item value of boss according to player class attack value
        #elif enemy class is mid-tier boss
            #deduct health item value of boss according to player class attack value
        #elif enemy class is high-tier boss
            #decuct health item value of boss according to player class attack value
    #elif player is in defense
        #if enemy class is low-tier boss
            #deduct health item value by 10
        #elif enemy class is mid-tier boss
            #deduct health item value by 25
        #elif enemy class is high-tier boss
            #decuct health item value by 50

#pick-up items
    #if player in same position as item
        #if length of backpack dictionary is less than ten
            #if item key is food in the item dictionary
                #append item to food key in backpack dictionary
            #if item key is weapon in the item dictionary
                #append item to weapon key in backpack dictionary
            #if item key is aid in the item dictionary
                #append item to aid key in backpack dictionary
        #if length of backpack dictionary is greater than or equal to ten
            #print not enough space
            #continue

