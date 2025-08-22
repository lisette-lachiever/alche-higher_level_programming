#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    if len(argv) == 0:
         print("0 arguments.")
    else:
        print("{} arguments".format(len(argv)))
        for i in range(len(argv)):
            print("{}:".format(i), argv[i])
