from helper import is_valid_pos, form_words, make_alphabet, count_points, make_bonus_board
from stack import Stack
from board import Board
from letter import Letter
import random


def place_letter(let, play, brd, pos, action_log):
    play.rm_letter(let)
    brd.add_letter(let, pos)
    action_log.append(pos)


def draw_letter(bag, play):
    if bag:
        let = bag.pop(random.randint(0, len(bag) - 1))
        play.add_letter(let)


def determine_words(brd, action_log):
    hor_explored = dict()
    ver_explored = dict()
    hor_directions = {"w": (0, -1), "e": (0, 1)}
    ver_directions = {"n": (-1, 0), "s": (1, 0)}
    s = Stack()

    def explore_horizontally(pos):
        for hdir in hor_directions:
            new_pos = (pos[0] + hor_directions[hdir][0], pos[1] + hor_directions[hdir][1])
            if is_valid_pos(new_pos) and new_pos not in hor_explored and not brd.is_free(new_pos):
                hor_explored[new_pos] = pos
                s.push(new_pos)

    def explore_vertically(pos):
        for vdir in ver_directions:
            new_pos = (pos[0] + ver_directions[vdir][0], pos[1] + ver_directions[vdir][1])
            if is_valid_pos(new_pos) and new_pos not in ver_explored and not brd.is_free(new_pos):
                ver_explored[new_pos] = pos
                s.push(new_pos)

    for el in action_log:
        s.push(el)
    while not s.is_empty():
        pos = s.pop()
        if pos in action_log:
            if pos not in hor_explored:
                hor_explored[pos] = None
            explore_horizontally(pos)
            if pos not in ver_explored:
                ver_explored[pos] = None
            explore_vertically(pos)
        if pos not in action_log:
            if pos in hor_explored:
                explore_horizontally(pos)
            elif pos in ver_explored:
                explore_vertically(pos)
    words = form_words(hor_explored) + form_words(ver_explored)
    return words


if __name__ == "__main__":
    brd = Board()
    alphabet = make_alphabet()
    letter_bonus_board = make_bonus_board("bonus_letter.txt")
    word_bonus_board = make_bonus_board("bonus_word.txt")


    def get_letter_index(let):
        return ord(let) - 97


    brd.add_letter(alphabet[get_letter_index("c")], (0, 1))
    brd.add_letter(alphabet[get_letter_index("a")], (1, 1))
    brd.add_letter(alphabet[get_letter_index("d")], (2, 1))
    brd.add_letter(alphabet[get_letter_index("e")], (3, 1))
    brd.add_letter(alphabet[get_letter_index("d")], (1, 0))
    brd.add_letter(alphabet[get_letter_index("c")], (1, 2))
    brd.add_letter(alphabet[get_letter_index("e")], (1, 3))

    assert brd.is_free((0, 0))
    assert not brd.is_free((3, 1))

    action_log = [(0, 1), (2, 1), (3, 1)]
    words = determine_words(brd, action_log)
    assert words == [[(3, 1), (2, 1), (1, 1), (0, 1)]]

    pts = count_points(words, brd, letter_bonus_board, word_bonus_board)
    assert pts == 14
