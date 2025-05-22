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
    player = Charicter(50 ,None,None , Class)
    print(player.Class)
    weapon = None
    if Class.lower() == 'barbarian':
        weapon = 'Great Sword'
    elif Class.lower() ==  'druid':
        weapon = 'fang dagger'
    print(f'you now have a {weapon}')
    return player
    #
def starting_gold(charicter_class):
    if charicter_class == 'druid' or 'barbarian':
        roll  = roll_dice(4) + roll_dice(4)
        amount = roll * 10
    if charicter_class == 'wizard' or 'warlock' or 'rouge':
        roll = roll_dice(4) + roll_dice(4) + roll_dice(4) + roll_dice(4) 
        amount = roll * 10

    print(f'you roll for starting gold. You roll a {roll} you get {amount} GP')
    return int(amount)




if __name__ == '__main__':  
    charicter_creation()
