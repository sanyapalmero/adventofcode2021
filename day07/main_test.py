from .main import part_1, part_2

input_txt = "16,1,2,0,4,2,7,1,2,14"


def test_part_1():
    assert part_1(input_txt) == 37


def test_part_2():
    assert part_2(input_txt) == 168
