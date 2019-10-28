#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows the factorial of a number


def main():
    
    power_of_number = 0
    total_number = 0
    # input
    number = input("Input the number: ")

    try:
        number_as_number = int(number)
        if number_as_number > 0:
            for power_of_number in range(number_as_number + 1):
                # process
                total_number = power_of_number**2
                print("{0}^2 = {1}".format(power_of_number, total_number))

        else:
            print("not a positive number")
            
    except(ValueError):
        print("That is not a valid number")


if __name__ == "__main__":
    main()
