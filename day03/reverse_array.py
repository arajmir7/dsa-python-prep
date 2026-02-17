
# Recursive function to calculate Fibonacci number
def fibonacci(n):
    # Base case: fib(0) = 0
    if n == 0:
        return 0

    # Base case: fib(1) = 1
    if n == 1:
        return 1

    # Recursive case: sum of previous two Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Define the position in Fibonacci series
n = 5

# Call the function and print the result
print(fibonacci(n))
