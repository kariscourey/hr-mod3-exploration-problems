def triangular(n):
    # acc = 0

    # for i in range(n + 1):
    #     acc += i

    # return acc

    # base case
    if n == 0:
        return 0
    # recursive cae
    else:
        return n + triangular(n - 1)


# def my_factorial(n):

#     # base case
#     if n == 1:
#         return 1

#     else:
#         # recursive case
#         return n * my_factorial(n - 1)
