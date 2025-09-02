#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for items in my_list:
            if type(items) is str:
                continue
            print("{:d}".format(items), end=" ")
        return True
    except (TypeError, ValueError):
       pass
