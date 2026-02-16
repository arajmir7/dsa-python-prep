def sum_of_n(n):
    if n == 0:
        return 0

    return n + sum_of_n(n - 1)

n = 15
print(sum_of_n(n))
