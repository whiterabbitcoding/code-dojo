from typing import List


def sum_two_smallest_numbers(numbers: List) -> int:
    return sum(sorted(numbers)[0:2])


def test_smallest_numbers():
    assert sum_two_smallest_numbers([1, 2, 3, 4]) == 3
