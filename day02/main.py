COMMAND_UP = "up"
COMMAND_DOWN = "down"
COMMAND_FORWARD = "forward"


def get_data_from_file():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    return lines


def part_1():
    position, depth = (0, 0)

    lines = get_data_from_file()
    for line in lines:
        command, number = line.split()
        if command == COMMAND_FORWARD:
            position += int(number)
        elif command == COMMAND_DOWN:
            depth += int(number)
        elif command == COMMAND_UP:
            depth -= int(number)
    
    print(position * depth)


def part_2():
    position, depth, aim = (0, 0, 0)

    lines = get_data_from_file()
    for line in lines:
        command, number = line.split()
        if command == COMMAND_FORWARD:
            position += int(number)
            depth += aim * int(number)
        elif command == COMMAND_DOWN:
            aim += int(number)
        elif command == COMMAND_UP:
            aim -= int(number)
    
    print(position * depth)


def main():
    part_1()
    part_2()


main()
