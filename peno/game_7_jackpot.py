from math import comb
from random import randint
from tables import load_pay_table
from utils import print_winnings
from utils import print_game_odds
from utils import odds
from utils import total_comb
from utils import pick
from utils import divide_chunks

def game_7_jackpot(games):
    """
    This is a combo game, 6 3 number groups and one 2 number group.
    Total of 20 numbers. Odds:

        > 7 out of 20: 11.33%
        > 3 out of 20: 1.39%, but we have 6 groups, 6 x 1.39 = 8.34
        > 2 out of 20: 6.01% 
    """
    jackpots = 0
    winnings = 0
    cost = 0

    for game in range(1,games+1):
        # >>> comb(6,2) 15
        # we have 6 groups of 3 and we need 2 of them
        # we have 1 group of 2
        # only 15 ways to make 7
        cost+= 15
        played = pick(20)
        picked = pick(20)

        # now we need to make 6 groups of 3
        # NOTE: need to convert generator into a list
        three_groups = list(divide_chunks(played, 3))
        # should be a total of 7 internal arrays
        # print('picked: ' + str(picked))
        # print('played: ' + str(played))
        # print('groups: ' + str(three_groups))

        caught_3_1 = 0;
        caught_3_2 = 0;
        caught_3_3 = 0;
        caught_3_4 = 0;
        caught_3_5 = 0;
        caught_3_6 = 0;
        caught_2 = 0;

        for play in played:
            if play in picked:
                if play in three_groups[0]:
                    caught_3_1+= 1
                if play in three_groups[1]:
                    caught_3_2+= 1
                if play in three_groups[2]:
                    caught_3_3+= 1
                if play in three_groups[3]:
                    caught_3_4+= 1
                if play in three_groups[4]:
                    caught_3_5+= 1
                if play in three_groups[5]:
                    caught_3_6+= 1
                if play in three_groups[6]:
                    caught_2+= 1

        # print('--------------------------------------')
        # print('caught_3_1:' + str(caught_3_1))
        # print('caught_3_2:' + str(caught_3_2))
        # print('caught_3_3:' + str(caught_3_3))
        # print('caught_3_4:' + str(caught_3_4))
        # print('caught_3_5:' + str(caught_3_5))
        # print('caught_3_6:' + str(caught_3_6))
        # print('caught_2:' + str(caught_2))

        total_full_three_groups = 0 ; 
        total_full_two_groups = 0 ; 

        if caught_3_1 == 3:
            total_full_three_groups+= 1;
        if caught_3_2 == 3:
            total_full_three_groups+= 1;
        if caught_3_3 == 3:
            total_full_three_groups+= 1;
        if caught_3_4 == 3:
            total_full_three_groups+= 1;
        if caught_3_5 == 3:
            total_full_three_groups+= 1;
        if caught_3_6 == 3:
            total_full_three_groups+= 1;

        if caught_2 == 2:
            total_full_two_groups+= 1;

        # print('------------------------')
        # print('full 3 goups:' + str(total_full_three_groups))
        # print('full 2 goups:' + str(total_full_two_groups))
        # print('------------------------')

        if total_full_three_groups > 1 and total_full_two_groups > 0:
            jackpots+= 1
            winnings+= 5000
            print('===========================================')
            print('====       JACKPOT WON ! ! !         ======')
            print('===========================================')

    print('--------------------------------------')
    print('total games played:' + str(games))
    print('total cost:' + str(cost))
    print('total jackpots:' + str(jackpots))
    print('total winnings:' + str(winnings))
    print('total proffit:' + str(winnings - cost))
    print('pay ratio:' + str(winnings / cost))
