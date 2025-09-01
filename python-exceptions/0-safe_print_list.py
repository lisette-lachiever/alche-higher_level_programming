#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    try:
        for element in range(x):
            print(f"{my_list[element]}", end="")

    except IndexError:
        print("\nIndex out of range")
    return element
