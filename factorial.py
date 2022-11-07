def my_factorial(n, a=1):

    # base case
    if n in [0, 1]:
        return 1 * a

    else:
        # recursive case
        return my_factorial(n - 1, a * n)

# increase the value of num
# until you get an error
num = 970

# the function call
print(my_factorial(num))
