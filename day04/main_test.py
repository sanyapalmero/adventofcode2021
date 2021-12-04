import copy

from .main import check_all_true_in_board_row, check_number_in_board, part_1, part_2

input_txt = (
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n"
    "\n"
    "22 13 17 11  0\n"
    " 8  2 23  4 24\n"
    "21  9 14 16  7\n"
    " 6 10  3 18  5\n"
    " 1 12 20 15 19\n"
    "\n"
    " 3 15  0  2 22\n"
    " 9 18 13 17  5\n"
    "19  8  7 25 23\n"
    "20 11 10 24  4\n"
    "14 21 16 12  6\n"
    "\n"
    "14 21 17 24  4\n"
    "10 16 15  9 19\n"
    "18  8 23 26 20\n"
    "22 11 13  6  5\n"
    " 2  0 12  3  7\n"
)


def test_part_1():
    assert part_1(input_txt) == 4512


def test_part_2():
    assert part_2(input_txt) == 1924


def test_check_number_in_board():
    board = [
        [[1, False], [2, False], [3, False], [4, False], [5, False]],
        [[6, False], [7, False], [8, False], [9, False], [10, False]],
        [[11, False], [12, False], [13, False], [14, False], [15, False]],
        [[16, False], [17, False], [18, False], [19, False], [20, False]],
        [[21, False], [22, False], [23, False], [24, False], [25, False]],
    ]

    board_2 = copy.deepcopy(board)

    assert check_number_in_board(13, board) == [
        [[1, False], [2, False], [3, False], [4, False], [5, False]],
        [[6, False], [7, False], [8, False], [9, False], [10, False]],
        [[11, False], [12, False], [13, True], [14, False], [15, False]],
        [[16, False], [17, False], [18, False], [19, False], [20, False]],
        [[21, False], [22, False], [23, False], [24, False], [25, False]],
    ]

    assert check_number_in_board(99, board_2) == [
        [[1, False], [2, False], [3, False], [4, False], [5, False]],
        [[6, False], [7, False], [8, False], [9, False], [10, False]],
        [[11, False], [12, False], [13, False], [14, False], [15, False]],
        [[16, False], [17, False], [18, False], [19, False], [20, False]],
        [[21, False], [22, False], [23, False], [24, False], [25, False]],
    ]


def test_check_all_true_in_board_row():
    board = [
        [[1, False], [2, True], [3, False], [4, False], [5, False]],
        [[6, True], [7, True], [8, True], [9, True], [10, True]],  # This row
        [[11, False], [12, False], [13, True], [14, False], [15, False]],
        [[16, False], [17, False], [18, False], [19, False], [20, False]],
        [[21, False], [22, False], [23, True], [24, False], [25, False]],
    ]

    assert check_all_true_in_board_row(board) is True

    board_2 = [
        [[1, True], [2, True], [3, False], [4, False], [5, False]],
        [[6, False], [7, True], [8, False], [9, False], [10, False]],
        [[11, False], [12, True], [13, True], [14, False], [15, False]],
        [[16, False], [17, True], [18, False], [19, False], [20, True]],
        [[21, False], [22, True], [23, False], [24, False], [25, False]],
    ]  # Second column has all True

    assert check_all_true_in_board_row(list(zip(*board_2))) is True
