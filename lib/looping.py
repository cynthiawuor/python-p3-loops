#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

    pass

def square_integers(int_list):
    squared_list = []  # Initialize an empty list to store squared elements
    for num in int_list:
        squared_list.append(num ** 2)  # Square each element and append to the new list
    return squared_list

    pass

def fizzbuzz():
    for num in range(1, 101):  # Iterate from 1 to 100
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

    pass
