from plates import is_valid


def test_first_two_letters():
    assert is_valid("PI314") == True


def test_beginning_alphabetical():
    assert is_valid("50") == False


def test_max_6_chars():
    assert is_valid("OUTATIME") == False


def test_min_2_chars():
    assert is_valid("H") == False


def test_numbers_in_the_mid():
    assert is_valid("AAA22A") == False


def test_periods():
    assert is_valid("PI3.14") == False


def test_zero_placement():
    assert is_valid("ad0") == False
