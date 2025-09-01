#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for element in range(x):
            print(f"{my_list[element]}", end="")
            n = n+1
    except IndexError:
        pass
    print()
    return n
