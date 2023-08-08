from numb3rs import validate


def test_validate1():
    assert validate("127.0.0.1") == True


def test_validate2():
    assert validate("255.255.255.255") == True


def test_validate3():
    assert validate("512.512.512.512") == False


def test_validate4():
    assert validate("1.2.3.1000") == False


def test_validate5():
    assert validate("cat") == False


def test_validate6():
    assert validate("10.256.10.10") == False
