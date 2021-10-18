from stack import Stack
from letter import Letter


def make_alphabet():
    alphabet = []
    f = open("alphabet.txt", "r")
    for line in f:
        lst = line.split()
        alphabet.append(Letter(lst[0], int(lst[1]), int(lst[2])))
    f.close()
    return alphabet


def make_bag(alphabet):
    bag = []
    while alphabet:
        let = alphabet.pop()
        reps = let.get_amount0()
        for ii in range(reps):
            bag.append(let)
    return bag


def make_bonus_board(bonus_board_file):
    bonus_brd = []
    f = open(bonus_board_file, "r")
    for line in f:
        lst = line.split()
        row = []
        for num in lst:
            row.append(int(num))
        bonus_brd.append(row)
    return bonus_brd


def is_valid_pos(pos):
    row, col = pos
    if (not 0 <= row < 17) or (not 0 <= col < 17):
        return False
    else:
        return True


def form_words(explored_dict):
    words = []
    idx = dict()
    count = 0
    for key in explored_dict:
        if explored_dict[key] is None:
            words.append([key])
            idx[key] = count
            count += 1
    for key in explored_dict:
        if key not in idx:
            parent = key
            while True:
                parent = explored_dict[parent]
                if parent in idx:
                    words[idx[parent]].append(key)
                    break
    copy_list = words.copy()
    for word in copy_list:
        if len(word) == 1:
            words.remove(word)
    return words


def count_points(words, brd, letter_bonus_board, word_bonus_board):
    tot_points = 0
    for word in words:
        word_points = 0
        word_bonus = 1
        for pos in word:
            letter_bonus = letter_bonus_board[pos[0]][pos[1]]
            word_bonus *= word_bonus_board[pos[0]][pos[1]]
            word_points += brd.get_letter(pos).get_points() * letter_bonus
        word_points *= word_bonus
        tot_points += word_points
    return tot_points


if __name__ == "__main__":
    print(make_alphabet().pop())
    # print(make_bonus_board("bonus_word.txt"))
    # print(make_bonus_board("bonus_letter.txt"))

    exp_d = {(0, 1): None, (1, 1): (0, 1), (0, 3): None, (1, 3): (0, 3), (2, 3): (0, 3)}
    assert form_words(exp_d) == [[(0, 1), (1, 1)], [(0, 3), (1, 3), (2, 3)]]

    exp_d = {(0, 1): None, (1, 1): (0, 1), (0, 3): None, (1, 3): (0, 3), (2, 3): (1, 3)}
    assert form_words(exp_d) == [[(0, 1), (1, 1)], [(0, 3), (1, 3), (2, 3)]]

    exp_d = {(0, 1): None, (1, 1): (0, 1), (0, 3): None, (1, 3): (0, 3), (2, 3): (1, 3), (3, 3): None}
    assert form_words(exp_d) == [[(0, 1), (1, 1)], [(0, 3), (1, 3), (2, 3)]]
