import random

while True:
    input()    #fake input to simulate user input
    roll = random.randint(1,6)
    print('You rolled dice and got : ',roll)
    if roll == 1:
        print('You Lose!')
        break
    elif roll == 6:
        print('You Win!')
        break
    else:
        print("Keep Rolling......")