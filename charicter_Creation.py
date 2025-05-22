from damage_system import *
class Charicter:
    def __init__(self, Health, Defence = 0 , Level = 1, Class = None):
        self.health =  Health
        self.Defence = Defence
        self.Level = Level
        self.Class = Class
        return 
def  charicter_creation():
    Class = input('What class do you want to be out of this list\nBarbarian\nDruid\nEnter your desision: ')
    player = Charicter(50,None,None ,Class)
    
    if Class.lower() == 'barbarian':
        weapon = 'Great Sword'
    if Class.lower() ==  'druid':
        weapon = 'scimitar'
    print(f'you now have a {weapon}')
    print(f'you roll for starting gold. You roll a {roll_dice(20)}')
if __name__ == '__main__':
    Player = Charicter(50,None,None,'Barbarian')
    print(Player.Class)
    if Player.Class == 'Barbarian':
        print('yes')
