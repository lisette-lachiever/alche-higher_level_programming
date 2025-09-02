#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            if type(my_list[i]) is str:
                continue
            else:
                print("{:d}".format(my_list[i]), end="")
            n = n + 1
        return True
    except (TypeError, ValueError, IndexError):
       pass
    print()
    return n
