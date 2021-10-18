from stack import Stack
from letter import Letter
from board import Board
from player import Player
from helper import make_alphabet, make_bonus_board, is_valid_pos, form_words, count_points, make_bag
from actions import place_letter, determine_words, draw_letter
import random


def makePlayers(num_players, names):
    players = []
    for ii in range(num_players):
        name = names[ii]
        players.append(Player(name))
    return players

def initialize():
    brd = Board()
    alphabet = make_alphabet()
    bag = make_bag(alphabet)
    letter_bonus_board = make_bonus_board("bonus_letter.txt")
    word_bonus_board = make_bonus_board("bonus_word.txt")
    return bag, brd, letter_bonus_board, word_bonus_board

def order_and_draw(players, bag):
    random.shuffle(players)
    for p in players:
        while p.get_num_letters() < 8 and bag:
            draw_letter(bag, p)

if __name__ == "__main__":
    brd = Board()
    alphabet = make_alphabet()
    bag = make_bag(alphabet)
    letter_bonus_board = make_bonus_board("bonus_letter.txt")
    word_bonus_board = make_bonus_board("bonus_word.txt")

    num_players = int(input("Enter number of players (2-4): "))
    players = []
    for ii in range(num_players):
        name = input("Enter name of player " + str(ii+1) + ": ")
        players.append(Player(name))

    # shuffle list to determine game order
    random.shuffle(players)
    for p in players:
        while p.get_num_letters() < 8 and bag:
            draw_letter(bag, p)

    is_game_finished = False
    closing_player_idx = None

    while not is_game_finished:
        for p, idx in zip(players, range(len(players))):
            action_log = []
            is_done = False
            while not is_done:
                my_letters = p.see_letters()
                print(p.name + "'s letters:")
                for my_let, ii in zip(my_letters, range(len(my_letters))):
                    print(str(ii) + ": " + str(my_let))
                print(brd)
                move = input("letter_idx row col - press q to stop - press u to undo: ")
                if move == "q":
                    is_done = True
                elif move == "u":
                    if action_log:
                        pos = action_log.pop()
                        let = brd.get_letter(pos)
                        brd.rm_letter(pos)
                        p.add_letter(let)
                else:
                    cmd = move.split()
                    let = my_letters[int(cmd[0])]
                    pos = (int(cmd[1]), int(cmd[2]))
                    place_letter(let, p, brd, pos, action_log)
            words = determine_words(brd, action_log)
            pts = count_points(words, brd, letter_bonus_board, word_bonus_board)
            print("\n" + p.name + " scored " + str(pts) + " points\n")
            p.add_points(pts)
            if (not bag) and (not p.get_num_letters()):
                is_game_finished = True
                closing_player_idx = idx
            else:
                while p.get_num_letters() < 8 and bag:
                    draw_letter(bag, p)

    bonus = 0
    for p in players:
        penalty = 0
        remaining_letters = p.see_letters()
        for let in remaining_letters:
            penalty += let.get_points()
            bonus += let.get_points()
        p.add_points(-penalty)

    players[closing_player_idx].add_points(bonus)

    win_points = 0
    winner = None
    for p in players:
        if p.points > win_points:
            win_points = p.points
            winner = p.name

    print("The winner is " + winner)
