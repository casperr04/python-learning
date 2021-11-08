def fizzbuzz(num):
    fizzbuzz_list = []
    for number in range(1, num + 1): # starts counting from 1, adds 1 to num to end on num (range ends a number before num)
        if number % 3 == 0:
            if number % 5 == 0:
                fizzbuzz_list.append("FizzBuzz")
            else:
                fizzbuzz_list.append("Fizz")
        if number % 5 == 0:
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(number)
    return fizzbuzz_list

# writes list to fizzbuzz.txt file

fizzbuzz_text = open("fizzbuzz.txt", "w")
fizzbuzz_text.write(str(fizzbuzz(500)))
fizzbuzz_text.close


