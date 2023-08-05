def get_num_of_aliens(n):
    if n <= 0:
        return "Invalid input. The position should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence[-1]

gen = int(input())
fibonacci_number = get_num_of_aliens(gen + 3)
print(f"Answer: {fibonacci_number}")
