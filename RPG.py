from charicter_Creation import *
from damage_system import * 
#tell the mean of the data
roll = None
def main():
    player = charicter_creation()
    i = 0
    l = 0
    h = 0
    total = 0
    while i < 100000000:
        amount = starting_gold(player.Class)
        total += amount
        

        if amount > h:
            h =  amount
        elif amount < l:
            l = amount
        i += 1
    mean = total / 100000000
    print(mean)
    


     
if __name__ == '__main__':
    main()



