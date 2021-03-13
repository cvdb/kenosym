import argparse
from math import comb
from random import randint
from tables import load_pay_table
from utils import print_winnings
from utils import print_game_odds
from utils import odds
from utils import total_comb
from utils import pick
from utils import divide_chunks
from combo_2 import combo_2
from game_4_combo_1 import game_4_combo_1
from game_5_combo_1 import game_5_combo_1
from game_10_combo_2 import game_10_combo_2
from game_7_jackpot import game_7_jackpot

def ProcessArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--picked', type=int, help='numbers picked')
    parser.add_argument('--caught', type=int, help='winning numbers')
    parser.add_argument('--games', type=int, help='number of games to play')
    parser.add_argument('--mode', help='[odds, winnings, combo_2_by_9]')
    return parser.parse_args()

if __name__ == '__main__':
    print('playing Keno...')
    pay_table = load_pay_table()
    args = ProcessArgs()

    if args.mode == 'odds':
        print('picked:{}, caught:{}'.format(args.picked, args.caught))
        print('odds:{}'.format(round(100*odds(args.picked, args.caught), 2)));
    elif args.mode == 'winnings':
        print_winnings()
    elif args.mode == 'game_odds':
        print_game_odds(args.picked)
    elif args.mode == 'combo_2':
        combo_2(args.picked)
        #combo_2_by_9()
    elif args.mode == 'play_game_4_combo_1':
        game_4_combo_1(args.games)
    elif args.mode == 'play_game_5_combo_1':
        game_5_combo_1(args.games)
    elif args.mode == 'play_game_10_combo_2':
        game_10_combo_2(args.games)
    elif args.mode == 'play_game_7_jackpot':
        game_7_jackpot(args.games)
    else:
        print('invalid mode:{}'.format(args.mode))

