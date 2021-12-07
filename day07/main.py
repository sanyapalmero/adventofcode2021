from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def part_1(input_txt):
    initial_positions = [int(num) for num in input_txt.strip().split(",")]
    initial_positions.sort()
    center_position = initial_positions[len(initial_positions) // 2]

    total_fuel = 0
    for pos in initial_positions:
        total_fuel += abs(pos - center_position)

    return total_fuel


def part_2(input_txt):
    initial_positions = [int(num) for num in input_txt.strip().split(",")]

    possible_fuel_costs = []
    min_pos = min(initial_positions)
    max_pos = max(initial_positions)
    for possible_position in range(min_pos, max_pos + 1):
        total_fuel = 0
        for crab_position in initial_positions:
            for i in range(abs(crab_position - possible_position)):
                total_fuel += i + 1
        possible_fuel_costs.append(total_fuel)

    return min(possible_fuel_costs)


def main():
    input_txt = (BASE_DIR / "input.txt").read_text()

    res_1 = part_1(input_txt)
    print(res_1)

    res_2 = part_2(input_txt)
    print(res_2)


if __name__ == "__main__":
    main()
