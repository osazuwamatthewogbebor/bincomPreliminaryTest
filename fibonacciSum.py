def fibonacci_sum(number):
    fibonacci = [0, 1]
    for i in range(2, number):
        n = len(fibonacci)
        fibonacci.append(fibonacci[n - 1] + fibonacci[n - 2])

    sum_fib = sum(fibonacci)
    len_fib = len(fibonacci)

    print(f"The sum of the first {len_fib} Fibonacci numbers is {sum_fib}")


fibonacci_sum(5)
