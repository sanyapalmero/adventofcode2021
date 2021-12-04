from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def parse_input(input_txt):
    """Парсит данные из файла и возвращает список чисел и список досок"""
    input_txt = input_txt.splitlines()
    first_row = input_txt[0].split(",")
    random_order = [int(num) for num in first_row]

    boards = []
    board = []
    for line in input_txt[2:]:
        splitted_line = [[int(num), False] for num in line.split()]

        if len(splitted_line) == 0:
            boards.append(board)
            board = []
            continue

        board.append(splitted_line)

    boards.append(board)
    return random_order, boards


def check_number_in_board(number, board):
    """Ищет число на доске и отмечает его, если оно найдено"""
    for row in board:
        for elem in row:
            if elem[0] == number:
                elem[1] = True
    return board


def check_all_true_in_board_row(board):
    """Проверяет кажду строку доски и возвращает True, если все числа отмечены"""
    for row in board:
        is_all_true_in_row = True
        for elem in row:
            if not elem[1]:
                is_all_true_in_row = False
        if is_all_true_in_row:
            return True
    return False


def is_board_is_winner(board):
    """
    Проверяет, является ли доска победной
    (в строке или столбце доски все числа отмечены)
    """
    is_board_has_winner_row = check_all_true_in_board_row(board)
    if is_board_has_winner_row:
        return True

    transposed_board = list(zip(*board))
    is_board_has_winner_column = check_all_true_in_board_row(transposed_board)
    if is_board_has_winner_column:
        return True

    return False


def find_first_win_board_with_last_number(random_order, boards):
    """
    Находит первую победную доску и возвращает её вместе с чем числом,
    с которым эта доска стала победной
    """
    for number in random_order:
        for board in boards:
            board = check_number_in_board(number, board)
            if is_board_is_winner(board):
                return board, number


def find_last_win_board_with_last_number(random_order, boards):
    """
    Находит последнюю победную доску и возвращает ее вместе с чем числом,
    с которым эта строка стала победной
    """
    boards_count = len(boards)
    winner_boards_count = 0
    boards_with_win_status = [[board, False] for board in boards]
    for number in random_order:
        for idx, board_elem in enumerate(boards_with_win_status):
            board, win_status = board_elem
            board = check_number_in_board(number, board)
            if not win_status and is_board_is_winner(board):
                boards_with_win_status[idx] = [board, True]
                winner_boards_count += 1
                if winner_boards_count == boards_count:
                    return board, number


def find_sum_of_unmarked_nums(board):
    """Находит сумму неотмеченных чисел на доске"""
    sum_of_unmarked_nums = 0
    for row in board:
        for elem in row:
            number, is_marked = elem
            if not is_marked:
                sum_of_unmarked_nums += number
    return sum_of_unmarked_nums


def part_1(input_txt):
    random_order, boards = parse_input(input_txt)
    board, number = find_first_win_board_with_last_number(random_order, boards)
    sum_of_unmarked_nums = find_sum_of_unmarked_nums(board)
    return number * sum_of_unmarked_nums


def part_2(input_txt):
    random_order, boards = parse_input(input_txt)
    board, number = find_last_win_board_with_last_number(random_order, boards)
    sum_of_unmarked_nums = find_sum_of_unmarked_nums(board)
    return number * sum_of_unmarked_nums


def main():
    input_txt = (BASE_DIR / "input.txt").read_text()

    res_1 = part_1(input_txt)
    print(res_1)

    res_2 = part_2(input_txt)
    print(res_2)


if __name__ == "__main__":
    main()
