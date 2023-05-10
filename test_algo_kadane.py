from sys import maxsize


def getMaxProfit(a, size):
    print("a")
    print(a)
    print("size")
    print(size)
    if size == 1:
        return max(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):
        max_so_far

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))


def get_profit():


print(
    getMaxProfit(
        [4, 3, -2, 9, -4, 2, 7],
        6,
    )
)
