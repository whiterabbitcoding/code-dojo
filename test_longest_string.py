def longest(a1, a2):
    return "".join(sorted(list(dict.fromkeys(a1 + a2))))


def test_longest():
    assert longest("ab", "bc") == "abc"
