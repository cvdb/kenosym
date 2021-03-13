from math import comb
from random import randint
from tables import load_pay_table
from utils import print_winnings
from utils import print_game_odds
from utils import odds
from utils import total_comb
from utils import pick
from utils import divide_chunks

def game_4_combo_1(games):
    """
    This is a 4 number game using combo of 1
    """
    winnings = 0
    cost = 0

    for game in range(1,games+1):
        cost+= 5
        played = pick(4)
        picked = pick(20)
        caught = 0;
        gamewon = 0;

        for play in played:
            if play in picked:
                caught+= 1

        if caught == 1:
           gamewon+= 3 # 1 X 1 number game
           #print('game:' + str(game) + ' caught 1, won:' + str(gamewon))

        if caught == 2:
           gamewon+= 6 # 2 X 1 number game 
           gamewon+= 1 # 4 number game 
           #print('game:' + str(game) + ' caught 2, won:' + str(gamewon))

        if caught == 3:
           gamewon+= 9 # 3 X 1 number game 
           gamewon+= 4 # 4 number game 
           #print('game:' + str(game) + ' caught 3, won:' + str(gamewon))

        if caught == 4:
           gamewon+= 12 # 4 X 1 number game
           gamewon+= 120 # 4 number game 
           print('game:' + str(game) + ' caught 4, won:' + str(gamewon))

        winnings+= gamewon

    print('--------------------------------------')
    print('total games played:' + str(games))
    print('total cost:' + str(cost))
    print('total winnings:' + str(winnings))
    print('total proffit:' + str(winnings - cost))
    print('pay ratio:' + str(winnings / cost))
