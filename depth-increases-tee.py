from itertools import tee


def pairwise(iterable):
    """
    Create a new iterable of next-value pairs.
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def sliding_window_sums(depths):
    """
    Create a list of three-measurement sums
    """
    return [
        a + b + c
        for a, b, c
        in zip(depths, depths[1:], depths[2:])
    ]


def count_depth_increases(depths):
    # Get the sliding window sums
    sums = sliding_window_sums(depths)

    # Create a list that has a 1 if the
    # first value in the pair is less than
    # the second value in a pair and a 0
    # if not, then sum the 1s and 0s
    return sum([1 if a < b else 0 for a, b in pairwise(sums)])


depths = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263
]

# print(count_depth_increases(depths))
print(tee(depths))
