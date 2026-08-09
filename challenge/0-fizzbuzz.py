#!/usr/bin/python3

import sys

number = int(sys.argv[1])

for i in range(1, number + 1):
    if i % 15 == 0:
        text = "FizzBuzz"
    elif i % 3 == 0:
        text = "Fizz"
    elif i % 5 == 0:
        text = "Buzz"
    else:
        text = str(i)

    if i < number:
        print(text, end=" ")
    else:
        print(text, end="")
