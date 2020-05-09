from validator.rules import Max


def test_max_01():
    rule = Max(18)
    value_to_check = 23
    assert rule(value_to_check) == False

    rule = Max(18)
    value_to_check = 13
    assert rule(value_to_check) == True


def test_max_02():
    rule = Max(-18)
    value_to_check = 0
    assert rule(value_to_check) == False

    rule = Max(0)
    value_to_check = 100
    assert rule(value_to_check) == False

    rule = Max(0)
    value_to_check = 100
    assert rule(value_to_check) == False

    rule = Max(999)
    value_to_check = -999
    assert rule(value_to_check) == True


def test_max_03():
    rule = Max(10)
    value_to_check = 10
    assert rule(value_to_check) == True

    rule = Max(0)
    value_to_check = 0
    assert rule(value_to_check) == True

    rule = Max(-23)
    value_to_check = -23
    assert rule(value_to_check) == True