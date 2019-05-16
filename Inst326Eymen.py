'''
Eymen Yagar
Final PRJ
326
'''

def main():

    class Bosses():
        def __init__(self, health, attack):
            self.attack = attack
            self.health = health


    Low_boss= Bosses(50,5)
    print(Low_boss.attack)
    print(Low_boss.health)

    Mid_boss=Bosses(100,10)
    print(Mid_boss.attack)
    print(Mid_boss.health)

    High_boss=Bosses(300,20)
    print(High_boss.attack)
    print(High_boss.health)

if __name__ == '__main__':
    main()
