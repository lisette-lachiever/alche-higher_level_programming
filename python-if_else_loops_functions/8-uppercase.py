#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) not in range(65, 91):
            letter = chr(ord(letter) - 32)
            print ("{}".format(letter), end='')
        else:
            print ("{}".format(letter), end='')
