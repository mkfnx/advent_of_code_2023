numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def parse_calibration_doc(doc):
    calibration_vals_sum = 0
    for val_line in doc:
        calibration_vals_sum += find_calibration_val(val_line)
    return calibration_vals_sum


def find_calibration_val(val_line):
    # use a set for storing digits and positions to avoid duplicates
    digits = set()

    # check all positions in the input line
    for i in range(len(val_line)):
        c = val_line[i]

        if c.isdigit():
            digits.add((i, c))
        else:
            # try to find each digit from current position i
            for k, v in numbers.items():
                di = val_line.find(k, i)
                if di != -1:
                    digits.add((di, v))

    fd = (len(val_line), "")
    ld = (-1, "")

    for d in digits:
        if d[0] < fd[0]:
            fd = (d[0], d[1])

        if d[0] > ld[0]:
            ld = (d[0], d[1])

    return int(fd[1] + ld[1])


###
###
###


def test_parse_calibration_doc():
    doc = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]

    assert 281 == parse_calibration_doc(doc)


def test_find_calibration_val():
    # simple test cases

    assert 11 == find_calibration_val("1")
    assert 11 == find_calibration_val("one")
    assert 11 == find_calibration_val("11")
    assert 11 == find_calibration_val("oneone")
    assert 11 == find_calibration_val("one1")
    assert 11 == find_calibration_val("1one")

    # Sample test cases

    assert 29 == find_calibration_val("two1nine")
    assert 83 == find_calibration_val("eightwothree")
    assert 13 == find_calibration_val("abcone2threexyz")
    assert 24 == find_calibration_val("xtwone3four")
    assert 42 == find_calibration_val("4nineeightseven2")
    assert 14 == find_calibration_val("zoneight234")
    assert 76 == find_calibration_val("7pqrstsixteen")

    # Input real cases until success

    assert 57 == find_calibration_val("ckmb52fldxkseven3fkjgcbzmnr7")
    assert 61 == find_calibration_val("gckhqpb6twoqnjxqplthree2fourkspnsnzxlz1")
    assert 27 == find_calibration_val("2onetwocrgbqm7")
    assert 25 == find_calibration_val("frkh2nineqmqxrvdsevenfive")
    assert 42 == find_calibration_val("four9two")
    assert 61 == find_calibration_val("six7sixqrdfive3twonehsk")


if __name__ == "__main__":
    # TODO: Create file reading functions (read as list)
    with open("input/in1_2.txt") as file:
        list_input = []

        for line in file:
            list_input.append(line)

        result = parse_calibration_doc(list_input)
        print(result)
