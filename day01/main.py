def get_data_from_file():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    return lines


def find_increase(nums_list):
    increase_count = 0
    prev_number = int(nums_list[0])
    for line in nums_list:
        number = int(line)
        if prev_number < number:
            increase_count += 1
        prev_number = number
    return increase_count


def part_1():
    lines = get_data_from_file()
    increase_count = find_increase(lines)
    print(increase_count)


def part_2():
    lines = get_data_from_file()
    start_idx = 2
    sums_list = []

    while start_idx < len(lines):
        number_1 = int(lines[start_idx])
        number_2 = int(lines[start_idx - 1])
        number_3 = int(lines[start_idx - 2])
        sums_list.append(number_1 + number_2 + number_3)
        start_idx += 1

    increase_count = find_increase(sums_list)
    print(increase_count)


def main():
    part_1()
    part_2()


main()
