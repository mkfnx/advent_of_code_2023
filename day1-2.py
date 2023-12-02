def parse_calibration_doc(doc):
    calibration_vals_sum = 0
    for amended_val in doc:
        calibration_vals_sum += find_calibration_val(amended_val)
    return calibration_vals_sum


def find_calibration_val(amended_val):
    fd = ''
    ld = ''

    for c in amended_val:
        if c.isdigit():
            fd = c
            break

    for i in range(len(amended_val) - 1, -1, -1):
        c = amended_val[i]
        if c.isdigit():
            ld = c
            break

    return int(fd + ld)


###
###
###


def test_parse_calibration_doc():
    doc = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    assert 142 == parse_calibration_doc(doc)


def test_find_calibration():
    assert 29 == find_calibration_val("two1nine")
    assert 83 == find_calibration_val("eightwothree")
    assert 13 == find_calibration_val("abcone2threexyz")
    assert 24 == find_calibration_val("xtwone3four")
    assert 42 == find_calibration_val("4nineeightseven2")
    assert 14 == find_calibration_val("zoneight234")
    assert 76 == find_calibration_val("7pqrstsixteen")


if __name__ == "__main__":
    # TODO: Create file reading functions (read as list)
    with open("input/in1.txt") as file:
        list_input = []

        for line in file:
            list_input.append(line)

        result = parse_calibration_doc(list_input)
        print(result)
