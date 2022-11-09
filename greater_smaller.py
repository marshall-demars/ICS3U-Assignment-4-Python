#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program tells the user which input is greater and smaller


def main():
    # This program tells the user which input is greater and smaller

    # Input
    integer_one_as_string = input("\nEnter a positive number: ")
    integer_two_as_string = input("\nEnter a second positive number: ")

    # Process and Output
    try:
        integer_one_as_int = int(integer_one_as_string)
        integer_two_as_int = int(integer_two_as_string)
        if integer_one_as_int < 0 or integer_two_as_int < 0:
            print("\nPlease input only positive numbers.")
        elif integer_one_as_int > integer_two_as_int:
            print(
                "\n{0} is a larger number than {1}.".format(
                    integer_one_as_int, integer_two_as_int
                )
            )
        elif integer_one_as_int < integer_two_as_int:
            print(
                "\n{0} is a larger number than {1}.".format(
                    integer_two_as_int, integer_one_as_int
                )
            )
        else:
            print(
                "\n{0} is the same number as {1}.".format(
                    integer_one_as_int, integer_two_as_int
                )
            )

    except Exception:
        print("\nInvalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
