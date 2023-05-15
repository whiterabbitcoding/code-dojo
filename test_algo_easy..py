def algo(n):
    output = []
    if n not in range(1, 20):
        pass
    else:
        for i in range(0, n):
            output.append(i**i)
            print(i * i)


def test_algo():
    assert algo(5) == [0, 1, 4, 9, 16]
