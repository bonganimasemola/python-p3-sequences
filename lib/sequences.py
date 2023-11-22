#!/usr/bin/env python3


def print_fibonacci(length):
    fib_sequence = []

    for i in range(length):
        if i == 0:
            fib_sequence.append(0)
        elif i == 1:
            fib_sequence.append(1)
        else:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)

    print(fib_sequence)

