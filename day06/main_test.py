from .main import part_1, part_2

input_txt = "3,4,3,1,2"


def test_part_1_18_days():
    assert part_1(input_txt, 18) == 26


def test_part_1_80_days():
    assert part_1(input_txt, 80) == 5934


def test_part_2():
    assert part_2(input_txt, 256) == 26984457539
