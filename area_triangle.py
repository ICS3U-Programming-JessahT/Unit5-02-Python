#!/usr/bin/env python3

# Created By: Jessah
# Date: December 16, 2022
# This program ask the for base and height of a triangle
# It then uses a function to get the area

# function for area of a triangle
def area_triangle(base, height):
    # calculate the are
    area = (base * height) / 2

    # display the area to user when called
    print("with the base of {} and height of {}".format(base, height))
    print("the area is {}cm^2".format(area))


# main function
def main():
    # get base and height from user
    user_string_base = input("Enter the base of the triangle (cm): ")
    user_string_height = input("Enter the height of the triangle (cm): ")
    # check if the user entered any strings
    try:
        user_base = float(user_string_base)
        user_height = float(user_string_height)
    except (Exception):  # display when invalid
        print("That is invalid, the base and height can only positive")
        print("integers or decimals")
    # check if the number they entered isn't an negative
    else:
        if user_base > 0 and user_height > 0:
            # call function
            area_triangle(user_base, user_height)
        else:
            print("Negative numbers can't be the base or height")


if __name__ == "__main__":
    main()
