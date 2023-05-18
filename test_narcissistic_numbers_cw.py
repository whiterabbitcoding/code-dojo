"""
Codewars:

https://www.codewars.com/kata/5287e858c6b5a9678200083c/solutions/python

cool lambda example:

narcissistic = lambda n: sum([int(d) ** len(str(n)) for d in list(str(n))]) == n

"""


def narcissistic(value: int) -> bool:
    return (
        True
        if sum([int(i) ** (len(str(value))) for i in str(value)]) == value
        else False
    )


def test_narcissistic():
    assert narcissistic(7) is True
    assert narcissistic(371) is True
