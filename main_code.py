import time as t
player_class =  None
player_level = 1
choice = None
base_goblin_health = 10
sof = input('Do you want the text to go slow or fast: ')

def punch(level, enemey_health):
    damage_delt = level*2.5
    enemey_health =  enemey_health - damage_delt
    return enemey_health, damage_delt
if 'f' in sof:

    def slowprint(text):
        if '. . .' in text:
            for char in text:
                if char == '.':
                    print(char, end = '')
                    t.sleep(0.5)
                else:
                    print(char, end = '')
                    t.sleep(.11)
        else:
            for char in text:
                print(char, end = '')
            t.sleep(0.11)
        print()
else:
    def slowprint(text):
        print(text)
def classslect():
    slowprint('What class do you want: ')
    player_class = input()
    return player_class
def starter_quest():
    slowprint('Bartender: Hello their, I have a quest for you if your willing to take it (y/n): ')
    choice = input()
    if 'y' in choice:
        slowprint('Thank you so much, there are some goblins out side the bar you might have seen them can you get rid of them (y/n)?')
        choice = input()
        if 'y' in choice:
            slowprint('Quest accepted')
            slowprint('you walk outside')
            slowprint('You encounter a goblin what do you do (attack, or run)? ')
            choice = input()
            if 'a' in choice:
                slowprint('You throw a punch at the goblin . . .')
                enemey_health, damage_delt = punch(player_level, base_goblin_health)
                slowprint("you did " + str(damage_delt)+" damage they now have "+str(enemey_health))
                slowprint('Do you want to attack again or run away? ')
                choice = input()
    return print()

def main():
    starter_quest()
    while player_level <= 5:
        if player_level == 5:
            player_class = classslect()
    
    
    return
main()

