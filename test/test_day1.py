import day1


def test_find_calibration():
    assert 12 == day1.find_calibration_val("1abc2")
    assert 38 == day1.find_calibration_val("pqr3stu8vwx")
    assert 15 == day1.find_calibration_val("a1b2c3d4e5f")
    assert 77 == day1.find_calibration_val("treb7uchet")


if __name__ == "__main__":
    test_find_calibration()
