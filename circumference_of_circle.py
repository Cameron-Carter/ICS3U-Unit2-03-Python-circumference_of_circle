#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on April 2021
# This program calculates the circumference of a circle with an inputted radius

import constants


def main():
    # This function calculates circumference

    # Input
    radius = int(input("Enter the radius of a circle (mm): "))

    # Process
    circumference = constants.TAU * radius

    # Output
    print("The circumference of the circle is {} mm.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
