from even_function import is_even


def collatz(collatz_number):
    while collatz_number != 1:
        if is_even(collatz_number):
            collatz_number = collatz_number / 2
            print(collatz_number)
        else:
            collatz_number = collatz_number * 3 + 1
            print(collatz_number)


print(collatz(22))
