from bank import value


def test_hello():
    assert value("Hello") == 0


def test_hello_with_extra_words():
    assert value("Hello, Newman") == 0


def test_greetings_starting_with_h():
    assert value("How you doing?") == 20


def test_not_starting_with_h():
    assert value("What's happening?") == 100
