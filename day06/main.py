from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


@dataclass
class Lanternfish:
    days_left_to_create_new_lanternfish: int
    previous_timer_value: int = None
    reset_timer_value: int = 6
    new_timer_value: int = 8
    is_new_fish: bool = False
    day_from_continue_simulation: int = None

    def create_new_lanternfish(self) -> "Lanternfish":
        return Lanternfish(days_left_to_create_new_lanternfish=self.new_timer_value, is_new_fish=True)

    def reset_timer(self):
        self.days_left_to_create_new_lanternfish = self.reset_timer_value

    def decrement_1_day(self):
        if not self.is_new_fish:
            self.days_left_to_create_new_lanternfish -= 1

    def remember_current_timer(self):
        self.previous_timer_value = self.days_left_to_create_new_lanternfish

    def simulate_day(self):
        self.remember_current_timer()
        self.decrement_1_day()

        if self.previous_timer_value == 0:
            self.reset_timer()
            new_lanternfish = self.create_new_lanternfish()
            return new_lanternfish

        return None

    def make_not_new(self):
        self.is_new_fish = False


@dataclass
class LanternfishState:
    fishes: list[Lanternfish]

    def make_all_fishes_not_new(self):
        for fish in self.fishes:
            fish.is_new_fish = False

    @property
    def fishes_count(self):
        return len(self.fishes)

    @property
    def current_state(self):
        return [fish.days_left_to_create_new_lanternfish for fish in self.fishes]


def create_lanternfish_state(input_text) -> LanternfishState:
    nums = [int(num) for num in input_text.strip().split(",")]

    lanternfish_list = []
    for num in nums:
        lanternfish_list.append(Lanternfish(num))

    return LanternfishState(lanternfish_list)


def simulate_lanternfishes(lanternfish_state: LanternfishState, simulation_days: int) -> int:
    for _ in range(simulation_days):
        for fish in lanternfish_state.fishes:
            new_fish = fish.simulate_day()
            if new_fish:
                lanternfish_state.fishes.append(new_fish)
        lanternfish_state.make_all_fishes_not_new()
    return lanternfish_state.fishes_count


def simulate_lanternfishes_v2(lanternfish_state: LanternfishState, simulation_days: int) -> int:
    counters = {}
    for i in range(9):
        counters[i] = 0

    for fish in lanternfish_state.fishes:
        counters[fish.days_left_to_create_new_lanternfish] += 1

    for _ in range(simulation_days):
        fishes_with_zero_count = counters[0]
        for i in range(1, 9):
            counters[i - 1] = counters[i]
        counters[6] += fishes_with_zero_count
        counters[8] = fishes_with_zero_count

    fishes_count = 0
    for i in range(9):
        fishes_count += counters[i]

    return fishes_count


def part_1(input_txt, simulation_days):
    lanternfish_state = create_lanternfish_state(input_text=input_txt)
    fishes_count_after_simulation = simulate_lanternfishes_v2(lanternfish_state, simulation_days)
    return fishes_count_after_simulation


def part_2(input_txt, simulation_days):
    lanternfish_state = create_lanternfish_state(input_text=input_txt)
    fishes_count_after_simulation = simulate_lanternfishes_v2(lanternfish_state, simulation_days)
    return fishes_count_after_simulation


def main():
    input_txt = (BASE_DIR / "input.txt").read_text()

    simulation_days_part_1 = 80
    res_1 = part_1(input_txt, simulation_days_part_1)
    print(res_1)

    simulation_days_part_2 = 256
    res_2 = part_2(input_txt, simulation_days_part_2)
    print(res_2)


if __name__ == "__main__":
    main()
