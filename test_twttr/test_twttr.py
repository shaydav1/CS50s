from twttr import shorten


def test_argument():
    assert shorten("Twitter") == "Twttr"


def test_argument_2():
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_argument_3():
    assert shorten("CS50") == "CS50"


def test_argument_4():
    assert shorten("AEIOU") == ""
