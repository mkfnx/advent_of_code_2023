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
    assert 12 == find_calibration_val("1abc2")
    assert 38 == find_calibration_val("pqr3stu8vwx")
    assert 15 == find_calibration_val("a1b2c3d4e5f")
    assert 77 == find_calibration_val("treb7uchet")


if __name__ == "__main__":
    # TODO: Create file reading functions (read as list)
    with open("input/in1.txt") as file:
        list_input = []

        for line in file:
            list_input.append(line)

        result = parse_calibration_doc(list_input)
        print(result)