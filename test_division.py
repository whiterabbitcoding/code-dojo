def different_types_of_division(a, b):
    return {"rounded down": a // b, "float": a / b}


def test_division():
    assert different_types_of_division(5, 2) == {"rounded_down": 2, "float": 2.5}
