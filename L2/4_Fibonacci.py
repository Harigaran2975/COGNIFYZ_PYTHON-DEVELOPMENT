def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Get user input
n = int(input("Enter number of terms: "))
if n > 0:
    print("Fibonacci Sequence:")
    fibonacci(n)
else:
    print("Enter a positive number.")
