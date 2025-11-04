def fibonacci_iter(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1
    steps = 0
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
        steps += 1
    return c, steps + 1

def fibonacci_recur(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1
    fib1, steps1 = fibonacci_recur(n - 1)
    fib2, steps2 = fibonacci_recur(n - 2)
    return fib1 + fib2, steps1 + steps2 + 1

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    fib_iter, steps_iter = fibonacci_iter(n)
    fib_recur, steps_recur = fibonacci_recur(n)

    print("\nIterative Method:")
    print("Fibonacci Number:", fib_iter)
    print("Steps:", steps_iter)

    print("\nRecursive Method:")
    print("Fibonacci Number:", fib_recur)
    print("Steps:", steps_recur)
