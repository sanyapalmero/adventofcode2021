from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def part_1(input_txt):
    data = {}
    for i in range(len(input_txt[0])):
        data[i] = (0, 0)

    for line in input_txt:
        for idx, number in enumerate(line):
            zero_counter, one_counter = data[idx]
            if int(number) == 0:
                zero_counter += 1
            elif int(number) == 1:
                one_counter += 1
            data[idx] = (zero_counter, one_counter)
    
    gamma = ""
    epsilon = ""
    for i in range(len(input_txt[0])):
        zero_counter, one_counter = data[i]
        if zero_counter > one_counter:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    
    res = int(gamma, 2) * int(epsilon, 2)
    return res


def get_popular_bits(updated_list):
    data = {}
    for i in range(len(updated_list[0])):
        data[i] = (0, 0)

    for line in updated_list:
        for idx, number in enumerate(line):
            zero_counter, one_counter = data[idx]
            if int(number) == 0:
                zero_counter += 1
            elif int(number) == 1:
                one_counter += 1
            data[idx] = (zero_counter, one_counter)
    
    return data


def remove_strings_from_list(updated_list, start_value, number_position):
    tmp_list = []
    for line in updated_list:
        if start_value != line[number_position]:
            tmp_list.append(line)
    return tmp_list


def part_2(input_txt):
    nums_count = len(input_txt[0])

    oxy_tmp_list = list(input_txt)
    while len(oxy_tmp_list) > 1:
        for i in range(nums_count):
            bits = get_popular_bits(oxy_tmp_list)
            zero_counter, one_counter = bits[i]
            if zero_counter > one_counter:
                oxy_tmp_list = remove_strings_from_list(oxy_tmp_list, "1", i)
            elif zero_counter < one_counter or zero_counter == one_counter:
                oxy_tmp_list = remove_strings_from_list(oxy_tmp_list, "0", i)
            if len(oxy_tmp_list) == 1:
                break

    co2_tmp_list = list(input_txt)
    while len(co2_tmp_list) > 1:
        for i in range(nums_count):
            bits = get_popular_bits(co2_tmp_list)
            zero_counter, one_counter = bits[i]
            if zero_counter > one_counter:
                co2_tmp_list = remove_strings_from_list(co2_tmp_list, "0", i)
            elif zero_counter < one_counter or zero_counter == one_counter:
                co2_tmp_list = remove_strings_from_list(co2_tmp_list, "1", i)
            if len(co2_tmp_list) == 1:
                break

    res = int(oxy_tmp_list[0], 2) * int(co2_tmp_list[0], 2)
    return res


def main():
    input_txt = (BASE_DIR / "input.txt").read_text().splitlines()

    res_1 = part_1(input_txt)
    print(res_1)

    res_2 = part_2(input_txt)
    print(res_2)


if __name__ == "__main__":
    main()

