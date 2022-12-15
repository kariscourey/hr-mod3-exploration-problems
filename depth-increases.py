def count_depth_increases(depths):

    # increases = 0

    # for i in (range(len(depths) - 1)):
    #     if depths[i] < depths[i + 1]:
    #         increases += 1
    # return increases

    return len(
        [i for i in range(len(depths) - 1) if depths[i] < depths[i + 1]]
    )


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

print(count_depth_increases(depths))
